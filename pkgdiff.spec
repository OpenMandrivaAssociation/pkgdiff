Summary:	A tool for analyzing changes in Linux software packages
Name:		pkgdiff
Version:	1.7.2
Release:	1
Group:		Development/Other
License:	GPLv2+
URL:		https://lvc.github.io/pkgdiff/
Source0:	https://github.com/lvc/pkgdiff/archive/%{version}.tar.gz
Requires:	wdiff
Requires:	binutils
Requires:       gawk
Suggests:       abi-compliance-checker >= 1.96.7
BuildRequires:  help2man
BuildArch:	noarch

%description
Package Changes Analyzer (pkgdiff) is a tool for analyzing changes
in Linux software packages (RPM, DEB, TAR.GZ, etc). The tool is
intended for Linux maintainers who are interested in ensuring
compatibility of old and new versions of packages.

%prep
%setup -q
chmod 0644 LICENSE README
chmod 0755 %{name}.pl
cp %{name}.pl %{name}
# Generate man page
help2man -N --no-discard-stderr -o %{name}.1 ./%{name}
sed -i 's/\(.\)/\n\1/' %{name}.1
sed -i 's/PACKAGE/PKGDIFF/' %{name}.1

%build
# Nothing to build.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_prefix}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1
perl Makefile.pl -install --prefix=%{_prefix} --destdir=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_mandir}/man1/*
%doc LICENSE README doc/*
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Wed Apr 04 2012 Andrey Ponomarenko <andrey.ponomarenko@rosalab.ru> 1.3.3-1mdv2011.0
+ Revision: 789183
- Updated to 1.3.3

* Tue Mar 06 2012 Andrey Ponomarenko <andrey.ponomarenko@rosalab.ru> 1.3-1
+ Revision: 782485
- Updated to 1.3

* Fri Feb 17 2012 Andrey Ponomarenko <andrey.ponomarenko@rosalab.ru> 1.2-1
+ Revision: 775947
- Updated to 1.2

* Fri Feb 10 2012 Andrey Ponomarenko <andrey.ponomarenko@rosalab.ru> 1.1.1-1
+ Revision: 772484
- Updated to 1.1.1

* Thu Feb 09 2012 Andrey Ponomarenko <andrey.ponomarenko@rosalab.ru> 1.1-1
+ Revision: 772334
- Updated to 1.1

* Thu Feb 02 2012 Andrey Ponomarenko <andrey.ponomarenko@rosalab.ru> 1.0.1-1
+ Revision: 770631
- Updated to 1.0.1

* Mon Jan 30 2012 Andrey Ponomarenko <andrey.ponomarenko@rosalab.ru> 1.0-2
+ Revision: 769732
- Initial package.
- Created package structure for pkgdiff.

