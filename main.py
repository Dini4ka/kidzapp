import time
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from config import *
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Filters
Cities = []
Categories = []

driver = uc.Chrome()
driver.get(website)
try:
    # Getting all attributes for filters
    filters = driver.find_elements(By.CLASS_NAME, 'js-example-disabled-results')
    for filter in filters:
        if 'Al Ain' in filter.text:
            Cities = filter.text.split('\n')[1:]
            continue
        if 'Category*' in filter.text:
            Categories = filter.text.split('\n')[1:]
            break

    # handle categories
    category_field = Select(driver.find_element(By.ID, 'categoryDropdown'))
    for category in Categories:
        category_field.select_by_visible_text(category)

    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    print(Categories)
    print(Cities)
    driver.close()
