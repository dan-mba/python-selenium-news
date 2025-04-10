from datetime import date
import pandas as pd
from selenium.webdriver.common.by import By


def build_df(containers):
    titles = []
    sites = []
    links = []
    dates = []

    for container in containers:
        base = container.find_element(By.TAG_NAME, 'a')
        link = base.get_attribute('href')

        # articles without an img are displayed differently
        try:
            title = base.find_element(
                By.XPATH, './div/div[2]/div[2]').text.replace('|', '').replace('"', '\'')
            site = base.find_element(
                By.XPATH, './div/div[2]/div[1]/div[2]/span').text.replace('|', '')
        except:
            title = base.find_element(
                By.XPATH, './div/div/div[2]').text.replace('|', '').replace('"', '\'')
            site = base.find_element(
                By.XPATH, './div/div/div[1]/div[2]/span').text.replace('|', '')
        titles.append(title)
        sites.append(site)
        links.append(link)
        dates.append(date.today())

    my_dict = {'Title': titles, 'Website': sites,
               'Link': links, 'Date': dates}

    return pd.DataFrame(my_dict)
