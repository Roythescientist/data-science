import pandas as pd
import numpy as np
from pandas._libs import indexing
from pandas.core.indexes.base import Index
exam_data  =({'name': ['Anjum', 'Anali', 'Souria', 'Rockea', 'Imani', 'Mouliya', 'Julie', 'Rana', 'Kavin', 'Bosia'], 
              'score': [15.5, 9, 16.5, np.nan, 9, 30, 17.5, np.nan, 8, 20], 
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 
              'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']})
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
exam_data1= pd.DataFrame(exam_data, index=labels)
#print(exam_data1)

print(exam_data1.iloc[:4]) 
re=exam_data1.iloc[[1,3,5,7],[1,2]]
print("the number of rows are: ", exam_data1.index.size)
print("the number of columns are: ", exam_data1.columns.size)
sel=exam_data1['score'].between(16,20)
print(exam_data1[sel])
de=(exam_data1['attempts']<2) & (exam_data1['score']>16)
print(exam_data1[de])

print(exam_data1)
exam_data1.loc[['C','I'], 'score']=16
print(exam_data1)
total=(exam_data1['attempts'].sum())
print(total)

exam_data1.loc['L']=['Rupali', 16, 2, 'yes']
print(exam_data1)
exam_data1.drop('L', inplace=True)
print(exam_data1)
new_df=exam_data1.iloc[:-4]
print(new_df)
