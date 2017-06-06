# -*- coding: utf-8 -*-
"""
Created on Tue Jun 06 13:32:48 2017

@author: Alex
"""

import random

class Question: 
    
    def __init__(self, question_text, correct_answer, answer_list):
        self.question_text = question_text
        self.correct_answer = correct_answer
        self.answer_list = answer_list
    
    def answer_shuffle(self, answer_list):
        return random.shuffle(self.answer_list)