#!/usr/bin/env python3
########################################################################
__author__ = "seppe.gadeyne@student.kdg.be"
__description__ = "NULL scan script, opens output in wireshark"
__license__ = "GPLv3 https://www.gnu.org/licenses/gpl-3.0.nl.html"
__arguments__ = "None"
__version__ = "1.0"
__requires__ = "sudo apt install python3-scapy wireshark"
########################################################################

import sys
from os import getuid
if getuid() != 0:
    print("You need to run this application as root")
    sys.exit(1)

from scapy.all import *

destination = "192.168.0.234"
interface = "wlp4s0"
dstports = (0, 100)
conf.prog.wireshark = "/usr/bin/wireshark"

res, unans = sr(IP(dst=destination) / TCP(flags="", dport=dstports), timeout=1, verbose=0)

# wireshark(unans)
unans.summary()


