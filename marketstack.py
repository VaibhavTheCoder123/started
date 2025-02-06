import requests
from config import MARKETSTACK_API_KEY

BASE_URL = "http://api.marketstack.com/v1/eod"

def get_stock_price(symbol):
    params = {
        "access_key": MARKETSTACK_API_KEY,
        "symbols": symbol
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if "data" in data and len(data["data"]) > 0:
        return data["data"][0]["close"]  # Closing price of the stock
    return None 