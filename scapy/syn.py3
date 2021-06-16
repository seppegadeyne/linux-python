#!/usr/bin/env python3
########################################################################
__author__ = "seppe.gadeyne@student.kdg.be"
__description__ = "TCP SYN scan"
__license__ = "GPLv3 https://www.gnu.org/licenses/gpl-3.0.nl.html"
__arguments__ = "<network>"
__version__ = "1.0"
__requires__ = "sudo apt install python3-scapy nmap"
########################################################################
import sys
from os import getuid
if getuid() != 0:
    print("You need to run this application as root")
    sys.exit(1)

from scapy.all import *
from itertools import chain

interface = "wlp4s0"
dstports = (1, 1024)

if len(sys.argv) != 2:
    print("Usage: sudo " + sys.argv[0] + " " + __arguments__)
    print(" eg: sudo " + sys.argv[0] + " 192.168.0.234")
    sys.exit(1)

ports = (dstports,)
nmap = "nmap -rp " + '-'.join(map(str, chain.from_iterable(ports))) + " -sS " + str(sys.argv[1])
ans, unans = sr(IP(dst=str(sys.argv[1])) / TCP(flags="S", dport=dstports), timeout=1, verbose=0)

print("Scapy scan report for " + str(sys.argv[1]))
for s, r in ans:
    if r.haslayer(TCP) and r.getlayer(TCP).flags == "SA":
        # r.show()
        print(r.sprintf("Port %TCP.sport% is open"))

# os.system(nmap)  # om  te vergelijken met nmap

