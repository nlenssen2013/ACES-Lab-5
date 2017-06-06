#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 09:03:19 2017

@author: ssroka
"""

# tuples are distinct from numbers

T=tuple((1,2,3))
len(T)



# dictionaries are unordered, values are asociated wiht keys
#tuple cannot contain mutable elements
# strings or integers are common strings
# keys have to be unique, teh value can be a list, but only one thing


capitals={"Alabama":"Montgomery"}
capitals["Alaska"]="Juneau"
capitals["Arizona"]="Phoenix"
capitals["Arkansas"]="Little Rock"
print capitals.keys()
print "Virginia" in capitals
print "Arkansas" in capitals
newstate="Connecticut"
newcapital="Hartford"
if newstate not in capitals:
    capitals[newstate]=newcapital
for key in capitals:
    print "The capital of ", key,\
    "is ", capitals[key]
    



