Summary:	Mozilla Easy Search Toolbar
Summary(pl):	Pasek narzêdziowy EasySearch dla mozilli
Name:		mozilla-addon-easysearch
%define		_realname	easysearch
Version:	097
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://easysearch.mozdev.org/download/%{_realname}_%{version}.xpi
Source1:	%{_easysearch-installed-chrome.txt
URL:		http://easysearch.mozdev.org/
BuildRequires:	unzip
Requires:	mozilla >= 1.0
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define         _chromedir      %{_libdir}/mozilla/chrome

%description
Mozilla EasySearch Toolbar - a toolbar with search engines support.

%description -l pl
Pasek narzêdziowy z wyszukiwarkami dla mozilli.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
cd %{_chromedir}
cat %{_realname}-installed-chrome.txt >> installed-chrome.txt

%postun
cd %{_chromedir}
cat installed-chrome.txt | grep -v "easysearch.jar" > installed-chrome.txt.tmp
cat installed-chrome.txt.tmp > installed-chrome.txt
rm -f installed-chrome.txt.tmp

%files
%defattr(644,root,root,755)
%{_chromedir}/easysearch.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
