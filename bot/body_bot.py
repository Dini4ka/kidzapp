import time
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from config import *


class KidzappParse:

    def __init__(self):
        self.driver = uc.Chrome()
        self.links = []

    def start(self):
        self.driver.get(website)

    def Getting_offers(self):
        # Filters
        categories = []
        # Getting all attributes for filters
        _filters = self.driver.find_elements(By.CLASS_NAME, 'js-example-disabled-results')
        for _filter in _filters:
            if 'Category*' in _filter.text:
                categories = _filter.text.split('\n')[1:]
                break

        # handle categories
        category_field = Select(self.driver.find_element(By.ID, 'categoryDropdown'))
        for _category in categories:
            category_field.select_by_visible_text(_category)
            time.sleep(2)
            # Getting offer's link
            offer_list = self.driver.find_element(By.CLASS_NAME, 'reviewDiv')
            self.links = [offer.get_attribute('href') for offer in offer_list.find_elements(By.TAG_NAME, 'a')]
            print(self.links)
        time.sleep(5)

    def end(self):
        self.driver.close()
