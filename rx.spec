Summary:	GNU Regular Expression Library
Summary(pl):	Biblioteka wyraøeÒ GNU
Name:		rx
Version:	1.5
Release:	1
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	ftp://sunsite.icm.edu.pl/pub/gnu/rx/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Regular Expression Library.

%description -l pl
Biblioteka wyraøeÒ GNU.

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
gzip -9nf ANNOUNCE BUILDING COOKOFF COPYING doc/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/librx.a
%{_includedir}/rxposix.h

%doc doc ANNOUNCE.gz BUILDING.gz COOKOFF.gz COPYING.gz
