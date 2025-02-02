import streamlit as st
import yfinance as yf
import pandas as pd

def get_fundamental_data(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    
    fundamental_data = {
        "Company Name": info.get("longName", "N/A"),
        "Sector": info.get("sector", "N/A"),
        "Industry": info.get("industry", "N/A"),
        "Market Cap": info.get("marketCap", "N/A"),
        "PE Ratio": info.get("trailingPE", "N/A"),
        "Forward PE Ratio": info.get("forwardPE", "N/A"),
        "Price to Book Ratio": info.get("priceToBook", "N/A"),
        "Dividend Yield": info.get("dividendYield", "N/A"),
        "Revenue": info.get("totalRevenue", "N/A"),
        "EBITDA": info.get("ebitda", "N/A"),
        "Debt to Equity Ratio": info.get("debtToEquity", "N/A"),
        "Return on Assets (ROA)": info.get("returnOnAssets", "N/A"),
        "Return on Equity (ROE)": info.get("returnOnEquity", "N/A"),
        "Current Ratio": info.get("currentRatio", "N/A"),
        "Quick Ratio": info.get("quickRatio", "N/A")
    }
    return fundamental_data

# Streamlit UI
st.set_page_config(page_title="Stock Fundamental Analysis", layout="wide")
st.title("📈 Stock Fundamental Analysis Dashboard")

st.sidebar.header("Enter Stock Ticker")
ticker = st.sidebar.text_input("Stock Ticker (e.g., AAPL, TSLA, MSFT)", value="AAPL").upper()

if ticker:
    try:
        data = get_fundamental_data(ticker)
        df = pd.DataFrame(data.items(), columns=["Metric", "Value"])
        
        st.subheader(f"Fundamental Analysis of {ticker}")
        st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.error(f"Error retrieving data: {e}")