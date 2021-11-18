from numpy.core.defchararray import index
import pandas as pd
import numpy as np
exam_data  = {'name': ['Anjum', 'Anali', 'Souria', 'Rockea', 'Imani', 'Mouliya', 'Julie', 'Rana', 'Kavin', 'Bosia'], 
              'score': [15.5, 9, 16.5, np.nan, 9, 30, 17.5, np.nan, 8, 20], 
              'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 
              'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']} 
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
data=pd.DataFrame(exam_data, index=labels)
print(data)

#Sort the DataFrame by 'name' in descending order and then by 'attempts' in ascending order.
print(data.sort_values(by=['name'],ascending=[False]))
print(data.sort_values(by=['attempts'], ascending=[True]))


# Drop the 'attempts' column from the DataFrame.
print(data.drop(columns=['attempts']))


 #Reindex the columns as 'name', 'attempts', 'score' and 'qualify'
new_index=['name', 'attempts', 'score','qualify']
print(data.reindex(columns=new_index))

#Reindex the row labels as 'A', 'C', 'B', 'E', 'D', ... 'J'
net = ['A', 'C', 'B', 'E', 'D','G','F','I','H','J']
print(data.reindex(net))

#Find the maximum 'score' and the maximum 'attempts' made by the students using the "apply" function
data.loc[:,['name','attempts']]
f= lambda x: x.max()
print(data.loc[:,['name','attempts']].apply(f))


#Find the maximum, minimum, and mean of the 'score' and 'attempts' made by the students using user defined function
def f(x):
   return pd.Series([x.max(),x.min(),x.mean()],index=['MAX:','MIN:','MEAN'])
print(data.loc[:, ['score', 'attempts']].apply(f))

#Sort the index labels in reverse direction
print(data.sort_index(ascending=False, axis=0, level=0))


#Sort the DataFrame based on the values of 'score' and 'attempts' 
print(data.sort_values(by=['score'],axis='index',ascending=True))
print(data.sort_values(by=['attempts'],axis='index',ascending=True))

#Rank the 'score' and 'attempts' columns without converting them to an integer values
print(data.loc[:,['score','attempts']].rank(method='first',numeric_only=True))
print(data.rank(method='first',numeric_only=True))

# Find the labels for which the maximum values of 'score' and the 'attempts' of the students occurs
print(data.loc[:, ['score', 'attempts']].idxmax())

#Count the total number of 'score' and the 'attempts' made by the students
print(data.loc[:, ['score', 'attempts']].apply(pd.value_counts))