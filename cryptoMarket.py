import json
import requests
import asyncio
from flask_socketio import SocketIO, emit

apiCryptoNames = {
    "Bitcoin":"BTCUSDT",
    "Etherum":"ETHUSDT",
    "BNB":"BNBUSDT",
    "Ripple":"XRPUSDT",
    "BUSD":"BUSDUSDT",
    "Cardano":"ADAUSDT",
    "Dodgecoin":"DOGEUSDT",
    "Polygon":"MATICUSDT",
    "Litecoin":"LTCUSDT"
}

cryptoValues={
    "Bitcoin":0,
    "Etherum":0,
    "BNB":0,
    "Ripple":0,
    "BUSD":0,
    "Cardano":0,
    "Dodgecoin":0,
    "Polygon":0,
    "Litecoin":0
}

# Defining Binance API URL
key = "https://api.binance.com/api/v1/ticker/price?symbol="

def get_crypto_market_data():
    j = 0
    while True:
    # running loop to print all crypto prices
        for k in apiCryptoNames:
            # completing API for request
            url = key+apiCryptoNames[k]
            data = requests.get(url)
            data -=k
            data = data.json()
            j = j+1
            cryptoValues[k]=data['price']
        emit(cryptoValues)
            