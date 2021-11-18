import pandas as pd
import numpy as np

#Set the MultiIndex for the data with the columns 'sex' and 'name'
titanic = pd.read_csv('C:/Users/ROY/Desktop/original_titanic.csv')
tit_index= titanic.set_index(['sex', 'name'],drop=False)
print(tit_index)

#Extract the columns ['sex', 'name', 'survived', 'pclass'] as two separate data sets and combine them using join method
titan =titanic[['name', 'sex','survived' ]]
titan1=titanic[['pclass','survived','sex']]
titan_join =titan.join(titan1,lsuffix='titan',rsuffix='titan1')
print(titan_join)

#Concat the two data sets given below with the lavel names as 'data1' and 'data2'
#* data1 = titanic[['sex', 'name', 'survived']]
#* data2 = titanic[['pclass', 'age', 'cabin']]
data1 = titanic[['sex', 'name', 'survived']]
data2 = titanic[['pclass', 'age', 'cabin']]
pd.concat([data1,data2],axis=1,join='outer',keys=['data1,data2'])
pd.concat([data1,data2],axis=1,join='inner',keys=['data1,data2'],sort=True)

#Stack the titanic data on the columns 'sex' and 'name' and observe how the data looks
titanic_reindex=titanic.set_index(['sex','name'])
print(titanic_reindex.stack().head(n=20))
