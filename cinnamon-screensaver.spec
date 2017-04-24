#global _internal_version 8de7ff0

%global gtk3_version           2.99.3
%global dbus_version           0.90
%global dbus_glib_version      0.74
%global cinnamon_desktop_version 2.2.0
%global libgnomekbd_version    2.91.1


%define major   0
%define girmajor   1.0
%define libname %mklibname %{name} %{major}
%define libdev  %mklibname %{name} -d
%define girlib    %mklibname %{name}-gir %{girmajor}

Summary: Cinnamon Screensaver
Name:    cinnamon-screensaver
Version: 3.2.13
Release: 1
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
BuildRequires: pkgconfig(webkit2gtk-4.0)

Requires: cinnamon-translations
Requires: cinnamon-desktop
# since we use it, and pam spams the log if a module is missing
Requires: gnome-keyring

# I have no idea why this is required, but for now, just get things to build
BuildRequires:  libxklavier-devel



%description
cinnamon-screensaver is a screen saver and locker.


#--------------------------------------------------------------------

%package -n %libname
Summary:  Libraries for %name
License:  LGPLv2+
Group:    System/Libraries

%description -n %libname
Libraries for %name

#--------------------------------------------------------------------

%package -n %{girlib}
Summary: GObject introspection interface library for %{name}
Group: System/Libraries
Requires: %{libname} = %{version}-%{release}

%description -n %{girlib}
GObject introspection interface library for %{name}.

#--------------------------------------------------------------------

%package -n %libdev
Summary:  Libraries and headers for libcinnamon-screensaver
License:  LGPLv2+
Group:    Development/C
Requires: %{libname} = %{version}-%{release}
Requires: %{girlib} = %{version}-%{release}
Requires: gtk3-devel >= %{gtk3_version}
Requires: glib2-devel >= %{glib2_version}
Requires: startup-notification-devel >= %{startup_notification_version}

%description -n %libdev
Libraries and header files for the CINNAMON-internal private library
libcinnamondesktop.

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
%{_libexecdir}/cinnamon-screensaver-pam-helper
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/scalable/*/*.svg
%config %{_sysconfdir}/pam.d/cinnamon-screensaver

%files -n %libname
%{_libdir}/libcscreensaver*.so.%{major}*

%files -n %{girlib}
%{_libdir}/girepository-1.0/C*-%{girmajor}.typelib

%files -n %libdev
%{_libdir}/libcscreensaver.so
%{_libdir}/pkgconfig/cscreensaver.pc
%{_includedir}/cinnamon-screensaver/
%{_datadir}/gir-1.0/C*-%{girmajor}.gir

