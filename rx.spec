Summary:	GNU Regular Expression Library
Summary(pl):	Biblioteka wyra¿eñ regularnych GNU
Name:		rx
Version:	1.5
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.gnu.org/pub/gnu/rx/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Regular Expression Library.

%description -l pl
Biblioteka wyra¿eñ regularnych GNU.

%prep
%setup -q

%build
%{__autoconf}
cd rx
%{__autoconf}
cd ..
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix},%{_infodir}}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	exec_prefix=$RPM_BUILD_ROOT%{_prefix}

install doc/rx.info $RPM_BUILD_ROOT%{_infodir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc ANNOUNCE BUILDING COOKOFF
%{_libdir}/librx.a
%{_includedir}/rxposix.h
%{_infodir}/*.info*
