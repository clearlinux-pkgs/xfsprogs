#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xfsprogs
Version  : 4.17.0
Release  : 21
URL      : https://cdn.kernel.org/pub/linux/utils/fs/xfs/xfsprogs/xfsprogs-4.17.0.tar.xz
Source0  : https://cdn.kernel.org/pub/linux/utils/fs/xfs/xfsprogs/xfsprogs-4.17.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: xfsprogs-bin
Requires: xfsprogs-config
Requires: xfsprogs-lib
Requires: xfsprogs-license
Requires: xfsprogs-locales
Requires: xfsprogs-man
BuildRequires : e2fsprogs-dev
BuildRequires : icu4c-dev
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
Requires: xfsprogs-config
Requires: xfsprogs-license
Requires: xfsprogs-man

%description bin
bin components for the xfsprogs package.


%package config
Summary: config components for the xfsprogs package.
Group: Default

%description config
config components for the xfsprogs package.


%package dev
Summary: dev components for the xfsprogs package.
Group: Development
Requires: xfsprogs-lib
Requires: xfsprogs-bin
Provides: xfsprogs-devel

%description dev
dev components for the xfsprogs package.


%package doc
Summary: doc components for the xfsprogs package.
Group: Documentation
Requires: xfsprogs-man

%description doc
doc components for the xfsprogs package.


%package lib
Summary: lib components for the xfsprogs package.
Group: Libraries
Requires: xfsprogs-license

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
%setup -q -n xfsprogs-4.17.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530236103
%configure --disable-static --enable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1530236103
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/xfsprogs
cp doc/COPYING %{buildroot}/usr/share/doc/xfsprogs/doc_COPYING
cp debian/copyright %{buildroot}/usr/share/doc/xfsprogs/debian_copyright
%make_install PKG_ROOT_SBIN_DIR=%{_sbindir} PKG_ROOT_LIB_DIR=%{_libdir} install-dev
%find_lang xfsprogs
## make_install_append content
mv libxlog/.libs/*.so* %{buildroot}%{_libdir}
mv libxfs/.libs/*.so* %{buildroot}%{_libdir}
mv libxcmd/.libs/*.so* %{buildroot}%{_libdir}
## make_install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/xfsprogs/xfs_scrub_all.cron
/usr/lib64/xfsprogs/xfs_scrub_fail

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
/usr/bin/xfs_scrub_all
/usr/bin/xfs_spaceman

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/xfs_scrub@.service
/usr/lib/systemd/system/xfs_scrub_all.service
/usr/lib/systemd/system/xfs_scrub_all.timer
/usr/lib/systemd/system/xfs_scrub_fail@.service

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
/usr/include/xfs/xfs_log_format.h
/usr/include/xfs/xfs_types.h
/usr/include/xfs/xqm.h
/usr/lib64/libhandle.so
/usr/lib64/libxcmd.so
/usr/lib64/libxfs.so
/usr/lib64/libxlog.so

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/xfsprogs/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libhandle.so.1
/usr/lib64/libhandle.so.1.0.3
/usr/lib64/libxcmd.so.0
/usr/lib64/libxcmd.so.0.0.0
/usr/lib64/libxfs.so.0
/usr/lib64/libxfs.so.0.0.0
/usr/lib64/libxlog.so.0
/usr/lib64/libxlog.so.0.0.0

%files license
%defattr(-,root,root,-)
/usr/share/doc/xfsprogs/COPYING
/usr/share/doc/xfsprogs/doc_COPYING

%files man
%defattr(-,root,root,-)
/usr/share/man/man2/ioctl_xfs_scrub_metadata.2
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

