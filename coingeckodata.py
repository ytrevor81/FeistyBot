from pycoingecko import CoinGeckoAPI
from db_functions import *
from messagehandling import *

gecko = CoinGeckoAPI()

class CoinGecko(object):
    '''These will serve as user /watch functionality'''

    @classmethod
    def watchquery(cls, username, message):
        api_tuple = WatchMessage.api_tuple(message)
        token = api_tuple[0]
        timeframe = CoinGecko.time_processing(api_tuple[2])
        percentage = CoinGecko.percentage_processing(api_tuple[2])
        data = gecko.get_price(ids=token, vs_currencies='usd', include_24hr_vol='true')
        SQL.updated_data(token, timeframe, percentage, data)

    @classmethod
    def time_processing(cls, timeframe):
        '''Process time string into usable integer'''
        pass

    @classmethod
    def percentage_processing(cls, percentage):
        '''Process time string into usable integer'''
        pass
