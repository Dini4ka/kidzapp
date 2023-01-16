from bot import *

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

bot = KidzappParse()

try:
    bot.start()
    bot.Getting_offers()
except Exception as ex:
    print(ex)
finally:
    bot.end()