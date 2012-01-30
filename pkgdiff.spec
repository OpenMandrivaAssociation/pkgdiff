Summary:	A tool for analyzing changes in Linux software packages
Name:		pkgdiff
Version:	1.0
Release:	%mkrel 2
Group:		Development/Other
License:	GPLv2+
URL:		http://pkgdiff.github.com/pkgdiff/
Source0:	https://github.com/downloads/pkgdiff/pkgdiff/pkgdiff-%{version}.tar.gz
Requires:	wdiff
Requires:	binutils
Requires:       gawk
Suggests:       abi-compliance-checker >= 1.96
BuildRequires:  help2man
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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