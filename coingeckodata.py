from pycoingecko import CoinGeckoAPI
import sqlite3

conn = sqlite3.connect('bot.db')
c = conn.cursor()

gecko = CoinGeckoAPI()

data = gecko.get_price(ids='bitcoin', vs_currencies='usd', include_24hr_vol='true')

print(data)

c.close()
conn.close()
