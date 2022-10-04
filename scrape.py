from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from urllib.parse import urlparse
from os.path import exists
from datetime import date
import pandas as pd
import os

cwd_path = os.getcwd()
test_driver_path = os.path.join(cwd_path, 'bin', 'chromedriver')
driver_path = os.environ.get('CHROMEDRIVER_PATH', test_driver_path)

WEB = 'https://www.google.com/search?q=JavaScript&tbm=nws&tbs=qdr:w&dpr=1'

options = Options()
options.headless = True
driver_service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=driver_service, options=options)
driver.get(WEB)

xpath_string = '//*[@id="rso"]/div'

csv_exists = exists('history.csv')
csv_mode = 'a' if csv_exists else 'w'
action_event = os.environ.get('GITHUB_EVENT_NAME', 'workflow_dispatch')
csv_output = action_event != 'workflow_dispatch'

containers = driver.find_elements(by='xpath', value=xpath_string)
while (len(containers) == 1):
    xpath_string = xpath_string + '/div'
    containers = driver.find_elements(by='xpath', value=xpath_string)

titles = []
sites = []
links = []
domains = []
dates = []
exit_code = 0

try:
    for container in containers:
        try:
            base = container.find_element(
                by='xpath', value='./div/a')
        except:
            base = container.find_element(
                by='xpath', value='./div/div/a')
        link = base.get_attribute('href')
        # articles without an img are displayed differently
        try:
            title = base.find_element(
                by='xpath', value='./div/div[2]/div[2]').text.replace('|', '').replace('"', '\'')
            site = base.find_element(
                by='xpath', value='./div/div[2]/div[1]/span').text.replace('|', '')
        except:
            title = base.find_element(
                by='xpath', value='./div/div/div[2]').text.replace('|', '').replace('"', '\'')
            site = base.find_element(
                by='xpath', value='./div/div/div[1]/span').text.replace('|', '')
        titles.append(title)
        sites.append(site)
        links.append(link)
        domains.append(urlparse(link).netloc)
        dates.append(date.today())

    my_dict = {'Title': titles, 'Website': sites,
               'Link': links, 'Domain': domains, 'Date': dates}

    df_csv = pd.DataFrame(my_dict)
    
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
