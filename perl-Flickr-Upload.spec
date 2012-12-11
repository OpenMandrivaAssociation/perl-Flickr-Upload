%define upstream_name    Flickr-Upload
%define upstream_version 1.32

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Upload images to flickr.com
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Flickr/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Flickr::API)
BuildRequires:	perl(XML::Parser::Lite::Tree)
BuildRequires:	perl-libwww-perl
BuildArch:	noarch

%description
Upload an image to flickr.com

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std
# Should be in a new package as it requires additionnal libs
rm -f %{buildroot}%{_bindir}/thickr_upload

%files
%doc README ChangeLog 
%{perl_vendorlib}/Flickr
%{_mandir}/*/*
%{_bindir}/flickr_upload


%changelog
* Wed Aug 05 2009 Jérôme Quelin <jquelin@mandriva.org> 1.320.0-1mdv2010.0
+ Revision: 410058
- rebuild using %%perl_convert_version

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.32-1mdv2009.1
+ Revision: 292163
- update to new version 1.32

* Fri Jun 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.31-1mdv2009.0
+ Revision: 227493
- new version

* Tue Mar 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.30-1mdv2008.1
+ Revision: 185152
- new version
  drop patch 0, merged upstream

* Sat Mar 08 2008 Pascal Terjan <pterjan@mandriva.org> 1.29-3mdv2008.1
+ Revision: 182097
- Fix handling of gzipped responses

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.29-2mdv2008.0
+ Revision: 90053
- rebuild

* Wed Jul 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.29-1mdv2008.0
+ Revision: 48066
- new version

  + Pascal Terjan <pterjan@mandriva.org>
    - 1.28

* Fri Apr 20 2007 Pascal Terjan <pterjan@mandriva.org> 1.25-1mdv2008.0
+ Revision: 15219
- 1.25
- use mkrel


* Wed Feb 08 2006 Pascal Terjan <pterjan@mandriva.org> 1.22-2mdk
- BuildRequires perl-libwww-perl for make test

* Wed Aug 31 2005 Pascal Terjan <pterjan@mandriva.org> 1.22-1mdk
- 1.22

* Sat Aug 20 2005 Pascal Terjan <pterjan@mandriva.org> 1.18-1mdk
- First version of the package

