#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v16
# autospec commit: 1bec16f
#
Name     : xfsprogs
Version  : 6.9.0
Release  : 63
URL      : https://mirrors.kernel.org/pub/linux/utils/fs/xfs/xfsprogs/xfsprogs-6.9.0.tar.gz
Source0  : https://mirrors.kernel.org/pub/linux/utils/fs/xfs/xfsprogs/xfsprogs-6.9.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: xfsprogs-bin = %{version}-%{release}
Requires: xfsprogs-config = %{version}-%{release}
Requires: xfsprogs-data = %{version}-%{release}
Requires: xfsprogs-lib = %{version}-%{release}
Requires: xfsprogs-libexec = %{version}-%{release}
Requires: xfsprogs-license = %{version}-%{release}
Requires: xfsprogs-locales = %{version}-%{release}
Requires: xfsprogs-man = %{version}-%{release}
BuildRequires : LVM2-dev
BuildRequires : buildreq-configure
BuildRequires : e2fsprogs-dev
BuildRequires : file
BuildRequires : icu4c-dev
BuildRequires : inih-dev
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(uuid)
BuildRequires : readline-dev
BuildRequires : systemd-dev
BuildRequires : userspace-rcu-dev
BuildRequires : util-linux-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
_____________________
See the file doc/INSTALL for build, installation and post-
install configuration steps.

%package bin
Summary: bin components for the xfsprogs package.
Group: Binaries
Requires: xfsprogs-data = %{version}-%{release}
Requires: xfsprogs-libexec = %{version}-%{release}
Requires: xfsprogs-config = %{version}-%{release}
Requires: xfsprogs-license = %{version}-%{release}

%description bin
bin components for the xfsprogs package.


%package config
Summary: config components for the xfsprogs package.
Group: Default

%description config
config components for the xfsprogs package.


%package data
Summary: data components for the xfsprogs package.
Group: Data

%description data
data components for the xfsprogs package.


%package dev
Summary: dev components for the xfsprogs package.
Group: Development
Requires: xfsprogs-lib = %{version}-%{release}
Requires: xfsprogs-bin = %{version}-%{release}
Requires: xfsprogs-data = %{version}-%{release}
Provides: xfsprogs-devel = %{version}-%{release}
Requires: xfsprogs = %{version}-%{release}

%description dev
dev components for the xfsprogs package.


%package doc
Summary: doc components for the xfsprogs package.
Group: Documentation
Requires: xfsprogs-man = %{version}-%{release}

%description doc
doc components for the xfsprogs package.


%package extras
Summary: extras components for the xfsprogs package.
Group: Default

%description extras
extras components for the xfsprogs package.


%package lib
Summary: lib components for the xfsprogs package.
Group: Libraries
Requires: xfsprogs-data = %{version}-%{release}
Requires: xfsprogs-libexec = %{version}-%{release}
Requires: xfsprogs-license = %{version}-%{release}

%description lib
lib components for the xfsprogs package.


%package libexec
Summary: libexec components for the xfsprogs package.
Group: Default
Requires: xfsprogs-config = %{version}-%{release}
Requires: xfsprogs-license = %{version}-%{release}

%description libexec
libexec components for the xfsprogs package.


%package license
Summary: license components for the xfsprogs package.
Group: Default

%description license
license components for the xfsprogs package.


%package locales
Summary: locales components for the xfsprogs package.
Group: Default

%description locales
locales components for the xfsprogs package.


%package man
Summary: man components for the xfsprogs package.
Group: Default

%description man
man components for the xfsprogs package.


%prep
%setup -q -n xfsprogs-6.9.0
cd %{_builddir}/xfsprogs-6.9.0
pushd ..
cp -a xfsprogs-6.9.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1721668345
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static --enable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static --enable-static
make  %{?_smp_mflags}
popd
%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1721668345
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xfsprogs
cp %{_builddir}/xfsprogs-%{version}/debian/copyright %{buildroot}/usr/share/package-licenses/xfsprogs/37d59df178f349b9b48ddae9baf7de9fe0c41069 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3 PKG_ROOT_SBIN_DIR=%{_sbindir} PKG_ROOT_LIB_DIR=%{_libdir} install-dev
popd
GOAMD64=v2
%make_install PKG_ROOT_SBIN_DIR=%{_sbindir} PKG_ROOT_LIB_DIR=%{_libdir} install-dev
%find_lang xfsprogs
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/mkfs.xfs
/V3/usr/bin/xfs_copy
/V3/usr/bin/xfs_db
/V3/usr/bin/xfs_estimate
/V3/usr/bin/xfs_fsr
/V3/usr/bin/xfs_growfs
/V3/usr/bin/xfs_io
/V3/usr/bin/xfs_logprint
/V3/usr/bin/xfs_mdrestore
/V3/usr/bin/xfs_quota
/V3/usr/bin/xfs_repair
/V3/usr/bin/xfs_rtcp
/V3/usr/bin/xfs_scrub
/V3/usr/bin/xfs_spaceman
/usr/bin/fsck.xfs
/usr/bin/mkfs.xfs
/usr/bin/xfs_admin
/usr/bin/xfs_bmap
/usr/bin/xfs_copy
/usr/bin/xfs_db
/usr/bin/xfs_estimate
/usr/bin/xfs_freeze
/usr/bin/xfs_fsr
/usr/bin/xfs_growfs
/usr/bin/xfs_info
/usr/bin/xfs_io
/usr/bin/xfs_logprint
/usr/bin/xfs_mdrestore
/usr/bin/xfs_metadump
/usr/bin/xfs_mkfile
/usr/bin/xfs_ncheck
/usr/bin/xfs_quota
/usr/bin/xfs_repair
/usr/bin/xfs_rtcp
/usr/bin/xfs_scrub
/usr/bin/xfs_spaceman

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/64-xfs.rules

