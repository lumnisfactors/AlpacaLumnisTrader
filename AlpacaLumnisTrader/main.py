from AlpacaLumnisTrader import AlpacaLumnisTrader
from utils import COINS
from KEYS import API_KEY_BINANCE, SECRET_KEY_BINANCE, API_KEY_LUMNIS


if __name__ == "__main__":
        
    tradingAgent                 = AlpacaLumnisTrader(API_KEY_BINANCE, SECRET_KEY_BINANCE, API_KEY_LUMNIS, COINS)

    tradingAgent.run()