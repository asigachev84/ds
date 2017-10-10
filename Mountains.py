
# coding: utf-8

# In[82]:


import pandas as pd
import numpy as np

df = pd.read_csv('Mountains.csv')
df.groupby(['Parent mountain']).size().reset_index(name='Count').query('Count>3')

