import streamlit as st
import pandas as pd
import datetime

# --- 1. ENTERPRISE PAGE CONFIG ---
st.set_page_config(
    page_title="LadenPass | Enterprise Platform",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. PROFESSIONAL STYLING SYSTEM (CSS) ---
st.markdown("""
    <style>
    /* --- GLOBAL THEME & BACKGROUND --- */
    .stApp {
        background-color: #0f172a; 
        /* Heavy Hauler Background Image */
        background-image: linear-gradient(rgba(15, 23, 42, 0.85), rgba(15, 23, 42, 0.9)), 
        url("https://images.unsplash.com/photo-1601584115197-04ecc0da31d7?q=80&w=2670&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* --- TYPOGRAPHY --- */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        font-weight: 600;
    }
    p, li, label, span, div {
        color: #e2e8f0 !important;
    }
    
    /* --- SIDEBAR BRANDING --- */
    [data-testid="stSidebar"] {
        background-color: #064e3b !important; /* Deep Enterprise Green */
        border-right: 1px solid rgba(255,255,255,0.1);
    }
    
    /* --- BIG LOGO BADGE (SIDEBAR) --- */
    .logo-box {
        background-color: white;
        padding: 20px; /* Increased padding */
        border-radius: 12px;
        margin-bottom: 30px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        text-align: center;
    }

    /* --- GLASSMORPHISM CARDS --- */
    .glass-card {
        background-color: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 12px;
        margin-bottom: 20px;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .glass-card:hover {
        transform: translateY(-2px);
        background-color: rgba(255, 255, 255, 0.12);
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }

    /* --- INPUT FIELDS --- */
    .stTextInput input, .stNumberInput input, .stSelectbox div[data-baseweb="select"] {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border: 1px solid #cbd5e1;
        border-radius: 6px;
    }
    div[role="listbox"] ul { background-color: white !important; }
    div[role="option"] { color: black !important; }

    /* --- BUTTONS --- */
    .stButton > button {
        background-color: #22c55e !important;
        color: white !important;
        border: none;
        border-radius: 6px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        width: 100%;
    }
    .stButton > button:hover { background-color: #16a34a !important; }
    
    /* HIDE DEFAULT ELEMENTS */
    #MainMenu, footer, header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    # --- LOGO SECTION ---
    # This is the primary brand anchor in the sidebar
    st.markdown('<div class="logo-box">', unsafe_allow_html=True)
    try:
        st.image("logo.jpg", use
