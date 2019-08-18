S"""
Created on Sun Aug 18 18:47:32 2019

@author: lenovo
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#df = pd.read_csv('data/mtcars.csv')
from pydataset import data
mtcars = data('mtcars')
mtcars.head()
df = mtcars
df
type(df)
df
df.head()
df.columns
catcolumns1=['cyc','vs','am','gear','carb']
catcolums1
df[catcolumns1]=df[catc
