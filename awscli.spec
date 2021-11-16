#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : awscli
Version  : 1.22.6
Release  : 972
URL      : https://files.pythonhosted.org/packages/e9/cf/3afa943a050b6fbd9114ef1d6e855a9920cba4588a828c30d2d4db01cc1a/awscli-1.22.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/e9/cf/3afa943a050b6fbd9114ef1d6e855a9920cba4588a828c30d2d4db01cc1a/awscli-1.22.6.tar.gz
Summary  : Universal Command Line Environment for AWS.
Group    : Development/Tools
License  : Apache-2.0
Requires: awscli-bin = %{version}-%{release}
Requires: awscli-license = %{version}-%{release}
Requires: awscli-python = %{version}-%{release}
Requires: awscli-python3 = %{version}-%{release}
Requires: PyYAML
Requires: botocore
Requires: colorama
Requires: docutils
Requires: jmespath
Requires: rsa
Requires: s3transfer
BuildRequires : PyYAML
BuildRequires : botocore
BuildRequires : buildreq-distutils3
BuildRequires : colorama
BuildRequires : docutils
BuildRequires : jmespath
BuildRequires : rsa
BuildRequires : s3transfer
Patch1: deps.patch

%description
This package provides a unified command line interface to Amazon Web Services.

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
Provides: pypi(awscli)
Requires: pypi(botocore)
Requires: pypi(colorama)
Requires: pypi(docutils)
Requires: pypi(pyyaml)
Requires: pypi(rsa)
Requires: pypi(s3transfer)

%description python3
python3 components for the awscli package.


%prep
%setup -q -n awscli-1.22.6
cd %{_builddir}/awscli-1.22.6
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1637020833
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . docutils
pypi-dep-fix.py . PyYAML
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/awscli
cp %{_builddir}/awscli-1.22.6/LICENSE.txt %{buildroot}/usr/share/package-licenses/awscli/4be62be059d3caeb4224228692644230d266368b
python3 -tt setup.py build  install --root=%{buildroot}
pypi-dep-fix.py %{buildroot} docutils
pypi-dep-fix.py %{buildroot} PyYAML
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
/usr/share/package-licenses/awscli/4be62be059d3caeb4224228692644230d266368b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
