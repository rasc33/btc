#!/usr/bin/env python
# coding: UTF-8

import sys
import configparser
from bittrex.bittrex import API_V2_0, Bittrex

confFile = "../apikey.txt"
apiKeyFile = "../apikey.txt"
apiSecretFile = "../apisecret.txt"

config = configparser.ConfigParser()

try:
   config.read(confFile)
   apikey = config['bittrex']['apikey']
   apisecret = config['bittrex']['apisecret']

except:
   print('Error occured')
   exit()

print('API Key is ', apikey)
print('API Secret is ', apisecret)

my_Bittrex = Bittrex(apikey, apisecret, api_version=API_V2_0)
#print (my_Bittrex.get_balances())


btc_balance = my_Bittrex.get_balance('BTC')
{'success': True, 
 'message': '',
 'result': {'Currency': 'BTC', 'Balance': 0.0, 'Available': 0.0, 
            'Pending': 0.0, 'CryptoAddress': None}
}

print (btc_balance)
