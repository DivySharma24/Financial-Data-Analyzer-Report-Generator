import pandas as pd

def calculate_ratios(df):
    """
    Calculates key financial ratios from the provided dataframe.
    Expected columns: Revenue, Net Income, Total Assets, Current Assets, 
                      Total Liabilities, Current Liabilities, Shareholder Equity
    """
    df = df.copy()
    
    # 1. Profit Margin = Net Income / Revenue
    df['Profit Margin (%)'] = (df['Net Income'] / df['Revenue']) * 100
    
    # 2. Return on Equity (ROE) = Net Income / Shareholder Equity
    df['ROE (%)'] = (df['Net Income'] / df['Shareholder Equity']) * 100
    
    # 3. Current Ratio = Current Assets / Current Liabilities
    df['Current Ratio'] = df['Current Assets'] / df['Current Liabilities']
    
    # 4. Debt-to-Equity = Total Liabilities / Shareholder Equity
    df['Debt-to-Equity'] = df['Total Liabilities'] / df['Shareholder Equity']
    
    # 5. Return on Assets (ROA) = Net Income / Total Assets
    df['ROA (%)'] = (df['Net Income'] / df['Total Assets']) * 100
    
    return df
