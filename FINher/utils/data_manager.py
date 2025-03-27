import pandas as pd
import json
import streamlit as st
from datetime import datetime

def save_expense(amount, category, date, description):
    """Save expense to session state"""
    if 'expenses' not in st.session_state:
        st.session_state.expenses = []
    
    expense = {
        'amount': amount,
        'category': category,
        'date': date.strftime('%Y-%m-%d'),
        'description': description
    }
    st.session_state.expenses.append(expense)

def get_expenses():
    """Get all expenses from session state"""
    if 'expenses' not in st.session_state:
        st.session_state.expenses = []
    return pd.DataFrame(st.session_state.expenses)

def save_investment(name, amount, type, date):
    """Save investment to session state"""
    if 'investments' not in st.session_state:
        st.session_state.investments = []
    
    investment = {
        'name': name,
        'amount': amount,
        'type': type,
        'date': date.strftime('%Y-%m-%d')
    }
    st.session_state.investments.append(investment)

def get_investments():
    """Get all investments from session state"""
    if 'investments' not in st.session_state:
        st.session_state.investments = []
    return pd.DataFrame(st.session_state.investments)

def calculate_budget_summary():
    """Calculate budget summary from expenses"""
    expenses_df = get_expenses()
    if expenses_df.empty:
        return {
            'total_expenses': 0,
            'by_category': {},
            'recent_transactions': []
        }
    
    total = expenses_df['amount'].sum()
    by_category = expenses_df.groupby('category')['amount'].sum().to_dict()
    recent = expenses_df.sort_values('date', ascending=False).head(5).to_dict('records')
    
    return {
        'total_expenses': total,
        'by_category': by_category,
        'recent_transactions': recent
    }
