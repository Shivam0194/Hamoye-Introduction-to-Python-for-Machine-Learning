# -*- coding: utf-8 -*-
"""Hamoye Introduction to Python for Machine Learning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mNGitkVi2lQdS4tH_sxvbZ1_UQQiVWOF
"""

import pandas as pd
import numpy as np
import seaborn as sns

#renamaing the sheet (FoodBalanceSheets_E_Africa_NOFLAG.csv) to Foodbalancesheet.

df=pd.read_csv('/content/FoodBalanceSheet.csv' , encoding='latin-1')

df

df['Element'].value_counts()

#12. What is the mean and standard deviation across the whole dataset for the year 2015 to 3 decimal places?
round(df['Y2015'].mean(),3)

round(df['Y2015'].std(axis = 0),3)

#13. What is the total number and percentage of missing data in 2016 to 2 decimal places?
df['Y2016'].isnull().sum()

round(((df['Y2016'].isnull().sum())*100)/len(df),2)

#14 
df1=df[['Element Code','Y2014','Y2015','Y2016','Y2017','Y2018']]

df['Area'].nunique()

df1.corr()

df.groupby('Element')['Element'].count()

