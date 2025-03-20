# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
"""Hooks to produce reports of spec installations"""
import collections
import gzip
import os
import time
import traceback

import llnl.util.filesystem as fs

import spack.build_environment
import spack.util.spack_json as sjson

reporter = None
report_file = None

Property = collections.namedtuple("Property", ["name", "value"])


class Record(dict):
    def __getattr__(self, name):
        # only called if no attribute exists
        if name in self:
            return self[name]
        raise AttributeError(f"RequestRecord for {self.name} has no attribute {name}")

    def __setattr__(self, name, value):
        if name.startswith("_"):
            super().__setattr__(name, value)
        else:
            self[name] = value


class RequestRecord(Record):
    def __init__(self, spec):
        super().__init__()
        self.name = spec.name
        self.errors = None
        self.nfailures = None
        self.npackages = None
        self.time = None
        self.timestamp = time.strftime("%a, d %b %Y %H:%M:%S", time.gmtime())
        self.properties = [
            Property("architecture", spec.architecture),
            Property("compiler", spec.compiler),
        ]
        self.packages = []
        self._seen = set()

    def append_record(self, record, key):
        self.packages.append(record)
        self._seen.add(key)

    def seen(self, key):
        return key in self._seen

    def summarize(self):
        self.npackages = len(self.packages)
        self.nfailures = len([r for r in self.packages if r.result == "failure"])
        self.nerrors = len([r for r in self.packages if r.result == "error"])
        self.time = sum(float(r.elapsed_time or 0.0) for r in self.packages)


class SpecRecord(Record):
    pass


class InstallRecord(SpecRecord):
    def __init__(self, spec):
        super().__init__()
        self._spec = spec
        self._package = spec.package
        self._start_time = time.time()
        self.name = spec.name
        self.id = spec.dag_hash()
        self.elapsed_time = None
        self.result = None
        self.message = None
        self.installed_from_binary_cache = None

    def fetch_log(self):
        try:
            if os.path.exists(self._package.install_log_path):
                stream = gzip.open(self._package.install_log_path, "rt", encoding="utf-8")
            else:
                stream = open(self._package.log_path, encoding="utf-8")
            with stream as f:
                return f.read()
        except OSError:
            return f"Cannot open log for {self._spec.cshort_spec}"

    def fetch_time(self):
        try:
            with open(self._package.times_log_path, "r", encoding="utf-8") as f:
                data = sjson.load(f.read())
            return data["total"]
        except Exception:
            return None

    def skip(self, msg):
        self.result = "skipped"
        self.elapsed_time = 0.0
        self.message = msg

    def succeed(self):
        self.result = "success"
        self.stdout = self.fetch_log()
        self.installed_from_binary_cache = self._package.installed_from_binary_cache
        self.elapsed_time = self.fetch_time()

    def fail(self, exc):
        if isinstance(exc, spack.build_environment.InstallError):
            self.result = "failure"
            self.message = exc.message or "Installation failure"
            self.exception = exc.traceback
        else:
            self.result = "error"
            self.message = str(exc) or "Unknown error"
            self.exception = traceback.format_exc()
        self.stdout = self.fetch_log() + self.message


requests = {}


def pre_installer(specs):
    global requests

    for root in specs:
        request = RequestRecord(root)
        requests[root.dag_hash()] = request

        for dep in filter(lambda x: x.installed, root.traverse()):
            record = InstallRecord(dep)
            record.skip(msg="Spec already installed")
            request.append_record(record, dep.dag_hash())


def post_installer(specs, hashes_to_failures):
    global requests
    global report_file
    global reporter

    try:
        for root in specs:
            request = requests[root.dag_hash()]

            # Associate all dependency jobs with this request
            for dep in root.traverse():
                if request.seen(dep.dag_hash()):
                    continue  # Already handled

                record = InstallRecord(dep)
                if dep.dag_hash() in hashes_to_failures:
                    record.fail(hashes_to_failures[dep.dag_hash()])
                elif dep.installed:
                    record.succeed()
                else:
                    # This package was never reached because of an earlier failure
                    continue
                request.append_record(record, dep.dag_hash())

            # Aggregate request-level data
            request.summarize()

        # Write the actual report
        if not report_file:
            basename = specs[0].format("test-{name}-{version}-{hash}.xml")
            dirname = os.path.join(spack.paths.reports_path, "junit")
            fs.mkdirp(dirname)
            report_file = os.path.join(dirname, basename)
        if reporter:
            reporter.build_report(report_file, specs=list(requests.values()))

    finally:
        # Clean up after ourselves
        requests = {}
        reporter = None
        report_file = None


# This is not thread safe, but that should be ok
# We only have one top-level thread launching build requests, and all parallelism
# is between the jobs of different requests
# requests: Dict[str, RequestRecord] = {}
# specs: Dict[str, InstallRecord] = {}


# def pre_installer(specs):
#     global requests
#     global specs

#     for spec in specs:
#         record = RequestRecord(spec)
#         requests[spec.dag_hash()] = record

#         for dep in filter(lambda x: x.installed, spec.traverse()):
#             spec_record = InstallRecord(dep)
#             spec_record.elapsed_time = "0.0"
#             spec_record.result = "skipped"
#             spec_record.message = "Spec already installed"
#             specs[dep.dag_hash()] = spec_record

# def pre_install(spec):
#     global specs

#     specs[spec.dag_hash()] = InstallRecord(spec)


# def post_install(spec, explicit: bool):
#     global specs

#     record = specs[spec.dag_hash()]
#     record.result = "success"
#     record.stdout = record.fetch_log()
#     record.installed_from_binary_cache = record._package.installed_from_binary_cache
#     record.elapsed_time = time.time() - record._start_time


# def post_failure(spec, error):
#     global specs

#     record = specs[spec.dag_hash()]
#     if isinstance(error, spack.build_environment.InstallError):
#         record.result = "failure"
#         record.message = exc.message or "Installation failure"
#         record.exception = exc.traceback
#     else:
#         record.result = "error"
#         record.message = str(exc) or "Unknown error"
#         record.exception = traceback.format_exc()
#     record.stdout = record.fetch_log() + record.message
#     record.elapsed_time = time.time() - record._start_time


# def post_installer(specs):
#     global requests
#     global specs
#     global reporter
#     global report_file

#     for spec in specs:
#         # Find all associated spec records
#         request_record = requests[spec.dag_hash()]
#         for dep in spec.traverse(root=True):
#             spec_record = specs[dep.dag_hash()]
#             request_record.records.append(spec_record)

#         # Aggregate statistics
#         request_record.npackages = len(request_record.records)
#         request_record.nfailures = len([r for r in request_record.records if r.result == "failure"])
#         request_record.errors = len([r for r in request_record.records if r.result == "error"])
#         request_record.time = sum(float(r.elapsed_time) for r in request_record.records)

#     # Write the actual report
#     filename = report_file or specs[0].name
#     reporter.build_report(filename, specs=specs)

#     # Clean up after ourselves
#     requests = {}
#     specs = {}
