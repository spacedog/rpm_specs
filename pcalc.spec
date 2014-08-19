Name:           pcalc
Version:        2
Release:        1%{?dist}
Summary:        Programmers calulator

Group:          Development/tools
License:        LGPLv2 with exceptions
URL:            http://sourceforge.net/projects/pcalc/
Source0:        http://sourceforge.net/projects/pcalc/dl/pcalc-2.tar.lzma
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  flex-devel


%description
Programmer's calculator, command line utility.

%prep
%setup

%build
make


%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin/pcalc
