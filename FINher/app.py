import streamlit as st
import pandas as pd
from PIL import Image
import os

# Page configuration
st.set_page_config(
    page_title="FinHer - Women's Financial Empowerment",
    page_icon="💰",
    layout="wide"
)

# Load custom CSS
with open('styles/custom.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def main():
    # Header
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown('<h1 class="main-header">Welcome to FinHer</h1>', unsafe_allow_html=True)
        st.write("Your journey to financial empowerment starts here!")

    # Dashboard Overview
    st.subheader("Your Financial Dashboard")
    
    # Quick Stats
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Monthly Savings", value="₹15,000", delta="↑ 2,000")
    with col2:
        st.metric(label="Investment Value", value="₹1,25,000", delta="↑ 12%")
    with col3:
        st.metric(label="Financial Goals", value="2/5 Completed")

    # Featured Educational Content
    st.subheader("Featured Learning Modules")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://images.unsplash.com/photo-1497633762265-9d179a990aa6", 
                 caption="Start Your Financial Journey")
        st.markdown("""
        ### Getting Started
        Learn the basics of financial planning and investment.
        - Budgeting basics
        - Investment fundamentals
        - Risk management
        """)
        
    with col2:
        st.image("https://images.unsplash.com/photo-1519452575417-564c1401ecc0",
                 caption="Advanced Topics")
        st.markdown("""
        ### Growing Your Wealth
        Take your financial knowledge to the next level.
        - Stock market basics
        - Retirement planning
        - Tax optimization
        """)

    # Quick Access Tools
    st.subheader("Quick Access Tools")
    tool_col1, tool_col2, tool_col3 = st.columns(3)
    
    with tool_col1:
        if st.button("📊 SIP Calculator"):
            st.switch_page("pages/2_Calculators.py")
    with tool_col2:
        if st.button("💰 Budget Tracker"):
            st.switch_page("pages/3_Budget_Tracker.py")
    with tool_col3:
        if st.button("📈 Investment Portfolio"):
            st.switch_page("pages/4_Investment_Portfolio.py")

if __name__ == "__main__":
    main()
