#!/bin/python3

import os
import ipaddress
total=-1
online=0
listaIPs=[]
for host in ipaddress.IPv4Network('192.168.10.0/24'):
    resposta = os.system("ping -c 1 " + str(host) + " > /dev/null 2>&1")
    if resposta == 0:
        print (str(host)+ " está online")
        online=online+1
        total=total+1
    else:  
        print (str(host)+ " está offline")
        total=total+1
    if total < 51:
        listaIPs.append(str(host))
print(listaIPs)

