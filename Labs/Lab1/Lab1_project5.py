#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 14:24:20 2017

@author: ssroka
"""

N=input("Please enter a positive integer : ")

running_num = N;
max_num = N;
maxIt=1000
iter=1
print " iter Collatz Num."
while (running_num!=1 and iter<maxIt):
    last_num = N
    print "% 3.0f  |  % 5.0f" %( iter, running_num)
    if (running_num % 2 == 0):
        running_num = running_num/2
    else :
        running_num = running_num*3+1
    iter+=1
    # Part B is these couple lines
    if max_num<running_num:
        max_num=running_num
print "% 3.0f  |  % 5.0f" %( iter, running_num)


if iter==maxIt:
    print "Maximum number of iterations reached"
else:
    print "Stopping time is: %d iterations" % iter
    
print "Max number reached %d " % max_num










