Summary:	File archiving utility with compression
Summary(pl):	Program do archiwizacji i kompresji
Name:		zoo
Version:	2.10
Release:	5
License:	Copyrighted, freely distributable if unmodified
Group:		Applications/Archiving
Group(de):	Applikationen/Archivierung
Group(pl):	Aplikacje/Archiwizacja
#Source0:	ftp://sunsite.unc.edu:/pub/Linux/utils/compress/%{name}-%{PACKAGE_VERSION}.tar.gz
Source0:	ftp://ftp.slackware.org/pub/slackware/source/a/bin/%{name}-%{version}.tar.gz
Patch0:		ftp://sunsite.unc.edu/pub/Linux/utils/compress/%{name}-2.10.linux.diff.gz
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
zoo is a file archiving utility for maintaining collections of files.
It uses Lempel-Ziv compression to provide space savings in the range
of 20 to 80 percent depending on the type of data. Written by Rahul
Dhesi, and posted to the USENET newsgroup comp.sources.misc.

%description -l pl
zoo jest programem archiwizuj±cym. U¿ywa kompresji Lempel-Ziv. Mo¿e
zaoszczêdziæ od 20 do 80% miejsca, w zale¿no¶ci od rodzaju danych.
Napisany przez Rahula Dhesi, wys³any na grupê comp.sources.misc .

%prep
%setup -q 
%patch -p1

%build
%{__make} OPTIM="%{rpmcflags}" linux

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install fiz zoo $RPM_BUILD_ROOT%{_bindir}
install fiz.1 zoo.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf Copyright

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
