Summary:	Networking with the isdn subsystem
Name:		isdn4net
Version:	1.4.5
Release:	6mdk
License:	GPL
Group:		System/Kernel and hardware

Source0:	%{name}-%{version}.tar.bz2

Patch2:		isdn4net-1.4.5-extended.patch.bz2
Patch3:		isdn4net-isdn4linux.patch.bz2
Patch4:		isdn4net-isdn4linux2.patch.bz2
Patch5:		isdn4net-1.4.5-firmware.patch.bz2

URL:		http://www.terminator.net/isdn4net/
BuildArch:	noarch
BuildRoot:	%_tmppath/%name-%version-%release-root

%description
This package provides several scripts to do networking with isdn4linux, several
sample configurations for card and ippp setup and small configuration and
admin utility.

%prep

%setup -q
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%install
install -d $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/network-scripts
install network-scripts/ifup-ippp $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/network-scripts
install network-scripts/ifdown-ippp $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/network-scripts
install network-scripts/ifup-isdn $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/network-scripts
install network-scripts/ifdown-isdn $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/network-scripts

# Install default config files
install defaults/ifcfg-ippp0 $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/network-scripts/ifcfg-ippp0

#install defaults/ifcfg-isdn0 $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/network-scripts/ifcfg-isdn0
install -d $RPM_BUILD_ROOT/%{_initrddir}
install init.d/isdn4linux $RPM_BUILD_ROOT/%{_initrddir}
install -d $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig
install defaults/isdn $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/isdn
install -d $RPM_BUILD_ROOT/%{_sysconfdir}/isdn/profile
install defaults/ippp.default $RPM_BUILD_ROOT/%{_sysconfdir}/isdn/profile/ippp.default
install defaults/isdn.default $RPM_BUILD_ROOT/%{_sysconfdir}/isdn/profile/isdn.default
install defaults/isdn.map $RPM_BUILD_ROOT/%{_sysconfdir}/isdn/profile/isdn.map
install defaults/ippp.map $RPM_BUILD_ROOT/%{_sysconfdir}/isdn/profile/ippp.map
install -d $RPM_BUILD_ROOT/%{_sysconfdir}/isdn/profile/card
install defaults/mycard $RPM_BUILD_ROOT/%{_sysconfdir}/isdn/profile/card/mycard
install -d $RPM_BUILD_ROOT/%{_sysconfdir}/isdn/profile/link
install defaults/myisp $RPM_BUILD_ROOT/%{_sysconfdir}/isdn/profile/link/myisp
install -d $RPM_BUILD_ROOT/%{_sysconfdir}/isdn/budget

#install defaults/budget/ippp0 $RPM_BUILD_ROOT/%{_sysconfdir}/isdn/budget/ippp0
install -d  $RPM_BUILD_ROOT/%{_sysconfdir}/isdn/timru

#install defaults/timru/ippp0 $RPM_BUILD_ROOT/%{_sysconfdir}/isdn/timru/ippp0
install defaults/my_isdnlog.conf $RPM_BUILD_ROOT/%{_sysconfdir}/isdn/my_isdnlog.conf

# Install frontend
install -d $RPM_BUILD_ROOT/%{_bindir}
install bin/isdn $RPM_BUILD_ROOT/%{_bindir}/isdn

%post
echo -n "Activating isdn4linux card init:"
%_post_service isdn4linux
echo " done."

%preun
echo -n "Deactivating isdn4linux card init:"
%_preun_service isdn4linux
echo " done."

%clean
rm -fr %buildroot

