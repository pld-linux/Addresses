Summary:	Contact manager for GNUstep
Summary(pl):	Zarz±dca kontaktów dla GNUstepa
Name:		Addresses
Version:	0.3.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://giesler.biz/bjoern/Downloads/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	426ddc37e11cc09aca78965aace3f91d
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
%setup -q -n %{name}

find . -type d -name CVS | xargs rm -rf

%build
. %{_prefix}/System/Library/Makefiles/GNUstep.sh
%{__make} \
	debug=no \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Library/Makefiles/GNUstep.sh

%{__make} install debug=no \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc TODO Documentation/*.ps

%dir %{_prefix}/System/Applications/Contacts.app
%attr(755,root,root) %{_prefix}/System/Applications/Contacts.app/Contacts
%dir %{_prefix}/System/Applications/Contacts.app/Resources
%{_prefix}/System/Applications/Contacts.app/Resources/*.desktop
%{_prefix}/System/Applications/Contacts.app/Resources/*.plist
%{_prefix}/System/Applications/Contacts.app/Resources/*.tiff
%{_prefix}/System/Applications/Contacts.app/Resources/*.gorm

%dir %{_prefix}/System/Applications/Contacts.app/%{gscpu}
%dir %{_prefix}/System/Applications/Contacts.app/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Applications/Contacts.app/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Applications/Contacts.app/%{gscpu}/%{gsos}/%{libcombo}/Contacts
%{_prefix}/System/Applications/Contacts.app/%{gscpu}/%{gsos}/%{libcombo}/*.openapp
