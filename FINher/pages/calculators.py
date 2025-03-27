import streamlit as st
from utils.calculator_functions import calculate_sip, calculate_emi, calculate_goal_progress

st.set_page_config(page_title="Financial Calculators", page_icon="🧮")

def main():
    st.markdown('<h1 class="main-header">Financial Calculators</h1>', unsafe_allow_html=True)
    
    calculator_type = st.radio(
        "Select Calculator",
        ["SIP Calculator", "EMI Calculator", "Goal Calculator"]
    )
    
    st.markdown('<div class="calculator-card">', unsafe_allow_html=True)
    
    if calculator_type == "SIP Calculator":
        st.subheader("SIP Calculator")
        monthly_investment = st.number_input("Monthly Investment (₹)", min_value=500, value=5000)
        expected_return = st.slider("Expected Annual Return (%)", min_value=1, max_value=30, value=12)
        time_period = st.slider("Time Period (Years)", min_value=1, max_value=30, value=10)
        
        if st.button("Calculate SIP"):
            result = calculate_sip(monthly_investment, expected_return, time_period)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Investment", f"₹{result['total_investment']:,.2f}")
            with col2:
                st.metric("Expected Returns", f"₹{result['returns']:,.2f}")
            with col3:
                st.metric("Future Value", f"₹{result['future_value']:,.2f}")
    
    elif calculator_type == "EMI Calculator":
        st.subheader("EMI Calculator")
        principal = st.number_input("Loan Amount (₹)", min_value=1000, value=100000)
        rate = st.slider("Interest Rate (%)", min_value=1, max_value=30, value=10)
        tenure = st.slider("Loan Tenure (Years)", min_value=1, max_value=30, value=5)
        
        if st.button("Calculate EMI"):
            result = calculate_emi(principal, rate, tenure)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Monthly EMI", f"₹{result['emi']:,.2f}")
            with col2:
                st.metric("Total Interest", f"₹{result['total_interest']:,.2f}")
            with col3:
                st.metric("Total Payment", f"₹{result['total_payment']:,.2f}")
    
    else:
        st.subheader("Goal Calculator")
        target_amount = st.number_input("Target Amount (₹)", min_value=1000, value=1000000)
        current_amount = st.number_input("Current Savings (₹)", min_value=0, value=100000)
        monthly_contribution = st.number_input("Monthly Contribution (₹)", min_value=500, value=10000)
        expected_return = st.slider("Expected Annual Return (%)", min_value=1, max_value=30, value=12)
        
        if st.button("Calculate Goal Progress"):
            result = calculate_goal_progress(current_amount, target_amount, monthly_contribution, expected_return)
            
            st.metric("Time Needed", f"{result['years_needed']} years")
            st.progress(result['progress_percentage']/100)
            st.write(f"Current Progress: {result['progress_percentage']}%")
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
