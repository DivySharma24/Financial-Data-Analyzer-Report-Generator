import streamlit as st
import pandas as pd
import os

from src.data_ingestion import load_data, fetch_market_data, get_company_info
from src.financial_ratios import calculate_ratios
from src.trend_analysis import calculate_trends
from src.forecasting import forecast_revenue
from src.risk_metrics import calculate_sharpe_ratio, calculate_volatility
from src.visualization import plot_revenue_trend, plot_profitability_metrics, plot_stock_price, plot_forecast
from src.nlp_summary import generate_executive_summary
from src.export_report import create_markdown_report, create_pdf_report, get_pdf_download_link

# Set Page Config
st.set_page_config(page_title="Financial Data Analyzer", layout="wide")

st.title("📈 Financial Data Analyzer & Report Generator")
st.markdown("Upload corporate financial statements, calculate key ratios, visualize trends, and export comprehensive reports.")

# Sidebar for inputs
st.sidebar.header("Data Sources")

# Option 1: File Upload
st.sidebar.subheader("1. Upload Financial Data")
uploaded_file = st.sidebar.file_uploader("Upload CSV/Excel (Balance Sheet, Income, Cash Flow)", type=["csv", "xlsx"])

# Option 2: Live Market Data
st.sidebar.subheader("2. Live Market Data")
ticker_input = st.sidebar.text_input("Enter Ticker Symbol (e.g., AAPL)")

# Initialize state
if 'financial_df' not in st.session_state:
    st.session_state['financial_df'] = None

if uploaded_file is not None:
    try:
        df = load_data(uploaded_file)
        
        # Calculate Ratios and Trends
        df = calculate_ratios(df)
        df = calculate_trends(df)
        st.session_state['financial_df'] = df
        
        st.sidebar.success("Data uploaded and processed successfully!")
    except Exception as e:
        st.sidebar.error(f"Error processing file: {str(e)}")
        
        
if st.session_state['financial_df'] is not None:
    df = st.session_state['financial_df']
    companies = df['Company'].unique()
    selected_company = st.sidebar.selectbox("Select Company to Analyze", companies)
    
    # Tabs for navigation
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview & Ratios", "📈 Forecasting", "🛡️ Risk Metrics", "📄 Report Generation"])
    
    # --- TAB 1: Overview & Ratios ---
    with tab1:
        st.subheader(f"{selected_company} Financial Overview")
        company_data = df[df['Company'] == selected_company]
        
        # Display Raw Data
        with st.expander("View Processed Data Table"):
            st.dataframe(company_data)
            
        # Display Metrics
        col1, col2 = st.columns(2)
        with col1:
             st.plotly_chart(plot_revenue_trend(df, selected_company), use_container_width=True)
        with col2:
             st.plotly_chart(plot_profitability_metrics(df, selected_company), use_container_width=True)
             
    # --- TAB 2: Forecasting ---
    with tab2:
        st.subheader("Revenue Forecasting (Linear Regression)")
        forecast_years = st.slider("Years to Forecast", 1, 5, 3)
        forecast_df = forecast_revenue(df, selected_company, future_years=forecast_years)
        
        if forecast_df is not None:
            st.plotly_chart(plot_forecast(df, forecast_df, selected_company), use_container_width=True)
            with st.expander("View Forecast Data"):
                st.dataframe(forecast_df)
        else:
            st.warning("Not enough historical data to generate a reliable forecast.")

    # --- TAB 3: Risk Metrics (Requires Market Data) ---
    with tab3:
        st.subheader("Market Risk Analysis")
        if ticker_input:
            try:
                hist_data = fetch_market_data(ticker_input)
                info = get_company_info(ticker_input)
                
                if info and 'longBusinessSummary' in info:
                    with st.expander("Company Summary"):
                        st.write(info['longBusinessSummary'])
                
                volatility = calculate_volatility(hist_data)
                sharpe = calculate_sharpe_ratio(hist_data)
                
                # Metrics Display
                r1, r2 = st.columns(2)
                r1.metric(label="Annualized Volatility", value=f"{volatility * 100:.2f}%")
                r2.metric(label="Sharpe Ratio", value=f"{sharpe:.2f}")
                
                st.plotly_chart(plot_stock_price(hist_data, ticker_input), use_container_width=True)
                
            except Exception as e:
                st.error(f"Error fetching data for {ticker_input}: {str(e)}")
        else:
            st.info("Please enter a Ticker Symbol in the sidebar to view live market risk metrics (Volatility & Sharpe Ratio).")

    # --- TAB 4: Report Generation ---
    with tab4:
        st.subheader("Final Analyst Report")
        summary = generate_executive_summary(df, selected_company)
        
        st.markdown(summary)
        
        st.markdown("---")
        st.write("**Export Options**")
        
        # Generation Logic
        if st.button("Generate PDF Report"):
             pdf_path = f"{selected_company}_report.pdf"
             create_pdf_report(summary, company_data, selected_company, pdf_path)
             st.markdown(get_pdf_download_link(pdf_path), unsafe_allow_html=True)
             
        # Markdown download
        md_text = create_markdown_report(summary, company_data, selected_company)
        st.download_button(
            label="Download Markdown Report",
            data=md_text,
            file_name=f"{selected_company}_report.md",
            mime="text/markdown"
        )

else:
    st.info("👈 Please upload a CSV/Excel file in the sidebar to begin analysis. Use `data/sample_financials.csv` to test.")
