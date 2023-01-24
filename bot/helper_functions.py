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
    keys =['address', 'age_max', 'age_min', 'all_rating_scale',
           'all_rating_stars', 'answer_1', 'answer_2', 'answer_3',
           'answer_4', 'book_or_no', 'calendar', 'city', 'company',
           'contact_phone', 'description_ar', 'description_en',
           'district_ar', 'district_en', 'emergency_phone', 'friday',
           'header', 'image', 'map_link', 'mini_desc_ar',
           'mini_desc_en', 'monday', 'price', 'promotes', 'question_1',
           'question_2', 'question_3', 'question_4', 'questions_count',
           'rating_scale', 'rating_stars', 'reason_1', 'reason_2', 'reason_3',
           'reason_4', 'reason_5', 'reason_6', 'reviews_count', 'sale',
           'saturday', 'schedule', 'slug', 'status', 'sunday', 'thursday',
           'time', 'title_ar', 'title_en', 'tuesday', 'varieties_ar', 'varieties_en',
           'video', 'views', 'website', 'wednesday', 'weekend_price', 'weekend_sale', 'x_2_bonuses']
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
