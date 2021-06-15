#!/usr/bin/env python3
########################################################################
__author__ = "seppe.gadeyne@student.kdg.be"
__description__ = "snif 1 ARP packet"
__license__ = "GPLv3 https://www.gnu.org/licenses/gpl-3.0.nl.html"
__arguments__ = "none"
__version__ = "1.0"
__requires__ = "sudo apt install python3-scapy"
########################################################################

from scapy.all import sniff

def analyze(p):
    # p.show()
    print(p.sprintf("ARP SRC adres %ARP.psrc% DST adres %ARP.pdst%"))

packet = sniff(filter="arp", prn=analyze, count = 1)
print(packet)
