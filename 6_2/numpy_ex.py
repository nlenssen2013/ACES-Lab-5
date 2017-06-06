#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 09:45:10 2017

@author: ssroka
"""
import math
import os
import numpy
x=4
z=math.sqrt(x)
home_dir=os.getenv("HOME")
A=numpy.zeros(200)


import sys
from math import sqrt

def MySqrt(x):
   """Babylonian method"""
   s0=x
   my_sqrt=x/2.
   tol=1.e-12
   while abs(my_sqrt-s0)>tol:
      s0=my_sqrt
      my_sqrt=0.5*(my_sqrt+x/my_sqrt)
   return my_sqrt

def relerr(x1,x2):
      relerr=abs((x2-x1)/x2)
      return relerr

def main():
   print "%s%s%s" % ("x".center(20),"sqrt".center(10),"rel error".rjust(14))
   N=5
   for i in range(-N,N+1):
      x=10.0**(-i)
      print "%14.3e %14.3e %15.7e" % (x, sqrt(x), relerr(MySqrt(x),sqrt(x)))
  
if __name__=="__main__":
   main()

