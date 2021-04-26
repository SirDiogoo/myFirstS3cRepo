#!/bin/python3

import os 
import ipaddress
import 
user=os.getlogin()
print ("o utilizador actual do sistema é", user)

for host in ipaddress.IPv4Network('192.168.3.0/24'):
    response = os.system("ping -c 1 " + str(host) + " > /dev/null 2>&1")
    if response == 0:
        print (str(host)+ " está online!")
    else:
        print (str(host)+ " está offline!")