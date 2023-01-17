import time
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from config import *


def scroll_down(self):
    begin = 0
    while True:
        try:
            self.driver.find_element(By.ID, 'not-found1')
            break
        except:
            self.driver.execute_script(f"window.scrollTo({begin},{begin + 500});")
            begin += 500
            time.sleep(2)


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
        with open("файл.txt", "w") as file:
            for _category in categories:
                print(f'Parsing {_category} .... ')
                category_field.select_by_visible_text(_category)
                time.sleep(2)
                scroll_down(self)
                offer_list = self.driver.find_element(By.CLASS_NAME, 'reviewDiv')
                offer_links = [offer.get_attribute('href') for offer in offer_list.find_elements(By.TAG_NAME, 'a')
                                   if 'kids-activities' in offer.get_attribute('href')]
                print("\n".join(map(str,offer_links)), file=file)
                self.links.append(offer_links)
                print('Parsed ' + str(len(offer_links)))
        uniqlines = set(open(file, 'r', encoding='utf-8').readlines())
        gotovo = open(file, 'w', encoding='utf-8').writelines(set(uniqlines))
        file.close()
        time.sleep(5)

    def send(self):
        return self.links

    def end(self):
        self.driver.close()
