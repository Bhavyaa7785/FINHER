import streamlit as st
import pandas as pd

st.set_page_config(page_title="Financial Education", page_icon="📚")

def main():
    st.markdown('<h1 class="main-header">Financial Education Hub</h1>', unsafe_allow_html=True)
    
    # Featured Course
    st.image("https://images.unsplash.com/photo-1503676260728-1c00da094a0b",
             caption="Financial Literacy Fundamentals")
    
    # Course Categories
    categories = st.tabs(["Basics", "Investing", "Tax Planning", "Insurance"])
    
    with categories[0]:
        st.markdown("""
        ### Financial Basics
        
        #### Budgeting 101
        Learn how to create and maintain a budget that works for you.
        
        #### Emergency Fund
        Understanding the importance of emergency funds and how to build one.
        
        #### Credit Score
        Master the basics of credit scores and how to maintain a good one.
        """)
        
    with categories[1]:
        st.markdown("""
        ### Investment Knowledge
        
        #### Stock Market Basics
        - Understanding market fundamentals
        - How to start investing
        - Risk management
        
        #### Mutual Funds
        - Types of mutual funds
        - SIP investment strategy
        - Fund selection criteria
        """)
        
    with categories[2]:
        st.markdown("""
        ### Tax Planning
        
        #### Tax Saving Instruments
        - PPF and EPF
        - ELSS Funds
        - Tax-saving FDs
        
        #### Income Tax Basics
        - Tax slabs and calculation
        - Deductions under 80C
        - Filing returns
        """)
        
    with categories[3]:
        st.markdown("""
        ### Insurance Planning
        
        #### Life Insurance
        - Term vs Traditional plans
        - Calculating coverage needs
        - Policy selection
        
        #### Health Insurance
        - Individual vs Family floater
        - Coverage optimization
        - Claim process
        """)
    
    # Progress Tracking
    st.subheader("Your Learning Progress")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="progress-card">', unsafe_allow_html=True)
        st.progress(65)
        st.write("65% of Basics Completed")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="progress-card">', unsafe_allow_html=True)
        st.progress(30)
        st.write("30% of Investment Module Completed")
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
