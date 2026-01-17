import streamlit as st
import pandas as pd
import datetime

# --- 1. ENTERPRISE PAGE CONFIG ---
st.set_page_config(
    page_title="LadenPass | Enterprise Logistics",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. PROFESSIONAL STYLING SYSTEM (CSS) ---
st.markdown("""
    <style>
    /* --- GLOBAL THEME & BACKGROUND --- */
    .stApp {
        /* Fallback color */
        background-color: #0f172a; 
        
        /* NEW IMAGE: Heavy Hauler / Big Rig on Open Road */
        background-image: linear-gradient(rgba(15, 23, 42, 0.85), rgba(15, 23, 42, 0.9)), 
        url("https://images.unsplash.com/photo-1601584115197-04ecc0da31d7?q=80&w=2670&auto=format&fit=crop");
        
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* --- TYPOGRAPHY (Strict White for Readability) --- */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        font-weight: 600;
    }
    p, li, label, span, div {
        color: #e2e8f0 !important; /* Soft white for ease of reading */
    }
    
    /* --- SIDEBAR BRANDING --- */
    [data-testid="stSidebar"] {
        background-color: #064e3b !important; /* Deep Enterprise Green */
        border-right: 1px solid rgba(255,255,255,0.1);
    }
    
    /* --- LOGO CONTAINER (The "Badge" Fix) --- */
    .logo-box {
        background-color: white;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
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

    /* --- INPUT FIELDS (High Contrast) --- */
    .stTextInput input, .stNumberInput input, .stSelectbox div[data-baseweb="select"] {
        background-color: #ffffff !important;
        color: #0f172a !important; /* Dark Blue Text */
        border: 1px solid #cbd5e1;
        border-radius: 6px;
    }
    /* Dropdown text fix */
    div[role="listbox"] ul {
        background-color: white !important;
    }
    div[role="option"] {
        color: black !important;
    }

    /* --- BUTTONS --- */
    .stButton > button {
        background-color: #22c55e !important;
        color: white !important;
        border: none;
        border-radius: 6px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        letter-spacing: 0.5px;
        width: 100%;
        transition: background-color 0.3s;
    }
    .stButton > button:hover {
        background-color: #16a34a !important;
    }
    
    /* --- HIDE DEFAULT ELEMENTS --- */
    #MainMenu, footer, header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    # PROFESSIONAL LOGO BADGE
    st.markdown('<div class="logo-box">', unsafe_allow_html=True)
    try:
        st.image("logo.jpg", use_container_width=True)
    except:
        st.markdown("<h2 style='color:#064e3b !important; margin:0;'>LadenPass</h2>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("### Platform")
    menu = st.radio("", ["Dashboard", "Compliance Check", "Fleet Management"], label_visibility="collapsed")
    
    st.markdown("---")
    st.info("🟢 System Operational")
    st.markdown("<div style='text-align: center; font-size: 0.8rem; opacity: 0.7;'>© 2026 LadenPass Enterprise</div>", unsafe_allow_html=True)


# --- 4. MAIN CONTENT ---

if menu == "Dashboard":
    # HERO SECTION
    st.markdown("""
    <div style="text-align: center; padding: 40px 20px;">
        <h1 style="font-size: 3rem; margin-bottom: 10px;">Enterprise Heavy Haulage</h1>
        <p style="font-size: 1.2rem; max-width: 600px; margin: 0 auto; opacity: 0.9;">
            Automated network access and compliance for Class 1 Heavy Vehicles. 
            Reduce permit turnaround from 28 days to <span style="color:#4ade80; font-weight:bold;">seconds</span>.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

    # METRICS ROW
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown('<div class="glass-card"><h3>98%</h3><p>Auto-Approval Rate</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="glass-card"><h3>< 2s</h3><p>Calculation Time</p></div>', unsafe_allow_html=True)
    with c3:
        st.
