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
from scapy.all import *

# disable warnings
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

if len(sys.argv) != 2:
    print("Usage: sudo " + sys.argv[0] + " " + __arguments__)
    print(" eg: sudo " + sys.argv[0] + " 192.168.56.0/24")
    print(" eg: sudo " + sys.argv[0] + " 192.168.56.101-103")
    sys.exit(1)

ans, unans = sr(IP(src="192.168.0.43", dst=str(sys.argv[1])) / ICMP(), timeout=40)

# print("<html><ol>")
for s, r in ans:
    # r.show()
    # s.show()
    print(r.sprintf("<li>%IP.src% is alive</li>\n"))
# print("</ol></html>")
