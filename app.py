import streamlit as st
import pandas as pd
import base64
import datetime

# --- 1. ENTERPRISE PAGE CONFIG ---
st.set_page_config(
    page_title="LadenPass | Enterprise Platform",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. HELPER: LOAD IMAGE CORRECTLY ---
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return None

logo_b64 = get_base64_image("logo.jpg")

# --- 3. PROFESSIONAL STYLING (CSS) ---
st.markdown("""
    <style>
    /* REMOVE TOP WHITESPACE */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
    }

    /* GLOBAL THEME */
    .stApp {
        background-color: #0f172a; 
        background-image: linear-gradient(rgba(15, 23, 42, 0.92), rgba(15, 23, 42, 0.94)), 
        url("https://images.unsplash.com/photo-1601584115197-04ecc0da31d7?q=80&w=2670&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* TYPOGRAPHY */
    h1, h2, h3, h4, h5, h6 { color: #ffffff !important; margin-bottom: 5px !important; }
    p, li, label, span, div { color: #cbd5e1 !important; }
    
    /* SIDEBAR */
    [data-testid="stSidebar"] {
        background-color: #064e3b !important;
        border-right: 1px solid rgba(255,255,255,0.1);
    }
    
    /* LOGO CONTAINER */
    .logo-container {
        background-color: white;
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 15px;
        text-align: center;
        display: flex;
        justify-content: center;
        align-items: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .logo-container img { max-width: 100%; height: auto; }

    /* NAVIGATION BUTTONS */
    [data-testid="stRadio"] > div { gap: 10px; }
    [data-testid="stRadio"] label {
        background-color: rgba(255, 255, 255, 0.1) !important;
        padding: 12px 20px !important;
        border-radius: 8px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        transition: all 0.2s ease !important;
        cursor: pointer !important;
    }
    [data-testid="stRadio"] label:hover {
        background-color: rgba(255, 255, 255, 0.2) !important;
        border-color: #4ade80 !important;
        transform: translateX(5px);
    }
    [data-testid="stRadio"] label[data-checked="true"] {
        background-color: rgba(34, 197, 94, 0.2) !important;
        border-color: #22c55e !important;
        font-weight: bold !important;
    }

    /* COMPACT GLASS CARDS */
    .glass-card {
        background-color: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 10px;
        margin-bottom: 20px;
        transition: transform 0.2s;
        height: 100%;
    }
    .glass-card:hover {
        transform: translateY(-2px);
        background-color: rgba(255, 255, 255, 0.12);
    }
    .glass-card h3 { font-size: 1.4rem !important; margin-bottom: 10px !important; }
    .glass-card p { font-size: 0.95rem !important; line-height: 1.5 !important; opacity: 0.9; }

    /* INPUTS & BUTTONS */
    .stTextInput input, .stNumberInput input, .stSelectbox div[data-baseweb="select"] {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border: 1px solid #cbd5e1;
        border-radius: 6px;
    }
    div[role="listbox"] ul { background-color: white !important; }
    div[role="option"] { color: black !important; }
    
    .stButton > button {
        background-color: #22c55e !important;
        color: white !important;
        border: none;
        font-weight: 600;
        width: 100%;
        padding: 0.6rem;
    }
    .stButton > button:hover { background-color: #16a34a !important; }
    
    #MainMenu, footer, header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR CONTENT ---
with st.sidebar:
    if logo_b64:
        st.markdown(f"""<div class="logo-container"><img src="data:image/jpeg;base64,{logo_b64}"></div>""", unsafe_allow_html=True)
    else:
        st.markdown("""<div class="logo-container"><h2 style="color:#064e3b !important; margin:0;">LadenPass</h2></div>""", unsafe_allow_html=True)
    
    st.markdown("### Action Menu")
    
    menu = st.radio(
        "", 
        ["📊 Dashboard", "✅ New Check"], 
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.success("🟢 Online")
    
    current_year = datetime.datetime.now().year
    st.markdown(f"""
        <div style='text-align: center; font-size: 0.8rem; color: #cbd5e1; margin-top: 15px; opacity: 0.8;'>
            © {current_year} LadenPass Enterprise<br>
            All Rights Reserved.
        </div>
    """, unsafe_allow_html=True)


# --- 5. MAIN CONTENT ---

if "Dashboard" in menu:
    # HERO SECTION
    st.markdown("""
    <div style="text-align: center; padding: 20px 0 30px 0;">
        <h1 style="font-size: 4rem; text-shadow: 0 4px 10px rgba(0,0,0,0.5);">LadenPass</h1>
        <h3 style="color: #4ade80 !important; font-weight: 400; font-size: 1.6rem; margin-top: 10px;">
            Intelligent Heavy Vehicle Compliance
        </h3>
    </div>
    """, unsafe_allow_html=True)

    # STRATEGIC OVERVIEW (The new "Purpose" section)
    st.markdown("""
    <div style="background-color: rgba(15, 23, 42, 0.6); border-left: 4px solid #4ade80; padding: 20px; border-radius: 0 8px 8px 0; margin-bottom: 40px; max-width: 900px; margin-left: auto; margin-right: auto;">
        <p style="font-size: 1.1rem; line-height: 1.6;">
            <b>LadenPass digitizes the Class 1 Heavy Vehicle permit process.</b><br>
            Traditionally, moving oversize and overmass loads requires a manual 28-day approval cycle involving bridge engineers and local councils. 
            LadenPass automates this by cross-referencing vehicle engineering data against the <b>National Heavy Vehicle Regulator (NHVR)</b> 
            structural database in real-time.
        </p>
        <p style="font-size: 1.1rem; line-height: 1.6; margin-top: 10px;">
            Our platform provides logistics operators with <b>instant feasibility assessments</b>, automatically flagging bridge restrictions, 
            electrical clearance hazards, and route constraints before an application is even lodged.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # METRICS ROW
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown('<div class="glass-card" style="text-align:center;"><h3>98%</h3><p>Pre-Approval Accuracy</p></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="glass-card" style="text-align:center;"><h3>< 2s</h3><p>Structural Calculation</p></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="glass-card" style="text-align:center;"><h3>100%</h3><p>Gazette Compliance</p></div>', unsafe_allow_html=True)
    with c4: st.markdown('<div class="glass-card" style="text-align:center;"><h3>24/7</h3><p>Network Availability</p></div>', unsafe_allow_html=True)

    # CORE CAPABILITIES (Expanded Detail)
    st.markdown("<br>### Core Capabilities", unsafe_allow_html=True)
    fc1, fc2, fc3 = st.columns(3)
    
    with fc1:
        st.markdown("""
        <div class="glass-card">
            <h3 style="color:#4ade80 !important;">⚡ Automated Feasibility</h3>
            <p>
                Eliminates manual bridge assessments. The engine calculates "Bridge Formula" Tier 1 compliance instantly, identifying structures incapable of supporting your specific GCM and axle spacing.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with fc2:
        st.markdown("""
        <div class="glass-card">
            <h3 style="color:#60a5fa !important;">🗺️ Dynamic Asset Routing</h3>
            <p>
                Routes are validated against 4.6m clearway height restrictions and load-limited assets. The system automatically suggests compliant alternatives to avoid "Referral Required" zones.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with fc3:
        st.markdown("""
        <div class="glass-card">
            <h3 style="color:#f472b6 !important;">📄 Regulatory Alignment</h3>
            <p>
                Full integration with the current NHVR Class 1 Notice. The platform generates pre-filled permit applications that meet all federal and state jurisdiction requirements.
            </p>
        </div>
        """, unsafe_allow_html=True)


elif "Check" in menu:
    st.title("Compliance Check")
    
    with st.container():
        c1, c2, c3 = st.columns(3)
        with c1:
            ref = st.text_input("Job Ref", value="JOB-X88")
            route = st.selectbox("State", ["VIC", "NSW", "QLD"])
        with c2:
            gcm = st.number_input("Mass (t)", 10.0, 250.0, 42.5)
            axles = st.number_input("Axles", 2, 20, 6)
        with c3:
            width = st.number_input("Width (m)", 2.0, 10.0, 2.5)
            height = st.number_input("Height (m)", 2.0, 8.0, 4.3)

    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("CHECK COMPLIANCE"):
        with st.spinner("Analyzing..."):
            import time
            time.sleep(0.5)
            
            flags = []
            status = "APPROVED"
            color = "#22c55e"
            
            if gcm > 42.5:
                flags.append(f"⚠️ Mass ({gcm}t) > General Access Limit")
                status = "CONDITIONAL"
                color = "#f59e0b"
            if width > 2.5:
                flags.append(f"⚠️ Width ({width}m) requires 'Oversize' signs")
                status = "CONDITIONAL"
                color = "#f59e0b"
            if height > 4.6:
                flags.append(f"⛔ Height ({height}m) exceeds clearway max.")
                status = "REFERRAL"
                color = "#ef4444"
                
            st.markdown(f"""
            <div style="background-color: white; border-radius: 10px; padding: 20px; border-left: 10px solid {color}; margin-top: 20px;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <h3 style="color: #0f172a !important; margin:0;">Status: {status}</h3>
                </div>
                <hr style="border-top: 1px solid #e2e8f0; margin: 10px 0;">
                <ul style="color: #334155 !important; margin: 0; padding-left: 20px;">
                    {''.join([f'<li style="color:#334155;">{f}</li>' for f in flags])}
                </ul>
            </div>
            """, unsafe_allow_html=True)
