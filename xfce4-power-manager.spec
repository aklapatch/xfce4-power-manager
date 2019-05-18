#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xfce4-power-manager
Version  : 1.6.2
Release  : 1
URL      : https://archive.xfce.org/src/xfce/xfce4-power-manager/1.6/xfce4-power-manager-1.6.2.tar.bz2
Source0  : https://archive.xfce.org/src/xfce/xfce4-power-manager/1.6/xfce4-power-manager-1.6.2.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: xfce4-power-manager-bin = %{version}-%{release}
Requires: xfce4-power-manager-data = %{version}-%{release}
Requires: xfce4-power-manager-locales = %{version}-%{release}
Requires: xfce4-power-manager-man = %{version}-%{release}
BuildRequires : intltool
BuildRequires : libXScrnSaver-dev
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libnotify)
BuildRequires : pkgconfig(libxfce4ui-2)
BuildRequires : pkgconfig(libxfce4util-1.0)
BuildRequires : pkgconfig(libxfconf-0)
BuildRequires : pkgconfig(upower-glib)
BuildRequires : pkgconfig(xrandr)

%description
What is it?
===========
This software is a power manager for the Xfce desktop, Xfce power manager manages the power sources
on the computer and the devices that can be controlled to reduce their power consumption
(such as LCD brightness level, monitor sleep).
In addition, xfce4-power-manager provides a set of freedesktop-compliant DBus interfaces to
inform other applications about current power level so that they can adjust their power consumption.

%package bin
Summary: bin components for the xfce4-power-manager package.
Group: Binaries
Requires: xfce4-power-manager-data = %{version}-%{release}

%description bin
bin components for the xfce4-power-manager package.


%package data
Summary: data components for the xfce4-power-manager package.
Group: Data

%description data
data components for the xfce4-power-manager package.


%package locales
Summary: locales components for the xfce4-power-manager package.
Group: Default

%description locales
locales components for the xfce4-power-manager package.


%package man
Summary: man components for the xfce4-power-manager package.
Group: Default

%description man
man components for the xfce4-power-manager package.


%prep
%setup -q -n xfce4-power-manager-1.6.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1558196463
export GCC_IGNORE_WERROR=1
export LDFLAGS="${LDFLAGS} -fno-lto"
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1558196463
rm -rf %{buildroot}
%make_install
%find_lang xfce4-power-manager

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xfce4-pm-helper
/usr/bin/xfce4-power-manager
/usr/bin/xfce4-power-manager-settings
/usr/bin/xfpm-power-backlight-helper

