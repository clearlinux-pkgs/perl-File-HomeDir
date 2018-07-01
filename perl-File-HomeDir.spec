#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-HomeDir
Version  : 1.004
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/R/RE/REHSACK/File-HomeDir-1.004.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RE/REHSACK/File-HomeDir-1.004.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-homedir-perl/libfile-homedir-perl_1.004-1.debian.tar.xz
Summary  : 'Find your home and other directories on any platform'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0 GPL-2.0
Requires: perl-File-HomeDir-license
Requires: perl-File-HomeDir-man
BuildRequires : perl(File::Which)

%description
# NAME
File::HomeDir - Find your home and other directories on any platform
# SYNOPSIS

%package license
Summary: license components for the perl-File-HomeDir package.
Group: Default

%description license
license components for the perl-File-HomeDir package.


%package man
Summary: man components for the perl-File-HomeDir package.
Group: Default

%description man
man components for the perl-File-HomeDir package.


%prep
tar -xf %{SOURCE1}
cd ..
%setup -q -n File-HomeDir-1.004
mkdir -p %{_topdir}/BUILD/File-HomeDir-1.004/deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/File-HomeDir-1.004/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/perl-File-HomeDir
cp LICENSE %{buildroot}/usr/share/doc/perl-File-HomeDir/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/doc/perl-File-HomeDir/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/File/HomeDir.pm
/usr/lib/perl5/site_perl/5.26.1/File/HomeDir/Darwin.pm
/usr/lib/perl5/site_perl/5.26.1/File/HomeDir/Darwin/Carbon.pm
/usr/lib/perl5/site_perl/5.26.1/File/HomeDir/Darwin/Cocoa.pm
/usr/lib/perl5/site_perl/5.26.1/File/HomeDir/Driver.pm
/usr/lib/perl5/site_perl/5.26.1/File/HomeDir/FreeDesktop.pm
/usr/lib/perl5/site_perl/5.26.1/File/HomeDir/MacOS9.pm
/usr/lib/perl5/site_perl/5.26.1/File/HomeDir/Test.pm
/usr/lib/perl5/site_perl/5.26.1/File/HomeDir/Unix.pm
/usr/lib/perl5/site_perl/5.26.1/File/HomeDir/Windows.pm

%files license
%defattr(-,root,root,-)
/usr/share/doc/perl-File-HomeDir/LICENSE
/usr/share/doc/perl-File-HomeDir/deblicense_copyright

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/File::HomeDir.3
/usr/share/man/man3/File::HomeDir::Darwin.3
/usr/share/man/man3/File::HomeDir::Darwin::Carbon.3
/usr/share/man/man3/File::HomeDir::Darwin::Cocoa.3
/usr/share/man/man3/File::HomeDir::Driver.3
/usr/share/man/man3/File::HomeDir::FreeDesktop.3
/usr/share/man/man3/File::HomeDir::MacOS9.3
/usr/share/man/man3/File::HomeDir::Test.3
/usr/share/man/man3/File::HomeDir::Unix.3
/usr/share/man/man3/File::HomeDir::Windows.3
