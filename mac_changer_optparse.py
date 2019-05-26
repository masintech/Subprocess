#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 11:22:25 2019

@author: marcus
"""

import optparse
parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="interface")
parser.add_option("-m", "--mac", dest="mac", help="mac address")

(options, arguments) = parser.parse_args()

#interface = input("interface: ")
#mac = input("MAC: ")
print("interface: "+options.interface)
print("MAC: "+options.mac)
