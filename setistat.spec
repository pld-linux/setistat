Summary:	Program to monitor a SETI@home client
Summary(pl):	Program do monitorowania klienta SETI@home
Name:		setistat
Version:	0.8.90
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://www.rexi.org/downloads/setistat/%{name}-%{version}.tar.gz
# Source0-md5:	c51f87d005aeb3c831ba913f413a1df5
# Source0-size:	301747
BuildRequires:	ncurses-devel
BuildRequires:	libxml2-devel
Requires:	setiathome
URL:		http://www.rexi.org/software/setistat/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SetiStat is a program to monitor a SETI@home client. It displays
progress of the recieved work units, earned credit, host information
and so on.

%prep
%setup -q

%build

%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-ncurses-includes=%{_includedir}/ncurses/

%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
