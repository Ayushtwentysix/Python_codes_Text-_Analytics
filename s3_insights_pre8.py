import pandas as pd
import numpy as np
import string
k=pd.read_csv('SurveyFormFinal_1.csv')
u=['computer science and engineering','cs','cse','csccv','computer science  engineering','computer science','ccv','cse da','computer science with specialization in cloud computing and virtualization','computer science engineering','da','cseda','computer science engineering ','cse','compuer science']
p=k['Branch (if any):'].str.strip()   
o=p.str.lower()
o=o.fillna(value='0') 
punct = dict((ord(c), None) for c in string.punctuation)
no_punct = [s.translate(punct) for s in o]
df=pd.Series(np.array(no_punct))
def b(x):
    if x in u:
        return "CS"
    elif x in ["electronic and communication",'ece','electronics  communication','electronics  communication engineering','electronics and communication','electronics and communication engineering','ec']:
        return "ECE"
    elif x in ['mechanical engineering','me','mechanical', 'mechanical engg']:
        return "ME"
    elif x in ['electrical engineering', 'electrical','ee','EE']:
        return "EE"
    elif x in['civil engineering', 'civil','civil enginering']:
        return 'civil'
    else:
        return x    
a=k['Do you like coding?']
punct = dict((ord(c), None) for c in string.punctuation)
no_punct2= [s.translate(punct) for s in a]
df2=pd.Series(np.array(no_punct2))
def c(x):
    if x in ['a little bit only','0','depends upon conditions','5050','I like bt I am too much week', 'On basic level', 'I m not a computer science student']:
        return 'No'
    elif x in [ 'Sometime', 'I like cad designing', 'I like Automation likes to play with ServosRobotics']:
        return 'Yes'
    else:
        return x
v=df2.apply(c)
z=df.apply(b)
y=pd.concat([z,v],axis=1)
y.columns=['branch','Do you like coding?']
y['Choice']=y['Do you like coding?']
w=pd.pivot_table(y,index=['branch'],values=['Do you like coding?'],columns=['Choice'],aggfunc='count',fill_value=0)
j=w.drop(['0','banking','biotechnology','electrical and electronics','btech','cea','fb','marketing and finance','no'])
w.stack()

j.plot(grid=True,figsize=(8,8),marker='s',fontsize=10,title='No. of Students as per Coding Choice per Branch')
plt.savefig('hide10.png',dpi=400,bbox_inches='tight')