%files data
%defattr(-,root,root,-)
/usr/share/applications/xfce4-power-manager-settings.desktop
/usr/share/icons/hicolor/32x32/status/ac-adapter.png
/usr/share/icons/hicolor/32x32/status/battery-caution-charging.png
/usr/share/icons/hicolor/32x32/status/battery-caution.png
/usr/share/icons/hicolor/32x32/status/battery-empty-charging.png
/usr/share/icons/hicolor/32x32/status/battery-empty.png
/usr/share/icons/hicolor/32x32/status/battery-full-charged.png
/usr/share/icons/hicolor/32x32/status/battery-full-charging.png
/usr/share/icons/hicolor/32x32/status/battery-full.png
/usr/share/icons/hicolor/32x32/status/battery-good-charging.png
/usr/share/icons/hicolor/32x32/status/battery-good.png
/usr/share/icons/hicolor/32x32/status/battery-low-charging.png
/usr/share/icons/hicolor/32x32/status/battery-low.png
/usr/share/icons/hicolor/32x32/status/battery-missing.png
/usr/share/icons/hicolor/32x32/status/computer.png
/usr/share/icons/hicolor/32x32/status/input-keyboard.png
/usr/share/icons/hicolor/32x32/status/input-mouse.png
/usr/share/icons/hicolor/32x32/status/multimedia-player.png
/usr/share/icons/hicolor/32x32/status/pda.png
/usr/share/icons/hicolor/32x32/status/phone.png
/usr/share/icons/hicolor/32x32/status/tablet.png
/usr/share/icons/hicolor/32x32/status/uninterruptible-power-supply.png
/usr/share/icons/hicolor/32x32/status/video-display.png
/usr/share/icons/hicolor/48x48/status/ac-adapter.png
/usr/share/icons/hicolor/48x48/status/battery-caution-charging.png
/usr/share/icons/hicolor/48x48/status/battery-caution.png
/usr/share/icons/hicolor/48x48/status/battery-empty-charging.png
/usr/share/icons/hicolor/48x48/status/battery-empty.png
/usr/share/icons/hicolor/48x48/status/battery-full-charged.png
/usr/share/icons/hicolor/48x48/status/battery-full-charging.png
/usr/share/icons/hicolor/48x48/status/battery-full.png
/usr/share/icons/hicolor/48x48/status/battery-good-charging.png
/usr/share/icons/hicolor/48x48/status/battery-good.png
/usr/share/icons/hicolor/48x48/status/battery-low-charging.png
/usr/share/icons/hicolor/48x48/status/battery-low.png
/usr/share/icons/hicolor/48x48/status/battery-missing.png
/usr/share/icons/hicolor/48x48/status/computer.png
/usr/share/icons/hicolor/48x48/status/display-brightness.png
/usr/share/icons/hicolor/48x48/status/input-keyboard.png
/usr/share/icons/hicolor/48x48/status/input-mouse.png
/usr/share/icons/hicolor/48x48/status/keyboard-brightness.png
/usr/share/icons/hicolor/48x48/status/multimedia-player.png
/usr/share/icons/hicolor/48x48/status/pda.png
/usr/share/icons/hicolor/48x48/status/phone.png
/usr/share/icons/hicolor/48x48/status/tablet.png
/usr/share/icons/hicolor/48x48/status/uninterruptible-power-supply.png
/usr/share/icons/hicolor/48x48/status/video-display.png
/usr/share/icons/hicolor/scalable/status/ac-adapter-symbolic.svg
/usr/share/icons/hicolor/scalable/status/ac-adapter.svg
/usr/share/icons/hicolor/scalable/status/battery-caution-charging-symbolic.svg
/usr/share/icons/hicolor/scalable/status/battery-caution-charging.svg
/usr/share/icons/hicolor/scalable/status/battery-caution-symbolic.svg
/usr/share/icons/hicolor/scalable/status/battery-caution.svg
/usr/share/icons/hicolor/scalable/status/battery-empty-charging-symbolic.svg
/usr/share/icons/hicolor/scalable/status/battery-empty-charging.svg
/usr/share/icons/hicolor/scalable/status/battery-empty-symbolic.svg
/usr/share/icons/hicolor/scalable/status/battery-empty.svg
/usr/share/icons/hicolor/scalable/status/battery-full-charged-symbolic.svg
/usr/share/icons/hicolor/scalable/status/battery-full-charged.svg
/usr/share/icons/hicolor/scalable/status/battery-full-charging-symbolic.svg
/usr/share/icons/hicolor/scalable/status/battery-full-charging.svg
/usr/share/icons/hicolor/scalable/status/battery-full-symbolic.svg
/usr/share/icons/hicolor/scalable/status/battery-full.svg
/usr/share/icons/hicolor/scalable/status/battery-good-charging-symbolic.svg
/usr/share/icons/hicolor/scalable/status/battery-good-charging.svg
/usr/share/icons/hicolor/scalable/status/battery-good-symbolic.svg
/usr/share/icons/hicolor/scalable/status/battery-good.svg
/usr/share/icons/hicolor/scalable/status/battery-low-charging-symbolic.svg
/usr/share/icons/hicolor/scalable/status/battery-low-charging.svg
/usr/share/icons/hicolor/scalable/status/battery-low-symbolic.svg
/usr/share/icons/hicolor/scalable/status/battery-low.svg
/usr/share/icons/hicolor/scalable/status/battery-missing-symbolic.svg
/usr/share/icons/hicolor/scalable/status/battery-missing.svg
/usr/share/icons/hicolor/scalable/status/computer.svg
/usr/share/icons/hicolor/scalable/status/display-brightness-symbolic.svg
/usr/share/icons/hicolor/scalable/status/display-brightness.svg
/usr/share/icons/hicolor/scalable/status/keyboard-brightness-symbolic.svg
/usr/share/icons/hicolor/scalable/status/keyboard-brightness.svg
/usr/share/icons/hicolor/scalable/status/keyboard.svg
/usr/share/icons/hicolor/scalable/status/mouse.svg
/usr/share/icons/hicolor/scalable/status/multimedia-player.svg
/usr/share/icons/hicolor/scalable/status/pda.svg
/usr/share/icons/hicolor/scalable/status/phone.svg
/usr/share/icons/hicolor/scalable/status/tablet.svg
/usr/share/icons/hicolor/scalable/status/uninterruptible-power-supply.svg
/usr/share/icons/hicolor/scalable/status/video-display.svg
/usr/share/icons/hicolor/scalable/status/xfce4-power-manager-settings.svg
/usr/share/metainfo/xfce4-power-manager.appdata.xml
/usr/share/polkit-1/actions/org.xfce.power.policy

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xfce4-power-manager-settings.1
/usr/share/man/man1/xfce4-power-manager.1

%files locales -f xfce4-power-manager.lang
%defattr(-,root,root,-)

