%define module phonenumbers
%bcond_without tests

Name:		python-phonenumbers
Version:	9.0.6
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/p/phonenumbers/phonenumbers-%{version}.tar.gz
Summary:	Python version of
URL:		https://pypi.org/project/phonenumbers/
License:	Apache License 2.0
Group:		Development/Python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
%endif

%description
Python version of Google's common library for parsing, formatting, storing and validating international phone numbers.

%prep
%autosetup -p1 -n %{module}-%{version}
# Remove bundled egg-info
rm -rf %{module}.egg-info

# Remove git badge remote images from README
sed -i '4d;' README.md

%build
%py_build

%install
%py_install

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitearch}:${PWD}"
%{__python} -m pytest tests/*test.py
%endif

%files
%{py_sitedir}/phonenumbers
%{py_sitedir}/phonenumbers-%{version}*-info
%doc README.md HISTORY.md
%license LICENSE
