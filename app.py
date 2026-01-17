import streamlit as st
import datetime

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="LadenPass | Automated Compliance",
    page_icon="🚛",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. PROFESSIONAL STYLING (CSS) ---
# This section handles the Background Image, Fonts, and Colors
st.markdown("""
    <style>
    /* --- MAIN BACKGROUND --- */
    /* We add a dark overlay (0.7 opacity) so the white text pops against the photo */
    .stApp {
        background-image: linear-gradient(rgba(15, 23, 42, 0.75), rgba(15, 23, 42, 0.75)), 
        url("http://googleusercontent.com/image_collection/image_retrieval/14116698006579212757_0");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* --- TYPOGRAPHY --- */
    /* Force main headings and text to be White */
    .main h1, .main h2, .main h3, .main h4, .main p, .main li, .main span, .main label {
        color: #ffffff !important;
    }
    
    /* --- SIDEBAR STYLING --- */
    [data-testid="stSidebar"] {
        background-color: #0e3b28 !important; /* LadenPass Green */
        border-right: 1px solid #064e3b;
    }
    /* Force Sidebar text to be White */
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }

    /* --- GLASSMORPHISM CARDS (HOME PAGE) --- */
    .feature-card {
        background-color: rgba(255, 255, 255, 0.1); /* 10% White Transparency */
        padding: 25px;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        text-align: center;
        margin-bottom: 20px;
        backdrop-filter: blur(8px); /* Blurs the photo behind the box */
        transition: transform 0.2s;
    }
    .feature-card:hover {
        transform: translateY(-5px);
        background-color: rgba(255, 255, 255, 0.15);
    }
    .feature-card h3 {
        color: #4ade80 !important; /* Bright Green Title */
        font-weight: 700;
        margin-top: 0;
    }
    .feature-card p {
        color: #e2e8f0 !important; /* Light Grey Text */
        font-size: 1rem;
    }

    /* --- INPUT FIELDS (CRITICAL FOR USABILITY) --- */
    /* We force inputs to be White with Black text so they are easy to read */
    .stTextInput>div>div>input, 
    .stNumberInput>div>div>input, 
    .stSelectbox>div>div>div {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border-radius: 6px;
        border: none;
    }
    /* Label colors above inputs */
    .stTextInput label, .stNumberInput label, .stSelectbox label {
        color: #ffffff !important;
        font-weight: 600;
    }
    
    /* --- BUTTONS --- */
    .stButton>button {
        width: 100%;
        background-color: #22c55e !important; /* Brand Green */
        color: white !important;
        border: none;
        padding: 0.7rem 1rem;
        border-radius: 8px;
        font-weight: bold;
        font-size: 1.1rem;
        text-shadow: 0 1px 2px rgba(0,0,0,0.2);
        margin-top: 10px;
    }
    .stButton>button:hover { 
        background-color: #16a34a !important; 
        box-shadow: 0 4px 12px rgba(34, 197, 94, 0.4);
    }

    /* --- HIDE DEFAULT STREAMLIT MENU --- */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    # FAIL-SAFE LOGO LOGIC
    # Tries to load 'logo.jpg'. If missing, renders a text logo.
    try:
        st.image("logo.jpg", use_container_width=True)
    except:
        st.markdown("""
        <div style="padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.2); margin-bottom: 20px;">
            <h2 style="color: white; margin:0; font-weight: 800;">LadenPass</h2>
            <p style="color: #86efac; margin:0; font-size: 0.8rem;">Enterprise Logistics</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### Navigation")
    menu = st.radio("", ["🏠 Home", "🛠️ Start Assessment", "🚛 My Fleet"], label_visibility="collapsed")
    
    st.markdown("---")
    current_year = datetime.datetime.now().year
    st.caption(f"© {current_year} LadenPass Australia")
    st.caption("Support: admin@ladenpass.com.
