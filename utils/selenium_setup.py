from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os


def selenium_setup():
    cwd_path = os.getcwd()
    test_driver_path = os.path.join(cwd_path, 'bin', 'chromedriver')
    driver_path = os.environ.get('CHROMEDRIVER_PATH', test_driver_path)

    options = Options()
    options.headless = True
    driver_service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=driver_service, options=options)

    return driver
