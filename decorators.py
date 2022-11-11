#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 14:47:48 2022

@author: mikelin
"""
def decorDoCalc(func):
    def preCalc(a,b,c,d):
        if c*d==0:
            print('You will end up with a divide-by-zero error - halted')
            return
        else:
            return func(a,b,c,d)
    return preCalc

@decorDoCalc
def doCalc(a,b,c,d):
    return (a+b)/c*d

if __name__=='__main__':
    print('good calc = '+str(doCalc(1, 2, 3, 4)))
    print('bad calc = '+str(doCalc(1, 2, 3, 0)))