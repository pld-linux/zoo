Summary:	file archiving utility with compression
Name:		zoo
Version:	2.10
Release:	4
Copyright:	Copyrighted, freely distributable if unmodified
Group:		Applications/Archiving
Group(de):	Applikationen/Archivierung
Group(pl):	Aplikacje/Archiwizacja
Source0:	ftp://sunsite.unc.edu:/pub/Linux/utils/compress/%{name}-%{PACKAGE_VERSION}.tar.gz
Patch0:		%{name}-2.10.linux.diff.gz
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
zoo is a file archiving utility for maintaining collections of files.
It uses Lempel-Ziv compression to provide space savings in the range
of 20 to 80 percent depending on the type of data. Written by Rahul
Dhesi, and posted to the USENET newsgroup comp.sources.misc.

%prep
%setup -q 
%patch -p1

%build
%{__make} "OPTIM=$RPM_OPT_FLAGS" linux

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_prefix}/man/man1
install fiz $RPM_BUILD_ROOT%{_bindir}/fiz
install zoo $RPM_BUILD_ROOT%{_bindir}/zoo
install fiz.1 $RPM_BUILD_ROOT%{_prefix}/man/man1/fiz.1
install zoo.1 $RPM_BUILD_ROOT%{_prefix}/man/man1/zoo.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright
%attr(0755, root, root) %{_bindir}/fiz
%attr(0755, root, root) %{_bindir}/zoo
%{_prefix}/man/man1/fiz.1
%{_prefix}/man/man1/zoo.1
