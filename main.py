import time
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from config import *
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

driver = uc.Chrome()
driver.get(website)
try:
    filters = driver.find_element(By.CLASS_NAME, 'selected-section')
    print(filters.get_attribute('innerHTML'))
    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()