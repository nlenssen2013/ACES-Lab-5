#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 13:45:43 2017

@author: ssroka
"""
minC = input("Please enter an integer starting deg C temperature: ")
maxC = input("Please enter an integer ending deg C temperature: ")
dT = input("Please enter an integer deg C temperature increment: ")

tempsC = range(minC,maxC+dT,dT)
tempsF = [0.]*len(tempsC)
         
for i in range(0,len(tempsC)):
    tempsF[i]=tempsC[i]*9./5+32
    print tempsC[i],tempsF[i]

