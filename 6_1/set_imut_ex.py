#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 10:14:50 2017

@author: ssroka
"""

def set_x(x):
    print x
    x=100
    while x>0:
        x=x+1
        if x>10000:break
        if x<100:continue
        x=x+20
    return x

x=1 # integers are immutable
z=set_x(x)
print x; print z
