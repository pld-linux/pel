%include	/usr/lib/rpm/macros.php
Summary:	PEL: PHP EXIF Library
Name:		pel
Version:	0.6
Release:	1
License:	GPL v2
Group:		Development/Languages/PHP
Source0:	http://heanet.dl.sourceforge.net/pel/%{name}-%{version}.tar.bz2
# Source0-md5:	a3715567a986563d1974531aac7b1d0f
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
%dir %{php_pear_dir}/%{name}/locale/*
%dir %{php_pear_dir}/%{name}/locale/*/LC_MESSAGES
%{php_pear_dir}/%{name}/*.php
%{php_pear_dir}/%{name}/locale/*/LC_MESSAGES/*.mo