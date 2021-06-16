#!/usr/bin/env python3
########################################################################
__author__ = "seppe.gadeyne@student.kdg.be"
__description__ = "arguments exercise, use as sudo ./arguments 192.168.199.129"
__license__ = "GPLv3 https://www.gnu.org/licenses/gpl-3.0.nl.html"
__arguments__ = "ip address eg.: 192.168.199.129"
__version__ = "1.0"
__requires__ = "sudo apt install python3-scapy"
########################################################################

import sys
from scapy.all import sr1, IP, ICMP

packet = sr1(IP(dst=str(sys.argv[1])) / ICMP(), timeout=1)

if packet:
    packet.show()
