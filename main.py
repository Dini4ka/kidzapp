from bot import *
from data import *

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# # Parce offers from site
bot = KidzappParse()
try:
    bot.start()
    bot.Getting_offers()
    print(bot.send())
except Exception as ex:
    print(ex)
finally:
    bot.end()

# removing duplicates
uniqlines = set(open('config/file.txt', 'r', encoding='utf-8').readlines())
gotovo = open('config/file.txt', 'w', encoding='utf-8').writelines(set(uniqlines))

# Making xlsx offers
Make_Table()
with open('config/file.txt', "r") as file:
    lines = [line.rstrip() for line in file]
for line in lines:
    offer_key_id = make_note_in_offers(line)
    make_notes_in_child_offers(line, offer_key_id)
    make_notes_in_offers_image(line, offer_key_id)