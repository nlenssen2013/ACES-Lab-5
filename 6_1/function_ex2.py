#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 09:58:56 2017

@author: ssroka
"""

def side_effect(L,x):
    L.append(x)
    return None

L=[1,2,3,4]
side_effect(L,11)
print L
print side_effect(L,99)
