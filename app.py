import streamlit as st
import time
import pandas as pd
import datetime

# --- 1. PAGE CONFIGURATION (Must be first) ---
st.set_page_config(
    page_title="LadenPass | Enterprise Logistics",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. PROFESSIONAL STYLING (CSS) ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #f4f6f9;
    }
    /* Hide Streamlit Header/Footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Custom Header Styling */
    h1 {
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 700;
        color: #1e293b;
        font-size: 2.2rem;
    }
    h2, h3 {
        font-family: 'Helvetica Neue', sans-serif;
        color: #334155;
    }
    
    /* Card Styling for Results */
    .result-card {
