%include	/usr/lib/rpm/macros.php
Summary:	PEL: PHP EXIF Library
Summary(pl):	PEL - biblioteka PHP EXIF
Name:		pel
Version:	0.8
Release:	1
License:	GPL v2
Group:		Development/Languages/PHP
Source0:	http://heanet.dl.sourceforge.net/pel/%{name}-%{version}.tar.bz2
# Source0-md5:	36cb1cb011c674625d722bdfbbdb38bc
# Source0-size:	285673
URL:		http://pel.sourceforge.net/
BuildRequires:	rpm-php-pearprov
Requires:	php >= 5.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PEL is a library that will read and write EXIF headers found in JPEG
images. It is written in pure PHP 5, which means that it does not
depend on anything outside the core of PHP 5.

%description -l pl
PEL to biblioteka odczytuj±ca i zapisuj±ca nag³ówki EXIF w plikach
obrazków JPEG. Jest napisana w czystym PHP 5, co oznacza, ¿e nie
wymaga niczego spoza podstawowego PHP 5.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{name}/locale/{da,de,es,fr}/LC_MESSAGES

install *.php $RPM_BUILD_ROOT%{php_pear_dir}/%{name}

# install locales:
for i in da de es fr; do
	install locale/$i/LC_MESSAGES/*.mo $RPM_BUILD_ROOT%{php_pear_dir}/%{name}/locale/$i/LC_MESSAGES
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL NEWS README TODO test doc
%dir %{php_pear_dir}/%{name}
%dir %{php_pear_dir}/%{name}/locale
%lang(da) %{php_pear_dir}/%{name}/locale/da
%lang(de) %{php_pear_dir}/%{name}/locale/de
%lang(es) %{php_pear_dir}/%{name}/locale/es
%lang(fr) %{php_pear_dir}/%{name}/locale/fr
%{php_pear_dir}/%{name}/*.php
