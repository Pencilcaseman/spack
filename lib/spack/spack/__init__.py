# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

#: PEP440 canonical <major>.<minor>.<micro>.<devN> string
__version__ = "0.22.6.dev0"
spack_version = __version__

#: The current Package API version implemented by this version of Spack. The Package API defines
#: the Python interface for packages as well as the layout of package repositories. The minor
#: version is incremented when the package API is extended in a backwards-compatible way. The major
#: version is incremented upon breaking changes. This version is changed independently from the
#: Spack version.
package_api_version = (1, 0)

#: The minimum Package API version that this version of Spack is compatible with. This should
#: always be a tuple of the form ``(major, 0)``, since compatibility with vX.Y implies
#: compatibility with vX.0.
min_package_api_version = (1, 0)


def __try_int(v):
    try:
        return int(v)
    except ValueError:
        return v


#: (major, minor, micro, dev release) tuple
spack_version_info = tuple([__try_int(v) for v in __version__.split(".")])


__all__ = ["spack_version_info", "spack_version", "package_api_version", "min_package_api_version"]
