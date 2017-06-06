#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 09:32:52 2017

@author: ssroka
"""


s=set()
s.update("California")
print s
s1={"Alabama","Arkansas","California","California"}
print s1
s2=set()
s2.add("California")
s2.add("Colorado")
s2.add("Oregon")

print s1-s2
print s1^s2
print s1&s2
print s1|s2

