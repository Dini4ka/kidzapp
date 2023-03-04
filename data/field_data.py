# main table fields
main_fields_null = ['all_rating_scale', 'all_rating_stars', 'answer_1',
                    'answer_2', 'answer_3', 'answer_4', 'calendar',
                    'company_id', 'emergency_phone', 'estimations_count',
                    'friday', 'header',
                    'monday', 'promotes', 'question_1', 'question_2',
                    'question_3', 'question_4', 'questions_count',
                    'rating_scale', 'rating_stars', 'reason_1',
                    'reason_2', 'reason_3', 'reason_4', 'reason_5',
                    'reason_6', 'reviews_count', 'saturday', 'sunday',
                    'thursday', 'tuesday', 'views_id', 'wednesday',
                    'weekend_price', 'weekend_sale', 'x_2_bonuses',
                    'estimations_count']
main_field_dbl_lang = ['varieties', 'district', 'mini_desc', 'description']


main_fields = ['id', 'city', 'title', 'title_en', 'title_ar', 'slug', 'header',
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



# child table fields
child_fields_null = ['company_id', 'weekend_price', 'weekend_sale', 'delivery', 'views,_id', 'image',
                     'duration', 'delivery']
child_field_dbl_lang = ['title', ]
child_fields = ['company_id', 'agency_id', 'subcategory', 'subcategory_en', 'subcategory_ar',
                'title', 'title_en', 'title_ar', 'image', 'price', 'sale',
                'weekend_price', 'weekend_sale', 'mini_desc',
                'mini_desc_en', 'mini_desc_ar', 'description',  'description_en', 'description_ar',
                'duration', 'measurement_units',  # measurement_units = ''
                'delivery', 'status', 'views_id']

# image table fields
image_null = ['product_id', 'review_id', 'question_id', 'audit_element_id']
image = ['product_id', 'review_id', 'question_id', 'audit_element_id', 'image']
