 # %%
import numpy as np
import pandas as pd
# %%# Display the data with 'name' column as the index
titanic= pd.read_csv("C:/Users/ROY/Desktop/original_titanic.csv",index_col=['name'])

#Count the number of null and non-null values in the column 'body' using 'isnull' and 'notnull' methods
null_values=titanic['body'].isnull()
print(null_values.sum())
non_null_values=titanic['body'].notnull()
print(non_null_values.sum())

#Drop the rows and columns which are having all the null values
print(titanic.dropna(axis=0, how='all'))
print(titanic.dropna(axis=1, how='all'))

#Replace all the null values of titanic data with '0'
print(titanic.fillna(value=0))

#Count the number of rows which are duplicated and display them.
duplicated_value=titanic.duplicated()
print(duplicated_value.value_counts())

#Drop the duplicated rows from the titanic data
print(duplicated_value.drop_duplicates())

#Count the number of 'tickets' with repeated number and display them
dup_tickets=titanic['ticket'].duplicated()
print(dup_tickets.value_counts())

#Convert the 'sex' column names 'male' and 'female' to a title case
titanic['sex'].str.title()
print(titanic.head(n=5))

#Replace the 'male' and 'female' names with the title case 'Male' and 'Female'
print(titanic.replace(to_replace=['male','female'], value=['Male','Female']))

#Rename the columns of titanic data to a title case
print(titanic.rename(columns=str.title))

#Find the number of passangers with different age groups, and rename the age groups with different names
bin_size=[0,18,30,45,60,80,90]
age_group=pd.cut(titanic['age'],bin_size, labels=['child','youth','young adults','adults','aged','very old'])
print(age_group.value_counts())

#Count the number of passengers with age greater than 50
age_50_and_above=titanic['age']>50
print(age_50_and_above.sum())

#Use the dummy variable for the 'survived' data of titanic with the prefix 'Survived'
print(pd.get_dummies(titanic['survived'],prefix='survived'))