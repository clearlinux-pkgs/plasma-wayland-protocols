#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: fbbd4e3
#
# Source0 file verified with key 0x11968C44928CAEFC (bshah@mykolab.com)
#
Name     : plasma-wayland-protocols
Version  : 1.17.0
Release  : 25
URL      : https://download.kde.org/stable/plasma-wayland-protocols/plasma-wayland-protocols-1.17.0.tar.xz
Source0  : https://download.kde.org/stable/plasma-wayland-protocols/plasma-wayland-protocols-1.17.0.tar.xz
Source1  : https://download.kde.org/stable/plasma-wayland-protocols/plasma-wayland-protocols-1.17.0.tar.xz.sig
Source2  : 11968C44928CAEFC.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.1 MIT
Requires: plasma-wayland-protocols-data = %{version}-%{release}
Requires: plasma-wayland-protocols-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : pkg-config
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : wayland
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Plasma Wayland Protocols
This project provides the xml files of the non-standard wayland
protocols we use in Plasma.

%package data
Summary: data components for the plasma-wayland-protocols package.
Group: Data

%description data
data components for the plasma-wayland-protocols package.


%package dev
Summary: dev components for the plasma-wayland-protocols package.
Group: Development
Requires: plasma-wayland-protocols-data = %{version}-%{release}
Provides: plasma-wayland-protocols-devel = %{version}-%{release}
Requires: plasma-wayland-protocols = %{version}-%{release}

%description dev
dev components for the plasma-wayland-protocols package.


%package license
Summary: license components for the plasma-wayland-protocols package.
Group: Default

%description license
license components for the plasma-wayland-protocols package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 11968C44928CAEFC' gpg.status
%setup -q -n plasma-wayland-protocols-1.17.0
cd %{_builddir}/plasma-wayland-protocols-1.17.0
pushd ..
cp -a plasma-wayland-protocols-1.17.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742580844
mkdir -p clr-build
pushd clr-build
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
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
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
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
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
export SOURCE_DATE_EPOCH=1742580844
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/plasma-wayland-protocols
cp %{_builddir}/plasma-wayland-protocols-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/plasma-wayland-protocols/9a1929f4700d2407c70b507b3b2aaf6226a9543c || :
cp %{_builddir}/plasma-wayland-protocols-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/plasma-wayland-protocols/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/plasma-wayland-protocols-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/plasma-wayland-protocols/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/plasma-wayland-protocols-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/plasma-wayland-protocols/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/plasma-wayland-protocols-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/plasma-wayland-protocols/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/plasma-wayland-protocols/appmenu.xml
/usr/share/plasma-wayland-protocols/blur.xml
/usr/share/plasma-wayland-protocols/contrast.xml
/usr/share/plasma-wayland-protocols/dpms.xml
/usr/share/plasma-wayland-protocols/fake-input.xml
/usr/share/plasma-wayland-protocols/fullscreen-shell.xml
/usr/share/plasma-wayland-protocols/idle.xml
/usr/share/plasma-wayland-protocols/kde-external-brightness-v1.xml
/usr/share/plasma-wayland-protocols/kde-lockscreen-overlay-v1.xml
/usr/share/plasma-wayland-protocols/kde-output-device-v2.xml
/usr/share/plasma-wayland-protocols/kde-output-management-v2.xml
/usr/share/plasma-wayland-protocols/kde-output-order-v1.xml
/usr/share/plasma-wayland-protocols/kde-primary-output-v1.xml
/usr/share/plasma-wayland-protocols/kde-screen-edge-v1.xml
/usr/share/plasma-wayland-protocols/keystate.xml
/usr/share/plasma-wayland-protocols/org-kde-plasma-virtual-desktop.xml
/usr/share/plasma-wayland-protocols/output-management.xml
/usr/share/plasma-wayland-protocols/outputdevice.xml
/usr/share/plasma-wayland-protocols/plasma-shell.xml
/usr/share/plasma-wayland-protocols/plasma-virtual-desktop.xml
/usr/share/plasma-wayland-protocols/plasma-window-management.xml
/usr/share/plasma-wayland-protocols/remote-access.xml
/usr/share/plasma-wayland-protocols/screencast.xml
/usr/share/plasma-wayland-protocols/server-decoration-palette.xml
/usr/share/plasma-wayland-protocols/server-decoration.xml
/usr/share/plasma-wayland-protocols/shadow.xml
/usr/share/plasma-wayland-protocols/slide.xml
/usr/share/plasma-wayland-protocols/surface-extension.xml
/usr/share/plasma-wayland-protocols/text-input-unstable-v2.xml
/usr/share/plasma-wayland-protocols/text-input.xml
/usr/share/plasma-wayland-protocols/wayland-eglstream-controller.xml
/usr/share/plasma-wayland-protocols/zkde-screencast-unstable-v1.xml

%files dev
%defattr(-,root,root,-)
/usr/lib64/cmake/PlasmaWaylandProtocols/PlasmaWaylandProtocolsConfig.cmake
/usr/lib64/cmake/PlasmaWaylandProtocols/PlasmaWaylandProtocolsConfigVersion.cmake

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/plasma-wayland-protocols/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/plasma-wayland-protocols/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/plasma-wayland-protocols/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/plasma-wayland-protocols/9a1929f4700d2407c70b507b3b2aaf6226a9543c
/usr/share/package-licenses/plasma-wayland-protocols/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
