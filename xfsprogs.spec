#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xfsprogs
Version  : 4.3.0
Release  : 8
URL      : ftp://oss.sgi.com/projects/xfs/cmd_tars/xfsprogs-4.3.0.tar.gz
Source0  : ftp://oss.sgi.com/projects/xfs/cmd_tars/xfsprogs-4.3.0.tar.gz
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
%setup -q -n xfsprogs-4.3.0

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%install
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
/usr/lib64/*.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/xfsprogs/*
%doc /usr/share/man/man3/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*

%files locales -f xfsprogs.lang 
%defattr(-,root,root,-)

