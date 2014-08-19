%global _hardened_build 1

Summary:          Fast NTLM authentication proxy with tunneling
Name:             cntlm
Version:          0.92.3
Release:          5%{?dist}
License:          GPLv2+
Group:            System Environment/Daemons
URL:              http://cntlm.sourceforge.net/
Source0:          http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:          cntlm.tmpfiles
Source2:          cntlm.service
Patch0:           cntlm_makefile.patch
Requires:         systemd
BuildRequires:    systemd
Requires(pre):    shadow-utils
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd


%description
Cntlm is a fast and efficient NTLM proxy, with support for TCP/IP tunneling,
authenticated connection caching, ACLs, proper daemon logging and behavior
and much more. It has up to ten times faster responses than similar NTLM
proxies, while using by orders or magnitude less RAM and CPU. Manual page
contains detailed information.


%prep
%setup -q
%patch0 -p1


%build
%configure
make %{?_smp_mflags} SYSCONFDIR=%{_sysconfdir}


%install
make BINDIR=%{buildroot}%{_sbindir} MANDIR=%{buildroot}%{_mandir} SYSCONFDIR=%{buildroot}%{_sysconfdir} install

install -D -m 0644 rpm/%{name}.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/cntlmd
install -D -m 0644 %{SOURCE1} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service

install -D -d -m 0755 %{buildroot}/run/%{name}/


%pre
getent group %{name} > /dev/null || groupadd -r %{name}
getent passwd %{name} > /dev/null || \
  useradd -r -g %{name} -d %{_localstatedir}/run/%{name} -s /sbin/nologin \
    -c "%{name} daemon" %{name}
exit 0


%post
%systemd_post %{name}.service


%preun
%systemd_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service


%files
%doc LICENSE README COPYRIGHT
%{_sbindir}/%{name}
%{_mandir}/man1/%{name}.1*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/sysconfig/cntlmd
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/%{name}.service
%attr(755, %{name}, %{name}) %dir /run/%{name}/

%changelog
* Fri Dec 13 2013 Sandro Mani <manisandro@gmail.com> - 0.92.3-5
- Set correct permissions on /run/cntlm/

* Thu Dec 12 2013 Sandro Mani <manisandro@gmail.com> - 0.92.3-4
- Really create /run/cntlm/ on install

* Wed Oct 23 2013 Sandro Mani <manisandro@gmail.com> - 0.92.3-3
- Install /run/cntlm, change /var/run -> /run

* Mon Aug 26 2013 Sandro Mani <manisandro@gmail.com> - 0.92.3-2
- Fix debuginfo package empty (rhbz#1001302)

* Thu Aug 22 2013 Sandro Mani <manisandro@gmail.com> - 0.92.3-1
- Update to 0.92.3

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan  4 2012 Matt Domsch <mdomsch@fedoraproject.org> - 0.92-2
- convert to systemd (BZ771504), with unit file by Jóhann B. Guðmundsson

* Mon Dec  5 2011 Matt Domsch <mdomsch@fedoraproject.org> - 0.92-1
- update to new bugfix release (BZ760164)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 24 2010 Matt Domsch <mdomsch@fedoraproject.org> - 0.35.1-8
- add /etc/tmpfiles.d/cntlm.conf to create /var/run/cntlm/ (BZ656561)

* Mon Nov  8 2010 Matt Domsch <mdomsch@fedoraproject.org> - 0.35.1-7
- install NetworkManager dispatcher script, fixes BZ650079

* Mon Sep 27 2010 Matt Domsch <mdomsch@fedoraproject.org> - 0.35.1-6
- set SYSCONFDIR during build.  Fixes BZ637767

* Wed Sep  1 2010 Matt Domsch <mdomsch@fedoraproject.org> - 0.35.1-5
- add define for _initddir, needed on el5

* Thu Aug 26 2010 Matt Domsch <mdomsch@fedoraproject.org> - 0.35.1-4
- initscript: use pidfile to killproc

* Wed Aug 25 2010 Matt Domsch <mdomsch@fedoraproject.org> - 0.35.1-3
- additional fixes per package review

* Tue Aug 24 2010 Matt Domsch <mdomsch@fedoraproject.org> - 0.35.1-2
- updated spec to match Fedora packaging guidelines

* Fri Jul 27 2007 Radislav Vrnata <vrnata at gedas.cz>
- added support for SuSE Linux

* Fri Jul 27 2007 Radislav Vrnata <vrnata at gedas.cz>
- fixed pre, post, preun, postun macros bugs affecting upgrade process

* Wed May 30 2007 Since 0.28 maintained by <dave@awk.cz>


* Mon May 28 2007 Radislav Vrnata <vrnata at gedas.cz>
- Version 0.27
- First release
