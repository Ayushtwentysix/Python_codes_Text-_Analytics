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
l=k["Give ratings to your technical classes."]
j=k["Give ratings to your aptitude classes."]
g=pd.concat([t,l,j],axis=1)
g.columns=['Branch','technical classes','aptitude classes']
g['Number of Students']=g['technical classes']
g['ac']=g['aptitude classes']
t=pd.pivot_table(g,index=['Branch','technical classes','aptitude classes'],values=['Number of Students'],aggfunc='count')
dc=t.drop(['0','banking','biotechnology','btech','cea','fb','marketing and finance','no'])
dc.plot.barh(grid=True,figsize=(13,13),title='Ratings of Technical & Aptitude Classes',fontsize=12,color='mediumseagreen')
"""plt.savefig('hide16.png',dpi=400,bbox_inches='tight')
"""