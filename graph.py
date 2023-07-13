from datetime import datetime, timedelta
import pandas as pd

df = pd.read_csv("./history.csv",parse_dates=['Date'], usecols=['Date', 'Website'])
df = df[(df['Date'] > (datetime.today() - timedelta(days=7)))]
ax = df.value_counts(subset=['Website']).plot.bar(rot=0)
fig = ax.get_figure()
fig.savefig('last-week.png')
