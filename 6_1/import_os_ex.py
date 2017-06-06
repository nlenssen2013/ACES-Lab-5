#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 11:25:34 2017

@author: ssroka
"""

import os
print os.getcwd()
#following should work on Windows and Mac
newfile=os.path.join ("/Users/ssroka/Desktop","Output")

fid=open(newfile,"w+")
fid.write("I can print output")
fid.close()

