# $Rev: 3214 $, $Date: 2005-08-27 17:42:48 $
#
Summary:	font-mutt-misc
Summary(pl):	font-mutt-misc
Name:		xorg-font-font-mutt-misc
Version:	0.99.0
Release:	0.01
License:	MIT
Group:		X11
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/font/font-mutt-misc-%{version}.tar.bz2
# Source0-md5:	721dd9eb39f5ecce4c4e179db3466ff1
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-font-font-util
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRoot:	%{tmpdir}/font-mutt-misc-%{version}-root-%(id -u -n)

%description
font-mutt-misc

%description -l pl
font-mutt-misc


%prep
%setup -q -n font-mutt-misc-%{version}


%build
%{__aclocal}
%{__autoconf}
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
%{_libdir}/X11/fonts/misc/*
