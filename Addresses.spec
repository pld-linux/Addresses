Summary:	Contact manager for GNUstep
Summary(pl):	Zarz±dca kontaktów dla GNUstepa
Name:		Addresses
Version:	0.4.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://giesler.biz/bjoern/Downloads/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	9ace064497b4775e2a451f39430ac107
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
Contacts to ksi±¿ka adresowa oraz us³uga ksi±¿ki adresowej dla
aplikacji GNUstepa.

%prep
%setup -q 

find . -type d -name CVS | xargs rm -rf

%build
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Library/Makefiles/GNUstep.sh
TOPDIR="`pwd`"
GNUSTEP_LOCAL_ROOT="$RPM_BUILD_ROOT%{_prefix}/System"
%{__make} \
	OPTFLAG="%{rpmcflags} -I$RPM_BUILD_DIR/%{name}-%{version}" \
	debug=no \
	messages=yes

%install
make install GNUSTEP_INSTALLATION_DIR="$RPM_BUILD_ROOT%{_prefix}/System"

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc TODO


%dir %{_prefix}/System/Library/Frameworks/Addresses.framework
%dir %{_prefix}/System/Library/Frameworks/Addresses.framework/Versions
%dir %{_prefix}/System/Library/Frameworks/Addresses.framework/Versions/A
%attr(755,root,root) %{_prefix}/System/Library/Frameworks/Addresses.framework/Versions/A/ix86
%{_prefix}/System/Library/Frameworks/Addresses.framework/Versions/A/Headers
%dir %{_prefix}/System/Library/Frameworks/Addresses.framework/Versions/A/Resources
%{_prefix}/System/Library/Frameworks/Addresses.framework/Versions/A/Resources/*.plist
%{_prefix}/System/Library/Frameworks/Addresses.framework/Versions/A/Resources/English.lproj
%lang(de) %{_prefix}/System/Library/Frameworks/Addresses.framework/Versions/A/Resources/German.lproj
%{_prefix}/System/Library/Frameworks/Addresses.framework/Versions/Current
%{_prefix}/System/Library/Frameworks/Addresses.framework/Resources
%{_prefix}/System/Library/Frameworks/Addresses.framework/Headers
%dir %{_prefix}/System/Library/Frameworks/AddressView.framework
%dir %{_prefix}/System/Library/Frameworks/AddressView.framework/Versions
%dir %{_prefix}/System/Library/Frameworks/AddressView.framework/Versions/A
%attr(755,root,root) %{_prefix}/System/Library/Frameworks/AddressView.framework/Versions/A/ix86
%{_prefix}/System/Library/Frameworks/AddressView.framework/Versions/A/Headers
%{_prefix}/System/Library/Frameworks/AddressView.framework/Versions/A/Resources
%{_prefix}/System/Library/Frameworks/AddressView.framework/Versions/A/Resources/*.plist
%{_prefix}/System/Library/Frameworks/AddressView.framework/Versions/A/Resources/*.tiff
%{_prefix}/System/Library/Frameworks/AddressView.framework/Versions/A/Resources/English.lproj
%lang(de) %{_prefix}/System/Library/Frameworks/AddressView.framework/Versions/A/Resources/German.lproj
%{_prefix}/System/Library/Frameworks/AddressView.framework/Versions/Current
%{_prefix}/System/Library/Frameworks/AddressView.framework/Resources
%{_prefix}/System/Library/Frameworks/AddressView.framework/Headers
%attr(755,root,root) %{_prefix}/System/Library/Libraries/ix86/linux-gnu/gnu-gnu-gnu/*
%{_prefix}/System/Library/Headers/gnu-gnu-gnu/Addresses
%{_prefix}/System/Library/Headers/gnu-gnu-gnu/AddressView
%attr(755,root,root) %{_prefix}/System/Tools/ix86/linux-gnu/gnu-gnu-gnu/*
%dir %{_prefix}/System/Applications/AddressManager.app
%attr(755,root,root) %{_prefix}/System/Applications/AddressManager.app/ix86
%attr(755,root,root) %{_prefix}/System/Applications/AddressManager.app/AddressManager
%dir %{_prefix}/System/Applications/AddressManager.app/Resources
%{_prefix}/System/Applications/AddressManager.app/Resources/*.plist
%{_prefix}/System/Applications/AddressManager.app/Resources/*.desktop
%{_prefix}/System/Applications/AddressManager.app/Resources/*.tiff
%{_prefix}/System/Applications/AddressManager.app/Resources/English.lproj
%lang(de) %{_prefix}/System/Applications/AddressManager.app/Resources/German.lproj
