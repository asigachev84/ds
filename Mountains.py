import pandas as pd

df = pd.read_csv('Mountains.csv')
df.groupby(['Parent mountain']).size().reset_index(name='Count').query('Count>3')
