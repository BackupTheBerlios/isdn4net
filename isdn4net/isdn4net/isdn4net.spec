Summary: Networking with the isdn subsystem.
Name: isdn4net
Version: 1.4.5
Release: 1
Copyright: GPL
Group: Networking/Utilities
Source0: %{name}-%{version}.tar.gz
URL: http://www.terminator.net/isdn4net/
Packager: Stein Vråle <stein@terminator.net>
BuildRoot:/tmp/rpm-%{name}
%description
Provides several scripts to do networking with isdn4linux.
Provides several sample configurations for card and ippp setup.
Provides small configuration and admin utility.
%prep
%setup
%install
install/rpm-install
%post
echo -n "Adding isdn4linux initscript:"
chkconfig --del isdn4linux
chkconfig --add isdn4linux
echo " done."
echo -n "Adding isdnlog initscript:"
chkconfig --del isdnlog
chkconfig --add isdnlog
echo " done."
cat /usr/doc/%{name}-%{version}/doc/README.rpm
%preun
if [ "$1" = 0 ] ; then
  echo -n "Removing isdn4linux initscript:"
  chkconfig --del isdn4linux
  echo " done."
  echo -n "Removing isdnlog initscript:"
  chkconfig --del isdnlog
  echo " done."
fi
%files
/etc/sysconfig/network-scripts/ifup-ippp
/etc/sysconfig/network-scripts/ifdown-ippp
/etc/sysconfig/network-scripts/ifup-isdn
/etc/sysconfig/network-scripts/ifdown-isdn
/etc/rc.d/init.d/isdn4linux
/etc/rc.d/init.d/isdnlog
/usr/local/bin/isdn
%config(noreplace) /etc/sysconfig/isdn
%config(noreplace) /etc/sysconfig/network-scripts/ifcfg-ippp0
%config(noreplace) /etc/isdn/profile/ippp.default
%config(noreplace) /etc/isdn/profile/isdn.default
%config(noreplace) /etc/isdn/profile/ippp.map
%config(noreplace) /etc/isdn/profile/isdn.map
%config(noreplace) /etc/isdn/profile/link/myisp
%config(noreplace) /etc/isdn/profile/card/mycard
%config(noreplace) /etc/isdn/my_isdnlog.conf
%doc defaults
%doc samples
%doc doc
%doc isdn4net.spec
%doc README
%dir /etc/isdn/profile
%dir /etc/isdn/profile/link
%dir /etc/isdn/profile/card
%dir /etc/isdn/timru
%dir /etc/isdn/budget
