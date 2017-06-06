#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 13:45:43 2017

@author: ssroka
"""
minC = input("Please enter an integer starting deg C temperature: ")
maxC = input("Please enter an integer ending deg C temperature: ")
dT = input("Please enter an integer deg C temperature increment: ")

def C_2_F(degC):
    "takes in deg C changes to deg F"
    return degC*9./5+32


tempsC = range(minC,maxC+dT,dT)
tempsF = [0.]*len(tempsC)
         
for i in range(0,len(tempsC)):
    tempsF[i]=C_2_F(tempsC[i])
    print tempsC[i],tempsF[i]






