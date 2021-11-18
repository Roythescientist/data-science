import numpy as np
from numpy.core.defchararray import index
from numpy.core.fromnumeric import shape, size
from numpy.lib.utils import info
import pandas as pd

pd_num=np.linspace(1,20)
pd_num=50
pd_rand=pd.Series(np.random.randn(pd_num))
print(pd_rand.head)
lis =[1,2,3,4,56,7,88,87,6,54,34]
pd.Series(lis)
print(lis)
Data = {"India": "New Delhi", "Japan": "Tokyo", "UK": "London"} 
d.Series(Data)
Data.values
Data.index


num1 = np.arange(10) 
index1=["A","B","C","D","E","F","G","H","I","J"]
z=pd.Series(num1,index=index1)
k=z[4::3]
print(k)
g=z[::-1]
print(g)
print(z[::2])
print(z.tolist) 

data =['25', '50', '100', '200', '300', '400']
pd.Series(data)
da=pd.Series([500, 600,700])
v=(data.append(da))
q=pd.to_numeric(v)
print([q<=100])
