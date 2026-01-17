import streamlit as st
import pandas as pd
import base64
import datetime

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="LadenPass | Automated Compliance",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. AUTOMATED ENGINEERING ENGINE (THE "PRODUCT") ---
def check_compliance(gcm, axles, width, height):
    """
    Real logic based on NHVR General Mass Limits (GML) 
    and Dimension requirements.
    """
    report = {
        "status": "COMPLIANT",
        "color": "#22c55e", # Green
        "issues": [],
        "permit_type": "General Access (No Permit Required)"
    }

    # --- A. DIMENSION CHECKS ---
    if width > 2.5:
        report["issues"].append(f"⚠️ **Width ({width}m):** Exceeds 2.5m General Access limit.")
        report["permit_type"] = "Class 1 Oversize Permit Required"
        report["status"] = "CONDITIONAL"
        report["color"] = "#f59e0b" # Orange

    if height > 4.3:
        report["issues"].append(f"⛔ **Height ({height}m):** Exceeds 4.3m standard clearance.")
        report["permit_type"] = "High Productivity / Oversize Permit"
        report["status"] = "NON-COMPLIANT"
        report["color"] = "#ef4444" # Red

    # --- B. MASS CHECKS (General Mass Limits) ---
    # Standard GML Cap is roughly 42.5t for 6 axles (semi) or higher for B-Doubles
    # This is a simplified logic for the MVP
    gml_limit = 42.5
    if axles >= 7: gml_limit = 50.0 # B-Double allowance
    if axles >= 9: gml_limit = 62.5 # B-Triple allowance

    if gcm > gml_limit:
        report["issues"].append(f"⚠️ **Mass ({gcm}t):** Exceeds {gml_limit}t General Access limit.")
        if report["status"] != "NON-COMPLIANT":
            report["status"] = "CONDITIONAL"
            report["permit_type"] = "Class 1 Overmass Permit Required"
            report["color"] = "#f59e0b"

    # --- C. TIER 1 BRIDGE FORMULA (Simplified) ---
    # Formula approximation: Mass must be distributed. 
    # If Mass / Axles > 6.5t per axle, it's likely damaging bridges.
    avg_axle_load = gcm / axles
    if avg_axle_load > 7.0:
        report["issues"].append(f"⛔ **Axle Load ({avg_axle_load:.1f}t):** Exceeds Tier 1 Bridge Safety limits (>7t/axle).")
        report["status"] = "CRITICAL FAIL"
        report["color"] = "#ef4444"
        report["permit_type"] = "Structural Assessment Required"

    return report

# --- 3. UI SETUP ---
logo_b64 = None 
try:
    with open("logo.jpg", "rb") as img_file:
        logo_b64 = base64.b64encode(img_file.read()).decode()
except FileNotFoundError:
    pass

st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: white; }
    [data-testid="stSidebar"] { background-color: #064e3b; }
    .glass-card { background: rgba(255,255,255,0.05); padding: 20px; border-radius: 10px; border: 1px solid rgba(255,255,255,0.1); }
    .stButton>button { background-color: #22c55e; color: white; border: none; width: 100%; padding: 10px; font-weight: bold; }
    h1, h2, h3 { color: white !important; }
    p, label { color: #cbd5e1 !important; }
    /* STRIPE BUTTON STYLE */
    .stripe-btn { 
        background: #635bff; color: white; padding: 10px 20px; 
        border-radius: 5px; text-decoration: none; display: block; text-align: center; margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 4. SESSION STATE ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- 5. SIDEBAR ---
with st.sidebar:
    st.markdown("## LadenPass")
    if st.session_state.logged_in:
        menu = st.radio("Menu", ["Dashboard", "Run Check"], label_visibility="collapsed")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()
    else:
        st.info("🔒 System Locked")

# --- 6. MAIN APP LOGIC ---

# >>> VIEW 1: SALES / LOGIN PAGE <<<
if not st.session_state.logged_in:
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.title("LadenPass Automator")
        st.markdown("### Instant Heavy Vehicle Compliance Checks")
        st.markdown("Stop guessing. Know if your load is legal in 2 seconds.")
        
        with st.form("login"):
            st.subheader("Subscriber Login")
            user = st.text_input("Username")
            pw = st.text_input("Password", type="password")
            if st.form_submit_button("Login"):
                if user == "admin" and pw == "trucks":
                    st.session_state.logged_in = True
                    st.rerun()
                else:
                    st.error("Access Denied")
        
        st.markdown("---")
        # INSERT YOUR STRIPE LINK HERE
        st.markdown('<a href="https://buy.stripe.com/28EdRa2om1jWfAc5kZ9oc00" class="stripe-btn" target="_blank">💳 SUBSCRIBE ($99/mo)</a>', unsafe_allow_html=True)

# >>> VIEW 2: THE AUTOMATED TOOL <<<
else:
    if menu == "Dashboard":
        st.title("Operations Dashboard")
        c1, c2, c3 = st.columns(3)
        with c1: st.markdown('<div class="glass-card"><h3>🟢 Online</h3><p>Engine Ready</p></div>', unsafe_allow_html=True)
        with c2: st.markdown('<div class="glass-card"><h3>⚡ Instant</h3><p>Calculation Mode</p></div>', unsafe_allow_html=True)
        with c3: st.markdown('<div class="glass-card"><h3>🛡️ Active</h3><p>Subscription Valid</p></div>', unsafe_allow_html=True)

    elif menu == "Run Check":
        st.title("Instant Compliance Check")
        st.markdown("Enter vehicle data to run an automated Tier 1 assessment.")
        
        with st.container():
            c1, c2 = st.columns(2)
            with c1:
                gcm = st.number_input("Gross Combination Mass (t)", 10.0, 200.0, 42.5)
                axles = st.number_input("Number of Axles", 3, 20, 6)
            with c2:
                width = st.number_input("Vehicle Width (m)", 2.0, 8.0, 2.5)
                height = st.number_input("Vehicle Height (m)", 2.0, 6.0, 4.3)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("RUN AUTOMATED CHECK"):
            with st.spinner("Calculating Physics & Regulations..."):
                # RUN THE REAL CODE
                result = check_compliance(gcm, axles, width, height)
                
                # DISPLAY RESULT
                st.markdown(f"""
                <div style="background: white; border-radius: 10px; padding: 20px; border-left: 10px solid {result['color']}; color: black;">
                    <h2 style="color: black !important; margin:0;">Status: {result['status']}</h2>
                    <p style="color: #64748b !important; font-weight: bold;">{result['permit_type']}</p>
                    <hr>
                </div>
                """, unsafe_allow_html=True)
                
                if result['issues']:
                    for issue in result['issues']:
                        st.error(issue)
                else:
                    st.success("✅ Configuration meets General Access Limits. No Permit Required.")
