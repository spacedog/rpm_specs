Name:	gcalcli
Version: 2.4.2
Release:	1%{?dist}
Summary:	Google Calendar Command Line Interface

Group: Productivity/Tools/Calendars
License: GPL 
URL: https://github.com/insanum/gcalcli
Source0: https://github.com/insanum/gcalcli/archive/gcalcli-2.4.2.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
Requires: python,python-gdata,python-dateutil,python-gflags	

%description


%prep
%setup -q

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
cp gcalcli %{buildroot}/usr/bin/


%clean
rm -rf %{buildroot}


%files
/usr/bin/gcalcli


%changelog

