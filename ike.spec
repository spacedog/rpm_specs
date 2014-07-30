Name:           ike
Version:        2.2.1
Release:        2%{?dist}
Summary:        Shrew Soft VPN Client For Linux
Group:          Applications/Communications
License:        Sleepycat
URL:            http://www.shrew.net/
Source0:        http://www.shrew.net/download/%{name}/%{name}-%{version}-release.tbz2
Source1:        iked.init
Source2:        ike.desktop
Source3:        ike.logrotate
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  cmake flex bison qt-devel openldap-devel openssl-devel libedit-devel
BuildRequires:  desktop-file-utils
Requires(post): chkconfig
Requires(preun): chkconfig
Requires(preun): initscripts

%description
This free IPSEC VPN client can be used to communicate with 
Open Source IPSEC VPN servers as well as some commercial
IPSEC VPN servers.

%prep
%setup -q -n %{name}

sed -i 's:/var/log/:/var/log/iked/:' source/iked/iked.conf.sample
sed -i 's/\r//' TODO.TXT

%build
%cmake -DQTGUI=YES -DNATT=YES -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DETCDIR:PATH=%{_sysconfdir} \
      -DMANDIR:PATH=%{_mandir} -DLDAP=YES -DLIBDIR=%{_libdir} 
#      -DQT_QT_LIBRARY=/usr/lib64/qt-3.3 \
#      -DQT_INCLUDE_DIR=/usr/lib64/qt-3.3/include \
#make VERBOSE=1 %{?_smp_mflags}
make VERBOSE=1 


%install
rm -rf $RPM_BUILD_ROOT

make INSTALL="install -p" install DESTDIR=$RPM_BUILD_ROOT

install -d -p $RPM_BUILD_ROOT%{_initrddir}
install -d -p $RPM_BUILD_ROOT%{_localstatedir}/run/%{name}d
install -d -p $RPM_BUILD_ROOT%{_localstatedir}/log/%{name}d
install -d -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
#install -D -p -m0755 %SOURCE1 $RPM_BUILD_ROOT%{_initrddir}/%{name}d
mv $RPM_BUILD_ROOT%{_sysconfdir}/iked.conf.sample $RPM_BUILD_ROOT%{_sysconfdir}/iked.conf

# Create desktop file
install -p source/qikea/png/ikea.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}a.png
desktop-file-install --dir $RPM_BUILD_ROOT/%{_datadir}/applications \
    %{SOURCE2} --vendor=""

# Create /etc/logrotate.d/ike
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
install -m 0644 -p %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/%{name}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE.TXT TODO.TXT
%config(noreplace) %{_sysconfdir}/iked.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/ike
%{_libdir}/*.so.*
%{_libdir}/*.so
#%{_initrddir}/%{name}d
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man*/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%dir %{_localstatedir}/run/%{name}d
%dir %{_localstatedir}/log/%{name}d

%changelog
* Sun Nov 20 2011 Andrew Colin Kissa <andrew@topdog.za.net> - 2.1.7-6
- Fix desktop-file-install issue

* Sun Nov 20 2011 Andrew Colin Kissa <andrew@topdog.za.net> - 2.1.7-5
- Fix bugzilla #752343

* Sun Mar 13 2011 Andrew Colin Kissa <andrew@topdog.za.net> - 2.1.7-4
- fix perms on logrotate file

* Sat Feb 12 2011 Andrew Colin Kissa <andrew@topdog.za.net> - 2.1.7-3
- Cleanup minor rpmlint errors

* Thu Oct 14 2010 Jochen Schmitt <Jochen herr-schmitt de> - 2.1.7-2
- Fix cmake related issues

* Wed Oct 13 2010 Jochen Schmitt <Jochen herr-schmitt de> - 2.1.7-1
- New upstream release

* Thu Mar 04 2010 Andrew Colin Kissa <andrew@topdog.za.net> - 2.1.5-2
- Fix source miss packaging

* Tue Dec 15 2009 Andrew Colin Kissa <andrew@topdog.za.net> - 2.1.5-1
- Upgrade to new upstream release
- Use cmake macro

* Wed Aug 19 2009 Andrew Colin Kissa <andrew@topdog.za.net> - 2.1.5-0.1.rc2
- Initial packaging
