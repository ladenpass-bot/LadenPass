import streamlit as st
import pandas as pd
import base64

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
    /* --- GLOBAL THEME --- */
    .stApp {
        background-color: #0f172a; 
        background-image: linear-gradient(rgba(15, 23, 42, 0.9), rgba(15, 23, 42, 0.9)), 
        url("https://images.unsplash.com/photo-1601584115197-04ecc0da31d7?q=80&w=2670&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* --- TYPOGRAPHY --- */
    h1, h2, h3, h4, h5, h6 { color: #ffffff !important; }
    p, li, label, span, div { color: #e2e8f0 !important; }
    
    /* --- SIDEBAR --- */
    [data-testid="stSidebar"] {
        background-color: #064e3b !important;
        border-right: 1px solid rgba(255,255,255,0.1);
    }
    
    /* --- LOGO CONTAINER --- */
    .logo-container {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
        text-align: center;
        display: flex;
        justify-content: center;
        align-items: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .logo-container img {
        max-width: 100%;
        height: auto;
    }

    /* --- NAVIGATION TRANSFORMATION (The "Big Button" Fix) --- */
    /* This targets the radio button container */
    [data-testid="stRadio"] > div {
        gap: 15px; /* Adds space between buttons */
    }

    /* This targets the individual radio options to look like Cards */
    [data-testid="stRadio"] label {
        background-color: rgba(255, 255, 255, 0.1) !important;
        padding: 15px 20px !important; /* Make them fat and clickable */
        border-radius: 10px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        transition: all 0.3s ease !important;
        margin-bottom: 5px !important;
        cursor: pointer !important;
    }
    
    /* Hover Effect */
    [data-testid="stRadio"] label:hover {
        background-color: rgba(255, 255, 255, 0.2) !important;
        border-color: #4ade80 !important; /* Green border on hover */
        transform: translateX(5px); /* Slight nudge to the right */
    }

    /* Active/Selected State (Make the text bold/green) */
    [data-testid="stRadio"] label[data-checked="true"] {
        background-color: rgba(34, 197, 94, 0.2) !important; /* Green tint */
        border-color: #22c55e !important;
        font-weight: bold !important;
    }
    /* Increase font size of the options */
    [data-testid="stRadio"] p {
        font-size: 1.1rem !important;
        font-weight: 500 !important;
    }

    /* --- GLASS CARDS --- */
    .glass-card {
        background-color: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 12px;
        margin-bottom: 20px;
        transition: transform 0.2s;
    }
    .glass-card:hover {
        transform: translateY(-2px);
        background-color: rgba(255, 255, 255, 0.12);
    }

    /* --- INPUTS & BUTTONS --- */
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
        padding: 0.8rem;
        font-size: 1.1rem;
    }
    .stButton > button:hover { background-color: #16a34a !important; }
    
    #MainMenu, footer, header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR CONTENT ---
with st.sidebar:
    # 1. LOGO
    if logo_b64:
        st.markdown(f"""<div class="logo-container"><img src="data:image/jpeg;base64,{logo_b64}"></div>""", unsafe_allow_html=True)
    else:
        st.markdown("""<div class="logo-container"><h2 style="color:#064e3b !important; margin:0;">LadenPass</h2></div>""", unsafe_allow_html=True)
    
    # 2. GUIDING HEADER
    st.markdown("### Select Action")
    st.markdown("Please choose a module below to begin.")
    
    # 3. BIG NAVIGATION BUTTONS
    # We use emojis and longer text to make them feel like "options"
    menu = st.radio(
        "", 
        [
            "📊 Operations Dashboard", 
            "✅ Start Compliance Check", 
            "🚛 Manage Fleet Assets"
        ], 
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.success("🟢 System Online")
    st.markdown("<div style='font-size: 0.8rem; opacity: 0.7;'>© 2026 LadenPass Enterprise</div>", unsafe_allow_html=True)


# --- 5. MAIN CONTENT ---

# MAPPING SELECTION TO CONTENT
# Because we changed the names in the menu, we map them back to logic
if "Dashboard" in menu:
    # HERO
    st.markdown("""
    <div style="text-align: center; padding: 50px 20px 30px 20px;">
        <h1 style="font-size: 4.5rem; margin-bottom: 0; text-shadow: 0 4px 10px rgba(0,0,0,0.5);">
            LadenPass
        </h1>
        <h3 style="font-size: 1.8rem; color: #4ade80 !important; margin-top: 10px; font-weight: 400;">
            Enterprise Heavy Haulage
        </h3>
        <p style="font-size: 1.2rem; max-width: 700px; margin: 20px auto; opacity: 0.9;">
            The automated network access platform for Class 1 Heavy Vehicles. 
            <br>Permit compliance in seconds, not days.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

    # METRICS
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown('<div class="glass-card"><h3>98%</h3><p>Auto-Approval Rate</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="glass-card"><h3>< 2s</h3><p>Calculation Time</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="glass-card"><h3>100%</h3><p>NHVR Compliance</p></div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="glass-card"><h3>24/7</h3><p>System Uptime</p></div>', unsafe_allow_html=True)

    # CAPABILITIES
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


elif "Compliance" in menu:
    st.title("New Movement Assessment")
    
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
            time.sleep(1)
            
            flags = []
            status = "APPROVED"
            color = "#22c55e"
            
            if gcm > 42.5:
                flags.append(f"⚠️ GCM ({gcm}t) triggers Bridge Formula Tier 1 check")
                status = "CONDITIONAL"
                color = "#f59e0b"
            if width > 2.5:
                flags.append(f"⚠️ Width ({width}m) requires 'Oversize' signage & flags")
                status = "CONDITIONAL"
                color = "#f59e0b"
            if height > 4.6:
                flags.append(f"⛔ Height ({height}m) exceeds clearway max. Electrical asset check required.")
                status = "REFERRAL REQUIRED"
                color = "#ef4444"
                
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


elif "Fleet" in menu:
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
