def generate_executive_summary(df, company_name):
    """
    Generates a brief analyst-style NLP summary of the company's financial state.
    """
    company_data = df[df['Company'] == company_name].sort_values(by='Year')
    
    if len(company_data) < 2:
        return "Insufficient data to generate a multi-year trend summary."
    
    latest_year = company_data.iloc[-1]
    prev_year = company_data.iloc[-2]
    
    rev_growth = ((latest_year['Revenue'] - prev_year['Revenue']) / prev_year['Revenue']) * 100
    profit_growth = ((latest_year['Net Income'] - prev_year['Net Income']) / prev_year['Net Income']) * 100
    
    summary = f"### Executive Summary for {company_name} ({int(latest_year['Year'])})\n\n"
    summary += f"In {int(latest_year['Year'])}, {company_name} generated a total revenue of ${latest_year['Revenue']:,.2f}, "
    summary += f"which represents a {'growth' if rev_growth > 0 else 'decline'} of {abs(rev_growth):.2f}% compared to {int(prev_year['Year'])}. "
    
    summary += f"Net income for the year stood at ${latest_year['Net Income']:,.2f}, marking a {'positive' if profit_growth > 0 else 'negative'} "
    summary += f"change of {abs(profit_growth):.2f}%.\n\n"
    
    if 'Profit Margin (%)' in company_data.columns:
         pm = latest_year['Profit Margin (%)']
         summary += f"The company achieved a profit margin of {pm:.2f}%. "
         if pm > 15:
             summary += "This indicates a strong ability to convert sales into actual profit. "
         elif pm > 5:
             summary += "This suggests a healthy, sustainable operational structure. "
         else:
             summary += "This indicates tight margins, suggesting high operating costs relative to revenue. "
             
    if 'Current Ratio' in company_data.columns:
        cr = latest_year['Current Ratio']
        summary += f"The current ratio is {cr:.2f}. "
        if cr >= 1.5:
            summary += "This shows robust short-term liquidity, meaning the company can comfortably cover its immediate liabilities. "
        elif cr >= 1.0:
            summary += "This shows adequate liquidity. "
        else:
            summary += "This highlights potential liquidity risks as current liabilities exceed current assets. "
            
    if 'Debt-to-Equity' in company_data.columns:
        de = latest_year['Debt-to-Equity']
        summary += f"Finally, the debt-to-equity ratio of {de:.2f} "
        if de > 2.0:
            summary += "suggests aggressive financing strategies and higher financial risk."
        elif de > 1.0:
            summary += "indicates moderate leverage."
        else:
            summary += "points to a conservative capital structure with low reliance on debt."
            
    return summary
