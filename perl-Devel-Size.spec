Name:           perl-Devel-Size
Version:        0.82
Release:        5
Summary:        Perl extension for finding the memory usage of Perl variables
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Devel-Size
Source0:        https://cpan.metacpan.org/modules/by-module/Devel/Devel-Size-%{version}.tar.gz

BuildRequires:  findutils gcc make perl-interpreter perl-generators perl(ExtUtils::MakeMaker) perl(Test::More)
BuildRequires:  perl-devel
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%?perl_default_filter

%description
This module figures out the real size of Perl variables in bytes, as accurately as possible.
Call functions with a reference to the variable you want the size of. If the variable is a
plain scalar it returns the size of this scalar. If the variable is a hash or an array, use
a reference when calling.

%package_help

%prep
%setup -q -n Devel-Size-%{version}

%build
perl Makefile.PL NO_PACKLIST=1 INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

%check
make test

%files
%defattr(-,root,root)
%doc CHANGES
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Devel*

%files help
%{_mandir}/man3/*

%changelog
* Wed May 13 2020 openEuler Buildteam <buildteam@openeuler.org> - 0.82-5
- Add build requires of perl-devel

* Sat Jan 11 2020 openEuler Buildteam <buildteam@openeuler.org> - 0.82-4
- Package init
