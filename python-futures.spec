%{?scl:%scl_package python-futures}
%{!?scl:%global pkg_name %{name}}

Summary:       Backport of the concurrent.futures package from Python 3.2
Name:          %{?scl_prefix}python-futures
Version:       3.1.1
Release:       3%{?dist}
License:       Python
Group:         Development/Libraries
URL:           https://github.com/agronholm/pythonfutures
Source0:       https://files.pythonhosted.org/packages/source/f/futures/futures-%{version}.tar.gz
BuildRequires: python2-devel
BuildArch:     noarch
%{?scl:Requires: %scl_runtime}
%{?scl:BuildRequires: %scl-scldevel}

%description
The concurrent.futures module provides a high-level interface for
asynchronously executing callables.

%package -n %{?scl_prefix}python2-futures
Summary:        %{summary}
%{!?scl:%{?python_provide:%python_provide python2-futures}}
Provides:  %{?scl_prefix}python-futures = %{version}-%{release}
Obsoletes: %{?scl_prefix}python-futures < %{version}-%{release}

%description -n %{?scl_prefix}python2-futures
The concurrent.futures module provides a high-level interface for
asynchronously executing callables.

%prep
%setup -q -n futures-%{version}

%build
%{?scl:scl enable %{scl} - << "EOF"}
%{py2_build}
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - << "EOF"}
%{py2_install -- --prefix %{?_prefix}}
%{?scl:EOF}

%files -n %{?scl_prefix}python2-futures
%license LICENSE
%doc CHANGES
%{python2_sitelib}/concurrent
%{python2_sitelib}/futures-*.egg-info*

%changelog
* Fri Sep 22 2017 Augusto Caringi <acaringi@redhat.com> - 3.1.1-3
- scl conversion

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 18 2017 Terje Rosten <terje.rosten@ntnu.no> - 3.1.1-1
- 3.1.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan  4 2017 Peter Robinson <pbrobinson@fedoraproject.org> 3.0.5-2
- Obsolete/provide python-futures

* Mon Nov 21 2016 Orion Poplawski <orion@cora.nwra.com> - 3.0.5-1
- Update to 3.0.5
- Ship python2-futures

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
