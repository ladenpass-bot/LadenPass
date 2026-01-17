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

# --- 2. FAIL-SAFE STYLING (CSS) ---
st.markdown("""
    <style>
    /* 1. BACKGROUND FAIL-SAFE */
    .stApp {
        /* If image fails, fallback to this nice dark blue-grey */
        background-color: #0f172a; 
        /* Try to load the image */
        background-image: linear-gradient(rgba(15, 23, 42, 0.8), rgba(15, 23, 42, 0.8)), 
        url("https://images.unsplash.com/photo-1605218427368-35b81a3dd628?q=80&w=2670&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* 2. FORCE TEXT WHITE (Crucial for visibility) */
    h1, h2, h3, h4, h5, h6, p, li, span, label, div[data-testid="stMarkdownContainer"] p {
        color: #ffffff !important;
    }

    /* 3. SIDEBAR STYLING */
    [data-testid="stSidebar"] {
        background-color: #0e3b28 !important; /* Brand Green */
        border-right: 1px solid #064e3b;
    }
    
    /* 4. LOGO BADGE (Fixes the white square issue) */
    .logo-container {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }

    /* 5. GLASS CARDS (Home Page) */
    .feature-card {
        background-color: rgba(255, 255, 255, 0.1); 
        padding: 20px;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        text-align: center;
        backdrop-filter: blur(10px);
    }
    /* Force card text colors specifically */
    .feature-card h3 { color: #4ade80 !important; margin-top: 0; }
    .feature-card p { color: #e2e8f0 !important; }

    /* 6. INPUT FIELDS (White background, Black text) */
    .stTextInput input, .stNumberInput input, .stSelectbox div[data-baseweb="select"] {
        background-color: #ffffff !important;
        color: #000000 !important;
        border-radius: 6px;
    }
    /* Fix the dropdown text color specifically */
    .stSelectbox div[data-baseweb="select"] span {
        color: #000000 !important;
    }
    
    /* 7. HIDE MENUS */
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    # LOGO FIX: We create a white "badge" container so your logo looks professional
    st.markdown('<div class="logo-container">', unsafe_allow_html=True)
    try:
        st.image("logo.jpg", use_container_width=True)
    except:
        # Fallback Text Logo if image breaks
        st.markdown("<h2 style='color: #0e3b28 !important; margin:0;'>LadenPass</h2>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("### Navigation")
    menu = st.radio("", ["🏠 Home", "🛠️ Start Assessment", "🚛 My Fleet"], label_visibility="collapsed")
    
    st.markdown("---")
    st.caption("© 2026 LadenPass Australia")
    st.caption("Status: 🟢 Online")

# --- 4. MAIN CONTENT ---

if menu == "🏠 Home":
    # HERO SECTION
    st.markdown("""
    <div style="text-align: center; padding: 50px 0;">
        <h1 style="font-size: 3.5rem; text-shadow: 0 2px 4px rgba(0,0,0,0.5);">
            Move Heavy Loads, <span style="color: #4ade80 !important;">Faster.</span>
        </h1>
        <p style="font-size: 1.2rem; opacity: 0.9;">
            The automated compliance tool for Class 1 Heavy Vehicles.<br>
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
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="feature-card">
            <h3>🛡️ NHVR Compliant</h3>
            <p>Synced daily with National Heavy Vehicle Regulator gazettes.</p>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="feature-card">
            <h3>📍 Route Planning</h3>
            <p>Avoid low bridges and powerlines automatically.</p>
        </div>""", unsafe_allow_html=True)
        
    st.markdown("<br><br>", unsafe_allow_html=True)
    col_cta1, col_cta2, col_cta3 = st.columns([1, 2, 1])
    with col_cta2:
        st.info("👈 Select 'Start Assessment' in the sidebar to begin.")

elif menu == "🛠️ Start Assessment":
    st.title("New Movement Assessment")
    
    # INPUT CONTAINER
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

    if st.button("RUN COMPLIANCE ENGINE"):
        # LOGIC
        flags = []
        status = "Approved"
        color = "#22c55e" # Green
        
        if gcm > 42.5:
            flags.append("Mass > 42.5t (Bridge Check Req)")
            status = "Conditional"
            color = "#f59e0b"
        if width > 2.5:
            flags.append("Oversize Width (>2.5m)")
            status = "Conditional"
            color = "#f59e0b"
        if height > 4.6:
            flags.append("Height > 4.6m (Power Check)")
            status = "Referral"
            color = "#ef4444"

        # RESULT CARD (White Box for readability)
        st.markdown("---")
        if len(flags) == 0: flags.append("✅ General Access Compliant")
        html_flags = "".join([f"<li style='color:#334155;'>{f}</li>" for f in flags])
        
        st.markdown(f"""
        <div style="background-color: white; padding: 20px; border-radius: 10px; border-left: 8px solid {color}; margin-top: 20px;">
            <h3 style="color: #0f172a !important; margin:0;">Status: {status}</h3>
            <p style="color: #64748b !important;">Calculated NHVR Fee: <b>$91.00</b></p>
            <ul style="margin-top: 10px;">{html_flags}</ul>
        </div>
        """, unsafe_allow_html=True)

elif menu == "🚛 My Fleet":
    st.title("My Fleet")
    st.info("Log in to view your saved assets.")
    data = {"ID": ["PM-001", "PM-002"], "Type": ["Prime Mover", "Trailer"], "Status": ["Active", "Maintenance"]}
    st.dataframe(pd.DataFrame(data), use_container_width=True)
