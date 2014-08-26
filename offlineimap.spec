%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

#Do not remove the following commented defines.  They are useful for
#rc releases.
#%define rcnum	 rc3
#%define prereleasetag %{rcnum}0g%{githash}
#%define increment     1

%define githash  8bc2f35
%define packagedirprefix OfflineIMAP-offlineimap
%define packagedirname %{packagedirprefix}-%{githash}

Name:           offlineimap
Version:        6.5.5
Release:        2%{?dist}
Summary:        Powerful IMAP/Maildir synchronization and reader support

License:        GPLv2+
Group:          Applications/Internet
URL:            http://offlineimap.org
Source0:        %{packagedirprefix}-v%{version}-0-g%{githash}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python-devel
BuildRequires:  python-docutils
BuildRequires:  make
BuildRequires:  gzip
BuildRequires:  git
BuildRequires:  python-sphinx

BuildArch:      noarch

%description
OfflineIMAP is a tool to simplify your e-mail reading. With OfflineIMAP,
you can read the same mailbox from multiple computers.  You get a
current copy of your messages on each computer, and changes you make one
place will be visible on all other systems. For instance, you can delete
a message on your home computer, and it will appear deleted on your work
computer as well. OfflineIMAP is also useful if you want to use a mail
reader that does not have IMAP support, has poor IMAP support, or does
not provide disconnected operation.

%prep
%setup -q -n %{packagedirname}

%build
make build
make man
make doc
gzip -c docs/offlineimap.1 > docs/offlineimap.1.gz

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT

python setup.py install --root=$RPM_BUILD_ROOT --prefix=%{_prefix}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
install -p docs/offlineimap.1.gz $RPM_BUILD_ROOT/%{_mandir}/man1/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPY* offlineimap.conf* docs/html/*.html
%{_bindir}/offlineimap
%{python_sitelib}/offlineimap/
%{python_sitelib}/offlineimap-%{version}-py*.egg-info
%{_mandir}/man1/offlineimap.1.gz

%changelog
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Dec  1 2013 Dodji Seketeli <dodji@seketeli.org> - 6.5.5-1
- Update to upstream version 6.5.5-0

* Tue Sep 24 2013 Dodji Seketeli <dodji@seketeli.org> - 6.5.5-rc3-0-g254e848-1
- Update to pre-release version 6.5.5-rc3-0-g254e848
- Update Release field accordingly.
- Remove reference to the previous patch.  According to upstream that
  issue should be solved by a folderfilter that filters out empty
  directory names.
- Update %%setup directive in %%prep section to reflect the new naming
  scheme of the package source directory name.
- Update html files references.
- Update the *.egg-info file name reference.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.5.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.5.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 25 2012 Dodji Seketeli <dodji@seketeli.org> - 6.5.2.1-3
- Do away with the (too heavy) use of git to apply patches
- Apply 35bccdc7dfab8 - Avoid trying to synchronize folders that have empty names
  This is from git://github.com/OfflineIMAP/offlineimap, in the 'pu' branch.
  Fixes #835688 - offline fails to sync with 'new' folder in tree created by dovecot

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 14 2012 Christoph Höger <choeger@umpa-net.de> 6.5.2.1-1
- Upgrade to latest stable version
- Fixes #789805

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 16 2011 Christoph Höger <choeger@umpa-net.de> - 6.3.4-1
- Upgrade to latest stable version
- Fixes #708898

* Tue May 10 2011 Christoph Höger <choeger@umpa-net.de> - 6.3.3-1
- Upgrade to latest stable version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Sep 19 2010 Christoph Höger <choeger@cs.tu-berlin.de> - 6.2.0-1
- Update to the last (not latest, last!) released stable version
- This release fixed some bugs by removing IDLE support
- fixes #525824

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 6.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 Christoph Höger <choeger@cs.tu-berlin.de> - 6.1.2-1
- Update to latest version
- remove patch -> upstream
- fixes #510036 

* Thu Jul 02 2009 Christoph Höger <choeger@cs.tu-berlin.de> - 6.1.0-1
- Update to latest version
- Add a temporary patch for socket.ssl deprecation

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 18 2008 Christoph Höger <choeger@cs.tu-berlin.de> 6.0.3-1
- Update to latest version
- use own tarball instead of debian ftp

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 6.0.0-2
- Rebuild for Python 2.6

* Wed Jun 18 2008 Till Maas <opensource till name> - 6.0.0-1
- Update to latest release

* Tue Mar 04 2008 Till Maas <opensource till name> - 5.99.7-1
- Update to latest version

* Tue Mar 04 2008 Till Maas <opensource till name> - 5.99.6-1
- Update to latest version

* Mon Jan 07 2008 Till Maas <opensource till name> - 5.99.4-2
- add egg-info to %%files

* Sun Oct 21 2007 Till Maas <opensource till name> - 5.99.4-1
- update to new version

* Tue Sep 04 2007 Till Maas <opensource till name> - 5.99.2-1
- update to new version
- update license Tag
- add unclosed listitem in offlineimap.sgml
- add missing BR: docbook-utils
- build manpage
- remove todo and manual files from %%doc

* Sat Dec 09 2006 Till Maas <opensource till name> - 4.0.16-3
- rebuild for python2.5
- added BR: python-devel, which is needed now

* Mon Dec 04 2006 Till Maas <opensource till name> - 4.0.16-2
- added -p to cp to preserve timestamp of ChangeLog

* Sun Dec 03 2006 Till Maas <opensource till name> - 4.0.16-1
- version bump
- added one more %%{version} to Source0
- added FAQ.html, todo to %%doc
- added debian/changelog as ChangeLog to %%doc

* Sat Dec 02 2006 Till Maas <opensource till name> - 4.0.15-1
- added %%{?dist} tag
- made Source0 a valid URL
- rearranged tag order and changed whitespace
- added -q -n %%name to %%setup
- removed ChangeLog* from %%doc (not in archive)
- added offlineimap.conf* to %%doc
- Use %%{_bindir} and %%{python_sitelib}
- removed directory docs from %%doc
- added BuildArch: noarch
- added manpage

* Tue May 16 2006 Adam Spiers <adam@spiers.net> 4.0.13-3
- Force prefix to /usr

* Mon May 15 2006 Adam Spiers <adam@spiers.net> 4.0.13-2
- Finally get savemessage_searchforheader right?

* Sun May 14 2006 Adam Spiers <adam@spiers.net> 4.0.13-1
- Updated for 4.0.13

* Sat Apr 29 2006 Adam Spiers <offlineimap@adamspiers.org> 4.0.11-2
- Add patch for Groupwise IMAP servers.

* Fri Apr 28 2006 Adam Spiers <offlineimap@adamspiers.org> 4.0.11-1
- Initial build.
