import pandas as pd

def calculate_trends(df):
    """
    Calculates year-over-year trends for key metrics.
    """
    df = df.sort_values(by=['Company', 'Year']).copy()
    
    # Calculate YoY Growth for Revenue and Net Income
    df['Revenue YoY Growth (%)'] = df.groupby('Company')['Revenue'].pct_change() * 100
    df['Net Income YoY Growth (%)'] = df.groupby('Company')['Net Income'].pct_change() * 100
    
    return df
