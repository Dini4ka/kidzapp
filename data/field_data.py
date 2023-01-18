# main table fields
main_fields_null = ['all_rating_scale', 'all_rating_stars', 'answer_1',
                    'answer_2', 'answer_3', 'answer_4', 'calendar',
                    'company', 'emergency_phone', 'friday', 'header',
                    'monday', 'promotes', 'question_1', 'question_2',
                    'question_3', 'question_4', 'questions_count',
                    'rating_scale', 'rating_stars', 'reason_1',
                    'reason_2', 'reason_3', 'reason_4', 'reason_5',
                    'reason_6', 'reviews_count', 'saturday', 'sunday',
                    'thursday', 'tuesday', 'views', 'wednesday',
                    'weekend_price', 'weekend_sale', 'x_2_bonuses']
main_field_dbl_lang = ['varieties', 'district', 'mini_desc', 'description']
main_fields = ['address', 'age_max', 'age_min', 'all_rating_scale',
               'all_rating_stars', 'answer_1', 'answer_2', 'answer_3',
               'answer_4', 'book_or_no', 'calendar', 'city', 'company',
               'contact_phone', 'description_ar', 'description_en',
               'district_ar', 'district_en', 'emergency_phone', 'friday',
               'header', 'image', 'map_link', 'mini_desc_ar', 'mini_desc_en',
               'monday', 'price', 'promotes', 'question_1', 'question_2',
               'question_3', 'question_4', 'questions_count', 'rating_scale',
               'rating_stars', 'reason_1', 'reason_2', 'reason_3', 'reason_4',
               'reason_5', 'reason_6', 'reviews_count', 'sale', 'saturday',
               'schedule', 'slug', 'status', 'sunday', 'thursday', 'time',
               'title_ar', 'title_en', 'tuesday', 'varieties_ar', 'varieties_en',
               'video', 'views', 'website', 'wednesday', 'weekend_price',
               'weekend_sale', 'x_2_bonuses']

# child table fields
child_fields_null = ['company', 'weekend_price', 'weekend_sale', 'delivery', 'views']
child_fields = ['company', 'agency', 'subcategory',
                'title', 'image', 'price', 'sale',
                'weekend_price', 'weekend_sale',
                'mini_desc', 'duration', 'measurement_units',  # measurement_units = ''
                'delivery', 'satus', 'views']

# image table fields
image_null = ['product', 'review', 'question', 'audit_element']
image = ['product', 'review', 'question', 'audit_element', 'image']