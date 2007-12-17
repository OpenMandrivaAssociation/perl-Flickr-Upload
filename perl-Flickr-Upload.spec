%define module  Flickr-Upload
%define name    perl-%{module}
%define version 1.29
%define release %mkrel 2

Summary:	Upload images to flickr.com
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source:     http://www.cpan.org/modules/by-module/Flick/%{module}-%{version}.tar.bz2
BuildRequires:	perl-XML-Parser-Lite-Tree
BuildRequires:	perl-Flickr-API
BuildRequires:	perl-libwww-perl
BuildArch:	noarch

%description
Upload an image to flickr.com

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std
# Should be in a new package as it requires additionnal libs
rm -f %{buildroot}%{_bindir}/thickr_upload

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README ChangeLog 
%{perl_vendorlib}/Flickr
%{perl_vendorlib}/auto/Flickr
%{_mandir}/*/*
%{_bindir}/flickr_upload
