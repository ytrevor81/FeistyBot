##################This is just for testing##################

import sqlite3
from pycoingecko import CoinGeckoAPI

conn = sqlite3.connect("bot.db")
c = conn.cursor()
gecko = CoinGeckoAPI()

watch_msg = "/watch btc 1511h >5%"

api_info = watch_msg[7:]
api_tuple = api_info.partition(" ")

token_name = api_tuple[0]
api_requests = api_tuple[2]
print(token_name, api_requests)

data_tuple = api_requests.partition(" ")

timeframe = data_tuple[0]
percentage = data_tuple[2]

if percentage[-1] == "%":
    if percentage[0] == "<" or percentage[0] == ">":
        print(percentage[1:])
    else:
        print("nooooo")
else:
    print("fail")

print(isinstance(float("15"), float))

c.close()
conn.close()
