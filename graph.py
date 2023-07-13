from datetime import datetime, timedelta
import pandas as pd

df = pd.read_csv("./history.csv",parse_dates=['Date'], usecols=['Date', 'Website'])
df = df[(df['Date'] > (datetime.today() - timedelta(days=7)))]
df = df.value_counts(subset=['Website']).reset_index().head()
ax = df.plot(kind='bar',x='Website',rot=0, figsize=(20,10), xlabel='', fontsize=14)
fig = ax.get_figure()
fig.savefig('last-week.png', dpi=64, bbox_inches='tight')
