import pandas as pd
import numpy as np
from datetime import datetime
global_data=pd.read_csv('C:/Users/ROY/Desktop/global_data.csv')

#Import the datetime module from datetime and convert the columns 'Order Date' and 'Ship Date' to the DatetimeIndex objects
order_date=global_data['Order Date'].to_list()
order_datetime=pd.to_datetime(order_date)
print(order_datetime)
ship_date=global_data['Ship Date'].to_list()
ship_datetime=pd.to_datetime(ship_date)
print(ship_datetime)

#Check the DatetimeIndex objects converted for the null values
null_values=order_datetime[order_datetime.isnull()]
print(null_values)
not_null_values=order_datetime[order_datetime.notnull()]
print(not_null_values)

#Convert the DatetimeIndex objects to a Series objects with the names 'Order_Date' and 'Ship_Date'

series1=pd.Series(order_datetime, name='Order_Date')
series2=pd.Series(ship_datetime,name='Ship_Date')
print(series1[:2], series2[:2])

# Join the datetime Series objects created just above with the global_superstore_2016
#  columns ['Row ID', 'Order ID', 'Ship Mode', 'Customer ID', 'Customer Name', 'Segment', 'Category']
data_modified = pd.concat([series1, series2, global_data['Row ID'], global_data['Order ID'], global_data['Ship Mode'], 
                           global_data['Customer ID'], global_data['Customer Name'], global_data['Segment'], 
                           global_data['Category']], axis=1)
print(data_modified)

#Set the Series 'Order_Date' created as the index of the DataFrame 'data_modified'
indexed_data=data_modified.set_index(['Order_Date'])
indexed_data.index
print(indexed_data)

#Check whether the DatetimeIndex of the DataFRame is unique or not
datetime_unique=indexed_data.index.is_unique
print(datetime_unique)

#Find the number of orders made in each year for the data 'global_superstore_2016'
#len(indexed_data['order'])
#len(indexed_data['2013'])
#len(indexed_data['2014'])
#len(indexed_data['2015'])
#print(indexed_data['2012'].sum())

#Group the 'indexed_data' on level '0' that is on the 
# DatetimeIndex object and count the number of Orders made for any arbitrary date
grouped=indexed_data.groupby(level=0,)['Order ID']
print(grouped.value_counts())