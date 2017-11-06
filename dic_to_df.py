"""
File: dic_to_dc.py
author Petri Lamminaho
create simple python dictionary
convert dic to Pandas dataframe
and do all kind tricks with it
"""

import pandas as pd

stat = {
    'Day':[1,2,3,4,5,6],
    'Visitors':[100, 50, 70, 40, 80, 65],
    'Bounce_rate':[65, 63, 70, 55, 63, 60]
}

df = pd.DataFrame(stat)
#print(df)
#print(df.set_index('Day'))# print dataframe dosent save it


#df = df.set_index('Day') # saves the df to old df
#print(df)

#sorted_df = df.set_index('Day') # saves df to new sorted_df
#print(sorted_df)

df.set_index('Day', inplace=True) # clean way to do it
print(df)

print("Prints multiple columns:\n ", df[ ['Visitors', 'Bounce_rate'] ])

print(df.Visitors.tolist())# print column as python list

import  numpy as np

print("df to numpy array:")
print(np.array(df[ ['Visitors', 'Bounce_rate'] ]))

df2 = pd.DataFrame(np.array(df[['Bounce_rate', 'Visitors']]))
print(df2)