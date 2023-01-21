from bot import *
from data import *

import ssl
from datetime import datetime

ssl._create_default_https_context = ssl._create_unverified_context

start_time = datetime.now()

# # Parce offers from site
bot = KidzappParse()
try:
    bot.start()
    bot.gettingNewOffers()
    bot.end()
except Exception as ex:
    print(ex)


# Making xlsx offers
Make_Table()
with open('config/file.txt', "r") as file:
    lines = [line.rstrip() for line in file]
for line in lines:
    offer_key_id = make_note_in_offers(line)
    make_notes_in_child_offers(line, offer_key_id)
    make_notes_in_offers_image(line, offer_key_id)
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))