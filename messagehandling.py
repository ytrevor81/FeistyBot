'''This file holds all functionality processing the raw string data from /watch messages.'''
from pycoingecko import CoinGeckoAPI

class WatchMessage(object):
    '''Handles all raw data from /watch messages'''

    @classmethod
    def is_valid(cls, message):
        '''Returns a Boolean value. If True, then the message was valid
        and token name is valid'''
        api_tuple = WatchMessage.api_tuple(message)
        token_name = WatchMessage.valid_token_name(api_tuple)  #checks if token name entered by the user is valid
        percentage = WatchMessage.valid_api_data(percentage)   #checks if the timeframe and percentage entered by the user is usable
        if token_name == True and percentage == True:
            return True
        else:
            return False

    @classmethod
    def api_tuple(cls, message):
        '''Returns a tuple like ("token", " ", "percentage")
        example: ("bitcoin", " ", "6%")'''
        api_info = message[7:]
        return api_info.partition(" ")

    @classmethod
    def valid_api_data(cls, api_tuple):
        '''Returns Boolean'''
        percentage = WatchMessage.valid_percentage(api_tuple[2])
        if percentage == True:
            return True
        else:
            return False

    @classmethod
    def valid_percentage(cls, percentage_text):
        '''Returns a Boolean'''
        try:
            if percentage_text[-1] == "%":
                number_string = percentage_text.replace("%","")
                percentage_float = float(number_string)
                if isinstance(percentage_float, float):
                    return True
                else:
                    return False
            else:
                return False
        except (IndexError, ValueError) as e:
            return False

    @classmethod
    def valid_token_name(cls, api_tuple):
        '''Returns a Boolean'''
        gecko = CoinGeckoAPI()
        token_name = api_tuple[0]
        data = gecko.get_price(ids=token_name, vs_currencies='usd')
        if len(data) == 0:
            return False
        else:
            return True
