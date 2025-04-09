# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

import llnl.util.filesystem as fs
from spack.package import *


BUILD = "build"
RUN = "run"

ISC_PATH = os.environ.get("CODE_SATURNE_ISC_PATH", None)


class TrueValue:
    @staticmethod
    @property
    def value():
        return True


class CodeSaturne(AutotoolsPackage):
    """
    CodeSaturne is a CFD package
    """

    homepage = "https://www.code-saturne.org/cms/web/"
    url = "https://www.code-saturne.org/releases/code_saturne-8.3.0.tar.gz"
    git = "https://github.com/code-saturne/code_saturne.git"
    list_url = "https://www.code-saturne.org/releases"

    maintainers("Pencilcaseman")

    license("GPL2", checked_by="Pencilcaseman")

    version("master", branch="master")

    if ISC_PATH is not None:
        version(
            "8.3.1-ISC",
            sha256="59cb171acc683130341b94b446ea86a8cef12cb40ca49d768ee158e7294872c3",
            url=f"file://{ISC_PATH}",
        )

    # fmt: off
    version("8.3.0", sha256="6586cb33efd98358e5888562fa122a0834e1885c635f504d3ac809c6670e6865")
    version("8.2.1", sha256="4cdd8d15ff7ce272e60fb65d66c66c45de21932624d9e7237da1fb6da3e2ffcc")
    version("8.2.0", sha256="e90406b9c9cbd84203f2f6560a0ef9bc88508d4fd40ac76f1a5af92c18219b60")
    version("8.1.3", sha256="5036da07e6fe555bc9de6ad8e35431372c933a85ea7db9817fb744e5ed6a1d8b")
    version("8.1.1", sha256="8b7c70a03f08d3c41a79ebcd05a02b85f13488a661f3dde37800fc8c41675a61")
    version("8.1.0", sha256="6f2b067337b8ad003a26b91f59971a1028f01cf14c962031629203899dc4053f")
    version("8.0.4", sha256="fb9e6057acadc1f6f4c0627ecd4c8027ce9bc2ded1920585b6f3f895946c10af")
    version("8.0.3", sha256="c003455cd399b6d2fea062d600b192d3a6ab4c9f296018ca16ef988ccd48dd11")
    version("8.0.2", sha256="48d33a55e9f7b77b486e0fa1706223910eb9add7d13f11bb18dc79583587378f")
    # fmt: on

    depends_on("c", type=BUILD)
    depends_on("cxx", type=BUILD)
    depends_on("fortran", type=BUILD)

    depends_on("autoconf", type=BUILD)
    depends_on("automake", type=BUILD)
    depends_on("libtool", type=BUILD)
    depends_on("m4", type=BUILD)

    variant("cuda", default=False, description="CUDA offload")
    variant("cuda-cpp", default=False, description="CUDA offload for .cpp files")
    variant("hdf5", default=False, description="HDF5 support")
    variant("debug", default=False, description="Debugging (reduces optimization)")
    variant("profile", default=False, description="Profiling")
    variant("auto-flags", default=True, description="Define *FLAGS on known systems")
    variant("relocatable", default=False, description="Relocatable installation")
    variant("shared", default=True, description="Build shared libraries")
    variant("long-gnum", default=False, description="Use long global numbers")
    variant("long-lnum", default=False, description="Use long local numbers")
    variant("sycl", default=False, description="SYCL support")
    variant("openmp", default=True, description="OpenMP support")
    variant("openmp-target", default=False, description="OpenMP accelerator support")
    variant("dlloader", default=True, description="Dynamic shared library loading")
    variant(
        "dlopen-rtld-global",
        default=False,
        description="Add RTLD_GLOBAL to dlopen flags",
    )
    variant("mpi", default=True, description="MPI support")
    variant("mpi-io", default=True, description="Use MPI I/O when available")
    variant(
        "gui-coolprop",
        default=False,
        description="Allow CoolProp fluids in GUI even when not available",
    )
    variant(
        "medcoupling-as-plugin", default=False, description="Use MEDCoupling as plugin"
    )
    variant("catalyst-as-plugin", default=True, description="Use Catalyst as plugin")
    variant("melissa-as-plugin", default=True, description="Use Melissa as plugin")
    variant("dot", default=False, description="Graphviz dot for diagrams in HTML")
    variant("zlib", default=False, description="Gzipped file support")
    variant("mathjax", default=False, description="MathJax for math in HTML")
    variant("frontend", default=True, description="Front-end elements")
    variant("backend", default=True, description="Back-end elements")
    variant("gui", default=True, description="Graphical User Interface")
    variant("largefile", default=True, description="Support for large files")
    variant(
        "malloc-hooks", default=False, description="Use malloc hooks when available"
    )
    variant(
        "sockets", default=True, description="Allow communications through IP sockets"
    )
    variant(
        "cgns",
        default=False,
        description="Necessary to read or write mesh and visualization files using the CGNS format, available as an export format with many third-party meshing tools",
    )
    variant(
        "scotch",
        default=False,
        description="May be used to optimize mesh partitioning. Depending on the mesh, parallel computations with meshes partitioned with these libraries may be from 10% to 50% faster than using the built-in space-filling curve based partitioning",
    )
    variant(
        "metis",
        default=False,
        description="Alternative mesh partitioning libraries. These libraries have a separate source tree, but some of their functions have identical names, so only one of the 2 may be used. If both are available, ParMETIS will be used. Partitioning quality is similar to that obtained with Scotch or PT-Scotch",
    )
    variant(
        "melissa",
        default=False,
        description="May be used for in-situ statistical analysis and post-processing of ensemble runs",
    )
    variant(
        "blas",
        default=False,
        description="Use a BLAS library. Generally only useful for testing",
    )
    variant(
        "petsc",
        default=False,
        description="Portable, Extensible Toolkit for Scientific Computation. Consists of a variety of libraries, which may be used by code_saturne for the resolution of linear equation systems. In addition to providing many solver options, it may be used as a bridge to other major solver libraries",
    )
    variant(
        "hypre",
        default=False,
        description="High Performance Preconditioners. A library of high performance preconditioners and solvers featuring multigrid methods for the solution of large, sparse linear systems of equations on massively parallel computers",
    )
    variant(
        "amgx",
        default=False,
        description="A high performance multigrid and preconditioned iterative method library for NVIDIA GPUs. It includes a flexible solver composition system that allows a user to easily construct complex nested solvers and preconditioners",
    )

    conflicts("+mpi-io", when="~mpi", msg="MPI I/O requires MPI support")
    conflicts("^cgns@:3.1", when="+cgns")
    conflicts(
        "+scotch",
        when="+metis",
        msg="Only one mesh partitioning library can be specified",
    )

    # with when("+..."):
    #     depends_on("...")
    #
    # depends_on("...", when="+...")

    # Depends on python and PyQt5, but it's easier to use
    # a global install of these
    # depends_on("python")
    # depends_on("py-pyqt5", when="+gui)

    # depends_on("python")
    # depends_on("py-pyqt5", when="+gui")

    depends_on("cuda", when="+cuda", type=(BUILD,))
    depends_on("hdf5", when="+hdf5", type=(BUILD,))
    depends_on("mpi", when="+mpi", type=(BUILD,))
    depends_on("blas", when="+blas", type=(BUILD,))
    depends_on("zlib", when="+zlib", type=(BUILD,))

    with when("+medcoupling-as-plugin"):
        depends_on("med", type=(BUILD, RUN))
        depends_on("salome-configuration", type=(BUILD, RUN))
        depends_on("salome-med", type=(BUILD, RUN))
        depends_on("salome-medcoupling", type=(BUILD, RUN))

    depends_on("cgns", when="+cgns", type=(BUILD, RUN))
    depends_on("scotch", when="+scotch", type=(BUILD, RUN))
    depends_on("metis", when="+metis", type=(BUILD, RUN))
    depends_on("melissa", when="+melissa", type=(BUILD, RUN))
    depends_on("petsc", when="+petsc", type=(BUILD,))
    depends_on("hypre", when="+hypre", type=(BUILD, RUN))
    depends_on("amgx", when="+amgx", type=(BUILD, RUN))

    @run_before("autoreconf")
    def bootstrap(self):
        bootstrap_path = os.path.join(self.stage.source_path, "sbin", "bootstrap")
        which(bootstrap_path)()

    def autoreconf(self, spec, prefix):
        pass

    def configure(self, spec, prefix):
        if self.spec.variants["mpi"].value:
            env["CC"] = spec["mpi"].mpicc
            env["CXX"] = spec["mpi"].mpicxx
            env["F77"] = spec["mpi"].mpif77
            env["FC"] = spec["mpi"].mpifc

        options = ["--prefix={0}".format(prefix)]
        options += self.configure_args()

        with fs.working_dir(self.build_directory, create=True):
            self.module.configure(*options)

    def build(self, spec, prefix):
        if self.spec.variants["mpi"].value:
            env["CC"] = spec["mpi"].mpicc
            env["CXX"] = spec["mpi"].mpicxx
            env["F77"] = spec["mpi"].mpif77
            env["FC"] = spec["mpi"].mpifc

        params = []
        params += self.build_targets

        with fs.working_dir(self.build_directory):
            self.module.make(*params)

    def configure_args(self):
        args = []

        for flag in [
            "cuda",
            "cuda-cpp",
            "debug",
            "profile",
            "auto-flags",
            "relocatable",
            "shared",
            "long-gnum",
            "long-lnum",
            "sycl",
            "openmp",
            "openmp-target",
            "dlloader",
            "dlopen-rtld-global",
            "mpi-io",
            "gui-coolprop",
            "medcoupling-as-plugin",
            "melissa-as-plugin",
            "dot",
            "mathjax",
            "frontend",
            "backend",
            "gui",
            "largefile",
            "malloc-hooks",
        ]:
            if self.spec.variants[flag].value:
                tmp = "--enable-"
            else:
                tmp = "--disable-"

            tmp += flag

            args.append(tmp)

        for extra in [
            "hdf5",
            # "salome",
            "blas",
            "mpi",
            "metis",
            "scotch",
            "cgns",
            # "med",
            "zlib",
            "melissa",
            "petsc",
            "hypre",
            "amgx",
        ]:
            if self.spec.variants.get(extra, default=TrueValue).value:
                args.append(f"--with-{extra}={self.spec[extra].prefix}")

        if self.spec.variants["medcoupling-as-plugin"].value:
            args.append(f"--with-medcoupling={self.spec['salome-medcoupling'].prefix}")

        return args
