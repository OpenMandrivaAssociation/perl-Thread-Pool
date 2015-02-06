%define module_name Thread-Pool

Summary:	Group of threads for performing similar jobs
Name:		perl-%{module_name}
Version:	0.33
Release:	4
License:	Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/Thread-Pool/
Source:		http://www.cpan.org/modules/by-module/Thread/%{module_name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)

%description
The Thread::Pool allows you to set up a group of (worker) threads to
execute a (large) number of similar jobs that need to be executed
asynchronously. The routine that actually performs the job (the "do"
routine), must be specified as a name or a reference to a (anonymous)
subroutine.

This module only functions on Perl versions 5.8.0 and later.
And then only when threads are enabled with -Dusethreads.  It
is of no use with any version of Perl before 5.8.0 or without
threads enabled.
%prep
%setup -q -n %{module_name}-%{version}

%build
%{expand: %%define optflags %{optflags} -fPIC}

CFLAGS="%{optflags}" perl Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%make

%install
make pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec rm {} \;

%files
%defattr(-, root, root, 0755)
%doc MANIFEST README CHANGELOG TODO
%doc %{_mandir}/man3/Thread::Pool.3pm*
%dir %{perl_vendorlib}/Thread/
%{perl_vendorlib}/Thread/Pool.pm


%changelog
* Tue Sep 27 2011 Leonardo Coelho <leonardoc@mandriva.com> 0.33-1mdv2012.0
+ Revision: 701570
- first mandriva version
- Created package structure for 'perl-Thread-Pool'.

