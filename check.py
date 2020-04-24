from alice_blue import *
import csv
import requests
import urllib
access_token=AliceBlue.login_and_get_access_token(username='xx',password='xx',twoFA='xx',api_secret='xx')
print(access_token)
data = requests.post('https://ant.aliceblueonline.com/oauth2/auth?response_type=code&state=test_state&client_id=xx&redirect_uri=https://ant.aliceblueonline.com/plugin/callback')
data = data.text
print(data)
weburl = urllib.request.urlopen(data)
b = weburl.info()

with open('/Users/upendrasingh/Documents/Projects/alice_blue/access_token.txt','w') as wr1:
    wr=csv.writer(wr1)
    wr.writerow([access_token])



#resp = r.get(f"{config['host']}{config['routes']['authorize']}?response_type=code&state=test_state&client_id={username}&redirect_uri={redirect_url}")

#access_token=open('/Users/upendrasingh/Documents/Projects/alice_blue/access_token.txt','r').read().strip()   
"""alice=AliceBlue(username='username',password='password',access_token=access_token, master_contracts_to_download=['NSE', 'BSE'])
tatasteel_nse_eq = alice.get_instrument_by_symbol('NSE', 'TATASTEEL')
print(tatasteel_nse_eq)"""
