#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : awscli
Version  : 1.15.4
Release  : 167
URL      : https://pypi.python.org/packages/b8/0d/8266105c882c291d0a37a54397e30964608d2365cc2501cf8977455e098d/awscli-1.15.4.tar.gz
Source0  : https://pypi.python.org/packages/b8/0d/8266105c882c291d0a37a54397e30964608d2365cc2501cf8977455e098d/awscli-1.15.4.tar.gz
Summary  : Universal Command Line Environment for AWS.
Group    : Development/Tools
License  : Apache-2.0
Requires: awscli-bin
Requires: awscli-python3
Requires: awscli-python
Requires: PyYAML
Requires: argparse
Requires: botocore
Requires: colorama
Requires: docutils
Requires: nose
Requires: python-mock
Requires: rsa
Requires: s3transfer
Requires: tox
Requires: wheel
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


%package python
Summary: python components for the awscli package.
Group: Default
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
%setup -q -n awscli-1.15.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523403169
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
