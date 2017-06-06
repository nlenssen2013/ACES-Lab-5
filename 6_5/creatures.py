#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 11:06:19 2017

@author: ssroka
"""


class Animal:
    def __init__(self,name,species,food,food_qty):
        self.name=name
        self.species=species
        self.food=food
        self.food_qty=food_qty
    def get_name(self):
        return(self.name)    
    def get_food(self):
        return(self.food)
    def feeding(self):
        food_str = str(self.food_qty[0]) + " kg of " + self.food[0] 
        if len(self.food)>1:
            for x in range(1,len(self.food)):
              food_str = food_str + " and " + str(self.food_qty[x]) + " kg of " + self.food[x] 
        print food_str


