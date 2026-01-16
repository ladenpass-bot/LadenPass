import streamlit as st
import time
import pandas as pd
import datetime

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="LadenPass | Enterprise Logistics",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. PROFESSIONAL 'DARK MODE' STYLING ---
st.markdown("""
    <style>
    /* 1. Main Background - Deep Slate/Navy (Easy on eyes) */
    .stApp {
        background-color: #0f172a; 
    }
    
    /* 2. Text Colors - Off-White for readability */
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown {
        color: #e2e8f0 !important; 
        font-family: 'Segoe UI', sans-serif;
    }
    
    /* 3. Input Fields - Dark Grey with Light Text */
    .stTextInput>div>div>input, .stSelectbox>div>div>div, .stNumberInput>div>div>input {
        background-color: #1e293b; 
        color: white;
        border-color: #334155;
    }
    
    /* 4. Result Cards - Slightly Lighter than background */
    .result-card {
        background-color: #1e293b; /* Dark Blue-Grey */
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #3b82f6;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        margin-bottom: 20px;
        color: #f8fafc;
    }
    
    /* 5. Buttons - High Visibility Blue */
    .stButton>button {
        width: 100%;
        background-color: #3b82f6; /* Bright Blue */
        color: white;
        border: none;
        padding: 0.6rem 1rem;
        border-radius: 6px;
        font-weight: 600;
        font-size: 16px;
        transition: all 0.2s;
    }
    .stButton>button:hover {
        background-color: #2563eb;
