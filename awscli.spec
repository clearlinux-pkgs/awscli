#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : awscli
Version  : 1.14.14
Release  : 100
URL      : https://pypi.python.org/packages/48/40/6e01551b639f49b6365aefd7fb91f3d8200fa86065a024ae453a5f548db5/awscli-1.14.14.tar.gz
Source0  : https://pypi.python.org/packages/48/40/6e01551b639f49b6365aefd7fb91f3d8200fa86065a024ae453a5f548db5/awscli-1.14.14.tar.gz
Summary  : Universal Command Line Environment for AWS.
Group    : Development/Tools
License  : Apache-2.0
Requires: awscli-bin
Requires: awscli-legacypython
Requires: awscli-python3
Requires: awscli-python
Requires: PyYAML
Requires: botocore
Requires: rsa
Requires: s3transfer
BuildRequires : boto3
BuildRequires : botocore
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : s3transfer
BuildRequires : setuptools

%description
aws-cli
        =======

%package bin
Summary: bin components for the awscli package.
Group: Binaries

%description bin
bin components for the awscli package.


%package legacypython
Summary: legacypython components for the awscli package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the awscli package.


%package python
Summary: python components for the awscli package.
Group: Default
Requires: awscli-legacypython
Requires: awscli-python3

%description python
python components for the awscli package.


%package python3
Summary: python3 components for the awscli package.
Group: Default
Requires: python3-core

%description python3
python3 components for the awscli package.


%prep
%setup -q -n awscli-1.14.14

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1513876838
export CFLAGS="$CFLAGS -falign-functions=32 "
export FCFLAGS="$CFLAGS -falign-functions=32 "
export FFLAGS="$CFLAGS -falign-functions=32 "
export CXXFLAGS="$CXXFLAGS -falign-functions=32 "
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1513876838
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
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

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
