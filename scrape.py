from os.path import exists
from os import environ
import pandas as pd
from selenium.webdriver.common.by import By
from utils import selenium_setup
from utils import build_df

WEB = 'https://www.google.com/search?q=JavaScript&tbm=nws&tbs=qdr:w&dpr=1'

driver = selenium_setup()
driver.get(WEB)

csv_exists = exists('history.csv')
csv_mode = 'a' if csv_exists else 'w'
action_event = environ.get('GITHUB_EVENT_NAME', 'workflow_dispatch')
csv_output = action_event != 'workflow_dispatch'

xpath_string = '//*[@id="rso"]/div'
containers = driver.find_elements(By.XPATH, xpath_string)
while (len(containers) == 1):
    xpath_string = xpath_string + '/div'
    containers = driver.find_elements(By.XPATH, xpath_string)


exit_code = 0

try:
    df_csv = build_df(containers)

    if csv_output:
        df_csv.to_csv('history.csv', header=(not csv_exists),
                      mode=csv_mode, index=False)

    df_headlines = df_csv[['Title', 'Website', 'Link']]
    df_headlines.to_markdown('news.md', index=False)
except Exception as e:
    print(e)
    exit_code = 1
finally:
    driver.quit()
    exit(exit_code)
