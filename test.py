##################This is just for testing##################

import sqlite3
from pycoingecko import CoinGeckoAPI

conn = sqlite3.connect("bot.db")
c = conn.cursor()

string = "5544544%"
hey = string.replace("%","")
num = float(hey)
print(isinstance(num, float))



c.close()
conn.close()
