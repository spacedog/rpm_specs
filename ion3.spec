Name:           ion
Version:        3
Release:        20090110
Summary:        Ion is a tiling window manager

Group:          User Interface/Desktops
License:        LGPLv2 with exceptions
URL:            http://modeemi.fi/~tuomov/ion
Source0:        http://iki.fi/tuomov/dl/ion-3-20090110.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  lua lua-devel libX11-devel libSM-devel libXext-devel gettext 
Requires:       lua filesystem man

%description
Ion is a tiling tabbed window manager designed with keyboard users in mind.

%prep
%setup -n ion-3-20090110

sed 's-/usr/local-/usr-' system.mk > system.mk.$$
cp -f system.mk.$$ system.mk
sed 's/^ETCDIR\(.*\)\$(PREFIX)\(.*\)$/ETCDIR\1\2/' system.mk > system.mk.$$
cp -f system.mk.$$ system.mk
rm -f system.mk.$$

%build
make


%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
sed "s%^PREFIX=.*%PREFIX=$RPM_BUILD_ROOT/usr%" system.mk > system.mk.install.$$
cp -f system.mk.install.$$ system.mk
sed "s%ETCDIR=\(.*$\)%ETCDIR=$RPM_BUILD_ROOT\1%" system.mk > system.mk.install.$$
cp -f system.mk.install.$$ system.mk
rm -f system.mk.install.$$
make install
%find_lang %{name}3
#cd $RPM_BUILD_ROOT && find usr -type d | grep -v '^usr/share$' | grep -v '^usr/lib$' | grep -v '^usr/bin$' | grep -v '^usr$' | grep -v '^etc/$' | grep -v '^usr/share/doc$' | grep -v '$usr/share/man$'  | grep -v '^usr/share/man/man1$' | sed 's-^-%dir /-' > DIRLIST.RPM
# find usr -type d | grep ion3 | sed 's-^-%dir /-' > DIRLIST.RPM
#cd $RPM_BUILD_ROOT && find usr -type f | sed 's-^-/-' | grep -v '^/usr/lib/debug' > FILELIST.RPM

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}3.lang
#%files -f FILELIST.RPM
%defattr(-,root,root,-)
#%doc LICENSE
%config(noreplace) /etc/*

%dir /usr/share/doc/ion3
%dir /usr/share/ion3
%dir /usr/lib/ion3
%dir /usr/lib/ion3/bin
%dir /usr/lib/ion3/lc
%dir /usr/lib/ion3/mod

/usr/bin/ion3
/usr/bin/pwm3
/usr/share/man/man1/pwm3.1.gz
/usr/share/man/man1/ion3.1.gz
/usr/share/man/fi/man1/pwm3.1.gz
/usr/share/man/fi/man1/ion3.1.gz
/usr/share/man/cs/man1/pwm3.1.gz
/usr/share/man/cs/man1/ion3.1.gz
/usr/share/doc/ion3/LICENSE
/usr/share/doc/ion3/RELNOTES
/usr/share/doc/ion3/ChangeLog
/usr/share/doc/ion3/README
/usr/share/ion3/welcome.txt
/usr/share/ion3/welcome.fi.txt
/usr/share/ion3/ion-completeman
/usr/share/ion3/welcome.cs.txt
/usr/share/ion3/ion-runinxterm
/usr/lib/ion3/bin/ion-statusd
/usr/lib/ion3/bin/ion-completefile
/usr/lib/ion3/lc/ioncore_ext.lc
/usr/lib/ion3/lc/ioncore_winprops.lc
/usr/lib/ion3/lc/ioncore_tabnum.lc
/usr/lib/ion3/lc/ioncore_bindings.lc
/usr/lib/ion3/lc/de.lc
/usr/lib/ion3/lc/ioncore_luaext.lc
/usr/lib/ion3/lc/ioncore_wd.lc
/usr/lib/ion3/lc/statusd_mail.lc
/usr/lib/ion3/lc/mod_statusbar.lc
/usr/lib/ion3/lc/mod_sm.lc
/usr/lib/ion3/lc/statusd_load.lc
/usr/lib/ion3/lc/mod_query.lc
/usr/lib/ion3/lc/ioncore_misc.lc
/usr/lib/ion3/lc/mod_query_chdir.lc
/usr/lib/ion3/lc/statusd_date.lc
/usr/lib/ion3/lc/ioncore_efbb.lc
/usr/lib/ion3/lc/ioncore_quasiact.lc
/usr/lib/ion3/lc/mod_dock.lc
/usr/lib/ion3/lc/mod_tiling.lc
/usr/lib/ion3/lc/mod_sp.lc
/usr/lib/ion3/lc/ioncore_menudb.lc
/usr/lib/ion3/lc/mod_menu.lc
/usr/lib/ion3/mod/mod_menu.so
/usr/lib/ion3/mod/mod_statusbar.so
/usr/lib/ion3/mod/mod_sp.so
/usr/lib/ion3/mod/de.so
/usr/lib/ion3/mod/mod_query.so
/usr/lib/ion3/mod/mod_tiling.so
/usr/lib/ion3/mod/mod_sm.so
/usr/lib/ion3/mod/mod_dock.so



%changelog
* Sat Feb 7 2009 Timandahaf <timandahaf@gmail.com> 3-20090110
  - Upgraded to the 20090110 version.
* Fri Oct 17 2008 Timandahaf <timandahaf@gmail.com> 3-20081002
  - Upgraded to the 20081002 version.
* Tue Sep 23 2008 Timandahaf <timandahaf@gmail.com> 3-20080825
  - Upgraded to the 20080825 version.
* Sat Jan 05 2008 Timandahaf <timandahaf@gmail.com> 3-0.1.rc.20080103
  - Upgraded to the 20080103 version.
* Mon Dec 12 2007 Timandahaf <timandahaf@gmail.com> 3-0.1.rc.20071130
  - Initial build.
