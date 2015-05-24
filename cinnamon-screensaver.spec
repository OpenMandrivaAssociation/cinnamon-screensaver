#global _internal_version 8de7ff0

%global gtk3_version           2.99.3
%global dbus_version           0.90
%global dbus_glib_version      0.74
%global cinnamon_desktop_version 2.2.0
%global libgnomekbd_version    2.91.1

Summary: Cinnamon Screensaver
Name:    cinnamon-screensaver
Version: 2.4.0
Release: %mkrel 2
License: GPLv2+ and LGPLv2+
URL:     http://cinnamon.linuxmint.com
Group:   Graphical desktop/Cinnamon

Source0: %{name}-%{version}.tar.gz
#SourceGet0: https://github.com/linuxmint/cinnamon-screensaver/archive/%{version}.tar.gz

BuildRequires: pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires: pkgconfig(dbus-1) >= %{dbus_version}
BuildRequires: dbus-glib-devel >= %{dbus_glib_version}
BuildRequires: pkgconfig(cinnamon-desktop) >= %{cinnamon_desktop_version}
BuildRequires: pam-devel
BuildRequires: pkgconfig(nss)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xscrnsaver)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xinerama) 
BuildRequires: pkgconfig(xmu)
BuildRequires: pkgconfig(libgnomekbd) >= %{libgnomekbd_version}
# this is here because the configure tests look for protocol headers
BuildRequires: pkgconfig(xproto)
BuildRequires: intltool
BuildRequires: gnome-common
BuildRequires: pkgconfig(xxf86misc)
BuildRequires: pkgconfig(xxf86vm)
BuildRequires: pkgconfig(xtst)
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(systemd)

Requires: cinnamon-translations
Requires: cinnamon-desktop
# since we use it, and pam spams the log if a module is missing
Requires: gnome-keyring

# I have no idea why this is required, but for now, just get things to build
BuildRequires:  libxklavier-devel



%description
cinnamon-screensaver is a screen saver and locker.

%prep
%setup -q
echo "ACLOCAL_AMFLAGS = -I m4" >> Makefile.am
echo "AC_CONFIG_MACRO_DIR([m4])" >> configure.ac

NOCONFIGURE=1 ./autogen.sh

%build
%configure2_5x --with-mit-ext=no --without-console-kit
%make V=1

%install
%makeinstall_std

desktop-file-install                                     \
  --delete-original                                      \
  --remove-only-show-in=Xfce                             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications          \
  $RPM_BUILD_ROOT%{_datadir}/applications/cinnamon-screensaver.desktop

%files
%doc AUTHORS NEWS README COPYING
%{_bindir}/cinnamon-screensaver*
%{_datadir}/applications/cinnamon-screensaver.desktop
%{_datadir}/dbus-1/services/org.cinnamon.ScreenSaver.service
%{_libexecdir}/cinnamon-screensaver-dialog
%config %{_sysconfdir}/pam.d/cinnamon-screensaver
%doc %{_mandir}/man1/*.1.*



%changelog
* Wed Dec 03 2014 tmb <tmb> 2.4.0-2.mga5
+ Revision: 800487
- bump rel past testing

* Sun Nov 23 2014 joequant <joequant> 2.4.0-1.mga5
+ Revision: 798404
- upgrade to 2.4

* Wed Oct 15 2014 umeabot <umeabot> 2.2.4-4.mga5
+ Revision: 747459
- Second Mageia 5 Mass Rebuild

* Tue Sep 16 2014 umeabot <umeabot> 2.2.4-3.mga5
+ Revision: 678399
- Mageia 5 Mass Rebuild

* Thu Sep 04 2014 joequant <joequant> 2.2.4-2.mga5
+ Revision: 671955
- rebuild with new systemd

* Sat Aug 30 2014 joequant <joequant> 2.2.4-1.mga5
+ Revision: 669393
- update to 2.2.4
- upgrade to 2.2

* Wed Jan 08 2014 joequant <joequant> 2.0.3-2.mga5
+ Revision: 565561
- push to core/release

* Wed Jan 01 2014 joequant <joequant> 2.0.3-1.mga4
+ Revision: 563805
- upgrade to 2.0.3

* Wed Oct 23 2013 joequant <joequant> 2.0.2-1.mga4
+ Revision: 546392
- upgrade to 2.0.2

* Tue Oct 22 2013 umeabot <umeabot> 2.0.0-3.mga4
+ Revision: 545126
- Mageia 4 Mass Rebuild

* Tue Oct 15 2013 joequant <joequant> 2.0.0-2.mga4
+ Revision: 500822
- don't start up when running gnome

* Mon Oct 07 2013 joequant <joequant> 2.0.0-1.mga4
+ Revision: 492508
- remove upstream patch
- upgrade to 2.0.0

* Tue Oct 01 2013 joequant <joequant> 1.9.1-1.mga4
+ Revision: 490091
- change build requires to cinnamon-desktop
- upgrade to 1.9.1

* Mon Sep 02 2013 ennael <ennael> 1.8.0-5.mga4
+ Revision: 474351
- Rebuild against new gnome-desktop3

* Sun Aug 25 2013 joequant <joequant> 1.8.0-4.mga4
+ Revision: 471508
- remove selinux/fedora from pam

* Sun Aug 25 2013 joequant <joequant> 1.8.0-3.mga4
+ Revision: 471447
- remove xscreensaver conflict

* Fri Aug 23 2013 joequant <joequant> 1.8.0-2.mga4
+ Revision: 470131
- fix build requires

* Fri Aug 23 2013 joequant <joequant> 1.8.0-1.mga4
+ Revision: 470048
- add group information
- imported package cinnamon-screensaver

