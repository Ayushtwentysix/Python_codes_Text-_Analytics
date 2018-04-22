# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 23:21:39 2018

@author: Alka Gupta
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
k=pd.read_csv('SurveyFormFinal_1.csv')

j=pd.pivot_table(k,index=['Would you prefer to go in classroom with laptops?'],values=['Overall, how happy are you with your academic experience and university life?'],aggfunc=[np.mean])


fig=plt.figure()
ax=fig.add_subplot(1,1,1)


ax.set_xlabel('Would you prefer to go in classroom with laptops?', fontdict=dict(weight='bold'),color='crimson')
ax.set_ylabel(' Satisfaction Of Students [MEAN]', fontdict=dict(weight='bold'),color='crimson')
ax.set_xticklabels(['NO','YES'],rotation=30,fontsize='large')
plt.rc('figure',figsize=(8,8))
plt.rc('grid', linestyle="--", color='black')
ax.plot(j,color='dodgerblue')
ax.grid(color='darkseagreen', linestyle='-',marker='o')
"""plt.savefig('hide7.png',dpi=400,bbox_inches='tight')"""