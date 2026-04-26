import numpy as np

def calculate_volatility(hist_data):
    """
    Calculates annualized volatility based on daily stock price history.
    """
    # Calculate daily returns
    daily_returns = hist_data['Close'].pct_change()
    
    # Calculate daily standard deviation
    daily_volatility = np.std(daily_returns)
    
    # Annualize it (assume 252 trading days)
    annualized_volatility = daily_volatility * np.sqrt(252)
    return annualized_volatility

def calculate_sharpe_ratio(hist_data, risk_free_rate=0.04):
    """
    Calculates the generalized Sharpe Ratio based on historical data.
    """
    # Calculate daily returns
    daily_returns = hist_data['Close'].pct_change().dropna()
    
    # Annualized return
    avg_daily_return = np.mean(daily_returns)
    annualized_return = avg_daily_return * 252
    
    # Annualized volatility
    annualized_volatility = calculate_volatility(hist_data)
    
    if annualized_volatility == 0:
        return 0
    
    sharpe_ratio = (annualized_return - risk_free_rate) / annualized_volatility
    return sharpe_ratio