%files
%defattr(-,root,root,0755)
%config(noreplace) %{_sysconfdir}/sysconfig/network-scripts/ifup-ippp
%config(noreplace) %{_sysconfdir}/sysconfig/network-scripts/ifdown-ippp
%config(noreplace) %{_sysconfdir}/sysconfig/network-scripts/ifup-isdn
%config(noreplace) %{_sysconfdir}/sysconfig/network-scripts/ifdown-isdn
%config(noreplace) %{_initrddir}/isdn4linux
%{_bindir}/isdn
%config(noreplace) %{_sysconfdir}/sysconfig/isdn
%config(noreplace) %{_sysconfdir}/sysconfig/network-scripts/ifcfg-ippp0
%config(noreplace) %{_sysconfdir}/isdn/profile/ippp.default
%config(noreplace) %{_sysconfdir}/isdn/profile/isdn.default
%config(noreplace) %{_sysconfdir}/isdn/profile/ippp.map
%config(noreplace) %{_sysconfdir}/isdn/profile/isdn.map
%config(noreplace) %{_sysconfdir}/isdn/profile/link/myisp
%config(noreplace) %{_sysconfdir}/isdn/profile/card/mycard
%config(noreplace) %{_sysconfdir}/isdn/my_isdnlog.conf
%doc defaults
%doc samples
%doc doc
%doc README
%dir %{_sysconfdir}/isdn/profile
%dir %{_sysconfdir}/isdn/profile/link
%dir %{_sysconfdir}/isdn/profile/card
%dir %{_sysconfdir}/isdn/timru
%dir %{_sysconfdir}/isdn/budget

%changelog
* Wed Mar 20 2002 David BAUDENS <baudens@mandrakesoft.com> 1.4.5-4mdk
- Clean after build
- Fix BuildRoot

* Thu Jul 26 2001 dam's <damien@mandrakesoft.com> 1.4.5-3mdk
- added firmware support (isdn4net-firmware)

* Thu Mar 29 2001 dam's <damien@mandrakesoft.com> 1.4.5-2mdk
- new service policy.

* Mon Dec  4 2000 dam's <damien@mandrakesoft.com> 1.4.5-1mdk
- corrected patch4 (isdn4net-isdn4linux2).
- modified patch2 (isdn4net-1.4.3-extended) to isdn4net-1.4.5-extended
- version 1.4.5

* Mon Nov 27 2000 dam's <damien@mandrakesoft.com> 1.4.3-10mdk
- corrected isdn4linux init script (patch n°4 isdn4linux2)

* Thu Sep 14 2000 dam's <damien@mandrakesoft.com> 1.4.3-9mdk
- removed packager tag.
- removed iniscript install. dadou sux. Redhog too.
- transfomed the redhog modifs to a patch (n°3 isdn4linux)

* Wed Sep  6 2000 dam's <damien@mandrakesoft.com> 1.4.3-8mdk
- removed cat isdn doc in post...

* Fri Sep  1 2000 dam's <damien@mandrakesoft.com> 1.4.3-7mdk
- added noreplace.

* Thu Aug 31 2000 David BAUDENS <baudens@mandrakesoft.com> 1.4.3-6mdk
- Apply RedHog modification in init
- Fix Description

* Sat Aug 26 2000 dam's <damien@mandrakesoft.com> 1.4.3-5mdk
- removed patch 1 and integrated it in the specfile.

* Sat Aug 26 2000 dam's <damien@mandrakesoft.com> 1.4.3-4mdk
- BM + macros.
- changed /usr/local/bin/isdn to /usr/bin/isdn (patch 1 rpm-install)
- added patch 2 (extended) to support more isdn cards.

* Fri Mar 31 2000 Jesse Kuang <kjx@linux-mandrake.com> 1.4.3-3mdk
- Release.

* Sat Feb 26 2000 Jesse Kuang <kjx@linux-mandrake.com>
- build noarch package

* Sat Jan 29 2000 Jesse Kuang <kjx@linux-mandrake.com>
- update to isdn4net-1.4.3, fixes isdn shell script for bash 1.14

* Fri Jan 07 2000 Francis Galiegue <francis@mandrakesoft.com>
- Fixed braindead symlinks
- Fixed YAT (Yet Another Typo (tm)) in /usr/bin/isdn script
- SysV symlinks in specs disagreed with those of chkconfig, fixed

* Wed Nov 10 1999 John Buswell <johnb@mandrakesoft.com>
- Added BuildRoot
- Fixed path and permissions
- Build Release

* Sun Jun 27 1999 Jesse Kuang <kjx@linux.org.cn>
- add support for more mppp, SLAVE for ippp32/ippp33 ...
- Chmouel:
	More mandrake adaptations.
