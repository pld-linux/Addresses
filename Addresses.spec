Summary:	Contact manager for GNUstep
Summary(pl):	Zarz�dca kontakt�w dla GNUstepa
Name:		Addresses
Version:	0.4.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://giesler.biz/bjoern/Downloads/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	9ace064497b4775e2a451f39430ac107
Patch0:		%{name}-make.patch
URL:		http://giesler.biz/bjoern/English/Software.html#Addresses
BuildRequires:	gnustep-gui-devel >= 0.8.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/lib/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%{_target_cpu}
%endif

%description
Contacts is an address book and address book service for GNUstep apps.

%description -l pl
Contacts to ksi��ka adresowa oraz us�uga ksi��ki adresowej dla
aplikacji GNUstepa.

%package devel
Summary:	Header files for Addresses service
Summary(pl):	Pliki nag��wkowe dla us�ugi Addresses
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Addresses service.

%description devel -l pl
Pliki nag��wkowe dla us�ugi Addresses.

%prep
%setup -q 
%patch0 -p1

find . -type d -name CVS | xargs rm -rf

%build
. %{_prefix}/System/Library/Makefiles/GNUstep.sh
TOPDIR="`pwd`"
GNUSTEP_LOCAL_ROOT="$RPM_BUILD_ROOT%{_prefix}/System"
%{__make} \
	OPTFLAG="%{rpmcflags} -I$RPM_BUILD_DIR/%{name}-%{version}" \
	debug=no \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	GNUSTEP_INSTALLATION_DIR="$RPM_BUILD_ROOT%{_prefix}/System"

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc TODO

%dir %{_prefix}/System/Applications/AddressManager.app
%dir %{_prefix}/System/Applications/AddressManager.app/%{gscpu}
%dir %{_prefix}/System/Applications/AddressManager.app/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Applications/AddressManager.app/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Applications/AddressManager.app/%{gscpu}/%{gsos}/%{libcombo}/AddressManager
%{_prefix}/System/Applications/AddressManager.app/%{gscpu}/%{gsos}/%{libcombo}/*.openapp
%attr(755,root,root) %{_prefix}/System/Applications/AddressManager.app/AddressManager
%dir %{_prefix}/System/Applications/AddressManager.app/Resources
%{_prefix}/System/Applications/AddressManager.app/Resources/*.plist
%{_prefix}/System/Applications/AddressManager.app/Resources/*.desktop
%{_prefix}/System/Applications/AddressManager.app/Resources/*.tiff
%{_prefix}/System/Applications/AddressManager.app/Resources/English.lproj
%lang(nl) %{_prefix}/System/Applications/AddressManager.app/Resources/Dutch.lproj
%lang(fr) %{_prefix}/System/Applications/AddressManager.app/Resources/French.lproj
%lang(de) %{_prefix}/System/Applications/AddressManager.app/Resources/German.lproj

%dir %{_prefix}/System/Library/Frameworks/Addresses.framework
%{_prefix}/System/Library/Frameworks/Addresses.framework/Resources
%dir %{_prefix}/System/Library/Frameworks/Addresses.framework/Versions
%dir %{_prefix}/System/Library/Frameworks/Addresses.framework/Versions/A
%attr(755,root,root) %{_prefix}/System/Library/Frameworks/Addresses.framework/Versions/A/%{gscpu}
%dir %{_prefix}/System/Library/Frameworks/Addresses.framework/Versions/A/Resources
%{_prefix}/System/Library/Frameworks/Addresses.framework/Versions/A/Resources/*.plist
%{_prefix}/System/Library/Frameworks/Addresses.framework/Versions/A/Resources/English.lproj
%lang(nl) %{_prefix}/System/Library/Frameworks/Addresses.framework/Versions/A/Resources/Dutch.lproj
%lang(fr) %{_prefix}/System/Library/Frameworks/Addresses.framework/Versions/A/Resources/French.lproj
%lang(de) %{_prefix}/System/Library/Frameworks/Addresses.framework/Versions/A/Resources/German.lproj
%{_prefix}/System/Library/Frameworks/Addresses.framework/Versions/Current
%dir %{_prefix}/System/Library/Frameworks/AddressView.framework
%{_prefix}/System/Library/Frameworks/AddressView.framework/Resources
%dir %{_prefix}/System/Library/Frameworks/AddressView.framework/Versions
%dir %{_prefix}/System/Library/Frameworks/AddressView.framework/Versions/A
%attr(755,root,root) %{_prefix}/System/Library/Frameworks/AddressView.framework/Versions/A/%{gscpu}
%dir %{_prefix}/System/Library/Frameworks/AddressView.framework/Versions/A/Resources
%{_prefix}/System/Library/Frameworks/AddressView.framework/Versions/A/Resources/*.dict
%{_prefix}/System/Library/Frameworks/AddressView.framework/Versions/A/Resources/*.plist
%{_prefix}/System/Library/Frameworks/AddressView.framework/Versions/A/Resources/*.tiff
%{_prefix}/System/Library/Frameworks/AddressView.framework/Versions/A/Resources/English.lproj
%lang(nl) %{_prefix}/System/Library/Frameworks/AddressView.framework/Versions/A/Resources/Dutch.lproj
%lang(fr) %{_prefix}/System/Library/Frameworks/AddressView.framework/Versions/A/Resources/French.lproj
%lang(de) %{_prefix}/System/Library/Frameworks/AddressView.framework/Versions/A/Resources/German.lproj
%{_prefix}/System/Library/Frameworks/AddressView.framework/Versions/Current

%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/*.so
%{_prefix}/System/Library/Frameworks/Addresses.framework/Headers
%{_prefix}/System/Library/Frameworks/Addresses.framework/Versions/A/Headers
%{_prefix}/System/Library/Frameworks/AddressView.framework/Headers
%{_prefix}/System/Library/Frameworks/AddressView.framework/Versions/A/Headers
%{_prefix}/System/Library/Headers/%{libcombo}/Addresses
%{_prefix}/System/Library/Headers/%{libcombo}/AddressView
