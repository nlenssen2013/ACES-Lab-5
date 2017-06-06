#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 10:40:57 2017

@author: ssroka
"""

class PrivateStuff (object):
    def _init__(self,x):
        self.__u=11.
        self.x=x
    def set_u(self,u):
        self.__u=u
    def get_u(self):
        return self.__u
#secret=PrivateStuff(9.)
#secret.get_u()


