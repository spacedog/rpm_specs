Name:	stalonetray
Version: 0.8.1 
Release:	1%{?dist}
Summary:	Stalonetray is a stand-alone freedesktop.org and KDE system tray

Group: X11/trays 	
License: GPL 
URL: http://stalonetray.sourceforge.net/ 	
Source0:/stalonetray-0.8.1.tar.bz2
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
#Requires:	

%description


%prep
%setup -q


%build
%configure --prefix=/usr
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
/usr/bin/stalonetray
/usr/share/man/man1/stalonetray.1.gz


%changelog

