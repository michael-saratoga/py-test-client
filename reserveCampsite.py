#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 11:23:22 2022

@author: mikelin
"""

from campground import Campground

try:
    myCampsite = Campground()
except:
    print('No campsite available')

looping = True
customerName = input("Name please ")
siteWanted = input('Which campsite do you want? ')
while looping:
    try:
        reservedSite = myCampsite.reserveSite(siteWanted, customerName)
        print('YAY you got a reservation')
    except:
        print('Site unavailable')
    print('These sites are no longer available ', myCampsite.campSitesBooked)
    print('Checking availability ...')
    myCampsite.checkAvailability()
    another = input('Another reservation? [y/n] ')
    if (another == 'y'):
        customerName = input("Name please ")
        siteWanted = input('Which campsite do you want? ')
    else:
        looping = False
print('Exiting reservation system')
print(myCampsite.__repr__())
