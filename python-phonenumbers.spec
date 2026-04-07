%define module phonenumbers
%bcond tests 1

Name:		python-phonenumbers
Version:	9.0.27
Release:	1
Summary:	Python library for parsing, formatting, storing and validating international phone numbers
License:	Apache-2.0
Group:		Development/Python
URL:		https://pypi.org/project/phonenumbers/
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
%endif

%description
Python version of Google's common library for parsing, formatting, storing
and validating international phone numbers.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
pytest tests/*test.py
%endif

%files
%doc README.md HISTORY.md
%license LICENSE
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
