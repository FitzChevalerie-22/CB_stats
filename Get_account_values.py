###########  Reduire au max avec un fonction

import json
from coinbase.wallet.client import Client
key = ""
scrt = ""
client = Client(key, scrt)

def coinbase_client(api_key:str, api_secret:str):
    client = Client(api_key, api_secret)
    return client

currencies_list = [
    "ETH",
    "BTC",
    "LINK",
    "MANA",
    "FIL",
    "MKR",
    "ADA",
    "SHIB",
    "XLM",
    "UNI",   
    "LTC",
    "ALGO",
    "AMP",
    "BAT",
    "DOGE",
    "OXT",
    "XTZ",
    "CRO",
    "ANKR",
    "SOL",
    "CTSI",
    "NU",
    "FET",
    "CLV",
    "AUCTION",
    "LRC",
    "GRT",
    "SKL",
    "ICP",
    "FORTH",
    "DAI",
    "ALCX",
    "GALA",
    "POLY"
    ]

def total():    
    total = 0
    # test
    for c in currencies_list:
        total += valeur(c)
    return round(total, 2)

def valeur(wallets: str):
    account = client.get_account(wallets)
    #convert to dict.
    accountdict = json.loads(json.dumps(account))

    #using dict to get the current BTC balance
    balance = round(float(accountdict['balance']['amount']),2)
    nativebalance = round(float(accountdict['native_balance']['amount']),2)
    print (wallets , "Quantité ",  balance, " Valeur ", nativebalance, "EUR" )
    return float(accountdict['native_balance']['amount'])



total()
print("Total: ", total(), "EUR")
