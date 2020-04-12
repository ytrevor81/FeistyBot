##################This is just for testing##################

import sqlite3
from pycoingecko import CoinGeckoAPI

conn = sqlite3.connect("bot.db")
c = conn.cursor()
gecko = CoinGeckoAPI()

watch_msg = "/watch btc 1511h >5%"



c.close()
conn.close()
