# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 22:48:09 2015

@author: Administrator
"""

import math
import numpy
#import functools

def percentile(N, percent, key=lambda x:x):
    """
    Find the percentile of a list of values.

    @parameter N - is a list of values. Note N MUST BE already sorted.
    @parameter percent - a float value from 0.0 to 1.0.
    @parameter key - optional key function to compute value from each element of N.

    @return - the percentile of the values
    """
    if not N:
        return None
    k = (len(N)-1) * percent
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return key(N[int(k)])
    d0 = key(N[int(f)]) * (c-k)
    d1 = key(N[int(c)]) * (k-f)
    return d0+d1
    
a=[57.704031, 57.706322, 57.700175, 57.700064, 57.710205, 0.000000, 57.690024]
a.sort()
b=a
median=percentile(b,0.75)
print(median)
print(numpy.percentile(a,75))

# median is 50th percentile.
#median = functools.partial(percentile, percent=0.5)
## end of http://code.activestate.com/recipes/511478/ }}}