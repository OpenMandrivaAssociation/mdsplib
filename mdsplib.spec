
%define name	mdsplib
%define version	0.11
%define rel	1

Summary:	METAR Decoder Software Package Library
Name:		%name
Version:	%version
Release:	%mkrel %rel
License:	LGPL
Group:		System/Libraries
URL:		http://limulus.net/mdsplib/
Source:		http://limulus.net/mdsplib/mdsplib-0.11.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-root

%description
The MDSP Library provides a programmer with two functions, the major one
being DcdMETAR, which decodes a METAR into structures provided by the
library. Also prtDMETR, which prints out a decoded METAR structure.

The MDSP was written by Carl McCalla and released to the public by the
US National Weather Service. The MDSP Library is the original MDSP
modified to compile and run on *NIX systems.

%package devel
Summary:	METAR Decoder Software Package Library
Group:		Development/C

%description devel
The MDSP Library provides a programmer with two functions, the major one
being DcdMETAR, which decodes a METAR into structures provided by the
library. Also prtDMETR, which prints out a decoded METAR structure.

The MDSP was written by Carl McCalla and released to the public by the
US National Weather Service. The MDSP Library is the original MDSP
modified to compile and run on *NIX systems.

%prep
%setup -q

%build
%make CFLAGS="%optflags -fPIC"
ranlib libmetar.a

%install
rm -rf %{buildroot}
install -d -m755 %{buildroot}%{_includedir}
install -d -m755 %{buildroot}%{_libdir}
install -m644 metar.h %{buildroot}%{_includedir}
install -m644 libmetar.a %{buildroot}%{_libdir}

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc HISTORY README README.MDSP
%{_libdir}/libmetar.a
%{_includedir}/metar.h


