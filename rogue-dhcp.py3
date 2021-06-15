#!/usr/bin/env python3
########################################################################
__author__ = "seppe.gadeyne@student.kdg.be"
__description__ = "discover rogue DHCP server on your LAN"
__license__ = "GPLv3 https://www.gnu.org/licenses/gpl-3.0.nl.html"
__arguments__ = "None"
__version__ = "1.0"
__requires__ = "sudo apt install python3-scapy"
########################################################################

from scapy.all import *

conf.checkIPaddr = False
hw = get_if_raw_hwaddr(conf.iface)
dhcp_discover = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src="0.0.0.0", dst="255.255.255.255") / UDP(sport=68, dport=67) / BOOTP(chaddr=hw) / DHCP(options=[("message-type", "discover"), "end"])
ans, unans = srp(dhcp_discover, multi=True)  # Press CTRL-C after several seconds
ans.summary()

for p in ans:
    p.show()
    print(p[1][Ether].src, p[1][IP].src)
