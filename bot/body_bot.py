import json
import requests
from bs4 import BeautifulSoup

from config.config import *
from data.field_data import *
from bot.parcing_links import *
from bot.helper_functions import *

class kidzappParse:

    def __init__(self):
        try:
            with open('main_items.json', 'r', encoding='utf-8') as f:
                text = json.load(f)
                self.main_items = text
        except FileNotFoundError:
            self.main_items = []
        self.child_items = []
        self.image_items = []
        self.categories = []

    def startGettingFilters(self):

        # Общий html код страницы https://kidzapp.com/filter/
        soup = BeautifulSoup(requests.get(website).text, 'html.parser')

        # Ищем все фильтры, по которым будем искать категории
        filters = soup.find('select', {'onchange': 'getSubCategories(this.options[this.selectedIndex].value)'})
        self.categories = [filter.get('id') for filter in filters.findAll('option') if filter.get('id')]

    def getItems(self):

        # Определяем id следующего элемента
        try:
            with open('main_items.json', 'r', encoding='utf-8') as f:
                text = json.load(f)
                item_id = len(text) - 1
        except FileNotFoundError:
            item_id = 0

        for category in self.categories:

            # Parsing 2s from 20 categories (example)
            print(f'Parsing {self.categories.index(category) + 1}s from {len(self.categories)} categories ...')
            telegram_bot_sendtext(
                f'Parsing {self.categories.index(category) + 1}s from {len(self.categories)} categories ...')

            page = 1
            params = makeParams(page, category)

            # Список из 10 предложений по конкретной категории, полученных через API
            need_to_parce = requests.post(website, data=params).json()

            # Листаем страницы, пока будет ответ
            while need_to_parce['message'] == 'success':
                # Checking 2nd page (example)
                print(f'Checking {page}s page')
                telegram_bot_sendtext(f'Checking {page}s page')
                for item in need_to_parce['searchData']:
                    item_id += 1

                    # Достаем основное предложение, его дочерние предложения и изображения
                    item_res = parce_main_item(res=item, id=item_id)
                    child_items_res = parce_child_offers(res_en=item, offer_key_id=item_id)
                    image_items_res = parce_image_offers(res=item, offer_key_id=item_id)

                    # Если предложение дубируется, то пропускам, иначе - добавляем
                    if not check_item(inside_items=self.main_items, outside_item=item_res):
                        self.main_items.append(item_res)
                        [self.child_items.append(child_item) for child_item in child_items_res]
                        [self.image_items.append(image_item) for image_item in image_items_res]
                    else:
                        print('doubled element skipped')
                        telegram_bot_sendtext('doubled element skipped')
                page += 1

                # Переопределяем переменные
                params = makeParams(page, category)
                need_to_parce = requests.post(website, data=params).json()

    def makeJson(self):

        # Создаем json-файл и отправляем его в телеграмме
        with open('config/main_items.json', 'a+') as outfile:
            json.dump(self.main_items, outfile)
        send_file('config/main_items.json')
        with open('config/child_items.json', 'a+') as outfile:
            json.dump(self.child_items, outfile)
        send_file('config/child_items.json')
        with open('config/image_items.json', 'a+') as outfile:
            json.dump(self.image_items, outfile)
        send_file('config/image_items.json')
