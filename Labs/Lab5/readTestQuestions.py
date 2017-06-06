#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 13:37:43 2017

@author: ssroka
"""

#class UnfamiliarFile(Exception):
#    pass
#raise UnfamiliarFile('Unfamiliar file structure detected,\
# please check testQuestions.txt')

from question import *


def getQuestions(fileName)
    
    fid = open(fileName)
    lines=fid.readlines()
    fid.close()
    
    # There should be 6 lines (1 question, 5 answers) per question,
    # and one blank line inbetween each question, therefore there should be
    # 6n + (n-1) lines or 7n-1 lines in a file with n questions
     
    #if ((len(lines)+1) % 7 != 0):
    #    raise UnfamiliarFile
    questionList = []
    
    for i in [0]:#range(0,len(lines),7):
        question_str = ",".join(lines[i].strip().split(",")[1:])
        answer_corr  = ",".join(lines[i+1].strip().split(",")[1:])
    
        answer_choice = [None]*5
        answer_choice[0] = ",".join(lines[i+1].strip().split(",")[1:])
        answer_choice[1] = ",".join(lines[i+2].strip().split(",")[1:])
        answer_choice[2] = ",".join(lines[i+3].strip().split(",")[1:])
        answer_choice[3] = ",".join(lines[i+4].strip().split(",")[1:])
        answer_choice[4] = ",".join(lines[i+5].strip().split(",")[1:])
        questionList.extend(Question(question_str,answer_corr,answer_choice))

    
return questionList











