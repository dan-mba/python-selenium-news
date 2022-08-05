from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
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

containers = driver.find_elements(by='xpath', value=xpath_string)
while(len(containers) == 1):
    xpath_string = xpath_string + '/div'
    containers = driver.find_elements(by='xpath', value=xpath_string)
titles = []
sites = []
links = []
exit_code = 0
try:
    for container in containers:
        link = container.find_element(by='xpath', value='./div/a').get_attribute('href')
        # articles without an img are displayed differently
        try:
            title = container.find_element(by='xpath', value='./div/a/div/div[2]/div[2]').text.replace('|', '')
            site = container.find_element(by='xpath', value='./div/a/div/div[2]/div[1]/span').text.replace('|', '')
        except:
            title = container.find_element(by='xpath', value='./div/a/div/div/div[2]').text.replace('|', '')
            site = container.find_element(by='xpath', value='./div/a/div/div/div[1]/span').text.replace('|', '')
        titles.append(title)
        sites.append(site)
        links.append(link)

    my_dict = {'Title': titles, 'Website': sites, 'Link': links}
    df_headlines = pd.DataFrame(my_dict)
    df_headlines.to_markdown('news.md', index=False)
except Exception as e:
    print(e)
    exit_code = 1
finally:
    driver.quit()
    exit(exit_code)
