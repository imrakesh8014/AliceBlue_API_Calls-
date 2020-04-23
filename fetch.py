from alice_blue import *
import csv

access_token = 'DrS3PaaceaJwZO4ja9H8tXM9CETwochZTP10Ku_rnOc.3LYEW69RikurJW-BPmqzvG8o6P16-N42vUj8ejDYwAM'
alice = AliceBlue(username = 'AB051040', password = '#Tda@2k19', access_token = access_token)
tatasteel_nse_eq = alice.get_instrument_by_symbol('NSE', 'TATASTEEL')
print(tatasteel_nse_eq)
print(alice.get_profile())

#access_token = AliceBlue.login_and_get_access_token(username = 'AB051040', password = '#Tda@2k19', twoFA = 'O', redirect_url='https://ant.aliceblueonline.com/plugin/callback' ,app_id = 'SP37' ,api_secret = 'N34Q5C1CFU273Y97O8OMYT276MUGLAWY50UTXFHNCEWCXD0OAIGDLQ93B6TSSU0F')
#print(access_token)

