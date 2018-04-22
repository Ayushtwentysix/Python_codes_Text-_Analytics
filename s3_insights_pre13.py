import matplotlib.pyplot as plt
import pandas as pd
k=pd.read_csv('SurveyFormFinal_1.csv')
e=k[['Give ratings to your technical classes.','Give ratings to your aptitude classes.','Overall, how happy are you with your academic experience and university life?']]
e.columns=['technical classes','aptitude classes','Satisfaction of Students']
s=e.corr()

plt.rcParams['figure.figsize'] = [16, 6]

fig, ax = plt.subplots(nrows=1, ncols=2)

ax=ax.flatten()

cols = ['technical classes','aptitude classes']
colors=['#415952', '#f35134', '#243AB5', '#243AB5']
j=0

for i in ax:
    if j==0:
        i.set_ylabel('Satisfaction of Students')
    i.scatter(s[cols[j]], s['Satisfaction of Students'],  alpha=0.5, color=colors[j])
    i.set_xlabel(cols[j])
    i.set_title('Pearson: %s'%s.corr().loc[cols[j]]['Satisfaction of Students'].round(2))
    j+=1
    
plt.savefig('hide18.png',dpi=400,bbox_inches='tight')    