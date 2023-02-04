import requests
from data.field_data import *


def parce_child_offers(offer_key_id, res_en):
    offer_id = offer_id = res_en['id']
    params_ar = {
        "countryCode": 'ae',
        "id": offer_id,
        "lang": 'ar'
    }
    res_ar = requests.post('https://kidzapp.com/otherOffers', data=params_ar).json()['data']
    items = []
    #######################
    # Рассмотрим два случая
    #######################
    # 1) нет информации
    if not res_en['price']:
        offers_item = res_en['price_age_groups'].split('\r\n')
        offers_item_ar = res_ar['price_age_groups'].split('\r\n')
        offers_prices = res_en['price_age_prices'].split('\r\n')
        for offer in range(len(offers_item)):
            item = {}
            item['agency_id'] = offer_key_id
            item['title'] = offers_item[offer]
            item['title_en'] = offers_item[offer]
            item['title_ar'] = offers_item_ar[offer]
            try:
                item['price'] = offers_prices[offer].replace('AED', '')
            except IndexError as ex:
                print(ex)
                print(f'price not specified for {item["title_en"]}')
                item['price'] = None
            item['sale'] = None
            item['description_en'] = item['mini_desc_en'] = res_en['working_hours_brief']
            item['description_ar'] = item['mini_desc_ar'] = res_ar['working_hours_brief']
            item['description'] = item['description_en']
            item['subcategory'] = None
            item['subcategory_en'] = None
            item['subcategory_ar'] = None
            item['duration'] = None
            item['measurement_units'] = ''
            item['status'] = 'Одобрено'
            for field in child_fields_null:
                item[field] = None
            items.append(item)
    ######################
    # 2) есть информация
    else:
        offers_item_en = res_en['price']
        offers_item_ar = res_ar['price']
        for offer in range(len(offers_item_en)):
            item = {}
            item['agency_id'] = offer_key_id
            item['title_en'] = offers_item_en[offer]['type']
            item['title_ar'] = offers_item_ar[offer]['type']
            item['title'] = item['title_en']
            item['price'] = offers_item_en[offer]['orginal_price']
            item['sale'] = offers_item_en[offer]['final_price']
            item['mini_desc_en'] = offers_item_en[offer]['small_text_type'] if offers_item_en[offer][
                                                                                   'small_text_type'] is not None else \
            res_en['working_hours_brief']
            item['mini_desc_ar'] = offers_item_ar[offer]['small_text_type_ar'] if offers_item_ar[offer][
                                                                                      'small_text_type_ar'] is not None else \
            res_ar['working_hours_brief']
            item['description_en'] = item['mini_desc_en']
            item['description_ar'] = item['mini_desc_ar']
            item['description'] = item['description_en']
            item['subcategory_en'] = offers_item_ar[offer]['header_en']
            item['subcategory_ar'] = offers_item_ar[offer]['header_ar']
            item['subcategory'] = item['subcategory_en']
            item['duration'] = None
            item['measurement_units'] = ''
            item['status'] = 'Одобрено'
            for field in child_fields_null:
                item[field] = None
            items.append(item)
    return items


def parce_image_offers(offer_key_id, res):
    image_items = []
    images = res['image_carousel_list']
    for image in images:
        item = {'review_id': 'None', 'question_id': 'None', 'audit_element_id': 'None', 'product_id': offer_key_id, 'image': image}
        image_items.append(item)
    return image_items


def parce_main_item(res, id):
    offer_id = res['id']
    item = {}
    params_ar = {
        "countryCode": 'ae  ',
        "id": offer_id,
        "lang": 'ar'
    }
    schedule_param = {'id': offer_id}
    schedule = requests.post('https://kidzapp.com/scheduleData', data=schedule_param).json()

    res_ar = requests.post('https://kidzapp.com/otherOffers', data=params_ar).json()['data']
    # id
    item['id'] = id
    # city
    item['city'] = res['city']['name']
    # title_en, title_ar
    item['title'] = res['title']
    item['title_en'] = res['title']
    item['title_ar'] = res_ar['title']
    # slug
    item['slug'] = res['slug']
    # image
    try:
        item['image'] = res['image_carousel_list'][0]
    except Exception as ex:
        print(ex)
        item['image'] = None
    # video
    if res['video'] == '':
        item['video'] = None
    else:
        item['video'] = res['video']
    # price
    try:
        item['price'] = res['price'][0]['orginal_price']
    except Exception as ex:
        print(ex)
        item['price'] = None
    # sale
    try:
        if res['price'][0]['final_price'] == 0:
            item['sale'] = None
        item['sale'] = res['price'][0]['final_price']
    except Exception as ex:
        print(ex)
        item['sale'] = None
    # varieties
    for category in res['categories']:
        item['varieties_en'] = (category['name_en'])
        item['varieties_ar'] = (category['name_ar'])
    # age_max, age_min
    item['age_min'] = (res['ages_display'][0])
    item['age_max'] = (res['ages_display'][-1])
    # time
    item['time'] = res['working_hours_brief']
    # district_en, district_ar
    item['district_ar'] = (res['area']['name_ar'])
    item['district_en'] = (res['area']['name_en'])
    # address
    item['address'] = (res['address'])
    # map_link
    try:
        item['map_link'] = ('https://www.google.com/maps/search/?api=1&query=' + (
                str(res['location']['lat']) + ',' + str(res['location']['lon'])))
    except Exception as ex:
        print(ex)
        item['map_link'] = None
    # contact_phone
    item['contact_phone'] = (res['phone'])
    # mini_desc_en
    item['mini_desc_en'] = (res['description'].split('\n')[0])
    # mini_desc_ar
    if res_ar['description'].split('\n')[0] == '':
        item['mini_desc_ar'] = None
    else:
        item['mini_desc_ar'] = res_ar['description'].split('\n')[0]
    # status
    item['status'] = 'Одобрено'
    # schedule
    if schedule['status']:
        item['schedule'] = schedule['schedules']
    else:
        item['schedule'] = ('[{"day":"sun","open":"12:00 AM","close":"11:59 PM"},{"day":"mon",' \
                            '"open":"12:00 AM","close":"11:59 PM"},{"day":"tue","open":"12:00 AM",' \
                            '"close":"11:59 PM"},{"day":"wed","open":"12:00 AM","close":"11:59 PM"},' \
                            '{"day":"thu","open":"12:00 AM","close":"11:59 PM"},{"day":"fri",' \
                            '"open":"12:00 AM","close":"11:59 PM}]')
    # description_en,description_ar
    item['description'] = (res['description'])
    item['description_en'] = (res['description'])
    item['description_ar'] = (res_ar['description'])

    # book_or_no
    item['book_or_no'] = (res['bookable'])

    # website
    if res['website'] == '':
        item['website'] = None
    else:
        item['website'] = (res['website'])

    for field in main_fields_null:
        item[field] = None
    myKeys = list(item.keys())
    myKeys.sort()
    sorted_item = {i: item[i] for i in myKeys}
    return sorted_item
