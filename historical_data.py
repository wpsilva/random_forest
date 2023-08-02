import yfinance as yf
import pandas as pd
from datetime import datetime
import pytz

timezone = pytz.timezone("Etc/UTC")
utc_from = datetime(2000, 3, 10, tzinfo=timezone)

tickers = pd.read_excel("./bovespa/bovespastocks.xlsx")
tickers = tickers.drop('Unnamed: 0', axis=1)

for t in tickers["ticker"]:
    print(t)
    hd = yf.download(t+".SA", start='2017-01-01')
    hd.to_csv(f"./bovespa/{t}")