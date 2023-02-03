import requests
from config.config import *


def telegram_bot_sendtext(bot_message):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    requests.get(send_text)


def send_file(file):
    files = {'document': open(file, 'rb')}
    send_photo = 'https://api.telegram.org/bot' + bot_token + '/sendDocument?chat_id=' + bot_chatID
    requests.post(send_photo, files=files)


def check_item(inside_items, outside_item):
    keys = ['id', 'city', 'title', 'title_en', 'title_ar', 'slug', 'header',
            'rating_stars', 'rating_scale', 'image', 'video', 'price',
            'sale', 'weekend_price', 'weekend_sale', 'varieties_en', 'varieties_ar',
            'age_min', 'age_max', 'time', 'monday', 'tuesday', 'wednesday', 'thursday',
            'friday', 'saturday', 'sunday', 'district_en',
            'district_ar', 'address', 'map_link', 'contact_phone', 'emergency_phone',
            'mini_desc', 'mini_desc_en', 'mini_desc_ar', 'status', 'x_2_bonuses',
            'promotes', 'reason_1', 'reason_2', 'reason_3', 'reason_4', 'reason_5',
            'reason_6', 'question_1', 'answer_1', 'question_2', 'answer_2', 'question_3',
            'answer_3', 'question_4', 'answer_4', 'all_rating_stars', 'all_rating_scale',
            'reviews_count', 'questions_count', 'estimations_count', 'calendar', 'schedule',
            'description', 'description_en', 'description_ar', 'book_or_no', 'website', 'company_id',
            'views_id']
    for item in inside_items:
        res = True
        for key in keys:
            if item[key] == outside_item[key]:
                continue
            else:
                res = False
                break
        if res:
            return True


def makeParams(page, category):
    params = {
        "PageNum": f"{page}",
        "countryCode": "ae",
        "lang": "en",
        "searchQuery": f"&category={category}",
        "lat": "",
        "lan": ""
    }
    return params
