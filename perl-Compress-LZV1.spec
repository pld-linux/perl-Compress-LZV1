%include	/usr/lib/rpm/macros.perl
%define		pdir	Compress
%define		pnam	LZV1
Summary:	Compress::LZV1 Perl module - extremely leight-weight Lev-Zimpel-Vogt compression
Summary(pl):	Modu³ Perla Compress::LZV1 - ekstremalnie lekka kompresja Lev-Zimpel-Vogt
Name:		perl-Compress-LZV1
Version:	0.04
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1e6ee23a325a5f1475052576280d7250
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LZV1 is an extremely fast (not that much slower than a pure memcpy)
compression algorithm. It is ideal for applications where you want to
save *some* space but not at the cost of speed. It is ideal for
repetitive data as well. The module is self-contained and very small
(no large library to be pulled in). It is also free, so there should
be no problems incoporating this module into commercial programs. It
is believed that it is free from any patents.

%description -l pl
LZV1 jest ekstremalnie szybkim (nie tak du¿o wolniejszym od memcpy)
algorytmem kompresji. Jest idealny dla programów, które chc±
zaoszczêdziæ *trochê* miejsca, ale nie kosztem szybko¶ci. Jest idealny
dla powtarzaj±cych siê danych. Modu³ jest ma³y i nie wymaga ¿adnej
dodatkowej du¿ej biblioteki. Jest wolnodostêpny, wiêc nie powinno byæ
problemów z wykorzystaniem go w komercyjnych programach. Wed³ug
aktualnego stanu wiedzy jest wolny od patentów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Compress/LZV1.pm
%dir %{perl_vendorarch}/auto/Compress/LZV1
%{perl_vendorarch}/auto/Compress/LZV1/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Compress/LZV1/*.so
%{_mandir}/man3/*
