#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 14:03:19 2017

@author: ssroka
"""
# Part A ---------------------------------------------------------------------
N=input("Please enter an integer : ")
my_list = range(1,N+1)
print "With brute force:"
sum_num = 0
for i in range(0,N):
    sum_num = sum_num + my_list[i]
    
print sum_num

print "With python built in:"
print sum(my_list)
print "With Gauss:"

# check with Gauss
print N*(N+1)/2
#for i in range(1,N+1):
    

# Part B ---------------------------------------------------------------------
print "Integer   Sum"
sum_num = 0

if N>=25:
    max_num = 25
else:
    max_num = N
print max_num
for i in range(0,N):
    sum_num = sum_num + my_list[i]
    if i<max_num:
        print "% 3.0f     % 5.0f" %( i+1, sum_num)
    
    
print sum_num
\
#for i in range(1,N+1):