%files data
%defattr(-,root,root,-)
/usr/share/xfsprogs/mkfs/dax_x86_64.conf
/usr/share/xfsprogs/mkfs/lts_4.19.conf
/usr/share/xfsprogs/mkfs/lts_5.10.conf
/usr/share/xfsprogs/mkfs/lts_5.15.conf
/usr/share/xfsprogs/mkfs/lts_5.4.conf
/usr/share/xfsprogs/mkfs/lts_6.1.conf
/usr/share/xfsprogs/mkfs/lts_6.6.conf
/usr/share/xfsprogs/xfs_scrub_all.cron

%files dev
%defattr(-,root,root,-)
/usr/include/xfs/handle.h
/usr/include/xfs/jdm.h
/usr/include/xfs/linux.h
/usr/include/xfs/xfs.h
/usr/include/xfs/xfs_arch.h
/usr/include/xfs/xfs_da_format.h
/usr/include/xfs/xfs_format.h
/usr/include/xfs/xfs_fs.h
/usr/include/xfs/xfs_fs_compat.h
/usr/include/xfs/xfs_log_format.h
/usr/include/xfs/xfs_types.h
/usr/include/xfs/xqm.h
/usr/lib64/libhandle.so
/usr/share/man/man2/ioctl_xfs_ag_geometry.2
/usr/share/man/man2/ioctl_xfs_bulkstat.2
/usr/share/man/man2/ioctl_xfs_fsbulkstat.2
/usr/share/man/man2/ioctl_xfs_fscounts.2
/usr/share/man/man2/ioctl_xfs_fsgeometry.2
/usr/share/man/man2/ioctl_xfs_fsgetxattr.2
/usr/share/man/man2/ioctl_xfs_fsgetxattra.2
/usr/share/man/man2/ioctl_xfs_fsinumbers.2
/usr/share/man/man2/ioctl_xfs_fssetxattr.2
/usr/share/man/man2/ioctl_xfs_getbmap.2
/usr/share/man/man2/ioctl_xfs_getbmapa.2
/usr/share/man/man2/ioctl_xfs_getbmapx.2
/usr/share/man/man2/ioctl_xfs_getresblks.2
/usr/share/man/man2/ioctl_xfs_goingdown.2
/usr/share/man/man2/ioctl_xfs_inumbers.2
/usr/share/man/man2/ioctl_xfs_scrub_metadata.2
/usr/share/man/man2/ioctl_xfs_setresblks.2
/usr/share/man/man3/attr_list_by_handle.3
/usr/share/man/man3/attr_multi_by_handle.3
/usr/share/man/man3/fd_to_handle.3
/usr/share/man/man3/free_handle.3
/usr/share/man/man3/fssetdm_by_handle.3
/usr/share/man/man3/getparentpaths_by_handle.3
/usr/share/man/man3/getparents_by_handle.3
/usr/share/man/man3/handle_to_fshandle.3
/usr/share/man/man3/open_by_handle.3
/usr/share/man/man3/path_to_fshandle.3
/usr/share/man/man3/path_to_handle.3
/usr/share/man/man3/readlink_by_handle.3
/usr/share/man/man3/xfsctl.3

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/xfsprogs/*

%files extras
%defattr(-,root,root,-)
/usr/bin/xfs_scrub_all
/usr/lib/systemd/system/xfs_scrub@.service
/usr/lib/systemd/system/xfs_scrub_all.service
/usr/lib/systemd/system/xfs_scrub_all.timer
/usr/lib/systemd/system/xfs_scrub_fail@.service

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libhandle.so.1.0.3
/usr/lib64/libhandle.so.1
/usr/lib64/libhandle.so.1.0.3

%files libexec
%defattr(-,root,root,-)
/usr/libexec/xfsprogs/xfs_scrub_fail

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xfsprogs/37d59df178f349b9b48ddae9baf7de9fe0c41069

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/projects.5
/usr/share/man/man5/projid.5
/usr/share/man/man5/xfs.5
/usr/share/man/man8/fsck.xfs.8
/usr/share/man/man8/mkfs.xfs.8
/usr/share/man/man8/xfs_admin.8
/usr/share/man/man8/xfs_bmap.8
/usr/share/man/man8/xfs_copy.8
/usr/share/man/man8/xfs_db.8
/usr/share/man/man8/xfs_estimate.8
/usr/share/man/man8/xfs_freeze.8
/usr/share/man/man8/xfs_fsr.8
/usr/share/man/man8/xfs_growfs.8
/usr/share/man/man8/xfs_info.8
/usr/share/man/man8/xfs_io.8
/usr/share/man/man8/xfs_logprint.8
/usr/share/man/man8/xfs_mdrestore.8
/usr/share/man/man8/xfs_metadump.8
/usr/share/man/man8/xfs_mkfile.8
/usr/share/man/man8/xfs_ncheck.8
/usr/share/man/man8/xfs_quota.8
/usr/share/man/man8/xfs_repair.8
/usr/share/man/man8/xfs_rtcp.8
/usr/share/man/man8/xfs_scrub.8
/usr/share/man/man8/xfs_scrub_all.8
/usr/share/man/man8/xfs_spaceman.8

%files locales -f xfsprogs.lang
%defattr(-,root,root,-)

