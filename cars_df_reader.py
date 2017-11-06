"""
file cars_df_file.py
Author: Petri Lamminaho
reads two text file and convert files to Pandas df
raw txt file  and csv-format file
"""

import pandas as pd
df = pd.read_fwf('cars.txt')
data = pd.read_csv('cars_csv.txt', sep=",")
print(df)
print(data)