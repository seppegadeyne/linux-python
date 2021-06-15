#!/usr/bin/env python3
########################################################################
__author__ = "seppe.gadeyne@student.kdg.be"
__description__ = "Sniff 10 packets and write those to a PCAP + open wireshark"
__license__ = "GPLv3 https://www.gnu.org/licenses/gpl-3.0.nl.html"
__arguments__ = "<filename>"
__version__ = "1.0"
__requires__ = "sudo apt install python3-scapy wireshark"
########################################################################

import sys
from os import getuid
if getuid() != 0:
    print("You need to run this application as root")
    sys.exit(1)

from scapy.all import *

interface = "wlp4s0"
conf.prog.wireshark = "/usr/bin/wireshark"

if len(sys.argv) != 2:
    print("Usage: sudo " + sys.argv[0] + " " + __arguments__)
    print(" eg: sudo " + sys.argv[0] + " filename")
    sys.exit(1)

packets = sniff(count=10)
packets.summary()

wrpcap(str(sys.argv[1]) + ".cap", packets)
wireshark(packets)


