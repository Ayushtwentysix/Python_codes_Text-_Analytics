import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import string
k=pd.read_csv('SurveyFormFinal_1.csv')
u=['computer science and engineering','cs','cse','csccv','computer science  engineering','computer science','ccv','cse da','computer science with specialization in cloud computing and virtualization','computer science engineering','da','cseda','computer science engineering ','cse','compuer science']
p=k['Branch (if any):'].str.strip()   
o=p.str.lower()
o=o.fillna(value='0')
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
l=k["How frequently you visit to library?"]
j=k["Do you find the genre of books in library and their quality sufficient?"]
punct = dict((ord(c), None) for c in string.punctuation)
no_punct2 = [s.translate(punct) for s in l]
df2=pd.Series(np.array(no_punct2))
def f(x):
    if x in ['23 times a week']:
        return 'Ocassionally'
    elif x in['Never', 'no','Room study prefred','0','only when i need books cause i prefer to study at my room','never']:
        return 'Never'
    else:
        return x
r=df2.apply(f)
g=pd.concat([t,r,j],axis=1)
g.columns=['Branch','Frequency','Genre Rating']
c=pd.pivot_table(g,index=['Branch','Frequency'],values=['Genre Rating'],aggfunc=[np.mean])
dc=c.drop(['0','banking','biotechnology','btech','cea','fb','marketing and finance','no'])
"""dc.plot.barh(grid=True,figsize=(13,13),title='Frequency of Students going to Library and Genre Ratngs [MEAN]',fontsize=12,color='mediumvioletred')"""
"""plt.savefig('hide17.png',dpi=400,bbox_inches='tight')
"""