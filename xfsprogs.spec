#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xfsprogs
Version  : 4.14.0
Release  : 18
URL      : https://cdn.kernel.org/pub/linux/utils/fs/xfs/xfsprogs/xfsprogs-4.14.0.tar.xz
Source0  : https://cdn.kernel.org/pub/linux/utils/fs/xfs/xfsprogs/xfsprogs-4.14.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: xfsprogs-bin
Requires: xfsprogs-lib
Requires: xfsprogs-doc
Requires: xfsprogs-locales
BuildRequires : e2fsprogs-dev
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(uuid)
BuildRequires : readline-dev
BuildRequires : util-linux-dev

%description
_____________________
See the file doc/INSTALL for build, installation and post-
install configuration steps.

%package bin
Summary: bin components for the xfsprogs package.
Group: Binaries

%description bin
bin components for the xfsprogs package.


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

%description doc
doc components for the xfsprogs package.


%package lib
Summary: lib components for the xfsprogs package.
Group: Libraries

%description lib
lib components for the xfsprogs package.


%package locales
Summary: locales components for the xfsprogs package.
Group: Default

%description locales
locales components for the xfsprogs package.


%prep
%setup -q -n xfsprogs-4.14.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1512997547
%configure --disable-static --enable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1512997547
rm -rf %{buildroot}
%make_install PKG_ROOT_SBIN_DIR=%{_sbindir} PKG_ROOT_LIB_DIR=%{_libdir} install-dev
%find_lang xfsprogs
## make_install_append content
mv libxlog/.libs/*.so* %{buildroot}%{_libdir}
mv libxfs/.libs/*.so* %{buildroot}%{_libdir}
mv libxcmd/.libs/*.so* %{buildroot}%{_libdir}
## make_install_append end

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
/usr/include/xfs/xfs_log_format.h
/usr/include/xfs/xfs_types.h
/usr/include/xfs/xqm.h
/usr/lib64/libhandle.so
/usr/lib64/libxcmd.so
/usr/lib64/libxfs.so
/usr/lib64/libxlog.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/xfsprogs/*
%doc /usr/share/man/man3/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*

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

%files locales -f xfsprogs.lang
%defattr(-,root,root,-)

