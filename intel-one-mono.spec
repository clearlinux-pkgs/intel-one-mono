#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v18
# autospec commit: 356da62
#
Name     : intel-one-mono
Version  : 1.4.0
Release  : 6
URL      : https://github.com/intel/intel-one-mono/archive/V1.4.0/intel-one-mono-1.4.0.tar.gz
Source0  : https://github.com/intel/intel-one-mono/archive/V1.4.0/intel-one-mono-1.4.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : OFL-1.1
Requires: intel-one-mono-data = %{version}-%{release}
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Add-Makefile-for-install.patch

%description
# Intel One Mono Typeface
![Image of Intel One Mono character set](https://github.com/intel/intel-one-mono/assets/130394986/6c921cf4-f614-41bd-a909-363bb19f9a30)

%package data
Summary: data components for the intel-one-mono package.
Group: Data

%description data
data components for the intel-one-mono package.


%prep
%setup -q -n intel-one-mono-1.4.0
cd %{_builddir}/intel-one-mono-1.4.0
%patch -P 1 -p1
pushd ..
cp -a intel-one-mono-1.4.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1722265458
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
make  %{?_smp_mflags}

pushd ../buildavx2
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1722265458
rm -rf %{buildroot}
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/fonts/X11/OTF/IntelOneMono-Bold.otf
/usr/share/fonts/X11/OTF/IntelOneMono-BoldItalic.otf
/usr/share/fonts/X11/OTF/IntelOneMono-Italic.otf
/usr/share/fonts/X11/OTF/IntelOneMono-Light.otf
/usr/share/fonts/X11/OTF/IntelOneMono-LightItalic.otf
/usr/share/fonts/X11/OTF/IntelOneMono-Medium.otf
/usr/share/fonts/X11/OTF/IntelOneMono-MediumItalic.otf
/usr/share/fonts/X11/OTF/IntelOneMono-Regular.otf
/usr/share/fonts/X11/TTF/IntelOneMono-Bold.ttf
/usr/share/fonts/X11/TTF/IntelOneMono-BoldItalic.ttf
/usr/share/fonts/X11/TTF/IntelOneMono-Italic.ttf
/usr/share/fonts/X11/TTF/IntelOneMono-Light.ttf
/usr/share/fonts/X11/TTF/IntelOneMono-LightItalic.ttf
/usr/share/fonts/X11/TTF/IntelOneMono-Medium.ttf
/usr/share/fonts/X11/TTF/IntelOneMono-MediumItalic.ttf
/usr/share/fonts/X11/TTF/IntelOneMono-Regular.ttf
