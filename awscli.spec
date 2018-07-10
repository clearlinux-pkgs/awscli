#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : awscli
Version  : 1.15.55
Release  : 204
URL      : https://github.com/aws/aws-cli/archive/1.15.55.tar.gz
Source0  : https://github.com/aws/aws-cli/archive/1.15.55.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: awscli-bin
Requires: awscli-python3
Requires: awscli-license
Requires: awscli-python
Requires: PyYAML
Requires: botocore
Requires: colorama
Requires: docutils
Requires: jmespath
Requires: nose
Requires: rsa
Requires: s3transfer
Requires: wheel
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
=======
aws-cli
=======
.. image:: https://travis-ci.org/aws/aws-cli.svg?branch=develop
:target: https://travis-ci.org/aws/aws-cli
:alt: Build Status

%package bin
Summary: bin components for the awscli package.
Group: Binaries
Requires: awscli-license

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
%setup -q -n aws-cli-1.15.55

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1531189978
find -name "*pyx" | xargs touch ||:
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/awscli
cp LICENSE.txt %{buildroot}/usr/share/doc/awscli/LICENSE.txt
cp doc/source/guzzle_sphinx_theme/LICENSE %{buildroot}/usr/share/doc/awscli/doc_source_guzzle_sphinx_theme_LICENSE
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

%files license
%defattr(-,root,root,-)
/usr/share/doc/awscli/LICENSE.txt
/usr/share/doc/awscli/doc_source_guzzle_sphinx_theme_LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
