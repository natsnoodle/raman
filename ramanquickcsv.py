#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 14:34:07 2020

@author: natalies
"""
''' make Raman data accisble to Igor by putting it all in one sheet'''

import pandas as pd
import os
import glob

exp= '05-31-21'




fnames=[]
Rfolder = sorted(glob.glob('/Users/natalies/Documents/CU_mbpv/Owen_mbpv/data/Raman/'+exp+'/*.txt') )

for f in Rfolder:
    name1=(os.path.basename(f))[:-4]
    fnames.append(os.path.basename(name1))
#Udf0= pd.concat((pd.read_csv(f, usecols=['A'], skiprows=1) for f in UVfolder), axis=1)

DF= pd.concat((pd.read_csv(f, delimiter='\t', header=None, usecols=[1]) for f in Rfolder), axis=1)
DF.columns = fnames
DF.to_csv(exp+'DF.csv')