#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 13:43:35 2022

@author: mikelin
"""

def myFunc(x):
    def innerFunc(y):
        print('In function : ',x*y)
        return x*y
    return innerFunc
# above nested function innerFunc() references enxclosing functions variables x and y, and the enclosing 
# fucntion returns the inner function - not calling.  This sets up an CLOSURE. This closure then allows 
# the callers below, caller1 and caller2, to remember the params "2,2" and "3,3" after the myFunc() calls.
caller1 = myFunc(2)
print(caller1(3))
caller2 = myFunc(4)
print(caller2(5))

