# TODO
# - move gettext locale files to system dir
Summary:	PEL: PHP EXIF Library
Summary(pl.UTF-8):	PEL - biblioteka PHP EXIF
Name:		pel
Version:	0.9.1
Release:	1
License:	GPL v2
Group:		Development/Languages/PHP
Source0:	http://dl.sourceforge.net/pel/%{name}-%{version}.tar.bz2
# Source0-md5:	774654bf1b7b750cd2c1e37cff696da2
URL:		http://pel.sourceforge.net/
Requires:	php-common >= 4:5.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/php/%{name}

%description
PEL is a library that will read and write EXIF headers found in JPEG
images. It is written in pure PHP 5, which means that it does not
depend on anything outside the core of PHP 5.

%description -l pl.UTF-8
PEL to biblioteka odczytująca i zapisująca nagłówki EXIF w plikach
obrazków JPEG. Jest napisana w czystym PHP 5, co oznacza, że nie
wymaga niczego spoza podstawowego PHP 5.

%package phpdoc
Summary:	Online manual for %{name}
Summary(pl.UTF-8):	Dokumentacja online do %{name}
Group:		Documentation

%description phpdoc
Documentation for %{name}.

%description phpdoc -l pl.UTF-8
Dokumentacja do %{name}.

%prep
%setup -q

# remove phpdoc cachefiles
find doc -name ???????????????????????????????? | xargs rm -rf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}/locale/{da,de,es,fr}/LC_MESSAGES
cp -a *.php $RPM_BUILD_ROOT%{_appdir}

# install locales:
for i in da de es fr; do
	install locale/$i/LC_MESSAGES/*.mo $RPM_BUILD_ROOT%{_appdir}/locale/$i/LC_MESSAGES
done

install -d $RPM_BUILD_ROOT%{_docdir}/%{name}
cp -a doc/* $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL NEWS README TODO test
%dir %{_appdir}
%{_appdir}/*.php
%dir %{_appdir}/locale
%lang(da) %{_appdir}/locale/da
%lang(de) %{_appdir}/locale/de
%lang(es) %{_appdir}/locale/es
%lang(fr) %{_appdir}/locale/fr

%files phpdoc
%defattr(644,root,root,755)
%{_docdir}/%{name}
