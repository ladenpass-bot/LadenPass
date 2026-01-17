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
    .block-container { padding-top: 1rem !important; padding-bottom: 1rem !important; }

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
    h1, h2, h3, h4, h5, h6 { color: #ffffff !important; }
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

    /* GLASS CARDS */
    .glass-card {
        background-color: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 10px;
        margin-bottom: 20px;
        height: 100%;
    }
    
    /* INPUTS & BUTTONS */
    .stTextInput input, .stNumberInput input, .stSelectbox div[data-baseweb="select"] {
        background-color: #ffffff !important;
        color: #0f172a !important;
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

    /* FORM STYLING */
    [data-testid="stForm"] {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 30px;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }

    /* CUSTOM SUBSCRIBE BUTTON */
    .subscribe-btn-container {
        display: flex;
        justify-content: center;
        margin-top: 10px;
    }
    .subscribe-btn {
        display: inline-block;
        background: linear-gradient(45deg, #f59e0b, #d97706); /* Gold/Orange Gradient */
        color: white !important;
        padding: 12px 30px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: bold;
        font-size: 1.1rem;
        box-shadow: 0 4px 15px rgba(245, 158, 11, 0.4);
        transition: all 0.3s ease;
        border: 1px solid rgba(255,255,255,0.2);
    }
    .subscribe-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(245, 158, 11, 0.6);
        color: white !important;
        text-decoration: none;
    }
    
    #MainMenu, footer, header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 4. SESSION STATE (USER LOGIN) ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- 5. SIDEBAR CONTENT ---
with st.sidebar:
    if logo_b64:
        st.markdown(f"""<div class="logo-container"><img src="data:image/jpeg;base64,{logo_b64}"></div>""", unsafe_allow_html=True)
    else:
        st.markdown("""<div class="logo-container"><h2 style="color:#064e3b !important; margin:0;">LadenPass</h2></div>""", unsafe_allow_html=True)
    
    if st.session_state.logged_in:
        st.markdown("### Action Menu")
        menu = st.radio("", ["📊 Dashboard", "✅ New Check"], label_visibility="collapsed")
        
        st.markdown("---")
        if st.button("Log Out"):
            st.session_state.logged_in = False
            st.rerun()
            
        st.success("🟢 Online")
    else:
        st.info("🔒 Secure Access")
        st.caption("Please log in to access the Enterprise Platform.")

    current_year = datetime.datetime.now().year
    st.markdown(f"""
        <div style='text-align: center; font-size: 0.8rem; color: #cbd5e1; margin-top: 15px; opacity: 0.8;'>
            © {current_year} LadenPass Enterprise
        </div>
    """, unsafe_allow_html=True)


# --- 6. MAIN CONTENT ---

# --- SCENARIO A: LOGIN SCREEN ---
if not st.session_state.logged_in:
    st.markdown("""
    <div style="text-align: center; padding: 40px 0;">
        <h1 style="font-size: 3.5rem;">LadenPass Enterprise</h1>
        <p style="font-size: 1.2rem; max-width: 600px; margin: 0 auto; opacity: 0.9;">
            The automated network access platform for Class 1 Heavy Vehicles.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        with st.form("login_form"):
            st.subheader("Client Login")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login")
            
            if submitted:
                if username == "admin" and password == "trucks":
                    st.session_state.logged_in = True
                    st.rerun()
                else:
                    st.error("Invalid credentials.")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center; margin-bottom: 10px;'>Don't have an account?</div>", unsafe_allow_html=True)
        
        # --- PASTE YOUR STRIPE LINK BELOW ---
        st.markdown("""
            <div class="subscribe-btn-container">
                <a href="YOUR_STRIPE_LINK_HERE" class="subscribe-btn" target="_blank">
                    💳 SUBSCRIBE NOW ($99/mo)
                </a>
            </div>
        """, unsafe_allow_html=True)


# --- SCENARIO B: DASHBOARD (LOGGED IN) ---
else:
    if "Dashboard" in menu:
        st.markdown("""
        <div style="text-align: center; padding: 20px 0 30px 0;">
            <h1 style="font-size: 3rem;">Operations Dashboard</h1>
            <p style="font-size: 1.1rem; opacity: 0.9;">Welcome back, Admin User.</p>
        </div>
        """, unsafe_allow_html=True)

        c1, c2, c3, c4 = st.columns(4)
        with c1: st.markdown('<div class="glass-card" style="text-align:center;"><h3>98%</h3><p>Pre-Approval Accuracy</p></div>', unsafe_allow_html=True)
        with c2: st.markdown('<div class="glass-card" style="text-align:center;"><h3>< 2s</h3><p>Calculation Speed</p></div>', unsafe_allow_html=True)
        with c3: st.markdown('<div class="glass-card" style="text-align:center;"><h3>100%</h3><p>Gazette Compliance</p></div>', unsafe_allow_html=True)
        with c4: st.markdown('<div class="glass-card" style="text-align:center;"><h3>24/7</h3><p>Network Availability</p></div>', unsafe_allow_html=True)

        st.markdown("<br>### Features", unsafe_allow_html=True)
        fc1, fc2, fc3 = st.columns(3)
        with fc1:
            st.markdown('<div class="glass-card"><h3>⚡ Automated Feasibility</h3><p>Eliminates manual bridge assessments.</p></div>', unsafe_allow_html=True)
        with fc2:
            st.markdown('<div class="glass-card"><h3>🗺️ Dynamic Routing</h3><p>Routes validated against height restrictions.</p></div>', unsafe_allow_html=True)
        with fc3:
            st.markdown('<div class="glass-card"><h3>📄 Regulatory Alignment</h3><p>Full integration with NHVR Class 1 Notice.</p></div>', unsafe_allow_html=True)

    elif "Check" in menu:
        st.title("Compliance Check")
        with st.container():
            c1, c2, c3 = st.columns(3)
            with c1:
                ref = st.text_input("Job Ref", value="JOB-X88")
                route = st.selectbox("State", ["VIC", "NSW", "QLD"])
            with c2:
                gcm = st.number_input("Mass (t)", 10.0, 250.0, 42.5)
                axles = st.number_input("Axle Count", 2, 20, 6)
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
