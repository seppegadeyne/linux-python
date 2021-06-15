#!/usr/bin/env python3
########################################################################
__author__ = "seppe.gadeyne@student.kdg.be"
__description__ = "sends an ICMP packet and return output in HTML"
__license__ = "GPLv3 https://www.gnu.org/licenses/gpl-3.0.nl.html"
__arguments__ = "<network>"
__version__ = "1.0"
__requires__ = "sudo apt install python3-scapy"
########################################################################

import sys
import logging
import ipaddress
from scapy.all import *

# disable warnings
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

if len(sys.argv) != 3:
    print("Usage: sudo " + sys.argv[0] + " " + __arguments__)
    print(" eg: sudo " + sys.argv[0] + " 192.168.56.0 192.168.56.50")
    sys.exit(1)

# for ip in ipaddress.IPv4Network(str(sys.argv[1])):
for ip in range(int(ipaddress.IPv4Address(sys.argv[1])), int(ipaddress.IPv4Address(sys.argv[2]))):
    # print("Scanning ip " + str(ip))
    packet = sr1(IP(dst=str(ipaddress.IPv4Address(ip)))/ICMP(), timeout=1, verbose=0, iface="wlp4s0")

    if packet:
        # packet.show()
        print(packet.sprintf("%IP.src% is alive"))
