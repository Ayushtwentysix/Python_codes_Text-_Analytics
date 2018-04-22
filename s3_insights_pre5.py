# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 07:47:51 2018

@author: Alka Gupta
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
k=pd.read_csv('SurveyFormFinal_1.csv')
    
u=['computer science and engineering','cs','cse','csccv','computer science  engineering','computer science','ccv','cse da','computer science with specialization in cloud computing and virtualization','computer science engineering','da','cseda','computer science engineering ','cse','compuer science']
p=k['Branch (if any):'].str.strip()   
o=p.str.lower()
h=o.fillna(value='0')

import string 
punct = dict((ord(c), None) for c in string.punctuation)
no_punct = [s.translate(punct) for s in h]
df=pd.Series(np.array(no_punct))
def b(x):
    if x in u:
        return "CS"
    elif x in ["electronic and communication",'ece','electrical and electronics','electronics  communication','electronics  communication engineering','electronics and communication','electronics and communication engineering','ec']:
        return "ECE"
    elif x in ['mechanical engineering','me','mechanical', 'mechanical engg']:
        return "ME"
    elif x in ['electrical engineering', 'electrical','ee','EE']:
        return "EE"
    elif x in['civil engineering', 'civil','civil enginering']:
        return 'civil'
    else:
        return x
g=df.apply(b)
g_df=pd.DataFrame(g)
g_df["branch"]=g_df[0]
k['Mean Satisfaction']=k['Overall, how happy are you with your academic experience and university life?']
k_new=pd.concat([k,g_df["branch"]],axis=1)
r=pd.pivot_table(k_new,index=['branch'],values=['Mean Satisfaction'],aggfunc=[np.mean])
r=r.drop(['0','no','fb','btech','biotechnology','banking','marketing and finance'])
r.plot(title='Mean Satisfaction of Students per Branch',marker='o',figsize=(8,8),fontsize=15,grid=True,color='purple')
"""plt.savefig('hide11.png',dpi=400,bbox_inches='tight')"""