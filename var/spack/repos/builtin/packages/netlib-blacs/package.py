# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import re

from spack.package import *


INTERFACES = ["underscore", "none", "upper", "f77_is_f2c"]


def interface_to_flag(interface):
    if interface == "underscore":
        return "-DAdd_"
    if interface == "none":
        return "-DNoChange"
    if interface == "upper":
        return "-DUpCase"
    if interface == "f77_is_f2c":
        return "-Df77IsF2C"


class NetlibBlacs(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "http://www.netlib.org/blacs/mpiblacs.tgz"

    version("mpiblacs", sha256="88dd7265d412022948debb7a2737226cd53a3bf73b0b62fc55ceb3ccc8a598f7")

    maintainers("Pencilcaseman")

    license("https://www.netlib.org/scalapack/LICENSE", checked_by="Pencilcaseman")

    arch = "mpi"
    build_targets = [arch]

    variant(
        "suffix",
        default="LINUX",
        description="The platform identifier to suffix to the end of library names",
    )

    variant(
        "debug",
        default=False,
        description="Provide more debug information at the cost of performance",
    )

    variant(
        "interface",
        default="underscore",
        values=INTERFACES,
        description="The Fortran 77 to C interface to be used",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")

    depends_on("mpi", type=("build", "run"))

    def autoreconf(self, spec, prefix):
        # Prevent sanity check from killing the build
        touch("configure")

    def configure(self, spec, prefix):
        config = [
            "SHELL = /bin/sh",
            f"BTOPdir = {os.getcwd()}",
            f"COMMLIB = {self.arch.upper()}",
            f"PLAT = {self.spec.variants['suffix'].value}",
            f"BLACSDBGLVL = {1 if self.spec.variants['debug'].value else 0}",
            "BLACSdir    = $(BTOPdir)/LIB",
            "BLACSFINIT  = $(BLACSdir)/blacsF77init.a",
            "BLACSCINIT  = $(BLACSdir)/blacsCinit.a",
            "BLACSLIB    = $(BLACSdir)/blacs.a",
            f"MPIdir = {self.spec['mpi'].prefix}",
            "MPILIBdir = $(MPIdir)/lib/",
            "MPIINCdir = $(MPIdir)/include",
            f"MPILIB = {self.spec['mpi'].libs}",
            "BTLIBS = $(BLACSFINIT) $(BLACSLIB) $(BLACSFINIT) $(MPILIB)",
            "INSTdir = $(BTOPdir)/INSTALL/EXE",
            "TESTdir = $(BTOPdir)/TESTING/EXE",
            "FTESTexe = $(TESTdir)/xFbtest_$(COMMLIB)-$(PLAT)-$(BLACSDBGLVL)",
            "CTESTexe = $(TESTdir)/xCbtest_$(COMMLIB)-$(PLAT)-$(BLACSDBGLVL)",
            #
            "SYSINC = -I$(MPIINCdir)",
            f"INTFACE = {interface_to_flag(self.spec.variants['interface'].value)}",
            # DEFBSTOP   = -DDefBSTop="'1'"
            # DEFCOMBTOP = -DDefCombTop="'1'"
            "SENDIS = ",
            "BUFF = ",
            "TRANSCOMM = -DCSameF77",  # TODO: Fiddle?
            "WHATMPI =",
            "SYSERRORS = ",
            "DEBUGLVL = -DBlacsDebugLvl=$(BLACSDBGLVL)",
            "DEFS1 = -DSYSINC $(SYSINC) $(INTFACE) $(DEFBSTOP) $(DEFCOMBTOP) $(DEBUGLVL)",
            "BLACSDEFS = $(DEFS1) $(SENDIS) $(BUFF) $(TRANSCOMM) $(WHATMPI) $(SYSERRORS)",
            #
            f"F77            = {self.spec['mpi'].mpif77}",
            "F77NO_OPTFLAGS = ",
            "F77FLAGS       = $(F77NO_OPTFLAGS) -O3",
            "F77LOADER      = $(F77)",
            "F77LOADFLAGS   = ",
            f"CC            = {self.spec['mpi'].mpicc}",
            "CCFLAGS        = -O3 -Wno-implicit-function-declaration",
            "CCLOADER       = $(CC)",
            "CCLOADFLAGS    = ",
            "ARCH      = ar",
            "ARCHFLAGS = r",
            "RANLIB    = ranlib",
        ]

        with open("Bmake.inc", "w") as bmake:
            bmake.write("\n".join(config))

    def install(self, spec, prefix):
        mkdirp("blacs_include")

        for root, dirs, files in os.walk(self.stage.source_path):
            for filename in files:
                if filename.endswith(".h"):
                    filepath = join_path(root, filename)
                    copy(filepath, "blacs_include")

        install_tree("LIB", prefix.lib)
        install_tree("blacs_include", prefix.include)
