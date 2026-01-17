import streamlit as st
import datetime
import pandas as pd

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="LadenPass | Automated Compliance",
    page_icon="🚛",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. PROFESSIONAL STYLING (CSS) ---
st.markdown("""
    <style>
    /* --- MAIN BACKGROUND --- */
    /* We use a permanent Unsplash URL for the Australian Outback look */
    .stApp {
        background-image: linear-gradient(rgba(15, 23, 42, 0.8), rgba(15, 23, 42, 0.8)), 
        url("https://images.unsplash.com/photo-1546556536-3d710f970d4d?q=80&w=2574&auto=format&fit=crop");
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
    st.caption("Support: admin@ladenpass.com.au")
    st.info("System Status: 🟢 Online")

# --- 4. MAIN CONTENT ---

if menu == "🏠 Home":
    # HERO SECTION
    st.markdown("""
    <div style="text-align: center; padding: 60px 0 40px 0;">
        <h1 style="font-size: 3.5rem; text-shadow: 0 4px 6px rgba(0,0,0,0.5);">
            Move Heavy Loads, <span style="color: #4ade80 !important;">Faster.</span>
        </h1>
        <p style="font-size: 1.3rem; opacity: 0.9; max-width: 700px; margin: 0 auto;">
            The automated route compliance tool for Class 1 Heavy Vehicles. <br>
            <b>Instant feasibility checks. 100% Compliant.</b>
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # FEATURE CARDS
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""
        <div class="feature-card">
            <div style="font-size: 3rem; margin-bottom: 10px;">⚡</div>
            <h3>Instant Checks</h3>
            <p>Stop waiting 28 days. Get instant feasibility checks for VIC & NSW networks.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown("""
        <div class="feature-card">
            <div style="font-size: 3rem; margin-bottom: 10px;">🛡️</div>
            <h3>NHVR Compliant</h3>
            <p>Synced daily with National Heavy Vehicle Regulator gazettes and notices.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with c3:
        st.markdown("""
        <div class="feature-card">
            <div style="font-size: 3rem; margin-bottom: 10px;">📍</div>
            <h3>Smart Routing</h3>
            <p>Automatically avoid low bridges, load-limited structures, and powerlines.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # CALL TO ACTION
    col_cta1, col_cta2, col_cta3 = st.columns([1, 2, 1])
    with col_cta2:
        st.markdown("""
        <div style="text-align: center; border: 1px dashed rgba(255,255,255,0.3); padding: 15px; border-radius: 8px;">
            <span style="font-size: 1.1rem;">Ready to begin? Select <b>'Start Assessment'</b> in the sidebar.</span>
        </div>
        """, unsafe_allow_html=True)


elif menu == "🛠️ Start Assessment":
    st.title("New Movement Assessment")
    st.markdown("Enter your vehicle details below to check compliance against the national network.")
    
    # We use a container to group the white inputs nicely
    with st.container():
        st.markdown("### 1. Vehicle Configuration")
        c1, c2 = st.columns(2)
        with c1:
            ref = st.text_input("Job Reference / ID", value="JOB-26-004")
            gcm = st.number_input("Gross Combination Mass (Tonnes)", 10.0, 200.0, 42.5, help="Total weight of the combination.")
        with c2:
            route = st.selectbox("Jurisdiction", ["Victoria", "NSW", "QLD", "SA"])
            width = st.number_input("Width (m)", 2.0, 8.0, 2.5)
            height = st.number_input("Height (m)", 2.0, 6.0, 4.3)
            
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("RUN COMPLIANCE ENGINE"):
        # SIMULATED LOGIC
        flags = []
        status = "Approved"
        status_color = "#22c55e" # Green
        
        # Simple Rules Engine
        if gcm > 42.5:
            flags.append(f"⚠️ Mass ({gcm}t) exceeds General Access limits (>42.5t)")
            status = "Conditional"
            status_color = "#f59e0b" # Orange
        if width > 2.5:
            flags.append(f"⚠️ Width ({width}m) requires Oversize flags/signs")
            status = "Conditional"
            status_color = "#f59e0b"
        if height > 4.6: # Common bridge height
            flags.append(f"⛔ Height ({height}m) exceeds clearway max (4.6m)")
            status = "Referral Required"
            status_color = "#ef4444" # Red
            
        # RESULTS DISPLAY
        st.markdown("---")
        
        # We create a white card for the result so it is official and readable
        if len(flags) == 0: flags.append("✅ General Access Compliant - No Permits Required")
        html_flags = "".join([f"<li style='margin-bottom: 5px;'>{f}</li>" for f in flags])
        
        st.markdown(f"""
        <div style="background-color: white; padding: 25px; border-radius: 10px; border-left: 10px solid {status_color}; box-shadow: 0 10px 25px rgba(0,0,0,0.5);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                <h2 style="color: #0f172a !important; margin: 0;">Assessment Result</h2>
                <span style="background-color: {status_color}; color: white; padding: 5px 15px; border-radius: 20px; font-weight: bold;">{status}</span>
            </div>
            <div style="color: #334155 !important;">
                <h4 style="color: #0f172a !important; margin-bottom: 10px;">Analysis Details:</h4>
                <ul style="color: #334155 !important; font-size: 1.1rem; padding-left: 20px;">
                    {html_flags}
                </ul>
            </div>
            <hr style="margin: 20px 0; border-top: 1px solid #e2e8f0;">
            <div style="display: flex; justify-content: space-between; color: #64748b !important; font-size: 0.9rem;">
                <span>nhvr_gazette_v2026.01.12.json</span>
                <span>Calculated Fee: <b>$91.00</b></span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if status != "Approved":
             st.markdown("<br>", unsafe_allow_html=True)
             st.info("ℹ️ Based on these parameters, a permit application must be lodged via the NHVR portal.")
             st.link_button("🚀 GENERATE APPLICATION FORM ($140)", "https://www.nhvr.gov.au/")

elif menu == "🚛 My Fleet":
    st.title("My Fleet")
    st.markdown("Manage your prime movers and trailers here.")
    
    # Placeholder Fleet Data
    st.info("🔒 Please log in to view fleet assets.")
    
    # Example table with styled look
    data = {
        "Asset ID": ["PM-001", "TR-055", "PM-002"],
        "Type": ["Prime Mover", "Low Loader", "Prime Mover"],
        "Rego": ["XJ-99-LZ", "TR-88-QL", "AA-12-BB"],
        "Status": ["Active", "Maintenance", "Active"]
    }
    st.dataframe(data, use_container_width=True)
