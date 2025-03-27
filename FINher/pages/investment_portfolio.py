import streamlit as st
import plotly.express as px
from datetime import datetime
from utils.data_manager import save_investment, get_investments

st.set_page_config(page_title="Investment Portfolio", page_icon="📈")

def main():
    st.markdown('<h1 class="main-header">Investment Portfolio</h1>', unsafe_allow_html=True)
    
    # Add New Investment
    with st.expander("Add New Investment"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Investment Name")
            amount = st.number_input("Amount (₹)", min_value=0.0)
        with col2:
            investment_type = st.selectbox("Type", [
                "Stocks", "Mutual Funds", "Fixed Deposit", "PPF", "Others"
            ])
            date = st.date_input("Date", datetime.now())
        
        if st.button("Add Investment"):
            save_investment(name, amount, investment_type, date)
            st.success("Investment added successfully!")
    
    # Portfolio Overview
    investments_df = get_investments()
    
    if not investments_df.empty:
        total_investment = investments_df['amount'].sum()
        st.metric("Total Portfolio Value", f"₹{total_investment:,.2f}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Portfolio Distribution
            fig = px.pie(
                investments_df,
                values='amount',
                names='type',
                title="Portfolio Distribution"
            )
            st.plotly_chart(fig)
        
        with col2:
            # Investment List
            st.subheader("Your Investments")
            for _, investment in investments_df.iterrows():
                st.markdown(f"""
                <div style="padding: 10px; border-bottom: 1px solid #eee;">
                    <h4>{investment['name']}</h4>
                    <p>₹{investment['amount']:,.2f}<br>
                    <small>{investment['type']} • {investment['date']}</small></p>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.info("No investments recorded yet!")
    
    # Investment Tips
    st.subheader("Investment Tips")
    st.markdown("""
    ### Diversification Strategy
    - Spread investments across different asset classes
    - Consider risk tolerance and time horizon
    - Regular portfolio rebalancing
    
    ### Risk Management
    - Start with low-risk investments
    - Gradually increase exposure to growth assets
    - Maintain emergency fund
    """)

if __name__ == "__main__":
    main()
