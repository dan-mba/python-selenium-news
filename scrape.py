from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
import os

cwd_path = os.getcwd()
test_driver_path = os.path.join(cwd_path, 'bin', 'chromedriver')
driver_path = os.environ.get('CHROMEDRIVER_PATH', test_driver_path)

web = 'https://www.google.com/search?q=JavaScript&tbm=nws&tbs=qdr:w&dpr=1'

options = Options()
options.headless = True
driver_service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=driver_service, options=options)
driver.get(web)

containers = driver.find_elements(by='xpath', value='//*[@id="rso"]/div')

titles = []
sites = []
links = []
for container in containers:
    title = container.find_element(by='xpath', value='././div/a/div/div[2]/div[2]').text.replace('|', '')
    site = container.find_element(by='xpath', value='./div/a/div/div[2]/div[1]/span').text.replace('|', '')
    link = container.find_element(by='xpath', value='./div/a').get_attribute('href')
    titles.append(title)
    sites.append(site)
    links.append(link)

my_dict = {'Title': titles, 'Website': sites, 'Link': links}
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_markdown('news.md', index=False)

driver.quit()
