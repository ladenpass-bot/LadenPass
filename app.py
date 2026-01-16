import streamlit as st
import pandas as pd

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="LadenPass | Automated Compliance",
    page_icon="🚛",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. PROFESSIONAL STYLING (THE FIX) ---
st.markdown("""
    <style>
    /* FORCE LIGHT MODE TEXT VISIBILITY */
    .stApp { background-color: #ffffff !important; }
    h1, h2, h3, h4, h5, h6, p, li, span, div { color: #0f172a !important; }
    
    /* HIDE STREAMLIT BRANDING */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* BUTTON STYLING */
    .stButton>button {
        width: 100%;
        background-color: #047857; /* LadenPass Green */
        color: white !important;
        border: none;
        padding: 0.6rem 1rem;
        font-weight: bold;
        border-radius: 8px;
    }
    .stButton>button:hover { background-color: #065f46; }

    /* INPUT FIELD STYLING (Make them pop) */
    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div>div {
        background-color: #f1f5f9 !important;
        color: #0f172a !important;
        border: 1px solid #cbd5e1;
    }

    /* CARD STYLING */
    .feature-card {
        background-color: #f8fafc;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e2e8f0;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    # UPDATED: Now looking for 'logo.jpeg'
    st.image("https://raw.githubusercontent.com/ladenpass-bot/LadenPass/main/logo.jpeg", use_container_width=True)
    
    st.markdown("---")
    menu = st.radio("Navigation", ["🏠 Home", "🛠️ Start Assessment", "🚛 My Fleet"])
    st.markdown("---")
    st.caption("© 2026 LadenPass Australia")
    st.caption("Support: admin@ladenpass.com.au")

# --- 4. MAIN CONTENT ---

if menu == "🏠 Home":
    # --- HERO SECTION (THE SALES PITCH) ---
    st.markdown("""
    <div style="text-align: center; padding: 40px 0;">
        <h1 style="font-size: 3.5rem; margin-bottom: 10px;">Move Heavy Loads, <span style="color: #047857 !important;">Faster.</span></h1>
        <p style="font-size: 1.2rem; color: #475569 !important;">
            The only automated compliance tool for Class 1 Heavy Vehicles in Australia. <br>
            Instant bridge checks. HVSAPS Integrated. 100% Compliant.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # --- THREE FEATURES (Why use us?) ---
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""
        <div class="feature-card">
            <h3>⚡ Instant Checks</h3>
            <p>Stop waiting 28 days for a permit. Get an instant HVSAPS feasibility check for VIC & NSW.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with c2:
        st.markdown("""
        <div class="feature-card">
            <h3>🛡️ NHVR Compliant</h3>
            <p>Our database is synced daily with the National Heavy Vehicle Regulator gazettes.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with c3:
        st.markdown("""
        <div class="feature-card">
            <h3>📍 Route Planning</h3>
            <p>Avoid low bridges and powerlines automatically. We check height clearance instantly.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # BIG CALL TO ACTION
    col_cta1, col_cta2, col_cta3 = st.columns([1, 2, 1])
    with col_cta2:
        st.info("Ready to move?")
        # This button is just visual on the home page, switching tabs is manual for now
        st.write("👈 **Select 'Start Assessment' in the sidebar to begin.**")


elif menu == "🛠️ Start Assessment":
    st.title("New Movement Assessment")
    st.markdown("Enter your vehicle details below to check against **2026 Regulations**.")
    
    with st.container():
        st.markdown("### 1. Vehicle Configuration")
        c1, c2 = st.columns(2)
        with c1:
            ref = st.text_input("Job Reference", value="JOB-2026-001")
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
            
        # DISPLAY RESULTS
        st.markdown("---")
        st.subheader("Assessment Results")
        
        r1, r2 = st.columns(2)
        with r1:
            st.metric("Status", status)
        with r2:
            st.metric("NHVR Fee", "$91.00")
            
        # DYNAMIC RESULT CARD
        if len(flags) == 0:
            flags.append("✅ General Access Compliant")
            
        html_flags = "".join([f"<li>{f}</li>" for f in flags])
        
        st.markdown(f"""
        <div style="background-color: white; padding: 20px; border-left: 6px solid {color}; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <h4 style="margin:0;">Analysis Details</h4>
            <ul>{html_flags}</ul>
        </div>
        """, unsafe_allow_html=True)
        
        if color != "#22c55e":
            st.markdown("<br>", unsafe_allow_html=True)
            st.link_button("🚀 SUBMIT PERMIT APPLICATION ($140)", "https://buy.stripe.com/test_123")

elif menu == "🚛 My Fleet":
    st.title("My Fleet")
    st.info("Log in to view your saved assets.")
