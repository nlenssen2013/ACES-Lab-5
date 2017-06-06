#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 13:45:43 2017

@author: ssroka
"""
fid = open("HIV.txt","r")
line= fid.readline()
line_DNA=[]
while  line:
    line_DNA.append(line.split()[1])
    line= fid.readline()

fid.close()

#sampleInput = "ATCGG"
#sampleInput_seq = list(sampleInput)

def countBases(baseLetters):
    "takes in Letter A T C G and returns"
    "a dictionary where the key is the letter"
    baseDict = {x:baseLetters.count(x) for x in baseLetters}
    return baseDict


def printBaseComposition(inputDict):
    "takes in dictionary and computes fraction"
    print "Base   Percent"
    baseVec = [0.]*len(inputDict.keys())
    count = 0
    for key in inputDict:
     baseVec[count]=float(inputDict[key])
     count +=1
    sumTot=sum(baseVec)
    percentVec = [x / sumTot for x in baseVec]
    count = 0
    for key in inputDict:
     print "%s       %1.5f" % (key,percentVec[count])
     count +=1
    return percentVec

for i in range(0,len(line_DNA)):
    print "Sample %i----------------" % (i+1)
    countBases(line_DNA[i])
    printBaseComposition(countBases(list(line_DNA[i])))





