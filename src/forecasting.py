import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def forecast_revenue(df, company_name, future_years=3):
    """
    Forecasts future revenue using a simple linear regression based on historical data.
    """
    company_data = df[df['Company'] == company_name].sort_values(by='Year')
    
    if len(company_data) < 3:
        return None # Not enough data to forecast
    
    X = company_data[['Year']].values
    y = company_data['Revenue'].values
    
    model = LinearRegression()
    model.fit(X, y)
    
    last_year = int(X[-1][0])
    future_X = np.array([[last_year + i] for i in range(1, future_years + 1)])
    
    future_y = model.predict(future_X)
    
    forecast_df = pd.DataFrame({
        'Year': future_X.flatten(),
        'Forecasted Revenue': future_y
    })
    
    return forecast_df
