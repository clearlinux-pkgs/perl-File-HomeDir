#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-HomeDir
Version  : 1.006
Release  : 15
URL      : https://cpan.metacpan.org/authors/id/R/RE/REHSACK/File-HomeDir-1.006.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RE/REHSACK/File-HomeDir-1.006.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-homedir-perl/libfile-homedir-perl_1.004-1.debian.tar.xz
Summary  : 'Find your home and other directories on any platform'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0 GPL-2.0
Requires: perl-File-HomeDir-license = %{version}-%{release}
Requires: perl-File-HomeDir-perl = %{version}-%{release}
Requires: perl(File::Which)
BuildRequires : buildreq-cpan
BuildRequires : perl(File::Which)

%description
# NAME
File::HomeDir - Find your home and other directories on any platform
# SYNOPSIS

%package dev
Summary: dev components for the perl-File-HomeDir package.
Group: Development
Provides: perl-File-HomeDir-devel = %{version}-%{release}
Requires: perl-File-HomeDir = %{version}-%{release}

%description dev
dev components for the perl-File-HomeDir package.


%package license
Summary: license components for the perl-File-HomeDir package.
Group: Default

%description license
license components for the perl-File-HomeDir package.


%package perl
Summary: perl components for the perl-File-HomeDir package.
Group: Default
Requires: perl-File-HomeDir = %{version}-%{release}

%description perl
perl components for the perl-File-HomeDir package.


%prep
%setup -q -n File-HomeDir-1.006
cd %{_builddir}
tar xf %{_sourcedir}/libfile-homedir-perl_1.004-1.debian.tar.xz
cd %{_builddir}/File-HomeDir-1.006
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/File-HomeDir-1.006/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-HomeDir
cp %{_builddir}/File-HomeDir-1.006/LICENSE %{buildroot}/usr/share/package-licenses/perl-File-HomeDir/ef51e850423393335a21c5069af73674cdf6753f
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-File-HomeDir/7d1705b93e8bd056cd774e3956c8abf6ba0dfa79
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-HomeDir/7d1705b93e8bd056cd774e3956c8abf6ba0dfa79
/usr/share/package-licenses/perl-File-HomeDir/ef51e850423393335a21c5069af73674cdf6753f

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/File/HomeDir.pm
/usr/lib/perl5/vendor_perl/5.30.3/File/HomeDir/Darwin.pm
/usr/lib/perl5/vendor_perl/5.30.3/File/HomeDir/Darwin/Carbon.pm
/usr/lib/perl5/vendor_perl/5.30.3/File/HomeDir/Darwin/Cocoa.pm
/usr/lib/perl5/vendor_perl/5.30.3/File/HomeDir/Driver.pm
/usr/lib/perl5/vendor_perl/5.30.3/File/HomeDir/FreeDesktop.pm
/usr/lib/perl5/vendor_perl/5.30.3/File/HomeDir/MacOS9.pm
/usr/lib/perl5/vendor_perl/5.30.3/File/HomeDir/Test.pm
/usr/lib/perl5/vendor_perl/5.30.3/File/HomeDir/Unix.pm
/usr/lib/perl5/vendor_perl/5.30.3/File/HomeDir/Windows.pm
