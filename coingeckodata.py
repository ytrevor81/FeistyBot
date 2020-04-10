from pycoingecko import CoinGeckoAPI
from db_functions import *
from messagehandling import *

gecko = CoinGeckoAPI()

class CoinGecko(object):
    '''These will serve as user /watch functionality'''

    @classmethod
    def watchquery(cls):
        data = gecko.get_price(ids='bitcoin', vs_currencies='usd', include_24hr_vol='true')
