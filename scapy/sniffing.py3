#!/usr/bin/env python3
########################################################################
__author__ = "seppe.gadeyne@student.kdg.be"
__description__ = "scapy sniffer, sniffs 10 packets"
__license__ = "GPLv3 https://www.gnu.org/licenses/gpl-3.0.nl.html"
__arguments__ = "none"
__version__ = "1.0"
__requires__ = "sudo apt install tcpdump python3-scapy"
########################################################################

from os import getuid

if getuid() != 0:
    print("Warning: starting as non root user!")

try:
    from scapy.all import sniff

    about = "### " + __description__ + " ###"
    print(about)

    packets = sniff(count=10)
    packets.summary()

except:
    print("Error: unable to sniff packets, try using sudo.")
    exit(1)
