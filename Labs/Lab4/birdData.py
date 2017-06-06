
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 15:40:36 2017

@author: ssroka
"""
import numpy as np

class Bird (object):
    def __init__(self,species,observations):
        self.species=species
        self.observations=np.array(observations)
    def stats(self,years):
        print self.observations
        maxNumInd = np.argmax(self.observations)
        maxNum    = self.observations[maxNumInd]
        maxNumYr  = years[maxNumInd]

        minNumInd = np.argmin(self.observations)
        minNum    = self.observations[minNumInd]
        minNumYr  = years[minNumInd]        
        
        meanNum   = np.mean(self.observations)
        medianNum = np.median(self.observations)
        
        print "Maximum of %i in year %4.0f" %  (maxNum,maxNumYr)
        print "Minimum of %i in year %4.0f" %  (minNum,minNumYr)
        print "Mean of %f" % meanNum
        print "Median of %f" % medianNum
        
        ansDict = {"maxNum":maxNum}
        ansDict["maxNumYr"] = maxNumYr
        ansDict["minNum"]   = minNum
        ansDict["minNumYr"] = minNumYr
        ansDict["meanNum"]     = meanNum
        ansDict["medianNum"]   = medianNum
        return ansDict



