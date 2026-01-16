import streamlit as st
import pandas as pd

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="LadenPass | Automated Compliance",
    page_icon="🚛",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. PROFESSIONAL BRANDING (CSS) ---
st.markdown("""
    <style>
    /* 1. MAIN PAGE BACKGROUND (White) */
    .stApp {
        background-color: #ffffff !important;
    }
    
    /* 2. SIDEBAR BACKGROUND (Deep Forest Green) */
    [data-testid="stSidebar"] {
        background-color: #0e3b28 !important;
        border-right: 1px solid #064e3b;
    }

    /* 3. SIDEBAR TEXT (White) */
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] span, [data-testid="stSidebar"] div, [data-testid="stSidebar"] label, 
    [data-testid="stSidebar"] .stMarkdown {
        color: #ffffff !important;
    }

    /* 4. MAIN PAGE TEXT (Dark Blue/Black) */
    .main h1, .main h2, .main h3, .main p, .main li, .main label {
        color: #0f172a !important;
    }

    /* 5. INPUT FIELDS (White background, Dark text) */
    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div>div {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border: 1px solid #cbd5e1;
    }
    
    /* 6. HIDE MENU */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* 7. BUTTON STYLING (Green) */
    .stButton>button {
        width: 100%;
        background-color: #22c55e !important;
        color: white !important;
        border: none;
        padding: 0.6rem 1rem;
        border-radius: 8px;
        font-weight: bold;
    }
    .stButton>button:hover { background-color: #16a34a !important; }

    /* 8. CARDS */
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
    # Ensure logo.jpeg exists in your GitHub
    st.image("https://raw.githubusercontent.com/ladenpass-bot/LadenPass/main/logo.jpeg", use_container_width=True)
    
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
        <h1 style="font-size: 3rem;">Move Heavy Loads, <span style="color: #16a34a !important;">Faster.</span></h1>
        <p style="font-size: 1.2rem; color: #475569 !important;">
            The automated compliance tool for Class 1 Heavy Vehicles. <br>
            Instant bridge checks. 100% Compliant.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # FEATURES
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="feature-card"><h3>⚡ Instant Checks</h3><p>Stop waiting 28 days. Get instant feasibility checks.</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="feature-card"><h3>🛡️ NHVR Compliant</h3><p>Synced daily with National Heavy Vehicle Regulator gazettes.</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="feature-card"><h3>📍 Route Planning</h3><p>Avoid low bridges and powerlines automatically.</p></div>', unsafe_allow_html=True)

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
            
        # RESULTS DISPLAY
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
            <h4 style="margin:0;">Analysis Details</h4>
            <ul>{html_flags}</ul>
        </div>
        """, unsafe_allow_html=True)
        
        if color != "#22c55e":
            st.markdown("<br>", unsafe_allow_html=True)
            st.link_button("🚀 SUBMIT APPLICATION ($140)", "https://buy.stripe.com/test_123")

elif menu == "🚛 My Fleet":
    st.title("My Fleet")
    st.info("Log in to view your saved assets.")
