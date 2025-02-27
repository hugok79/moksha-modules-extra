%{!?_rel:%{expand:%%global _rel 0.r%(svnversion | sed 's/[^0-9].*$//' || echo 0000)}}
%define _missing_doc_files_terminate_build 0

Summary: ETrophy is a library that manages scores, trophies and unlockables.
Name: etrophy
Version: 0.5.1
Release: %{_rel}
License: BSD
Group: System Environment/Libraries
Source: http://download.enlightenment.org/releases/%{name}-%{version}.tar.gz
Packager: %{?_packager:%{_packager}}%{!?_packager:Rui Miguel Silva Seabra <rms@1407.org>}
Vendor: %{?_vendorinfo:%{_vendorinfo}}%{!?_vendorinfo:The Enlightenment Project (http://www.enlightenment.org/)}
Distribution: %{?_distribution:%{_distribution}}%{!?_distribution:%{_vendor}}
URL: http://www.enlightenment.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: efl, ecore
BuildRequires: efl-devel, ecore-devel

%description
ETrophy is a library that manages scores, trophies and unlockables. It will
store them and provide views to display them. Could be used by games based
on EFL.

%package devel
Summary: Etrophy headers, static libraries, documentation and test programs
Group: System Environment/Libraries
Requires: %{name} = %{version}

%description devel
Headers, static libraries, test programs and documentation for Etrophy

%prep
%setup -q

%build
%{configure} --prefix=%{_prefix}
%{__make} %{?_smp_mflags} %{?mflags}

%install
%{__make} %{?mflags_install} DESTDIR=$RPM_BUILD_ROOT install

%clean
test "x$RPM_BUILD_ROOT" != "x/" && rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS COPYING README
%{_libdir}/*.so.*
%{_datadir}/etrophy/*

%files devel
%defattr(-, root, root)
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/*

%changelog
