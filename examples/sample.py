# -*- coding: utf8 -*-
from SAMPQuery import SAMPQuery

IP_ADDRESS = "5.62.106.17"
PORT = 7777

samp = SAMPQuery(IP_ADDRESS, PORT)

print samp.getBasicInfo()
print samp.getRules()
print samp.getPlayers()
print samp.getDetailedPlayers()
