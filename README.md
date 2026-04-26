# Financial Data Analyzer & Report Generator

## Project Overview
The Financial Data Analyzer is a full-stack Python application built for corporate finance and investment analysis. It allows users to upload financial statements (like Balance Sheets, Income Statements, and Cash Flow Statements), computes critical financial ratios, conducts year-over-year trend analysis, and models future revenues using linear regression forecasting.

This tool acts as an automated equity analyst, generating rich data visualizations and compiling findings into downloadable natural-language PDF/Markdown reports. By integrating live stock market data via Yahoo Finance, it also calculates essential risk metrics (Volatility and Sharpe Ratio).

## Key Features
1. **Automated Ratio Calculation:** Dynamically calculates Profit Margin, ROE, ROA, Current Ratio, and Debt-to-Equity.
2. **Trend Analysis:** Computes YoY revenue and net income growth.
3. **Data Visualization:** Interactive Plotly charts for tracking profitability and historical revenue.
4. **Machine Learning Forecasting:** Simple predictive modeling using Scikit-learn's Linear Regression to forecast future financial performance.
5. **Live Market Integration:** Pulls historical stock data from Yahoo Finance to plot stock prices and evaluate market risk.
6. **Automated Report Generation:** Rule-based NLP constructs an executive summary; exports to PDF and Markdown formatted reports.

## Setup Instructions

### 1. Prerequisites
Ensure you have Python 3.8+ installed on your system.

### 2. Installation
Navigate to the root directory of this project and run the following command to install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3. Running the App
Start the Streamlit development server by running:
```bash
streamlit run app.py
```

### 4. Sample Data
Use the `data/sample_financials.csv` file to test the core features of the tool. Upload it via the sidebar in the Streamlit application. Enter tickers like `AAPL` or `MSFT` to test the live market data integration.

## Modular Structure
- `app.py`: The core Streamlit interface mapping user interactions.
- `src/data_ingestion.py`: Cleansing logic for CSV/Excel uploads and YFinance API responses.
- `src/financial_ratios.py` & `src/trend_analysis.py`: Pandas vector operations for quick transformations.
- `src/forecasting.py`: Incorporates the ML linear projection.
- `src/visualization.py`: Standardized graphical objects using Plotly.
- `src/nlp_summary.py` & `src/export_report.py`: Translates raw pandas dataframes into digestible intelligence reports.

## Scalability Considerations
- **Streamlit Caching (`@st.cache_data`):** Minimizes repeated I/O requests when loading the dataset or parsing market history, greatly improving speed for large tables.
- **Pandas Vectorization:** Functions compute ratios across thousands of rows concurrently rather than looping.
# Financial-Data-Analyzer-Report-Generator
