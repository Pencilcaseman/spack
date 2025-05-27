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
    version("8.0.1", sha256="f7276e273da79eea894ef5f9d15277ccde1113532e6f6c21f12d38b78b001ed4")
    version("8.0.0", sha256="f5ab127bac9e8f2fafcc582dab25682c131c1a0cd656cae36527b3ba402aa45e")
    version("7.3.1", sha256="ff8b24e718a8c7a915a6b40c00671b29d9d826c4011bcc9ac386c22bd69285c7")
    version("7.3.0", sha256="a754f9ffb142b4dc2821345de31e61f82355dea57ba4bf7eb052e750c2dbc026")
    version("7.2.2", sha256="80686eb260e546477d157af1bf98ee2f4845c3465a023c66c02a08726345e17c")
    version("7.2.1", sha256="e2521d7764496fa76d6333417b53975b4f380ffa4cd421aef68f99aff85d0f6d")
    version("7.2.0", sha256="810914973fae40fdd89d397125d9b6f089bc4728c019358e4c121888db5e90b8")
    version("7.1.2", sha256="d42127ea139a845873a1ed794f828958000d54349b5e18da0ab5a924ff867995")
    version("7.1.1", sha256="e3ab54a97281e9e7423645f09306892f6156bea03d41092404e6cae26063ad84")
    version("7.1.0", sha256="7144b8e46716ce13c19772a6b0478acf4bb6b1c2054fe93a8d3423166a3ee4ce")
    version("7.0.6", sha256="1b28fc672b32d98c5ed0e6a69f55b7de6759a3b8a6f71a26e94798d572aac60e")
    version("7.0.5", sha256="d4edc6c92f1fbd25695d1c445b4491ef2dab136e60ad08f7c047423becc5d7db")
    version("7.0.4", sha256="b26b617830a98f37bb741217f31bbdbddd55e5b068e68cc108526e2b5295a81d")
    version("7.0.3", sha256="50a427f9de3f6413328c65a872f75db059a40e2e4a4ce9e3584beac0689f07cf")
    version("7.0.2", sha256="45e1a7dc19a6af7c44a79b982c3139960d3b0e9a1b2e108d784b312b5c8f7b2c")
    version("7.0.1", sha256="75e22deabde1ad85969a205ddd945b97aa05c5af15bda0d253c70918a637dff1")
    version("7.0.0", sha256="fa8cb121c95872a1a9dfa607477a12d203bd58fc1cc6e6226d686f9db389e7e0")
    version("6.3.1", sha256="1dbf4a6a9e63c0b0a9e56a7cc4d3b1bebb6425fdd8f6303977cc8f2856de842b")
    version("6.3.0", sha256="e1df6631753229394b186efe1be9e6dfbba08e9ee50e2cdf714f9117c1c8f1b8")
    version("6.2.2", sha256="9dcdc7844ce3e707bcde3db7c3b2c95ecc41aeb712df75b2595a8e1e89e33c77")
    version("6.2.1", sha256="af2ee55444d27386b262ecac3a66cd9d47bb4e857f453a2730f242c282e12f79")
    version("6.2.0", sha256="8c5b72d47abeaf40918cb6b7e2e54bb8da755c8647914733311508482f58dadc")
    version("6.1.3", sha256="9d41f6efe347930b7d5dffdeea3d0fbb319f2bd0bef59bd3be047616dd10bf59")
    version("6.1.2", sha256="82cc42d0bf582566a2be2d12fb75eaba1d7771efaa9ba629c4bc14c228934233")
    version("6.1.1", sha256="622b69be0eedebaa85bfd90848960149601942850b6f29633d409b4ab9bbc9b6")
    version("6.1.0", sha256="6d178a2136d211ae91e465faa5cfe790b920e5958604555bf814f9df8ded003f")
    version("6.0.9", sha256="e5b0034a12fb8b40f883789c6e31c9b79c7e08ecb7c12f492f61131e1ba0e201")
    version("6.0.8", sha256="7bbbf0a6a5d2e612b8bb4dc8636b5db2e649549f642cc5b705db06906ea2ba9c")
    version("6.0.7", sha256="133286fdaa8804c7c5b99222abbc7f06917f25e3d6d559f8c9ee816246e5becf")
    version("6.0.6", sha256="86f9605d68c9ee7fd137c29980abbdd5d11c8731da623421ddbc2b69907f4f22")
    version("6.0.5", sha256="353308b43e54167a880814b613084e0feb3fe7b27b13348161cc82abbb1b2cb8")
    version("6.0.4", sha256="2a442790798ffe4dd69caf82eb0d48fa0e324e25e5c3796f179fa0b9664a828c")
    version("6.0.3", sha256="75e1732a41a6fd10d5c226a71f944768ede321ea71128bdc58d43d69752848e4")
    version("6.0.2", sha256="39ac1c167cd87d5dcb51eb2b6da4bec1607de7ad6a52e892fcf26c8fb9c55a49")
    version("6.0.0", sha256="93c72b3f34be0754ec285193f099dc8635b4048aa965e72e6462d79dd6d4c690")
    version("5.3.4", sha256="446c5a5637e0a2d4bda79789e23ae04b9cc3b3c78f2db8496e89eaae53a81255")
    version("5.3.3", sha256="3eb0ee26c50265bb0897063e79663d22461da9cdb8776dc0ff52dc6e72a8d891")
    version("5.3.2", sha256="250b5179dba325bad6ca73b80f8f09f252e14270737763f243e4922db6d8d1ac")
    version("5.3.1", sha256="c22711f7623f38d9312616879c75e5981afc19c915f1a4d72cd2568558c2a2ed")
    version("5.3.0", sha256="4cf066cc37354729de62e1ed67055198a2df195d53039d6a9b83850339b0c2d7")
    version("5.2.2", sha256="b50b9cdfc60c9b3b00e0af609e2c14d5b8818db6de2416a205a43ed07f8f13b5")
    version("5.2.1", sha256="9f18d2276263cea1464eb84922451cdac36a4ddd9decb75603b32ea26257389f")
    version("5.2.0", sha256="92f6f23606a633357bcd60d465558ec4ddbe6d5266c310b1b2fe7eeb0b6d9be5")
    version("5.1.6", sha256="1c45c37bc2980cf9ddce84ddddc3529fb9774dc4dcea808424d77ace496e62fc")
    version("5.1.5", sha256="51fedd9dcea80efcdc3c4effac31950b7a9f70549b9d3761d70d76ff5b9ee655")
    version("5.1.4", sha256="6ebcf9abb258938ed7a30987699c81cfa63225c69f4bd4f6765d63df264094b3")
    version("5.1.3", sha256="2395e6e463c5ffbb168d3f182f0c90c0d8c32373c6f6d3d907f934ae1735bcd4")
    version("5.1.2", sha256="94f36bb8b43fb8d08d787179baedf5fb51ad3123456f0acdca699f3f36ad2d02")
    version("5.1.1", sha256="193b27e06ebe7ce32ead1b8a1e3b23e52b28df4ead87848146ee8261baaf840a")
    version("5.1.0", sha256="0e87f75499db3bcfa5abd6267332df98d8c5c26a614a956750a9140d1cce79ff")
    version("5.0.14", sha256="6b855326ce904e9081aeee8c9c1c3f0aa54aafc8250004173c9231d1dc877e90")
    version("5.0.13", sha256="b6cefd43f93ee0000a50b09cf3317cb3f88068952d0822c98f480c498ff17031")
    version("5.0.12", sha256="8096bbb85717c0705b4a220fe9dd6e03a70d621613f02139b8eacd7d83f9e75c")
    version("5.0.11", sha256="a9581f172c4a9a2406ee8cf1cca0d4e9003033b90787b56e2747ce27fab69f76")
    version("5.0.10", sha256="844b70c6a29a52dc03de443d81d8811fdb41cd54e706d7dbbea91022ee842efd")
    version("4.0.10", sha256="63f41db5d439483f1ae29d6b8ea7f341b9424587ce8331d5b0016654109c734e")
    version("4.0.9", sha256="db35ce671243bc39baf59f67773d0d4c4bd6c4c24aea49f4a6bb71a8576baf6c")
    version("3.3.4", sha256="fb1106680f4f0fc8c26f40ef73eb3eb335747274deda136927dc4a10fbe44420")
    version("3.3.3", sha256="5810b10757a88cd3dc07ca499be57bef06bc1c3b042e45248834491893a232be")
    version("3.3.2", sha256="299b634e19e04f234c6c9f2c6fc737ab3ad92c14d25fc25c97916c72e9f5561e")
    version("3.3.1", sha256="9d40bd30b75f896365771088d9a515a1a547d58db981b4082ab01a9a52d0e64d")
    version("3.3.0", sha256="ee23b8ef8b499c92696f6b5357db4897b3a9f3b442a67e05b20e0aa815a5dd83")
    version("3.2.5", sha256="6edd058cb3a784bd2f55ca5b9262c866eeaf9a1c70f3fc6a0523aa5a931405d7")
    version("3.2.4", sha256="4a3a16238568893461edc1d7addd145c7930b8003afdd439dac6035d22cd6642")
    version("3.2.3", sha256="9549b4d18324d03e7f28cbb7ba6a011440c0a03af2a753c69ffbe8c1e71355bc")
    version("3.2.2", sha256="0efa9b42fd1ccbdf2dfab4a0d59f24c463daf7f0c62bab6decad9d89e61894a9")
    version("3.2.1", sha256="383f7c18a06ae47fbe4eae47a8b45b6180cb04e70614309b34a750f0e4b158aa")
    version("3.2.0", sha256="de198fe4f4e116aad687f8ea216422bf4a21246a68bde2f0a52dec1e2b63610c")
    version("3.1.4", sha256="6ca94d7bf1218c126a0500ab0eea273eee02562bace42e0ed81878a23c21b7a0")
    version("3.1.3", sha256="30a714dfa09be9352c8db85fa99c62c194c8c32341ca1f059eb726559ad27439")
    version("3.1.2", sha256="f230660844cf8c8710949206298ced47c83b7ae45c1c4cd37b7036853c5628c0")
    version("3.1.1", sha256="ca03402d421ccbfe99c9d6133690f64e5a5ffec884faf4ddce17a56e5dbc4c67")
    version("3.1.0", sha256="6f9a8076bc4187639cdb29facae3ab7eda166c91644c6b678444b726705be40a")
    # fmt: on

    depends_on("c", type=BUILD)
    depends_on("cxx", type=BUILD)
    depends_on("fortran", type=BUILD)

    depends_on("autoconf", type=BUILD)
    depends_on("automake", type=BUILD)
    depends_on("libtool", type=BUILD)
    depends_on("m4", type=BUILD)

    variant(
        "link-libfabric",
        default=True,
        description="Link again LibFabric. Sometimes necessary to fix linker errors",
    )

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
    variant("dlopen-rtld-global", default=False, description="Add RTLD_GLOBAL to dlopen flags")
    variant("mpi", default=True, description="MPI support")
    variant("mpi-io", default=True, description="Use MPI I/O when available")
    variant(
        "gui-coolprop",
        default=False,
        description="Allow CoolProp fluids in GUI even when not available",
    )
    variant("med", default=False, description="Enable MED and MEDCoupling")
    variant("catalyst", default=True, description="Enable Catalyst")
    variant("melissa", default=True, description="Enable Melissa")
    variant("dot", default=False, description="Graphviz dot for diagrams in HTML")
    variant("zlib", default=False, description="Gzipped file support")
    variant("mathjax", default=False, description="MathJax for math in HTML")
    variant("frontend", default=True, description="Front-end elements")
    variant("backend", default=True, description="Back-end elements")
    variant("gui", default=True, description="Graphical User Interface")
    variant("largefile", default=True, description="Support for large files")
    variant("malloc-hooks", default=False, description="Use malloc hooks when available")
    variant("sockets", default=True, description="Allow communications through IP sockets")
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
        "blas", default=False, description="Use a BLAS library. Generally only useful for testing"
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
    conflicts("+scotch", when="+metis", msg="Only one mesh partitioning library can be specified")

    depends_on("py-setuptools", type=(BUILD, RUN))
    depends_on("py-numpy", type=(BUILD, RUN))
    depends_on("py-matplotlib+animation+fonts+latex+movies+image", type=(BUILD, RUN))
    depends_on("vtk+ffmpeg+xdmf+python", type=(BUILD, RUN))

    depends_on("py-pyqt5", when="+gui", type=(BUILD, RUN))
    depends_on("vtk+qt", when="+gui", type=(BUILD, RUN))

    depends_on("cuda", when="+cuda", type=BUILD)
    depends_on("hdf5", when="+hdf5", type=BUILD)
    depends_on("mpi", when="+mpi", type=BUILD)
    depends_on("blas", when="+blas", type=BUILD)
    depends_on("zlib", when="+zlib", type=BUILD)

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
            "blas",
            "mpi",
            "metis",
            "scotch",
            "cgns",
            "zlib",
            "melissa",
            "petsc",
            "hypre",
            "amgx",
            "catalyst",
        ]:
            if self.spec.variants.get(extra, default=TrueValue).value:
                args.append(f"--with-{extra}={self.spec[extra].prefix}")

        if self.spec.variants["med"].value:
            args.append(f"--with-med={self.spec['med'].prefix}")
            args.append(f"--with-medcoupling={self.spec['salome-medcoupling'].prefix}")

        return args
