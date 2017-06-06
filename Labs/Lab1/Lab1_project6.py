#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 14:43:46 2017

@author: ssroka
"""
y = 1562
m = 5
d = 5

# -------------------------------- Begin --------------------------------

#date_input = raw_input(" Please enter a date as MM/DD/YYY: ")
#date_input_list = date_input.split('/')
#
#m = int(date_input_list[0])
#d = int(date_input_list[1])
#y = int(date_input_list[2])

str_Y = str(y)
first_two = str_Y[0:2]
last_two = str_Y[2:4]


# -------- Calc C --------
if (int(first_two) % 4 == 0):
   C=5
elif (int(first_two) % 4 == 1):
   C=4
elif (int(first_two) % 4 == 2):
   C=2
elif (int(first_two) % 4 == 3):
   C=0

# -------- Calc Y --------
Y = int(last_two)

# -------- Calc M --------
Months = [0,3,3,6,1,4,6,2,5,0,3,5]
M = Months[m-1]

# -------- Calc D --------
D = d

# -------- Calc L --------


L = int(last_two)//4
mod_4 = int(last_two) % 4
           
           
if ((int(first_two + "00") % 400) == 0): # if it is a century year and a leap year
        L = L+1
elif mod_4 == 0: # if it is not a century year and a leap year
    if 1<= m <=2 :
        L = L-1
            

# -------- Calc W --------

print C,Y,L,M,D

W=(C+Y+L+M+D ) % 7
  
print "Gregorian date: %f" % W




