# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 20:57:40 2018

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
no_punct = [s.translate(punct) for s in o]
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

h=k['Are you certified in any of the given language?']
h=h.fillna(value='0')
punct = dict((ord(c), None) for c in string.punctuation)
no_punct2 = [s.translate(punct) for s in h]
df2=pd.Series(np.array(no_punct2))

def c(x):
    if x in ['No','None of them','not certifyed','None','not yet but i will','No certificate','Im accountant not a programmer ','Not having any certified language', 'no','0','No interest','NO','No  I am not ','nil','not certified but have knowledge of each', '0',
 'Not yet','nota','not certified','No','No','No','No','Nopes','No certification ','No ','NO OTHER LANGUAGE','No','not interested','Not certified','Know them all including c but no certification','none','none of the above','not yet certified','not having any certification in any programming language','NOT CERTIFIED BUT I KNOW ABOUT C BASICS DUE TO CLASS 12','no language','not certified but i know c and c very well ','Knows C but not certified','No certificate','I am not certified in any language','I m not interested','Not certified But have learned it as the part of curriculum','not certified but know little bit of c language','none till now',]:
        return 'Never'
    elif x in ['also in R from data camp python from Lynda']:
        return 'R'
    elif x in ['HTMLCSSJAVASCRIPTPHP']:
        return 'Web Development'
    elif x in['Android Web Development','Also have a android certificate','Android']:
        return 'Android'
    elif x in ['AutoCAD','cad cam','Autocad, staadpro','AutoCAD','Autocad staadpro']:
        return 'AutoCAD'
    else:
        return x

y1=df.apply(b)
y2=df2.apply(c)
g=pd.concat([y1,y2],axis=1)
g.columns=['Branch','Number of Students']
g['Language']=g['Number of Students']
s=pd.pivot_table(g,index=['Branch'],values=['Number of Students'],columns=['Language'],aggfunc='count',fill_value=0)
t=s.drop(['0','banking','biotechnology','btech','cea','fb','marketing and finance','no'])
d=t.query('Branch ==["CS"]')
d.plot.barh(figsize=(12,12),grid=True,fontsize=15,title='Students Certified in various Languages for CS Branch')
"""plt.savefig('hide12.png',dpi=800,bbox_inches='tight')

t.plot.barh(figsize=(12,12),grid=True,fontsize=15,title='Students Certified in various Languages')
plt.savefig('hide13.png',dpi=400,bbox_inches='tight')
"""
""""
n=t.query('Branch ==["CS","ME"]')
n.plot.barh(figsize=(12,12),grid=True,fontsize=15,title='Students Certified in various Languages for CS & ME Branch')
plt.savefig('hide14.png',dpi=400,bbox_inches='tight')
"""