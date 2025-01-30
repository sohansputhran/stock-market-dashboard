import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start_date, end_date):
    stock = yf.download(ticker, start=start_date, end=end_date)
    stock.reset_index(inplace=True)
    stock.to_csv(f'../../data/{ticker}_stock_data.csv', index=False)
    print(f"Data collected for {ticker}")

fetch_stock_data('AAPL', '2024-01-01', '2025-01-01')