# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 14:52:44 2017

@author: Mohammed A
"""

from __future__ import print_function, division

import numpy as np

import nsfg
import first
import thinkstats2
import thinkplot

def CohenEffectSize(group1, group2):
    """Computes Cohen's effect size for two groups.
    
    group1: Series or DataFrame
    group2: Series or DataFrame
    
    returns: float if the arguments are Series;
             Series if the arguments are DataFrames
    """
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / np.sqrt(pooled_var)
    return d

pres = nsfg.ReadFemResp()
hist1 = thinkstats2.Hist(pres.fmar1age)

for val in sorted(hist1.Values()):
    print(val, hist1[val])

thinkplot.Hist(hist1)
thinkplot.Show(xlabel="Age at first marriage",ylabel = "Frequency")

hist2 = thinkstats2.Hist(pres.fmarno)
print (hist2)
for val in sorted(hist2.Values()):
    print(val, hist2[val])
    

thinkplot.Hist(hist2)
thinkplot.Show(xlabel="Fmarno Code",ylabel = "Frequency")

hist3 = thinkstats2.Hist(pres.totincr)
print (hist3)
for val in sorted(hist3.Values()):
    print(val, hist3[val])
    
thinkplot.Hist(hist3)

nevermarried = pres[pres.fmarno == 0]
married = pres[pres.fmarno != 0]

thinkplot.preplot(2, cols = 2)
width = 0.45
thinkplot.Hist(thinkstats2.Hist(married.totincr), align='right', width=width)
thinkplot.Hist(thinkstats2.Hist(nevermarried.totincr), align='left', width=width)

largest1 = max(married.totincr)
smallest1 = min(married.totincr)
mean1 = married.totincr.mean()
var1 = married.totincr.var()
std1 = married.totincr.std()

largest2 = max(nevermarried.totincr)
smallest2 = min(nevermarried.totincr)
mean2 = nevermarried.totincr.mean()
var2 = nevermarried.totincr.var()
std2 = nevermarried.totincr.std()

print ("The largest income of the married is %d and the smalles is %d , the mean is %d and the variance is %d and the standard deviation is %d . For the never married the largest income is is %d and the smallest is %d , the mean is %d and the variance is %d and the standard deviation is %d " % (largest1,smallest1,mean1,var1,std1,largest2,smallest2,mean2,var2,std2))

