# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 00:15:09 2018

@author: Alka Gupta
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import string
k=pd.read_csv('SurveyFormFinal_1.csv')

u=['computer science and engineering','cs','cse','csccv','computer science  engineering','computer science','ccv','cse da','computer science with specialization in cloud computing and virtualization','computer science engineering','da','cseda','computer science engineering ','cse','compuer science']
p=k['Branch (if any):'].str.strip()   
o=p.str.lower()
o=o.fillna(value='0')


import string 
punct = dict((ord(c), None) for c in string.punctuation)
no_punct3 = [s.translate(punct) for s in o]
df3=pd.Series(np.array(no_punct3))
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
    
    
t=df3.apply(b)    
l=k["Are you satisfied with your course curriculum ?"]
l=l.fillna(value='0')
j=k["Are you satisfied with lab work/ lab assignment?"]
j=j.fillna(value='0')

punct = dict((ord(c), None) for c in string.punctuation)
no_punct = [s.translate(punct) for s in l]
df=pd.Series(np.array(no_punct))

punct = dict((ord(c), None) for c in string.punctuation)
no_punct1 = [s.translate(punct) for s in j]
df1=pd.Series(np.array(no_punct1))

def d(x):
    if x in ['I think the course is very basic as per GATE perspective','Partially',' The Computer Science syllabus needs to get advanced like java must be there in 1semester instead of c','Good author books are available in small number','May be','Very easy  You are good in studies at a time but as time passes you become dumbvery early','should be improved','i dont know','Some changes need to be their like their must be ','A few theoretical subjects are not interesting']:
        return 'Partially'
    else:
        return x

def e(x):
    if x in ['Hh','0','At some extent','Not fully','Some what yes and somewhat no','small disinterest in lab','more practical approach',' small disinterest in lab']:
        return 'Partially'
    elif x in['Facing problem in Android labsTheir should be a separate lab for android','The practicals we are performing in 4th seen should have been done in 1sr year only','am not we waste our time in writing files instead of performing practicalsprinted files should be given in labs for better upgradation', 'No lab work is given to us','Labs in civil engineering are just a formality','The instruments in the lab is very old plzz change the instruments']:
        return 'No'
    else:
        return x

n=df.apply(d)
m=df1.apply(e)
b=pd.concat([t,n,m,],axis=1)
b.columns=(['Branch','course curriculum','lab work/ lab assignment'])
b['Number of Students']=b['course curriculum']
h=pd.pivot_table(b,index=['Branch','course curriculum','lab work/ lab assignment'],values=['Number of Students'],aggfunc='count')
y=h.drop(['0','banking','biotechnology','btech','cea','fb','marketing and finance','no'])
y.plot.barh(grid=True,figsize=(13,13),title='Number of students satisfied with their Course and Lab',fontsize=12,color='c')
"""plt.savefig('hide15.png',dpi=400,bbox_inches='tight')"""