%define name perl-Flickr-Upload
%define pkgname Flickr-Upload
%define version 1.28
%define release %mkrel 1

Summary:	Upload images to flickr.com
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/C/CP/CPB/%{pkgname}-%{version}.tar.gz
Url:		http://search.cpan.org/dist/%{pkgname}/
BuildRequires:	perl-devel perl-XML-Parser-Lite-Tree perl-Flickr-API perl-libwww-perl
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot/
Requires:	perl

%description
Upload an image to flickr.com

%prep
%setup -q -n %{pkgname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
# Should be in a new package as it requires additionnal libs
rm -f $RPM_BUILD_ROOT%{_bindir}/thickr_upload

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README ChangeLog 
%{perl_vendorlib}/
%{_mandir}/*/*
%{_bindir}/flickr_upload

