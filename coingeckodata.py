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
        timeframe = CoinGecko.time_processing(api_tuple[2])     #returns a list [15, "minutes"]
        percentage = CoinGecko.percentage_processing(api_tuple[2])  #returns a list [5.0, "greater"]
        data = gecko.get_price(ids=token, vs_currencies='usd', include_24hr_vol='true')
        SQL.updated_data(token, timeframe, percentage, data)
        CoinGecko.updates(data)

    @classmethod
    def time_processing(cls, api_tuple):
        '''Returns a list of the integer and hour/minute [integer, "hours" (or) "minutes"]'''
        new_tuple = api_tuple.partition(" ")
        time_string = new_tuple[0]
        integer_string = time_string.replace("h", "").replace("m", "")
        integer = int(integer_string)
        if time_string[-1] == "h":
            return [integer, "hours"]
        else:
            return [integer, "minutes"]

    @classmethod
    def percentage_processing(cls, api_tuple):
        '''Returns a list of the float and less/greater [float, "less" (or) "greater"]'''
        new_tuple = api_tuple.partition(" ")
        percentage_string = new_tuple[2]
        float_string = percentage_string.replace(">", "").replace("<", "")
        percentage = float(float_string)
        if percentage_string[0] == "<":
            return [percentage, "greater"]
        else:
            return [percentage, "less"]

    @classmethod
    def updates(cls, data):
        '''SQL queries and possibly asynch programming in here'''
        pass
