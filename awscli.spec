#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : awscli
Version  : 1.16.49
Release  : 290
URL      : https://files.pythonhosted.org/packages/92/5e/227dc1c87e8499cf1c1cc3d63dfbdd5a7af7ccf75acaa960ca458345e0e6/awscli-1.16.49.tar.gz
Source0  : https://files.pythonhosted.org/packages/92/5e/227dc1c87e8499cf1c1cc3d63dfbdd5a7af7ccf75acaa960ca458345e0e6/awscli-1.16.49.tar.gz
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
BuildRequires : buildreq-distutils3

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
%setup -q -n awscli-1.16.49

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541578489
python3 setup.py build

%install
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
