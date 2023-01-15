import time
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from config import *
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Filters
Cities = []
Areas = []
Categories = []
Sub_Categories = []

driver = uc.Chrome()
driver.get(website)
try:
    # Getting all attributes for filters
    filters = driver.find_elements(By.CLASS_NAME, 'js-example-disabled-results')
    for filter in filters:
        if 'Al Ain' in filter.text:
            Cities.append(filter.text.split('\n'))
            continue
        if 'Category*' in filter.text:
            Categories.append(filter.text.split('\n'))
            break
except Exception as ex:
    print(ex)
finally:
    print(Categories)
    print(Cities)
    driver.close()
