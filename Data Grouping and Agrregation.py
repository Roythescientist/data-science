import pandas as pd
import numpy as np

#Group the titanic data based on 'sex' column and find the mean age of the male and female passengers
titanic=pd.read_csv('C:/Users/ROY/Desktop/original_titanic.csv')
grouped=titanic['age'].groupby(by=titanic['sex'])
mean1=grouped.mean()
print(mean1)

#Use the indexing method to find the mean age istead of using the groupby method
print(titanic['age'][titanic['sex']=='male'].mean())
print(titanic['age'][titanic['sex']=='female'].mean())

#Group the data based on 'sex' column, and find the number of male and female passengers survived
group1=titanic['survived'].groupby(by=titanic['sex'])
print('the total number is:', group1.sum())

#Count the number of passengers survived and not-survived based on the gender, and cross check the result
group2=titanic['survived'].groupby(by=titanic['sex']).size()
print(group2)
print('total number of passengers is:',339+127+682+161)

#Group the data based on the column 'sex' and iterate over the key and data
titanic.groupby(by=titanic['sex'])
for key,data in grouped:
    print(key)
    print(data)

#Group the titanic data along the column, and iterate over the key and data
titanic.dtypes
grouped_column=titanic.groupby(by=titanic.dtypes,axis=1)
for datatypes,data in grouped_column:
    print(datatypes)
    print(data)

#Group the titanic data based on ['pclass', 'survived', 'sex'] and count the number of passengers survived on each type of 'pclass'
titanic_2 = titanic[['pclass', 'survived', 'sex']]
grouped_titanic_2 = titanic_2[['survived', 'sex']].groupby(by=titanic_2['pclass'])
print(grouped_titanic_2.sum())
print('the total number of survivors is:',200+119+181)

# Use the 'survived' data as the list of values to find the total number of passengers survived using groupby method
list_survived=titanic['survived'].tolist()
titanic_indexed=titanic.set_index(['name'])
print(titanic_indexed['survived'].groupby(list_survived).sum())

#Group the titanic data based on ['sex', 'name'] and find the total number of people survived
titanic_3=titanic.set_index(['sex', 'name'])
print(titanic_3.groupby(level='sex',axis=0)[['survived']].sum())

#Find the most used type of 'embarked' by the passengers
print(titanic['embarked'].value_counts)

#Find the maximum age and the maximum pclass type
print('the maximum age is:',titanic['age'].max(),' and the maximum pclass is :',titanic['pclass'].max())

#Find the top 'cabins' in the titanic ship using describe method on the column 'cabin'
print(titanic['cabin'].describe())