import streamlit as st
import pandas as pd

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="LadenPass | Automated Compliance",
    page_icon="🚛",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. THE VISIBILITY FIX (CSS) ---
st.markdown("""
    <style>
    /* 1. FORCE MAIN PAGE TO BE WHITE */
    .stApp {
        background-color: #ffffff !important;
    }
    
    /* 2. FORCE SIDEBAR TO BE WHITE */
    [data-testid="stSidebar"] {
        background-color: #f8fafc !important;
        border-right: 1px solid #e2e8f0;
    }

    /* 3. FORCE ALL TEXT TO BE DARK (Main + Sidebar) */
    h1, h2, h3, h4, h5, h6, p, li, span, div, label, .stMarkdown {
        color: #0f172a !important;
    }

    /* 4. FIX INPUT FIELDS (So you can see what you type) */
    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div>div {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border: 1px solid #cbd5e1;
    }
    
    /* 5. HIDE DEFAULT STREAMLIT MENU */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* 6. BUTTON STYLING */
    .stButton>button {
        width: 100%;
        background-color: #047857 !important; /* Green */
        color: white !important;
        border: none;
        padding: 0.6rem 1rem;
        border-radius: 8px;
    }
    .stButton>button:hover { background-color: #065f46 !important; }

    /* 7. CARD STYLING */
    .feature-card {
        background-color: #f1f5f9;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e2e8f0;
        text-align: center;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    # Looking for 'logo.jpeg' - ensure this matches your filename exactly
    st.image("https://raw.githubusercontent.com/ladenpass-bot/LadenPass/main/logo.jpeg", use_container_width=True)
    
    st.markdown("---")
    # This radio button text will now be dark and visible
    menu = st.radio("Navigation", ["🏠 Home", "🛠️ Start Assessment", "🚛 My Fleet"])
    st.markdown("---")
    st.caption("© 2026 LadenPass Australia")
    st.caption("Support: admin@ladenpass.com.au")

# --- 4. MAIN CONTENT ---

if menu == "🏠 Home":
    # HERO SECTION
    st.markdown("""
    <div style="text-align: center; padding: 40px 0;">
        <h1 style="font-size: 3rem;">Move Heavy Loads, <span style="color: #047857 !important;">Faster.</span></h1>
        <p style="font-size: 1.2rem; color: #475569 !important;">
            The automated compliance tool for Class 1 Heavy Vehicles. <br>
            Instant bridge checks. 100% Compliant.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # FEATURES
    c1, c2, c3 = st.columns
