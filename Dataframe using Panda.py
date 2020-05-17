import pandas as pd
import numpy as np


data = {'city': ['Mumbai', 'Mumbai', 'Mumbai',
                 'Hyderabad','Hyderabad','Hyderabad'],
        'year': [2010, 2011, 2012, 2010, 2011, 2012],
        'population': [10.0, 10.3, 10.5, 5.6, 5.7, 5.8]}

print(data)
print(type(data))

df1 = pd.DataFrame(data)
print(df1)

print(df1.head()) # Top 5 Records
print(df1.tail()) # Bottom 5 Records

df2 = pd.DataFrame(data, columns=['year','city','population'])
print(df2)

df3 = pd.DataFrame(data, columns=['year','city','population', 'GDP'],
                   index=['one','two','three','four','five','six'])
print(df3)

print(df3.dtypes)

print(df3.loc['one'])

df3.GDP= np.arange(6)
print(df3)

val = pd.Series([-1.9,2.6,1.3], index=['two', 'four', 'six'])

df3.GDP = val
print(df3)