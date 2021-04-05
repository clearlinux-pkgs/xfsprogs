#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xfsprogs
Version  : 5.11.0
Release  : 39
URL      : https://cdn.kernel.org/pub/linux/utils/fs/xfs/xfsprogs/xfsprogs-5.11.0.tar.xz
Source0  : https://cdn.kernel.org/pub/linux/utils/fs/xfs/xfsprogs/xfsprogs-5.11.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: xfsprogs-bin = %{version}-%{release}
Requires: xfsprogs-lib = %{version}-%{release}
Requires: xfsprogs-license = %{version}-%{release}
Requires: xfsprogs-locales = %{version}-%{release}
Requires: xfsprogs-man = %{version}-%{release}
BuildRequires : LVM2-dev
BuildRequires : e2fsprogs-dev
BuildRequires : icu4c-dev
BuildRequires : inih-dev
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(uuid)
BuildRequires : readline-dev
BuildRequires : systemd-dev
BuildRequires : util-linux-dev

%description
_____________________
See the file doc/INSTALL for build, installation and post-
install configuration steps.

%package bin
Summary: bin components for the xfsprogs package.
Group: Binaries
Requires: xfsprogs-license = %{version}-%{release}

%description bin
bin components for the xfsprogs package.


%package dev
Summary: dev components for the xfsprogs package.
Group: Development
Requires: xfsprogs-lib = %{version}-%{release}
Requires: xfsprogs-bin = %{version}-%{release}
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
Requires: xfsprogs-license = %{version}-%{release}

%description lib
lib components for the xfsprogs package.


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
%setup -q -n xfsprogs-5.11.0
cd %{_builddir}/xfsprogs-5.11.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1617649224
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --enable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1617649224
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xfsprogs
cp %{_builddir}/xfsprogs-5.11.0/debian/copyright %{buildroot}/usr/share/package-licenses/xfsprogs/37d59df178f349b9b48ddae9baf7de9fe0c41069
%make_install PKG_ROOT_SBIN_DIR=%{_sbindir} PKG_ROOT_LIB_DIR=%{_libdir} install-dev
%find_lang xfsprogs

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
%doc /usr/share/doc/xfsprogs/*

%files extras
%defattr(-,root,root,-)
/usr/bin/xfs_scrub_all
/usr/lib/systemd/system/xfs_scrub@.service
/usr/lib/systemd/system/xfs_scrub_all.service
/usr/lib/systemd/system/xfs_scrub_all.timer
/usr/lib/systemd/system/xfs_scrub_fail@.service
/usr/lib64/xfsprogs/xfs_scrub_all.cron
/usr/lib64/xfsprogs/xfs_scrub_fail

%files lib
%defattr(-,root,root,-)
/usr/lib64/libhandle.so.1
/usr/lib64/libhandle.so.1.0.3

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

