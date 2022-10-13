import pandas as pd

df = pd.read_csv('history.csv')
del df['Domain']
df.to_csv('history.csv', index=False, header=True)