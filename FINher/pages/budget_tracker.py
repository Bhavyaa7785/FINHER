import streamlit as st
import plotly.express as px
import sys
import os
from datetime import datetime
from fpdf import FPDF  # PDF Library

# Ensure the parent directory is in sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.data_manager import save_expense, get_expenses, calculate_budget_summary

st.set_page_config(page_title="Budget Tracker", page_icon="💰")

# Function to Generate PDF
def generate_pdf(expenses_df):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Expense Report", ln=True, align='C')
    pdf.ln(10)

    pdf.cell(40, 10, "Date", border=1)
    pdf.cell(50, 10, "Category", border=1)
    pdf.cell(40, 10, "Amount (INR)", border=1)
    pdf.cell(60, 10, "Description", border=1)
    pdf.ln()

    for index, row in expenses_df.iterrows():
        pdf.cell(40, 10, str(row['date']), border=1)
        pdf.cell(50, 10, row['category'], border=1)
        pdf.cell(40, 10, f"{row['amount']:.2f}", border=1)
        pdf.cell(60, 10, row['description'].encode('latin-1', 'replace').decode('latin-1'), border=1)
        pdf.ln()

    pdf_file = "expense_report.pdf"
    pdf.output(pdf_file, "F")
    return pdf_file


def main():
    st.markdown('<h1 class="main-header">Budget Tracker</h1>', unsafe_allow_html=True)
    
    # Add New Expense
    with st.expander("Add New Expense"):
        col1, col2 = st.columns(2)
        with col1:
            amount = st.number_input("Amount (₹)", min_value=0.0)
            category = st.selectbox("Category", [
                "Food", "Transportation", "Shopping", "Bills", "Entertainment", "Others"
            ])
        with col2:
            date = st.date_input("Date", datetime.now())
            description = st.text_input("Description")
        
        if st.button("Add Expense"):
            save_expense(amount, category, date, description)
            st.success("Expense added successfully!")
    
    # Budget Summary
    summary = calculate_budget_summary()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Expense Summary")
        st.metric("Total Expenses", f"₹{summary['total_expenses']:,.2f}")
        
        # Category-wise expenses
        if summary['by_category']:
            fig = px.pie(
                values=list(summary['by_category'].values()),
                names=list(summary['by_category'].keys()),
                title="Expenses by Category"
            )
            st.plotly_chart(fig)
    
    with col2:
        st.subheader("Recent Transactions")
        for transaction in summary['recent_transactions']:
            st.markdown(f"""
            <div style="padding: 10px; border-bottom: 1px solid #eee;">
                <h4>₹{transaction['amount']:,.2f}</h4>
                <p>{transaction['description']}<br>
                <small>{transaction['category']} • {transaction['date']}</small></p>
            </div>
            """, unsafe_allow_html=True)
    
    # Expense History
    st.subheader("Expense History")
    expenses_df = get_expenses()
    if not expenses_df.empty:
        st.dataframe(expenses_df)
        pdf_file = generate_pdf(expenses_df)
        with open(pdf_file, "rb") as file:
            st.download_button(
                label="📄 Download Expense Report as PDF",
                data=file,
                file_name="expense_report.pdf",
                mime="application/pdf"
            )
    else:
        st.info("No expenses recorded yet!")

if __name__ == "__main__":
    main()
