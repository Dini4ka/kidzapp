from bot import *
from data import *

import ssl
from datetime import datetime

ssl._create_default_https_context = ssl._create_unverified_context

# Parce offers from site
bot = kidzappParse()
try:
    bot.startGettingFilters()
    bot.makeJson()
    bot.getItems()
except Exception as ex:
    print(ex)

