Summary:	Mozilla Easy Search Toolbar
Summary(pl):	Pasek narzêdziowy EasySearch dla mozilli
Name:		mozilla-addon-easysearch
%define		_realname	easysearch
Version:	097
Release:	4
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://easysearch.mozdev.org/download/%{_realname}_%{version}.xpi
# Source0-md5:	bb0c5545182037fddb7c656156f89253
Source1:	%{_realname}-installed-chrome.txt
URL:		http://easysearch.mozdev.org/
BuildRequires:	unzip
Requires(post,postun):	mozilla >= 1.7.3-3
Requires(post,postun):	textutils
Requires:	mozilla >= 1.0-7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

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
%{_sbindir}/mozilla-chrome+xpcom-generate

%postun
%{_sbindir}/mozilla-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
