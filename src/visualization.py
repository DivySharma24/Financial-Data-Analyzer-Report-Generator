import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

def plot_revenue_trend(df, company_name):
    company_data = df[df['Company'] == company_name]
    fig = px.bar(
        company_data, 
        x='Year', 
        y='Revenue',
        title=f"{company_name} Revenue Trend",
        labels={'Revenue': 'Revenue ($)'},
        color_discrete_sequence=['#1f77b4']
    )
    return fig

def plot_profitability_metrics(df, company_name):
    company_data = df[df['Company'] == company_name]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=company_data['Year'], y=company_data['Profit Margin (%)'], mode='lines+markers', name='Profit Margin (%)'))
    fig.add_trace(go.Scatter(x=company_data['Year'], y=company_data['ROE (%)'], mode='lines+markers', name='ROE (%)'))
    fig.add_trace(go.Scatter(x=company_data['Year'], y=company_data['ROA (%)'], mode='lines+markers', name='ROA (%)'))
    
    fig.update_layout(title=f"{company_name} Profitability Trends", xaxis_title="Year", yaxis_title="Percentage (%)")
    return fig

def plot_stock_price(hist_data, ticker):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=hist_data.index, y=hist_data['Close'], mode='lines', name='Close Price'))
    fig.update_layout(title=f"{ticker} Historical Stock Price", xaxis_title="Date", yaxis_title="Price in USD")
    return fig

def plot_forecast(historical_df, forecast_df, company_name):
    company_data = historical_df[historical_df['Company'] == company_name]
    
    fig = go.Figure()
    # Historical
    fig.add_trace(go.Scatter(x=company_data['Year'], y=company_data['Revenue'], mode='lines+markers', name='Historical Revenue'))
    # Forecast
    fig.add_trace(go.Scatter(
        x=forecast_df['Year'], 
        y=forecast_df['Forecasted Revenue'], 
        mode='lines+markers', 
        name='Forecasted Revenue', 
        line=dict(dash='dash', color='red')
    ))
    
    fig.update_layout(title=f"{company_name} Revenue Forecast", xaxis_title="Year", yaxis_title="Revenue ($)")
    return fig
