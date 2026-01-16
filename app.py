import streamlit as st

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="LadenPass | Automated Compliance",
    page_icon="🚛",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. FAIL-SAFE STYLING (CSS) ---
st.markdown("""
    <style>
    /* 1. FORCE MAIN BACKGROUND TO WHITE */
    .stApp {
        background-color: #ffffff !important;
    }

    /* 2. FORCE SIDEBAR BACKGROUND TO BRAND GREEN */
    [data-testid="stSidebar"] {
        background-color: #0e3b28 !important; /* Deep Green from Logo */
        border-right: 1px solid #064e3b;
    }

    /* 3. FIX TEXT VISIBILITY (The Critical Fix) */
    /* Force all main page text to be Dark Blue/Black */
    .main h1, .main h2, .main h3, .main h4, .main p, .main li, .main span, .main div, .main label {
        color: #0f172a !important;
    }
    
    /* Force specific overrides for Streamlit containers that might try to be white */
    div[data-testid="stVerticalBlock"] > div > div {
        color: #0f172a !important;
    }

    /* 4. SIDEBAR TEXT (White) */
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, 
    [data-testid="stSidebar"] div, [data-testid="stSidebar"] label, [data-testid="stSidebar"] .stRadio div {
        color: #ffffff !important;
    }

    /* 5. FEATURE CARDS (Grey Box with Dark Text) */
    .feature-card {
        background-color: #f1f5f9;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e2e8f0;
        text-align: center;
        margin-bottom: 10px;
    }
    .feature-card h3 {
        color: #0f172a !important;
        margin-top: 0;
    }
    .feature-card p {
        color: #475569 !important;
    }

    /* 6. INPUT FIELDS (White Background, Dark Text) */
    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div>div {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border: 1px solid #cbd5e1;
    }
    
    /* 7. BUTTONS (Green Accent) */
    .stButton>button {
        width: 100%;
        background-color: #22c55e !important; /* Light Green from Logo */
        color: white !important;
        border: none;
        padding: 0.6rem 1rem;
        border-radius: 8px;
        font-weight: bold;
    }
    .stButton>button:hover { background-color: #16a34a !important; }

    /* 8. HIDE DEFAULT MENUS */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    # LOGO: This looks for "logo.jpg" in your GitHub root folder.
    # If the image is broken, check the spelling in your GitHub repo exactly.
    try:
        st.image("logo.jpg", use_container_width=True)
    except:
        # Fallback if image fails to load
        st.error("Logo not found. Please upload 'logo.jpg' to GitHub.")
    
    st.markdown("---")
    menu = st.radio("Navigation", ["🏠 Home", "🛠️ Start Assessment", "🚛 My Fleet"])
    st.markdown("---")
    st.caption("© 2026 LadenPass Australia")
    st.caption("Support: admin@ladenpass.com.au")

# --- 4. MAIN CONTENT ---

if menu == "🏠 Home":
    # HERO SECTION
    st.markdown("""
    <div style="text-align: center; padding: 40px 0;">
        <h1 style="font-size: 3rem; color: #0f172a !important;">Move Heavy Loads, <span style="color: #16a34a !important;">Faster.</span></h1>
        <p style="font-size: 1.2rem; color: #475569 !important;">
            The automated compliance tool for Class 1 Heavy Vehicles. <br>
            Instant bridge checks. 100% Compliant.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # FEATURES
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""
        <div class="feature-card">
            <h3>⚡ Instant Checks</h3>
            <p>Stop waiting 28 days. Get instant feasibility checks for VIC & NSW.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown("""
        <div class="feature-card">
            <h3>🛡️ NHVR Compliant</h3>
            <p>Synced daily with National Heavy Vehicle Regulator gazettes.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with c3:
        st.markdown("""
        <div class="feature-card">
            <h3>📍 Route Planning</h3>
            <p>Avoid low bridges and powerlines automatically.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # CALL TO ACTION
    col_cta1, col_cta2, col_cta3 = st.columns([1, 2, 1])
    with col_cta2:
        st.info("👈 Select 'Start Assessment' in the sidebar to begin.")


elif menu == "🛠️ Start Assessment":
    st.title("New Movement Assessment")
    
    with st.container():
        st.markdown("### 1. Vehicle Configuration")
        c1, c2 = st.columns(2)
        with c1:
            ref = st.text_input("Job Reference", value="JOB-26-004")
            gcm = st.number_input("GCM (Tonnes)", 10.0, 200.0, 42.5)
        with c2:
            route = st.selectbox("Jurisdiction", ["Victoria", "NSW", "QLD", "SA"])
            width = st.number_input("Width (m)", 2.0, 8.0, 2.5)
            height = st.number_input("Height (m)", 2.0, 6.0, 4.3)
            
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("RUN COMPLIANCE ENGINE"):
        # LOGIC
        flags = []
        status = "Approved"
        color = "#22c55e" # Green
        
        if gcm > 42.5:
            flags.append("Mass > 42.5t (Bridge Check Req)")
            status = "Conditional"
            color = "#f59e0b" # Orange
        if width > 2.5:
            flags.append("Oversize Width (>2.5m)")
            status = "Conditional"
            color = "#f59e0b"
        if height > 4.9:
            flags.append("Height > 4.9m (Power Check)")
            status = "Referral"
            color = "#ef4444" # Red
            
        # RESULTS CARD
        st.markdown("---")
        r1, r2 = st.columns(2)
        with r1:
            st.metric("Status", status)
        with r2:
            st.metric("NHVR Fee", "$91.00")
            
        if len(flags) == 0: flags.append("✅ General Access Compliant")
        html_flags = "".join([f"<li>{f}</li>" for f in flags])
        
        st.markdown(f"""
        <div style="background-color: white; padding: 20px; border-left: 6px solid {color}; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-top: 20px;">
            <h4 style="margin:0; color: #0f172a !important;">Analysis Details</h4>
            <ul style="color: #0f172a !important;">{html_flags}</ul>
        </div>
        """, unsafe_allow_html=True)
        
        if color != "#22c55e":
            st.markdown("<br>", unsafe_allow_html=True)
            st.link_button("🚀 SUBMIT APPLICATION ($140)", "https://buy.stripe.com/test_123")

elif menu == "🚛 My Fleet":
    st.title("My Fleet")
    st.info("Log in to view your saved assets.")
