from fpdf import FPDF
import base64
import os

def create_markdown_report(summary_text, dataframe, company_name):
    md_content = f"# Financial Analysis Report: {company_name}\n\n"
    md_content += f"{summary_text}\n\n"
    md_content += "### Key Metrics Summary (Last 5 Years)\n"
    md_content += dataframe.to_markdown(index=False)
    return md_content

def create_pdf_report(summary_text, dataframe, company_name, output_path="report.pdf"):
    class PDF(FPDF):
        def header(self):
            self.set_font('Arial', 'B', 15)
            self.cell(0, 10, f'Financial Analysis Report: {company_name}', 0, 1, 'C')
            self.ln(10)

        def footer(self):
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    pdf = PDF()
    pdf.add_page()
    
    # Summary
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Executive Summary', 0, 1)
    pdf.set_font('Arial', '', 11)
    
    # Process text for encoding issues
    clean_text = summary_text.replace('### Executive Summary', '').replace('\n\n', '\n').strip()
    pdf.multi_cell(0, 8, clean_text.encode('latin-1', 'replace').decode('latin-1'))
    
    pdf.ln(10)
    
    # Basic Table (simple output for metrics)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Recent Performance Highlights', 0, 1)
    
    pdf.set_font('Arial', '', 9)
    try:
        # Simplify table for PDF to fit
        display_cols = ['Year', 'Revenue', 'Net Income', 'Profit Margin (%)', 'Current Ratio']
        available_cols = [col for col in display_cols if col in dataframe.columns]
        
        # Table Header
        for col in available_cols:
            pdf.cell(38, 10, col, 1)
        pdf.ln()
        
        # Table Data
        for _, row in dataframe.iterrows():
            for col in available_cols:
                val = row[col]
                formatted_val = f"{val:.2f}" if isinstance(val, (float, int)) else str(val)
                pdf.cell(38, 10, formatted_val, 1)
            pdf.ln()
    except Exception as e:
        pdf.multi_cell(0, 10, f"Could not render table: {str(e)}")

    pdf.output(output_path)
    return output_path

def get_pdf_download_link(pdf_path, filename="financial_report.pdf"):
    with open(pdf_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    href = f'<a href="data:application/pdf;base64,{base64_pdf}" download="{filename}">Download PDF Report</a>'
    return href
