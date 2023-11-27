import pandas as pd
import numpy as np
import pathlib
import os

dataFolder = pathlib.Path('Projects') / 'Investment management' / 'Database'

def buy(ticker, market, price, units, broker):
    dataFile = os.path.join(dataFolder, 'portfolioLog.csv')
    dfLog = pd.read_csv(dataFile)
    # Add entry: Buy
    newEntry = {'action': 'buy', 'ticker': ticker, 'market': market, 'price': price, 'units': units, 'broker': broker}
    newDF = pd.DataFrame([newEntry])
    dfLog = pd.concat([dfLog, newDF], ignore_index=True)
    dfLog.to_csv(dataFile, index=False)
    print(dfLog) # TEST

def sell(ticker, market, price, units, broker):
    dataFile = os.path.join(dataFolder, 'portfolioLog.csv')
    dfLog = pd.read_csv(dataFile)
    # Add entry: Sell
    newEntry = {'action': 'sell', 'ticker': ticker, 'market': market, 'price': price, 'units': units, 'broker': broker}
    newDF = pd.DataFrame([newEntry])
    dfLog = pd.concat([dfLog, newDF], ignore_index=True)
    dfLog.to_csv(dataFile, index=False)
    print(dfLog) # TEST