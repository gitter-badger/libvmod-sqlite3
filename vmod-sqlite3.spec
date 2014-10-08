Summary: SQLite3 VMOD for Varnish
Name: vmod-sqlite3
Version: 0.1
Release: 1%{?dist}
License: BSD
Group: System Environment/Daemons
Source0: libvmod-sqlite3-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: varnish > 3.0
BuildRequires: make
BuildRequires: python-docutils
%description
SQLite3 VMOD
%prep
%setup -n libvmod-sqlite3
%build
./configure VARNISHSRC=%{VARNISHSRC} \
    VMODDIR="$(PKG_CONFIG_PATH=%{VARNISHSRC} \
    pkg-config --variable=vmoddir varnishapi)" \
    --prefix=/usr/ --docdir='${datarootdir}/doc/%{name}'
make
make check
%install
make install DESTDIR=%{buildroot}
%clean
rm -rf %{buildroot}
%files
%defattr(-,root,root,-)
%{_libdir}/varnis*/vmods/
%doc /usr/share/doc/%{name}/*
%changelog
* Wed Oct  8 2014 Federico G. Schwindt <fgsch@lodoss.net> - 0.1-1
- Initial version.
