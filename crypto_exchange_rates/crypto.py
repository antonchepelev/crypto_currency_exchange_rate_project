import requests 
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("API_KEY")


url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false&locale=en&api_key={API_KEY}"
response = requests.get(url)
coins = response.json()



class CryptoCoin:
    def __init__(self, name, id, symbol, image, current_price, market_cap, market_cap_rank, total_volume, high_24h, low_24h, price_change_24h, price_change_percentage_24h, circulating_supply, total_supply, max_supply, ath, ath_change_percentage, ath_date, atl, atl_change_percentage, atl_date, last_updated):
        self.name = name
        self.id = id
        self.symbol = symbol
        self.image = image
        self.current_price = current_price
        self.market_cap = market_cap
        self.market_cap_rank = market_cap_rank
        self.total_volume = total_volume
        self.high_24h = high_24h
        self.low_24h = low_24h
        self.price_change_24h = price_change_24h
        self.price_change_percentage_24h = price_change_percentage_24h
        self.circulating_supply = circulating_supply
        self.total_supply = total_supply
        self.max_supply = max_supply
        self.ath = ath
        self.ath_change_percentage = ath_change_percentage
        self.ath_date = ath_date
        self.atl = atl
        self.atl_change_percentage = atl_change_percentage
        self.atl_date = atl_date
        self.last_updated = last_updated

    def __str__(self):
        return f"{self.name} coin object"


coins_list = []

for coin_data in coins:
    coin = CryptoCoin(
        name=coin_data["name"],
        id=coin_data["id"],
        symbol=coin_data["symbol"],
        image=coin_data["image"],
        current_price=coin_data["current_price"],
        market_cap=coin_data["market_cap"],
        market_cap_rank=coin_data["market_cap_rank"],
        total_volume=coin_data["total_volume"],
        high_24h=coin_data["high_24h"],
        low_24h=coin_data["low_24h"],
        price_change_24h=coin_data["price_change_24h"],
        price_change_percentage_24h=coin_data["price_change_percentage_24h"],
        circulating_supply=coin_data["circulating_supply"],
        total_supply=coin_data["total_supply"],
        max_supply=coin_data["max_supply"],
        ath=coin_data["ath"],
        ath_change_percentage=coin_data["ath_change_percentage"],
        ath_date=coin_data["ath_date"],
        atl=coin_data["atl"],
        atl_change_percentage=coin_data["atl_change_percentage"],
        atl_date=coin_data["atl_date"],
        last_updated=coin_data["last_updated"]
    )
    coins_list.append(coin)

attribute_mapping = {
    "name": "Name",
    "id": "ID",
    "symbol": "Symbol",
    "image": "Image",
    "current_price": "Current Price",
    "market_cap": "Market Cap",
    "market_cap_rank": "Market Cap Rank",
    "total_volume": "Total Volume",
    "high_24h": "High 24h",
    "low_24h": "Low 24h",
    "price_change_24h": "Price Change 24h",
    "price_change_percentage_24h": "Price Change Percentage 24h",
    "circulating_supply": "Circulating Supply",
    "total_supply": "Total Supply",
    "max_supply": "Max Supply",
    "ath": "All-Time High (ATH)",
    "ath_change_percentage": "ATH Change Percentage",
    "ath_date": "ATH Date",
    "atl": "All-Time Low (ATL)",
    "atl_change_percentage": "ATL Change Percentage",
    "atl_date": "ATL Date",
    "last_updated": "Last Updated"
}






def get_coin_by_symbol(symbol):
    try:
        for coin in coins_list:
            if coin.symbol == symbol:
                return coin
    except Exception:
        print("Not found")






