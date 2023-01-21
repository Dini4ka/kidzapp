import time
import requests
from bs4 import BeautifulSoup

from config.config import *


class KidzappParse:

    def __init__(self):
        self.res = []
        self.new_res = []
        self.categories = []

    def start(self):
        soup = BeautifulSoup(requests.get(website).text, 'html.parser')
        filters = soup.find('select', {'onchange': 'getSubCategories(this.options[this.selectedIndex].value)'})
        self.categories = [filter.get('id') for filter in filters.findAll('option') if filter.get('id')]
        try:
            with open('config/file.txt', 'r') as f:
                self.res = [line.replace('\n', '') for line in f.readlines()]
            f.close()
        except FileNotFoundError:
            pass

    def gettingNewOffers(self):
        for category in self.categories:
            print(f'Parsing {self.categories.index(category) + 1}s from {len(self.categories)} categories ...')
            page = 1
            params = {
                "PageNum": f"{page}",
                "countryCode": "ae",
                "lang": "en",
                "searchQuery": f"&category={category}",
                "lat": "",
                "lan": ""
            }
            need_to_parce = requests.post(website, data=params).json()
            while need_to_parce['message'] == 'success':
                print(f'Checking {page}s page')
                links = ['https://kidzapp.com/' + item['url'] for item in need_to_parce['searchData']]
                [self.new_res.append(link) and print('Добавлена новая ссылка') for link in links
                 if link not in self.res and link not in self.new_res and link != '']
                page += 1
                params = {
                    "PageNum": f"{page}",
                    "countryCode": "ae",
                    "lang": "en",
                    "searchQuery": f"&category={category}",
                    "lat": "",
                    "lan": ""
                }
                need_to_parce = requests.post(website, data=params).json()
        print('Find ' + str(len(self.new_res)) + ' new links')

    def end(self):
        with open("config/file.txt", "a+") as file:
            print("\n".join(map(str, self.new_res)), file=file)
        file.close()
