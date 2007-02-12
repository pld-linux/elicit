Summary:	Screen zoomer / color picker
Summary(pl.UTF-8):	Narzędzie do powiększania ekranu i wybierania kolorów
Name:		elicit
Version:	0.9
%define _snap	20060307
Release:	0.%{_snap}.1
License:	BSD
Group:		X11/Window Managers/Tools
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
Source0:	http://sparky.homelinux.org/snaps/enli/e17/apps/%{name}-%{_snap}.tar.bz2
# Source0-md5:	4492ab0a224cda7d0e3e2e57a0380b4c
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esmart-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Elicit is a screen zoomer / color picker written with the
Enlightenment Foundation Libraries (http://www.enlightnement.org/).

%description -l pl.UTF-8
Elicit to narzędzie do powiększania ekranu i wybierania kolorów
napisane przy użyciu podstawowych bibliotek Enlightenmenta
(Enlightenment Foundation Libraries, http://www.englightenment.org/).

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README TODO ChangeLog
%attr(755,root,root) %{_bindir}/elicit
%{_datadir}/%{name}
