##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##
##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##
m4_define([v_maj], [0])
m4_define([v_min], [5])
m4_define([v_mic], [1])
m4_define([v_rev], m4_esyscmd([(svnversion "${SVN_REPO_PATH:-.}" | grep -v '\(export\|Unversioned directory\)' || echo 0) | awk -F : '{printf("%s\n", $1);}' | tr -d ' :MSP\n']))
m4_if(v_rev, [0], [m4_define([v_rev], m4_esyscmd([git log 2> /dev/null | (grep -m1 git-svn-id || echo 0) | sed -e 's/.*@\([0-9]*\).*/\1/' | tr -d '\n']))])
##--   When released, remove the dnl on the below line
m4_undefine([v_rev])
##--   When doing snapshots - change soname. remove dnl on below line
dnl m4_define([relname], [ver-pre-svn-07])
dnl m4_define([v_rel], [-release relname])
##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##
m4_ifdef([v_rev], [m4_define([v_ver], [v_maj.v_min.v_mic.v_rev])], [m4_define([v_ver], [v_maj.v_min.v_mic])])
m4_define([lt_cur], m4_eval(v_maj + v_min))
m4_define([lt_rev], v_mic)
m4_define([lt_age], v_min)
##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##
##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##

AC_INIT([etrophy], [v_ver], [enlightenment-devel@lists.sourceforge.net])
AC_PREREQ([2.52])
AC_CONFIG_SRCDIR([configure.ac])
AC_CONFIG_MACRO_DIR([m4])

AC_CONFIG_HEADERS([config.h])
AH_TOP([
#ifndef EFL_CONFIG_H__
#define EFL_CONFIG_H__
])
AH_BOTTOM([
#endif /* EFL_CONFIG_H__ */
])

AM_INIT_AUTOMAKE([1.6 dist-bzip2])
m4_ifdef([AM_SILENT_RULES], [AM_SILENT_RULES([yes])])

AC_LIBTOOL_WIN32_DLL
define([AC_LIBTOOL_LANG_F77_CONFIG], [:])dnl
AC_PROG_LIBTOOL

##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##
##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##
m4_ifdef([v_rev], , [m4_define([v_rev], [0])])
m4_ifdef([v_rel], , [m4_define([v_rel], [])])
AC_DEFINE_UNQUOTED(VMAJ, [v_maj], [Major version])
AC_DEFINE_UNQUOTED(VMIN, [v_min], [Minor version])
AC_DEFINE_UNQUOTED(VMIC, [v_mic], [Micro version])
AC_DEFINE_UNQUOTED(VREV, [v_rev], [Revison])
version_info="lt_cur:lt_rev:lt_age"
release_info="v_rel"
AC_SUBST(version_info)
AC_SUBST(release_info)
##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##
##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##
VMAJ=v_maj
AC_SUBST(VMAJ)

AC_DEFINE_UNQUOTED([SHARED_LIB_SUFFIX], ["$shrext_cmds"], [Suffix for shared objects])

### Default options with respect to host
AC_CANONICAL_BUILD
AC_CANONICAL_HOST


requirement_etrophy=""

AC_SUBST(MODULE_ARCH)
AC_DEFINE_UNQUOTED(MODULE_ARCH, "${MODULE_ARCH}", "Module architecture")

m4_ifdef([v_mic],
        [
        EFL_COMPILER_FLAG([-Wshadow])
        EFL_COMPILER_FLAG([-Wall])
        EFL_COMPILER_FLAG([-Wextra])
        EFL_COMPILER_FLAG([-W])
        ])

### Checks for programs
AC_PROG_CC

# doxygen program for documentation building

EFL_CHECK_DOXYGEN([build_doc="yes"], [build_doc="no"])

# python

AM_PATH_PYTHON([2.5], , [:])
AM_CONDITIONAL([HAVE_PYTHON], [test "$PYTHON" != : ])

# pkg-config

PKG_PROG_PKG_CONFIG

# Check whether pkg-config supports Requires.private

if $PKG_CONFIG --atleast-pkgconfig-version 0.22; then
   pkgconfig_requires_private="Requires.private"
else
   pkgconfig_requires_private="Requires"
fi
AC_SUBST(pkgconfig_requires_private)


### Checks for libraries

# Evil library for compilation on Windows

EFL_ETROPHY_BUILD=""
case "$host_os" in
   mingw*)
      PKG_CHECK_MODULES([EVIL], [evil >= 1.0.0])
      AC_DEFINE([HAVE_EVIL], [1], [Set to 1 if Evil library is installed])
      requirement_etrophy="evil ${requirement_etrophy}"
      EFL_ETROPHY_BUILD="-DEFL_ETROPHY_BUILD"
   ;;
esac
AC_SUBST(EFL_ETROPHY_BUILD)

# Dependencies for the library

PKG_CHECK_MODULES([ELEMENTARY],
   [
    elementary >= 1.7.0
    evas >= 1.7.0
    ecore-file >= 1.7.0
    ecore >= 1.7.0
    eet >= 1.7.0
    eina >= 1.7.0
   ])

if test "x$HAVE_GENEET" = "xfalse"; then
AC_MSG_ERROR([*** Geneet not found, make sure geneet.py is in your PATH])
fi

AC_ARG_WITH([edje-cc],
        [AC_HELP_STRING([--with-edje-cc=PATH],
            [specify a specific path to edje_cc])],
        [edje_cc=$withval;
        AC_MSG_NOTICE([edje_cc explicitly set to $edje_cc])
        ],[edje_cc=$(pkg-config --variable=prefix edje)/bin/edje_cc])
AC_SUBST(edje_cc)

requirement_etrophy="elementary >= 1.7.0 evas >= 1.7.0 ecore-file >= 1.7.0 ecore >= 1.7.0 eet >= 1.7.0 eina >= 1.7.0 ${requirement_etrophy}"

### Checks for header files
AC_CHECK_HEADERS([locale.h sys/resource.h])

EFL_CHECK_PATH_MAX

### Checks for compiler characteristics
AM_PROG_CC_C_O
AC_C_CONST
AC_PROG_CC_STDC
AC_HEADER_STDC
AC_C___ATTRIBUTE__

case "$host_os" in
   mingw32ce*)
      ETROPHY_CFLAGS="${ETROPHY_CFLAGS} -D_WIN32_WCE=0x0420"
      ;;
esac


### Checks for linker characteristics

lt_enable_auto_import=""
case "$host_os" in
   mingw*)
      lt_enable_auto_import="-Wl,--enable-auto-import"
      ;;
esac
AC_SUBST(lt_enable_auto_import)

AC_SUBST(requirement_etrophy)

AC_OUTPUT([
etrophy.pc
etrophy.spec
Makefile
src/Makefile
src/lib/Makefile
data/Makefile
data/theme/Makefile
doc/Makefile
doc/Doxyfile
])


#####################################################################
## Info

echo
echo
echo
echo "------------------------------------------------------------------------"
echo "$PACKAGE $VERSION"
echo "------------------------------------------------------------------------"
echo
echo "Configuration Options Summary:"
echo
echo "  Documentation........: ${build_doc}"
echo
echo "Compilation............: make (or gmake)"
echo "  CFLAGS...............: $CFLAGS"
echo "  LDFLAGS..............: $LDFLAGS"
echo
echo "Installation...........: make install (as root if needed, with 'su' or 'sudo')"
echo "  prefix...............: $prefix"
echo
