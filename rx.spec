Summary:	GNU Regular Expression Library
Summary(pl):	Biblioteka wyra¿eñ GNU
Name:		rx
Version:	1.5
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://sunsite.icm.edu.pl/pub/gnu/rx/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Regular Expression Library.

%description -l pl
Biblioteka wyra¿eñ GNU.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}
install -d $RPM_BUILD_ROOT%{_includedir}

install -c rx/librx.a $RPM_BUILD_ROOT%{_libdir}/librx.a
install -c rx/inst-rxposix.h $RPM_BUILD_ROOT%{_includedir}/rxposix.h

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/librx.a
%{_includedir}/rxposix.h

%doc doc ANNOUNCE BUILDING COOKOFF COPYING
