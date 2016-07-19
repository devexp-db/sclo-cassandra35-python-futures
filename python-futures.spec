Summary:       Backport of the concurrent.futures package from Python 3.2
Name:          python-futures
Version:       3.0.4
Release:       3%{?dist}
License:       BSD
Group:         Development/Libraries
URL:           https://github.com/agronholm/pythonfutures
Source0:       https://pypi.python.org/packages/source/f/futures/futures-%{version}.tar.gz
BuildRequires: python2-devel
BuildArch:     noarch
%{?python_provide:%python_provide python-futures}

%description
The concurrent.futures module provides a high-level interface for
asynchronously executing callables.

%prep
%setup -q -n futures-%{version}

%build
%{py2_build}

%install
%{py2_install}

%files
%license LICENSE
%doc CHANGES
%{python2_sitelib}/concurrent
%{python2_sitelib}/futures-*.egg-info*

%changelog
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.4-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Terje Rosten <terje.rosten@ntnu.no> - 3.0.4-1
- 3.0.4

* Wed Jun 24 2015 Terje Rosten <terje.rosten@ntnu.no> - 3.0.3-1
- 3.0.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 07 2015 Terje Rosten <terje.rosten@ntnu.no> - 3.0.2-1
- 3.0.2

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 2.1.6-3
- Replace python-setuptools-devel BR with python-setuptools

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 20 2014 Terje Rosten <terje.rosten@ntnu.no> - 2.1.6-1
- 2.1.6

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 10 2012 Terje Rosten <terje.rosten@ntnu.no> - 2.1.3-1
- 2.1.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Terje Rosten <terje.rosten@ntnu.no> - 2.1.2-2
- Remove old cruft
- Fix url and buildreq

* Mon Sep 26 2011 Terje Rosten <terje.rosten@ntnu.no> - 2.1.2-1
- initial package
