Summary:	GNU Regular Expression Library
Summary(pl.UTF-8):   Biblioteka wyrażeń regularnych GNU
Name:		rx
Version:	1.5
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.gnu.org/pub/gnu/rx/%{name}-%{version}.tar.gz
# Source0-md5:	e44e5f6ff9fd8ca9d46bda42bcacee5e
Patch0:		%{name}-warnings.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Regular Expression Library.

%description -l pl.UTF-8
Biblioteka wyrażeń regularnych GNU.

%prep
#%setup -q
# workaround for tar (some paths contain `..', use -P)
%setup -qcT
tar xz -P -f %{SOURCE0} -C ..
%patch0 -p1

%build
cp -f /usr/share/automake/config.* .
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
	libdir=$RPM_BUILD_ROOT%{_libdir}

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
