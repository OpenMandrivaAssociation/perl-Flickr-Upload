%define upstream_name    Flickr-Upload
%define upstream_version 1.32

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Upload images to flickr.com
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Flickr/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-Flickr-API
BuildRequires:	perl-XML-Parser-Lite-Tree
BuildRequires:	perl-libwww-perl
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Upload an image to flickr.com

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{_mandir}/*/*
%{_bindir}/flickr_upload
