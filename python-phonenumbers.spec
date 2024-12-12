Name:		python-phonenumbers
Version:	8.13.51
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/phonenumbers/phonenumbers-%{version}.tar.gz
Summary:	Python version of
URL:		https://pypi.org/project/phonenumbers/
License:	Apache License 2.0
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Python version of Google's common library for parsing, formatting, storing and validating international phone numbers.

%prep
%autosetup -p1 -n phonenumbers-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/phonenumbers
%{py_sitedir}/phonenumbers-*.*-info
