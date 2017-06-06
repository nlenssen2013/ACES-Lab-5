#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 18:43:33 2017

@author: ssroka
"""
import numpy as np
import random

def scrambleLine(line):
    list_of_words = line.split()
    for i in range(0,len(list_of_words)):
        list_of_words[i] = scrambleWord(list_of_words[i])
    return(" ".join(list_of_words))
    
    

def scrambleWord(word):
    wordL = [list(word)[x].isalnum() for x in range(0,len(word))]
    wordAr = np.array(wordL)
    if (not any(wordAr) or len(wordAr)<4):
        finalWord = word
    else:
        pre = min(np.where(wordAr)[0])
        suf = max(np.where(wordAr)[0])
        wordMid_old = list(word[pre+1:suf])
        wordMid = list(word[pre+1:suf])
        maxIt = 0
        while (wordMid == wordMid_old and maxIt>10):
            random.shuffle(wordMid)
            maxIt += 1
        finalWord = word[0:pre+1]+"".join(wordMid)+word[suf:]
    return finalWord


fileName = "Example.txt" #raw_input("Please enter the name of a file: ")

scrambledFileName = fileName.split('.')[0] + "_scrambled.txt"

fin = open(fileName,'r')
fout = open(scrambledFileName,'w+')
for line in fin:
    fout.write(scrambleLine(line))
    
print "done scrambling"

fout.close
fin.close


    
    
    
    
    
    
    
    