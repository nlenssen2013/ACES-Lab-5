#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 15:35:30 2017

@author: ssroka
"""

def convert_base(N,base):
    if N == 0:
        final_num = "0"
    else:
        div_res = -1
        new_num = N
        maxIt = 6
        iter = 1
        final_num = " " 
        while (div_res!=0 and iter < maxIt):
            rem = new_num % base
            div_res = new_num//base
            if new_num > 0 :
                new_num = div_res
                final_num = str(rem) + final_num
            if new_num == 0:
                break
            iter +=1
    return(final_num)

def convert_base_gt10(N,base):
    if N == 0:
        final_num = "0"
    else:
        div_res = -1
        new_num = N
        maxIt = 6
        iter = 1
        final_num = " " 
        while (div_res!=0 and iter < maxIt):
            rem = new_num % base
            div_res = new_num//base
            if new_num > 0 :
                new_num = div_res
                if rem>=10:
                    final_num = chr(65+rem-10) + final_num
                else:
                    final_num = str(rem) + final_num
            if new_num == 0:
                break
            iter +=1
    return(final_num)



# ---------------- Part A --------------------------------

print " base 10  base 8"

for i in range(0,51):
    print "  %s  %s " % (i,convert_base(i,8))


# ---------------- Part B --------------------------------

print " base 10  base 16"

for i in range(0,51):
    print "  %s  %s " % (i,convert_base_gt10(i,16))
