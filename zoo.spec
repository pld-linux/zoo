Summary:	File archiving utility with compression
Summary(pl.UTF-8):	Program do archiwizacji i kompresji
Summary(ru.UTF-8):	Утилита архивации и компрессии для архивов формата ZOO
Summary(uk.UTF-8):	Утиліта архивації та компресії для архівів формату ZOO
Name:		zoo
Version:	2.10
Release:	8
License:	Copyrighted, freely distributable if unmodified
Group:		Applications/Archiving
# ftp://sunsite.unc.edu/pub/Linux/utils/compress/%{name}-%{version}-3.src.rpm
Source0:	ftp://ftp.slackware.org/pub/slackware/source/a/bin/%{name}-%{version}.tar.gz
# Source0-md5:	f5d3ffdd65cc8a511c83e3c3f108c27e
# I hope these patches don't violate license...
# (source tarball is still unmodified, patches only make thing build,
# without any changes in behaviour of produced binary)
Patch0:		ftp://sunsite.unc.edu/pub/Linux/utils/compress/%{name}-2.10.linux.diff.gz
Patch1:		%{name}-morelinux.patch
Patch2:		%{name}-CAN-2005-2349.patch
Patch3:		%{name}-febz-183426.patch
Patch4:		%{name}-security_pathsize.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
zoo is a file archiving utility for maintaining collections of files.
It uses Lempel-Ziv compression to provide space savings in the range
of 20 to 80 percent depending on the type of data. Written by Rahul
Dhesi, and posted to the USENET newsgroup comp.sources.misc.

%description -l pl.UTF-8
zoo jest programem archiwizującym. Używa kompresji Lempel-Ziv. Może
zaoszczędzić od 20 do 80% miejsca, w zależności od rodzaju danych.
Napisany przez Rahula Dhesi, wysłany na grupę comp.sources.misc .

%description -l ru.UTF-8
Это утилита для архивирования и компрессирования файлов. В основном
она используется в мире DOS и Amiga, но может быть использована также
под Linux для извлечения файлов DOS из архивов ZOO.

%description -l uk.UTF-8
Це утиліта для архівації та компресування файлів. Вона в основному
використовується у світі DOS та Amiga, але може бути використана під
Linux для добування файлів з архівів ZOO.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1
%patch4 -p0

%build
%{__make} linux \
	CC="%{__cc}" \
	OPTIM="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install fiz zoo $RPM_BUILD_ROOT%{_bindir}
install fiz.1 zoo.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
