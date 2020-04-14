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
        api_data = WatchMessage.valid_api_data(api_tuple)   #checks if the timeframe and percentage entered by the user is usable
        if token_name == True and api_data == True:
            return True
        else:
            return False

    @classmethod
    def api_tuple(cls, message):
        '''Returns a tuple like ("token", " ", "timeframe percentage")
        example: ("bitcoin", " ", "15m >6%")'''
        api_info = message[7:]
        return api_info.partition(" ")

    @classmethod
    def valid_api_data(cls, api_tuple):
        '''Returns Boolean'''
        data_tuple = api_tuple[2].partition(" ")
        timeframe = WatchMessage.valid_timeframe(data_tuple[0])
        percentage = WatchMessage.valid_percentage(data_tuple[2])
        if timeframe and percentage == True:
            return True
        else:
            return False

    @classmethod
    def valid_timeframe(cls, timeframe_text):
        '''Returns a Boolean'''
        try:
            if timeframe_text[-1] == "h" or timeframe_text[-1] == "m":
                integer = WatchMessage.return_integer(timeframe_text)
                if isinstance(integer, int):
                    return True
                else:
                    return False
            else:
                return False
        except (IndexError, ValueError) as e:
            return False


    @classmethod
    def valid_percentage(cls, percentage_text):
        '''Returns a Boolean'''
        try:
            if percentage_text[-1] == "%":
                slice = len(percentage_text)-1
                new_string = percentage_text[:slice]
                if new_string[0] == ">" or new_string[0] == "<":
                    float_string = new_string[1:]
                    percentage_float = float(float_string)
                    if isinstance(percentage_float, float):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        except (IndexError, ValueError) as e:
            return False

    @classmethod
    def return_integer(cls, string):
        slice = len(string)-1   #the length of the string minus the last character, essentially removing the last character of the string
        string_integer = string[:slice]
        return int(string_integer)

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
