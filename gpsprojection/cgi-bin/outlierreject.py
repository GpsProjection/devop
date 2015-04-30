# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 22:28:32 2015

@author: Administrator
"""

import numpy as np

def RemoveOutliers(data):
    lowerquartile=np.percentile(data,25)
    upperquartile=np.percentile(data,75)
    interquartile=upperquartile-lowerquartile
    outerfence1=3*interquartile+upperquartile
    outerfence2=lowerquartile-3*interquartile
    for i in data:
        if i<outerfence2 or i>outerfence1:
            data.remove(i)
    return data

lats=[57.704031, 57.706322, 57.700175, 57.700064, 57.710205, 0.000000, 57.690024]

#longs=[11.910801, 11.911692, 11.976824, 11.976629, 11.921849, 0.000000, 11.998419]

RemoveOutliers(lats)