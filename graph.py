from datetime import datetime, timedelta
import pandas as pd

df = pd.read_csv("./history.csv",parse_dates=['Date'])

df_week = df[(df['Date'] > (datetime.today() - timedelta(days=7)))]
df_week = df_week.value_counts(subset=['Website']).reset_index().head()
ax = df_week.plot(kind='bar',x='Website',rot=0, figsize=(20,10), xlabel='', fontsize=14)
fig = ax.get_figure()
fig.savefig('last-week.png', dpi=64, bbox_inches='tight')

# Limit csv to 180 days
df = df[(df['Date'] > (datetime.today() - timedelta(days=180)))]
df.to_csv('history.csv', index=False, header=True)
