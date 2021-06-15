#!/usr/bin/env python3
########################################################################
__author__ = "seppe.gadeyne@student.kdg.be"
__description__ = "traceroute with graph output"
__license__ = "GPLv3 https://www.gnu.org/licenses/gpl-3.0.nl.html"
__arguments__ = "none"
__version__ = "1.0"
__output__      = "tracert" + __version__ + ".png"
__requires__    = "sudo apt install nmap python3-crypto ipython3"
__requires__ = "sudo apt install python3-graphviz imagemagick"
########################################################################

print("##### "+__description__+"#####")

from scapy.all import *

res, unans = traceroute(["straffesites.com"], dport=[80,443], maxttl=20, retry=-2)
res.graph(target=__output__)