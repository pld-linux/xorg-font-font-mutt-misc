Summary:	MUTT ClearlyU bitmap fonts
Summary(pl.UTF-8):	Fonty bitmapowe MUTT ClearlyU
Name:		xorg-font-font-mutt-misc
Version:	1.0.0
Release:	1
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-mutt-misc-%{version}.tar.bz2
# Source0-md5:	648b409b7eb78ad1cd5f6d7fac3eef88
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MUTT ClearlyU bitmap fonts, including Alternate Glyphs, Arabic,
Devangari and Ligature.

%description -l pl.UTF-8
Fonty bitmapowe MUTT ClearlyU, w tym Alternate Glyphs, Arabic,
Devangari i Ligature.

%prep
%setup -q -n font-mutt-misc-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-fontdir=%{_fontsdir}/misc

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst misc

%postun
fontpostinst misc

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%{_fontsdir}/misc/cu*.pcf.gz
