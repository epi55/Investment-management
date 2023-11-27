# https://python.plainenglish.io/coding-stock-breakouts-in-python-a-step-by-step-guide-592211e36774
# FOLLOWING THIS TUTORIAL, will test how to run this into the larger Investment management project

from yahoo_fin.stock_info import get_data
import pandas as pd
import numpy as np

ticker = input("What ticker would you like to review? ")

def potential_breakouts(ticker):
    '''A function that returns date and prices for potential breakouts of a stock using historical daily prices'''
 
    # Get the historical weekly prices from the specified start date and end date (both YYYY-mm-dd)
    hist = get_data(ticker, index_as_date=False)
    
    # Drop the adjusted close column
    prices = hist.drop(['adjclose'], axis=1)
    
    # Get the length of candle's body (from open to close)
    prices['O-to-C'] = prices['close'] - prices['open']
    
    # Get the rolling mean of the candles' bodies for recent 20 candles
    prices['OC-20D-Mean'] = prices['O-to-C'].rolling(20).mean()
    
    # Get the % change of the current OC relative from the rolling mean
    prices['OC-%-from-20D-Mean'] = 100*(prices['O-to-C'] - prices['OC-20D-Mean'])/prices['OC-20D-Mean']
    
    # Get the maximum OC compared to the recent 10 candles
    prices['MaxOC_Prev10'] = prices['O-to-C'].rolling(10).max()
    
    # Get the rolling mean of volume for the recent 20 candles
    prices['Volume-20D-Mean'] = prices['volume'].rolling(20).mean()
    
    # Get the % change of the current volume relative from the rolling mean
    prices['Volume-%-from-20D-Mean'] = 100*(prices['volume'] - prices['Volume-20D-Mean'])/prices['Volume-20D-Mean']
    
    # Drop the null values for the first 19 rows, where no mean can be computed yet
    prices = prices.dropna()
    
    # Rearrange columns
    prices = prices[['ticker', 'date', 'open', 'high', 'low', 'close', 
                     'O-to-C', 'OC-20D-Mean', 'volume', 'Volume-20D-Mean', 
                     'MaxOC_Prev10', 'OC-%-from-20D-Mean', 'Volume-%-from-20D-Mean', 
                ]]
    
    # Select the subset of dataframe where breakout conditions apply
    # Conditions: 1. green candle, 2. candle's body is longest in 10 days, 
    # 3. breakout volume is 50% higher than the rolling 20-day average, and
    # 4. breakout candle has body that is 100% higher than the rolling 20-day average
    
    condition = (prices['O-to-C'] >= 0.0) & (prices['O-to-C'] == prices['MaxOC_Prev10']) & (prices['OC-%-from-20D-Mean'] >= 100.0) & (prices['Volume-%-from-20D-Mean'] >= 50.0) 

    breakouts = prices[condition]

    print(breakouts)

potential_breakouts(ticker)