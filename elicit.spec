Summary:	Screen zoomer / color picker
Summary(pl):	Narzêdzie do powiêkszania ekranu i wybierania kolorów
Name:		elicit
Version:	0.9
%define _snap	20050105
Release:	0.%{_snap}.0.1
License:	BSD
Group:		X11/Window Managers/Tools
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
Source0:	ftp://ftp.sparky.homelinux.org/pub/e17/%{name}-0.0.0-%{_snap}.tar.gz
# Source0-md5:	261d0236f4219c136fa7108824df0739
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esmart-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Elicit is a screen zoomer / color picker written with the
Enlightenment Foundation Libraries (http://www.enlightnement.org/).

%description -l pl
Elicit to narzêdzie do powiêkszania ekranu i wybierania kolorów
napisane przy u¿yciu podstawowych bibliotek Enlightenmenta
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
