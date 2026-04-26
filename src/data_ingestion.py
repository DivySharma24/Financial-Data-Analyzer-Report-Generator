import pandas as pd
import yfinance as yf
import streamlit as st

@st.cache_data
def load_data(file):
    """
    Loads financial data from a CSV or Excel file.
    """
    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
    elif file.name.endswith('.xlsx'):
        df = pd.read_excel(file)
    else:
        raise ValueError("Unsupported file format. Please upload a CSV or Excel file.")
    return df

@st.cache_data
def fetch_market_data(ticker, period='5y'):
    """
    Fetches historical market data for a given ticker from Yahoo Finance.
    """
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period)
        if hist.empty:
             raise ValueError(f"No data found for ticker {ticker}.")
        return hist
    except Exception as e:
        raise ValueError(f"Error fetching data for {ticker}: {str(e)}")

def get_company_info(ticker):
    """
    Fetches general company info from Yahoo Finance.
    """
    try:
        stock = yf.Ticker(ticker)
        return stock.info
    except Exception:
        return {}
