from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os


def selenium_setup():
    cwd_path = os.getcwd()
    test_driver_path = os.path.join(cwd_path, 'bin', 'chromedriver', 'chromedriver')
    driver_path = os.environ.get('CHROMEDRIVER_PATH', test_driver_path)

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    if "CHROME_PATH" in os.environ:
        options.binary_location = os.environ["CHROME_PATH"]
    driver_service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=driver_service, options=options)

    return driver
