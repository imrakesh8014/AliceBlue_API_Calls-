from alice_blue import *
import requests
import alice_blue
import csv
access_token=AliceBlue.login_and_get_access_token(username='AB051040',password='#Tda@2k19',twoFA='O',api_secret='N34Q5C1CFU273Y97O8OMYT276MUGLAWY50UTXFHNCEWCXD0OAIGDLQ93B6TSSU0F')
print(access_token)
data = requests.get('https://ant.aliceblueonline.com/oauth2/auth?response_type=code&state=test_state&client_id=SP37&redirect_uri=https://ant.aliceblueonline.com/plugin/callback')
data = data.json
print(data)

"""alice=AliceBlue(username='username',password='password',access_token='O5LGEoKZXQbo8pLLr_mLTlBFziSI0R8OOORiMYdTtGE.Up98W5I903ZTrvvYUJ6NZab9CzFSZCkijlU19m3Y0xM', master_contracts_to_download=['NSE', 'BSE'])
tatasteel_nse_eq = alice.get_instrument_by_symbol('NSE', 'TATASTEEL')
print(tatasteel_nse_eq)"""

"""tok = requests.post('https://ant.aliceblueonline.com/oauth2/token?response_type=code&state=test_state&client_id=SP37&client_secret=N34Q5C1CFU273Y97O8OMYT276MUGLAWY50UTXFHNCEWCXD0OAIGDLQ93B6TSSU0F&grant_type=5rmoHnqXFkzXDCW8l85Re3yS6glunm65QoWKT3MZlLU.NCgjg19yGvtu6HbdremBGqLLCIsbgk787BGA1NNb9yU&redirect_uri=https://ant.aliceblueonline.com/plugin/callback&authorization_response=authorization_response')
print("tok -->",tok)"""
#https://ant.aliceblueonline.com/plugin/callback/?code=1_Z0LFW8URDmUJUSbY_x5OAK_Jot2K7bYcmkRDpIQ_w.aBAil9dAakw790FCyx1YEwvFHbJQ6web317dh6tjQ7s&scope=&state=test_state

"""with open('access_token.txt','w') as wr1:
    wr=csv.writer(wr1)
    wr.writerow([access_token])
access_token=open('access_token.txt','r').read().strip()   
alice=AliceBlue(username='AB051040',password='#Tda@2k20',access_token=access_token, master_contracts_to_download=['NSE', 'BSE'])
tatasteel_nse_eq = alice.get_instrument_by_symbol('NSE', 'TATASTEEL')
print(tatasteel_nse_eq)"""

#wss://[https://ant.aliceblueonline.com]/hydrasocket/v2/websocket?access_token={access_token}

#DELETE /api/v2/order?oms_order_id=180807000042019&order_status=open

#Base URL for the API will be: https://ant.aliceblueonline.com

"""Client ID:    SP37 
Client Secret:   N34Q5C1CFU273Y97O8OMYT276MUGLAWY50UTXFHNCEWCXD0OAIGDLQ93B6TSSU0F  
Callback URL :https://ant.aliceblueonline.com/plugin/callback
Auth URL :https://ant.aliceblueonline.com/oauth2/auth
Access Token URL : https://ant.aliceblueonline.com/oauth2/token
data=requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=INFY&interval=1min&apikey=QSDM61FZ7IKUSQTC')
data=data.json()
"""

#1_Z0LFW8URDmUJUSbY_x5OAK_Jot2K7bYcmkRDpIQ_w.aBAil9dAakw790FCyx1YEwvFHbJQ6web317dh6tjQ7s&scope=




