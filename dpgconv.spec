Name:			dpgconv
Version: 		9
Release:		%mkrel 1

Summary: 	Transcode video files to DPG (nDs mPeG)
Source0: 	http://theli.is-a-geek.org/files/dpgconv/dpgconv-9.py.bz2
Source1:	dpgconv-readme
Source2:	dpgshow

License: 	GPLv2
Group:	 	Video
URL:		http://theli.is-a-geek.org/blog/static/dpgconv

Requires:	mplayer
Requires:	mencoder
Requires:	mpeg-stat
Requires:	python-imaging

BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description
A script to transcode video files to DPG format suitable for Nintendo DS (tm)


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
bzip2 -dc %{SOURCE0} > %{buildroot}%{_bindir}/%{name}.py
install -D -m 644 %{SOURCE1} %{buildroot}%{_docdir}/%{name}/Get-Started
install -m 644 %{SOURCE2} %{buildroot}%{_docdir}/%{name}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_docdir}/%{name}/Get-Started
%{_docdir}/%{name}/dpgshow
%attr(0755,root,root) %{_bindir}/dpgconv.py


