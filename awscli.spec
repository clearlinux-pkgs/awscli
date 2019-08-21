#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : awscli
Version  : 1.16.223
Release  : 455
URL      : https://files.pythonhosted.org/packages/8b/ca/4604322373c1e18718e5b3611ba2460388cc0f0966657078c533f0203651/awscli-1.16.223.tar.gz
Source0  : https://files.pythonhosted.org/packages/8b/ca/4604322373c1e18718e5b3611ba2460388cc0f0966657078c533f0203651/awscli-1.16.223.tar.gz
Summary  : Universal Command Line Environment for AWS.
Group    : Development/Tools
License  : Apache-2.0
Requires: awscli-bin = %{version}-%{release}
Requires: awscli-license = %{version}-%{release}
Requires: awscli-python = %{version}-%{release}
Requires: awscli-python3 = %{version}-%{release}
Requires: PyYAML
Requires: argparse
Requires: botocore
Requires: colorama
Requires: docutils
Requires: jmespath
Requires: nose
Requires: rsa
Requires: s3transfer
Requires: wheel
BuildRequires : PyYAML
BuildRequires : argparse
BuildRequires : botocore
BuildRequires : buildreq-distutils3
BuildRequires : colorama
BuildRequires : docutils
BuildRequires : jmespath
BuildRequires : nose
BuildRequires : rsa
BuildRequires : s3transfer
BuildRequires : wheel

%description
aws-cli
        =======

%package bin
Summary: bin components for the awscli package.
Group: Binaries
Requires: awscli-license = %{version}-%{release}

%description bin
bin components for the awscli package.


%package license
Summary: license components for the awscli package.
Group: Default

%description license
license components for the awscli package.


%package python
Summary: python components for the awscli package.
Group: Default
Requires: awscli-python3 = %{version}-%{release}

%description python
python components for the awscli package.


%package python3
Summary: python3 components for the awscli package.
Group: Default
Requires: python3-core

%description python3
python3 components for the awscli package.


%prep
%setup -q -n awscli-1.16.223

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1566430764
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/awscli
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/awscli/LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/aws
/usr/bin/aws.cmd
/usr/bin/aws_bash_completer
/usr/bin/aws_completer
/usr/bin/aws_zsh_completer.sh

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/awscli/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
