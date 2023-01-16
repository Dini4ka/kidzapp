import openpyxl

wb = openpyxl.Workbook()
SheetName = wb.sheetnames
wb.save(filename='data.xlsx')

'''field | null: company,header,rating_stars,rating_scale,weekend_price
         weekend_sale,monday,tuesday,wednesday,thursday,friday,
         saturday,sunday,emergency_phone,x_2_bonuses,promotes,
         reason_1,reason_2,reason_3,reason_4,reason_5,reason_6,
         question_1,answer_1,question_2,answer_2,question_3,
         answer_3,question_4,answer_4,views,all_rating_stars,
         all_rating_scale, reviews_count, questions_count,calendar
'''

'''field | 2 lang: slug,varieties,time,district,mini_desc'''

fields = ['city', 'company', 'title', 'slug',
          'header', 'rating_stars', 'rating_scale',
          'image', 'video', 'price', 'sale',
          'weekend_price', 'weekend_sale',
          'varieties', 'age', 'time', 'monday',
          'tuesday', 'wednesday', 'thursday', 'friday',
          'saturday', 'sunday', 'district',
          'address', 'map_link', 'contact_phone',
          'emergency_phone', 'mini_desc', 'status',
          'x_2_bonuses', 'promotes', 'reason_1', 'reason_2',
          'reason_3', 'reason_4', 'reason_5', 'reason_6',
          'question_1', 'answer_1', 'question_2', 'answer_2',
          'question_3', 'answer_3', 'question_4', 'answer_4',
          'views', 'all_rating_stars', 'all_rating_scale',
          'reviews_count', 'questions_count', 'calendar',
          'schedule', 'description', 'book_or_no', 'website']


''' child_fields | null : company,weekend_price,weekend_sale,delivery,views
'''
child_fields = ['company', 'agency', 'subcategory',
                'title', 'image', 'price', 'sale',
                'weekend_price', 'weekend_sale',
                'mini_desc', 'duration', 'measurement_units',  # measurement_units = ''
                'delivery', 'satus', 'views']

image = ['product', 'review', 'question', 'audit_element', 'image'] # null: product, review, question, audit_element
