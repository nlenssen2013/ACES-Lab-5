#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 11:25:26 2017

@author: ssroka
"""
import numpy as np
from creatures import *
raja=Animal("Raja","tiger",['meat'],np.array([12]))
george=Animal("george","spider monkey",['meat','fruit','veggies'],np.array([1,2,3]))

zooDict = {raja.get_name():raja}
zooDict[george.get_name()] = george

