#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 12:58:57 2017

@author: ssroka
"""
import sys


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
                if rem>=10:
                    final_num = chr(65+rem-10) + final_num
                else:
                    final_num = str(rem) + final_num
            if new_num == 0:
                break
            iter +=1
    return(final_num)


base=int(sys.argv[2])
N=int(sys.argv[1])

print " base 10  base %i" % base

for i in range(0,N):
    print "     %s    |    %s " % (i,convert_base(i,base))
