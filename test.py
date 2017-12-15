#!/usr/bin/env python
# coding: UTF-8

from bittrex.bittrex import API_V2_0, Bittrex

apiKeyFile = "../apikey.txt"
apiSecretFile = "../apisecret.txt"

f = open(apiKeyFile, encoding='ASCII')
apikey = f.read()
f.close()
print (apikey)

f = open(apiSecretFile, encoding='ASCII')
apisecret = f.read()
f.close()
print (apisecret)


my_Bittrex = Bittrex(apikey, apisecret, api_version=API_V2_0)
#print (my_Bittrex.get_balances())


btc_balance = my_Bittrex.get_balance('BTC')
{'success': True, 
 'message': '',
 'result': {'Currency': 'BTC', 'Balance': 0.0, 'Available': 0.0, 
            'Pending': 0.0, 'CryptoAddress': None}
}

print (btc_balance)
