Name:           scrot
Version:        0.8
Release:        11%{?dist}
Summary:        Screen-shot capture using Imlib 2

Group:          User Interface/X
License:        MIT
URL:            http://www.linuxbrit.co.uk/scrot/
Source0:        http://linuxbrit.co.uk/downloads/%{name}-%{version}.tar.gz
Patch1:         scrot_Makefile_in.patch

BuildRequires:  imlib2-devel
BuildRequires:  libX11-devel
BuildRequires:  giblib-devel

%description
A nice and straightforward screen capture utility implementing the dynamic
loaders of imlib2.


%prep
%setup -q
%patch1


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/*
%{_mandir}/man1/*



%changelog
* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.8-3
- Autorebuild for GCC 4.3

* Wed Oct 04 2006 Michael Rice <errr[AT]errr-online.com> - 0.8-2
- Fix project home page link
- Fix license from BSD to MIT
- Fix version info for Changelog entrys
- Remove datadir/name to fix dup doc entrys
- Fix patch for docs:
  removed the data docs from being installed by src

* Mon Sep 25 2006 Michael Rice <errr[AT]errr-online.com> - 0.8-1
- Initial RPM release
