# main table fields
main_fields_null = ['company', 'header', 'rating_stars', 'rating_scale', 'weekend_price',
                    'weekend_sale', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday',
                    'saturday', 'sunday', 'emergency_phone', 'x_2_bonuses', 'promotes',
                    'reason_1', 'reason_2', 'reason_3', 'reason_4', 'reason_5', 'reason_6',
                    'question_1', 'answer_1', 'question_2', 'answer_2', 'question_3',
                    'answer_3', 'question_4', 'answer_4', 'views', 'all_rating_stars',
                    'all_rating_scale', 'reviews_count', 'questions_count', 'calendar']
main_field_dbl_lang = ['varieties', 'district', 'mini_desc', 'description']
main_fields = ['city', 'company', 'title', 'slug',
               'header', 'rating_stars', 'rating_scale',
               'image', 'video', 'price', 'sale',
               'weekend_price', 'weekend_sale',
               'varieties_en', 'varieties_ar', 'age_min', 'age_max',
               'time', 'monday',
               'tuesday', 'wednesday', 'thursday', 'friday',
               'saturday', 'sunday', 'district_en', 'district_ar'
               'address', 'map_link', 'contact_phone',
               'emergency_phone', 'mini_desc_en', 'mini_desc_ar', 'status',
               'x_2_bonuses', 'promotes', 'reason_1', 'reason_2',
               'reason_3', 'reason_4', 'reason_5', 'reason_6',
               'question_1', 'answer_1', 'question_2', 'answer_2',
               'question_3', 'answer_3', 'question_4', 'answer_4',
               'views', 'all_rating_stars', 'all_rating_scale',
               'reviews_count', 'questions_count', 'calendar',
               'schedule', 'description_en', 'description_ar', 'book_or_no', 'website']

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
