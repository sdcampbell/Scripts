#!/usr/bin/env python3
import netaddr
import sys

if len(sys.argv) < 2:
    print("Usage: iplist '192.168.1.0/24'")
    sys.exit()

for ip in netaddr.IPNetwork(sys.argv[1]).iter_hosts():
    print('%s' % ip)
