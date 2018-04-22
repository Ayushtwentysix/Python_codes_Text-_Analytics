import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import string
k=pd.read_csv('SurveyFormFinal_1.csv')
f=k["How much time you dedicate for your games?"].str.strip()
f=f.str.lower()
f=f.dropna()
h=k["How much time you dedicate for your studies?"].str.strip()
h=h.str.lower()
h=h.dropna()
punct = dict((ord(c), None) for c in string.punctuation)
no_punct1 = [s.translate(punct) for s in f]
df1=pd.Series(np.array(no_punct1))
punct = dict((ord(c), None) for c in string.punctuation)
no_punct2 = [s.translate(punct) for s in h]
df2=pd.Series(np.array(no_punct2))
def c(x):
    if x in ["nowadays not able to give because of university timings", 'none', 'i dont find any companion for the game i like','0', 'dont even a single minute', '0 hr', 'no', 'no time',
 'zero because of lack of time', 'no time', 'we dont get time for that because of tight schedule', 'zero hour','0hr','i am interested in games but internet attract me and unavailability of other student is  also the reason behind not spending time in outdoor games','can not give','cannot dedicate time these days','because of being a dayscholars couldnt take participation in games', 'no time for games', 'not given much time because of hectic academic schedule', 'no time dedicate🙁',
 'not a single minute', 'once or twice in a month ', 'couldnt give time',
 'not even a single hour','no time because lots of pressure given by faculty', 'i am not intrested in games', 'negligible','not enough time to dedicate for games', 'as no time left after classes',
 'i dont play outdoor games','i usually dont play','only when am free','i usually dont play only when am free sometimes','dedicated 8 hrs of college to the study','only during the classes 6 hr','0','i devote 0 minute to college study but devote 23 hour on research work  some time on my office work', '20 minsday', 'it depends', 'i never count the hours', 'depends','nowadays i spent no time in sports','0 hours']:
        return "0 hr"
    elif x in[ '1 hr', '1 hr', 'sometimes one','approx 1 hr on holidays','sometimes','half hour','30 minutes','half an hour probably', '30 min','sometimes only', 'less than 1 hr', 'only on weekends','approx 1 hr but only on holidays','half an hour']:
        return "<= 1 Hr"
    elif x in ['3 hr', '2 hr','2 hr','2 hours on sundays','3 hr','i give my time occasionally', 'about 12 an hour']:
        return "2-3 Hrs"
    elif x in [ 'more than 3 hr', '8','23 hr occasionaly', '05 hr','8hours in college']:
        return ">3 Hrs"
    else:
        return x
g1=df1.apply(c)
g2=df2.apply(c)
g1_df=pd.DataFrame(g1)
g2_df=pd.DataFrame(g2)

"""g1_df["play"]=g1_df[0]
g2_df["study"]=g2_df[0]"""
l=pd.concat([g1_df,g2_df],axis=1)
l.columns=['play','study']

l['number of students']=l['play']
b=pd.pivot_table(l,values=["number of students"],index=["play","study"],aggfunc='count')


v=b.query('play==["0 hr"]')
"""v.plot(figsize=(8,8),color='steelblue',grid=True,rot='30')
"""
b.plot.barh(grid=True,color='steelblue',figsize=(8,8),fontsize='10',title='Number of Students categorised under Play & Study')
plt.savefig('hide8.png',dpi=400,bbox_inches='tight')