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
        percentage = CoinGecko.percentage_processing(api_tuple[2])  #returns a float
        data = gecko.get_price(ids=token, vs_currencies='usd', include_24hr_vol='true')
        SQL.updated_data(token, percentage, data)
        CoinGecko.updates(data)

    @classmethod
    def percentage_processing(cls, perc_string):
        '''Returns a list of the float and less/greater [float, "less" (or) "greater"]'''
        float_string = perc_string.replace("%", "")
        percentage = float(float_string)
        return percentage

    @classmethod
    def updates(cls, data):
        '''SQL queries and possibly asynch programming in here'''
        pass
