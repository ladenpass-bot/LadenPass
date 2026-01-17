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
        st.markdown('<div class="glass-card"><h3>100%</h3><p>NHVR Compliance</p></div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="glass-card"><h3>24/7</h3><p>System Uptime</p></div>', unsafe_allow_html=True)

    # FEATURE CARDS
    st.markdown("### Core Capabilities")
    fc1, fc2, fc3 = st.columns(3)
    
    with fc1:
        st.markdown("""
        <div class="glass-card" style="height: 200px;">
            <h3 style="color:#4ade80 !important">⚡ Instant Feasibility</h3>
            <p>Real-time structural assessment of bridges and culverts across VIC & NSW networks.</p>
        </div>
        """, unsafe_allow_html=True)
    with fc2:
        st.markdown("""
        <div class="glass-card" style="height: 200px;">
            <h3 style="color:#60a5fa !important">🗺️ Dynamic Routing</h3>
            <p>Avoids height-restricted infrastructure and load-limited assets automatically.</p>
        </div>
        """, unsafe_allow_html=True)
    with fc3:
        st.markdown("""
        <div class="glass-card" style="height: 200px;">
            <h3 style="color:#f472b6 !important">📄 Permit Automation</h3>
            <p>Generates pre-filled NHVR permit applications ready for immediate submission.</p>
        </div>
        """, unsafe_allow_html=True)


elif menu == "Compliance Check":
    st.title("New Movement Assessment")
    
    # ASSESSMENT FORM
    with st.container():
        st.markdown("#### Vehicle Configuration")
        c1, c2, c3 = st.columns(3)
        with c1:
            ref = st.text_input("Job Reference ID", value="JOB-2026-X88")
            route = st.selectbox("Jurisdiction", ["Victoria (VIC)", "New South Wales (NSW)", "Queensland (QLD)"])
        with c2:
            gcm = st.number_input("Gross Mass (t)", 10.0, 250.0, 42.5)
            axles = st.number_input("Axle Count", 2, 20, 6)
        with c3:
            width = st.number_input("Width (m)", 2.0, 10.0, 2.5)
            height = st.number_input("Height (m)", 2.0, 8.0, 4.3)

    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("RUN COMPLIANCE ENGINE"):
        with st.spinner("Analyzing national network constraints..."):
            import time
            time.sleep(1) # Fake processing delay
            
            flags = []
            status = "APPROVED"
            color = "#22c55e" # Green
            
            if gcm > 42.5:
                flags.append(f"⚠️ GCM ({gcm}t) triggers Bridge Formula Tier 1 check")
                status = "CONDITIONAL"
                color = "#f59e0b" # Orange
            if width > 2.5:
                flags.append(f"⚠️ Width ({width}m) requires 'Oversize' signage & flags")
                status = "CONDITIONAL"
                color = "#f59e0b"
            if height > 4.6:
                flags.append(f"⛔ Height ({height}m) exceeds clearway max. Electrical asset check required.")
                status = "REFERRAL REQUIRED"
                color = "#ef4444" # Red
                
            # RESULT CARD
            if len(flags) == 0: flags.append("✅ Fully Compliant with General Access Notice")
            
            st.markdown(f"""
            <div style="background-color: white; border-radius: 10px; padding: 25px; border-left: 10px solid {color}; margin-top: 20px;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <h2 style="color: #0f172a !important; margin:0;">Assessment Status</h2>
                    <span style="background-color:{color}; color:white; padding: 5px 15px; border-radius: 20px; font-weight:bold;">{status}</span>
                </div>
                <hr style="border-top: 1px solid #e2e8f0; margin: 15px 0;">
                <h4 style="color: #0f172a !important;">Analysis Details:</h4>
                <ul style="color: #334155 !important;">
                    {''.join([f'<li style="color:#334155; margin-bottom:5px;">{f}</li>' for f in flags])}
                </ul>
                <div style="margin-top: 20px; text-align: right;">
                    <span style="color: #64748b !important; font-size: 0.9rem;">NHVR Gazette: v2026.1.4 | Fee Estimate: <b>$91.00</b></span>
                </div>
            </div>
            """, unsafe_allow_html=True)


elif menu == "Fleet Management":
    st.title("Fleet Assets")
    
    st.markdown("""
    <style>
    [data-testid="stDataFrame"] {
        background-color: white;
        padding: 10px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    data = {
        "Asset ID": ["PM-104", "PM-105", "TR-882", "TR-991"],
        "Registration": ["XJ-44-KL", "AB-22-ZZ", "TR-55-PL", "TR-11-QQ"],
        "Type": ["Prime Mover (6x4)", "Prime Mover (8x4)", "Low Loader (4 Rows)", "Dolly (2x8)"],
        "GVM Rating": ["26.5t", "32.0t", "45.0t", "18.0t"],
        "Status": ["Active", "Maintenance", "Active", "Active"]
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)
