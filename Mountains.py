import pandas as pd

df = pd.read_csv('Mountains.csv')
# Таблица с названиями хребтов, к которым относится более 3 гор
df.groupby(['Parent mountain']).size().reset_index(name='Count').query('Count>3')

# Исходная таблица, отфильтрованная так, что в ней остаются только горы, относящиеся к хребтам, к которым относится более 3 гор
df.groupby(['Parent mountain']).filter(lambda x: len(x) > 3)
