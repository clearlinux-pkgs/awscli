#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : awscli
Version  : 1.29.20
Release  : 1401
URL      : https://files.pythonhosted.org/packages/e8/38/05254f484d6a6bcd7ac88394c7ceb42a0f50baeb87d5d35a5af63f85a519/awscli-1.29.20.tar.gz
Source0  : https://files.pythonhosted.org/packages/e8/38/05254f484d6a6bcd7ac88394c7ceb42a0f50baeb87d5d35a5af63f85a519/awscli-1.29.20.tar.gz
Summary  : Universal Command Line Environment for AWS.
Group    : Development/Tools
License  : Apache-2.0
Requires: awscli-bin = %{version}-%{release}
Requires: awscli-license = %{version}-%{release}
Requires: awscli-python = %{version}-%{release}
Requires: awscli-python3 = %{version}-%{release}
Requires: pypi(botocore)
Requires: pypi(jmespath)
Requires: pypi(s3transfer)
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n awscli-1.29.20
cd %{_builddir}/awscli-1.29.20
pushd ..
cp -a awscli-1.29.20 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1691423489
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . docutils
pypi-dep-fix.py . PyYAML
pypi-dep-fix.py . rsa
pypi-dep-fix.py . colorama
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . docutils
pypi-dep-fix.py . PyYAML
pypi-dep-fix.py . rsa
pypi-dep-fix.py . colorama
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/awscli
cp %{_builddir}/awscli-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/awscli/4be62be059d3caeb4224228692644230d266368b || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
pypi-dep-fix.py %{buildroot} docutils
pypi-dep-fix.py %{buildroot} PyYAML
pypi-dep-fix.py %{buildroot} rsa
pypi-dep-fix.py %{buildroot} colorama
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
