import pandas as pd
import numpy as np

# Read the data using pandas read_csv method and count the number of rows and columns
titanic = pd.read_csv('C:/Users/ROY/Desktop/busi.csv')
print(pd.DataFrame(titanic), type(titanic))

#Display the column names using column attribute and convert the array of columns to list
print(titanic.columns.values.tolist())

#Read the first and last 10 rows using default file displaying methods
print("the first 10 rows are:", titanic.head(n=10))
print("the first 10 rows are:", titanic.tail(n=10))

#Get the information about the data and count the total number of missing values in each column
print(titanic.info, titanic.isnull().sum())

#getting percentage
print(titanic.describe())

#displaying data with respect to industry
print(titanic[titanic['industry']=='Agriculture'])

print([titanic['level']>=2])
print([titanic['level']<2])

print(titanic['level'].value_counts())

