import pandas as pd
import numpy as np

COINS = [

"ADA/USD",  #     Cardano (ADA)
"AVAX/USD",    #    Avalanche (AVAX)
"BNB/USD",    #	Binance Coin (BNB)
"BTC/USD",    #	Bitcoin (BTC)
"DASH/USD",   #	Dash (DASH)
"DOGE/USD",    #	Dogecoin (DOGE)
"DOT/USD",   #	Dot (DOT)
"ETH/USD",    #	Ethereum (ETH)
"LTC/USD",    #	Litecoin (LTC)
"MATIC/USD",  #	Matic (MATIC)
"NEO/USD",   #	NEO (NEO)
"SOL/USD",    #	Solana (SOL)
"XBT/USD",  #    Bitcoin (XBT)
"XMR/USD",   #	Monero (XMR)
"XRP/USD",    #	Ripple (XRP)
]

def getDailyVol(close,span0=100):
    df0=close.index.searchsorted(close.index-pd.Timedelta(days=1))
    df0=df0[df0>0]
    df0=pd.Series(close.index[df0-1], index=close.index[close.shape[0]-df0.shape[0]:])
    df0=close.loc[df0.index]/close.loc[pd.to_datetime( df0.values, utc=True)].values-1 # daily returns
    df0=df0.ewm(span=span0).std()
    return df0

def standardize(df, look_back, type='standard', dropna=True, drop_cols=False):
    """
    despite what it shows, it is minmax standardization, 
    not standard standardization.

    needs to be updated in the future to reflect
    
    """
    if type == 'minmax':
        x_bar   = df.rolling(look_back).min()
        z_std   = df.rolling(look_back).max() - x_bar
        z_score = 1 + (df - x_bar) / z_std
    elif type=='standard':
        x_bar   = df.rolling(look_back).mean()
        z_std   = df.rolling(look_back).std()
        z_score = (df - x_bar) / z_std
    else:
        raise ValueError("type must be 'standard' or 'minmax'")

    z_score.replace([np.inf, -np.inf], np.nan, inplace=True)

    if drop_cols:
        z_score.dropna(axis=1, thresh=( 0.7 * z_score.shape[0]), inplace=True)

    if dropna:
        return z_score.fillna(method ='ffill').dropna()
    
    return z_score.fillna(method ='ffill')

