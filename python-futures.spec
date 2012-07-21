%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(0)")}

%global oname  futures

Summary:       Backport of the concurrent.futures package from Python 3.2
Name:          python-futures
Version:       2.1.2
Release:       3%{?dist}
License:       BSD
Group:         Development/Libraries
URL:           http://code.google.com/p/pythonfutures/
Source0:       http://pypi.python.org/packages/source/f/futures/futures-%{version}.tar.gz
BuildRequires: python-setuptools-devel
BuildArch:     noarch

%description
The concurrent.futures module provides a high-level interface for
asynchronously executing callables.

%prep
%setup -q -n %{oname}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc CHANGES LICENSE 
%{python_sitelib}/concurrent
%{python_sitelib}/futures
%{python_sitelib}/futures-*.egg-info*

%changelog
* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Terje Rosten <terje.rosten@ntnu.no> - 2.1.2-2
- Remove old cruft
- Fix url and buildreq

* Mon Sep 26 2011 Terje Rosten <terje.rosten@ntnu.no> - 2.1.2-1
- initial package
