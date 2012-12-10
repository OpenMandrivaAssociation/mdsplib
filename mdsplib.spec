
%define name	mdsplib
%define version	0.11
%define rel	3

%define major	0
%define libname	%mklibname metar %major
%define devname %mklibname metar -d

Summary:	METAR Decoder Software Package Library
Name:		%name
Version:	%version
Release:	%mkrel %rel
License:	LGPLv2+
Group:		System/Libraries
Source:		http://limulus.net/mdsplib/mdsplib-%version.tar.bz2
Patch0:		mdsplib-fmtstr.patch
# fedora patches
Patch10:	mdsplib-0.11-makefile.patch
Patch11:	mdsplib-0.11-nullcheck.patch
Patch12:	mdsplib-0.11-shared.patch
Patch13:	mdsplib-0.11-typeerror.patch
BuildRoot:	%{_tmppath}/%{name}-root

%description
The MDSP Library provides a programmer with two functions, the major one
being DcdMETAR, which decodes a METAR into structures provided by the
library. Also prtDMETR, which prints out a decoded METAR structure.

The MDSP was written by Carl McCalla and released to the public by the
US National Weather Service. The MDSP Library is the original MDSP
modified to compile and run on *NIX systems.

%package -n %libname
Summary:	METAR Decoder Software Package Library
Group:		System/Libraries

%description -n %libname
The MDSP Library provides a programmer with two functions, the major one
being DcdMETAR, which decodes a METAR into structures provided by the
library. Also prtDMETR, which prints out a decoded METAR structure.

The MDSP was written by Carl McCalla and released to the public by the
US National Weather Service. The MDSP Library is the original MDSP
modified to compile and run on *NIX systems.

This package contains the shared library.

%package -n %devname
Summary:	Development headers for libmetar
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	mdsplib-devel = %{version}-%{release}
Provides:	metar-devel = %{version}-%{release}
Obsoletes:	mdsplib-devel < 0.11-2

%description -n %devname
The MDSP Library provides a programmer with two functions, the major one
being DcdMETAR, which decodes a METAR into structures provided by the
library. Also prtDMETR, which prints out a decoded METAR structure.

The MDSP was written by Carl McCalla and released to the public by the
US National Weather Service. The MDSP Library is the original MDSP
modified to compile and run on *NIX systems.

This package contains the development headers.

%prep
%setup -q
%apply_patches

%build
%make CFLAGS="%optflags -fPIC"

%install
rm -rf %{buildroot}
%makeinstall_std libdir=%{_libdir}

%clean
rm -rf %{buildroot}

%files -n %libname
%defattr(-,root,root)
%{_libdir}/libmetar.so.%{major}*

%files -n %devname
%defattr(-,root,root)
%doc HISTORY README README.MDSP
%{_libdir}/libmetar.so
%{_includedir}/metar.h




%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.11-3mdv2011.0
+ Revision: 612843
- the mass rebuild of 2010.1 packages

* Sat Feb 06 2010 Anssi Hannula <anssi@mandriva.org> 0.11-2mdv2010.1
+ Revision: 501457
- fix format strings (fmtstr.patch)
- build shared library (shared.patch from fedora)
- fix build (typeerror.patch from fedora)
- fix null check (nullcheck.patch from fedora)
- add proper rules to makefile and use them (makefile.patch from fedora)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.11-1mdv2008.1
+ Revision: 136576
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 04 2006 Anssi Hannula <anssi@mandriva.org> 0.11-1mdv2007.0
+ Revision: 76639
- Import mdsplib

