import requests
from pprint import pprint

def parce(link):
    offer_id = link.split('-')[-1]
    item = {}
    params_en = {
        "countryCode": 'ae',
        "id": offer_id,
        "lang": 'en'
    }
    params_ar = {
        "countryCode": 'ae',
        "id": offer_id,
        "lang": 'ar'
    }
    schedule_param = {'id': offer_id}
    schedule = requests.post('https://kidzapp.com/scheduleData', data=schedule_param).json()

    res = requests.post('https://kidzapp.com/otherOffers', data=params_en).json()['data']
    res_ar = requests.post('https://kidzapp.com/otherOffers', data=params_ar).json()['data']
    # city
    item['city'] = res['city']['name']
    # title_en, title_ar
    item['title_en'] = res['title']
    item['title_ar'] = res_ar['title']
    # slug
    item['slug'] = res['slug']
    # image
    item['image'] = res['image_carousel_list']
    # video
    if res['video'] == '':
        item['video'] = None
    else:
        item['video'] = res['video']
    # price
    try:
        item['price'] = res['price'][0]['orginal_price']
    except Exception:
        item['price'] = None
    # sale
    try:
        item['sale'] = res['price'][0]['final_price']
    except Exception:
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
    item['map_link'] = ('https://www.google.com/maps/search/?api=1&query=' + (
            str(res['location']['lat']) + ',' + str(res['location']['lon'])))
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
    item['status'] = 'approved'
    # schedule
    if schedule['status']:
        item['schedule'] = schedule['schedules']
    else:
        item['schedule'] = ('[{"day":"sun","open":"12:00 AM","close":"11:59 PM"},{"day":"mon",' \
                            '"open":"12:00 AM","close":"11:59 PM"},{"day":"tue","open":"12:00 AM",' \
                            '"close":"11:59 PM"},{"day":"wed","open":"12:00 AM","close":"11:59 PM"},' \
                            '{"day":"thu","open":"12:00 AM","close":"11:59 PM"},{"day":"fri",' \
                            '"open":"12:00 AM","close":"11:59 PM')
    # description_en,description_ar
    item['description_en'] = (res['description'])
    item['description_ar'] = (res_ar['description'])

    # book_or_no
    item['book_or_no'] = (res['bookable'])

    # website
    if res['website'] == '':
        item['website'] = ('None')
    else:
        item['website'] = (res['website'])

    return item

pprint(parce('https://kidzapp.com/kids-activities/abu-dhabi/theme-parks/the-wizarding-world-of-harry-potter-at-warner-bros-abu-dhabi-114534'))