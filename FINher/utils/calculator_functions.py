import numpy as np

def calculate_sip(monthly_investment, expected_return, time_period):
    """
    Calculate SIP returns
    """
    r = expected_return/1200  # Monthly rate
    n = time_period * 12     # Total months
    
    future_value = monthly_investment * ((1 + r) * ((1 + r)**n - 1)/r)
    total_investment = monthly_investment * n
    returns = future_value - total_investment
    
    return {
        'future_value': round(future_value, 2),
        'total_investment': round(total_investment, 2),
        'returns': round(returns, 2)
    }

def calculate_emi(principal, rate, tenure):
    """
    Calculate EMI for a loan
    """
    r = rate/(12*100)  # Monthly rate
    n = tenure * 12    # Total months
    
    emi = principal * r * ((1+r)**n)/((1+r)**n - 1)
    total_payment = emi * n
    total_interest = total_payment - principal
    
    return {
        'emi': round(emi, 2),
        'total_payment': round(total_payment, 2),
        'total_interest': round(total_interest, 2)
    }

def calculate_goal_progress(current_amount, target_amount, monthly_contribution, expected_return):
    """
    Calculate time and progress towards financial goal
    """
    r = expected_return/1200
    remaining = target_amount - current_amount
    
    # Calculate months needed
    months = np.log(1 + (remaining * r)/monthly_contribution) / np.log(1 + r)
    years = months/12
    
    progress_percentage = (current_amount/target_amount) * 100
    
    return {
        'years_needed': round(years, 1),
        'progress_percentage': round(progress_percentage, 1)
    }
