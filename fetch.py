from alice_blue import *
import csv

access_token = 'xx'
alice = AliceBlue(username = 'xx', password = 'xx', access_token = access_token)
tatasteel_nse_eq = alice.get_instrument_by_symbol('NSE', 'TATASTEEL')
print(tatasteel_nse_eq)
print(alice.get_profile())

#access_token = AliceBlue.login_and_get_access_token(username = 'xx', password = 'xx', twoFA = 'xx', redirect_url='https://ant.aliceblueonline.com/plugin/callback' ,app_id = 'xx' ,api_secret = 'xx')
#print(access_token)

