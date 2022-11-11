#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 10:57:36 2022

@author: mikelin
"""

class Campground:
    campSiteTotal=50
    campSiteBookedCount=0
    campSitesBooked=[]
    
    def __init__(self):
        if (self.campSiteBookedCount > self.campSiteTotal):
            raise Exception("Exceed total campsites")
    
    def reserveSite(self,siteRequested,customerName):
        if (siteRequested in self.campSitesBooked):
            raise Exception('Site not available')
        self.campSiteBookedCount+=1
        self.campSitesBooked.append(siteRequested)
        return siteRequested
        
    def cancelSite(self):
        self.site = input('Enter site number to cancel :')
        if (self.site not in self.campSitesBooked):
            raise Exception('This site was not reserved')
        self.campSitesBooked.remove(self.site)
        print('Reservation is now canceled')
        
    def checkAvailability(self):
        print(self.campSiteTotal-self.campSiteBookedCount)
    