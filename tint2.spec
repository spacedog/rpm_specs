Name:			tint2
Version:		0.11
Release:		9%{?dist}
Summary:		A lightweight X11 desktop panel and task manager
Group:			User Interface/Desktops
License:		GPLv2
URL:			http://code.google.com/p/tint2
Source0:		http://tint2.googlecode.com/files/%{name}-%{version}.tar.bz2
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	cairo-devel
BuildRequires:	cmake
BuildRequires:	gtk2-devel
BuildRequires:	imlib2-devel
BuildRequires:	libXcomposite-devel
BuildRequires:	libXdamage-devel
BuildRequires:	libXinerama-devel
BuildRequires:	libXrandr-devel
BuildRequires:	libXrender-devel
BuildRequires:	pango-devel


%description
tint2 is a simple panel/taskbar made for modern X window managers.


%prep
%setup -q


%build
%{cmake} .


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

rm -rf %{buildroot}%{_datadir}/doc/


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/xdg/*/*
%{_datadir}/%{name}/
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_mandir}/*/*

