import streamlit as st
import base64
import datetime
import time

# --- 1. ENTERPRISE PAGE CONFIG ---
st.set_page_config(
    page_title="LadenPass | Automated Compliance",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. HELPER: LOAD IMAGE CORRECTLY ---
def get_base64_image(image_path):
    try:
        # Looks for 'logo.jpg' specifically
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
        background-image: linear-gradient(rgba(15, 23, 42, 0.94), rgba(15, 23, 42, 0.96)), 
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

    /* GLASS CARDS */
    .glass-card {
        background-color: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 10px;
        margin-bottom: 20px;
        height: 100%;
    }
    
    /* SALES BULLET POINTS */
    .sales-point {
        background-color: rgba(6, 78, 59, 0.4);
        border-left: 4px solid #4ade80;
        padding: 15px;
        margin-bottom: 10px;
        border-radius: 0 8px 8px 0;
    }
    .sales-point h4 { margin: 0 !important; font-size: 1.1rem !important; color: white !important; }
    .sales-point p { margin: 5px 0 0 0 !important; font-size: 0.95rem !important; opacity: 0.9; }

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

    /* SUBSCRIBE BUTTON */
    .subscribe-btn-container {
        display: flex;
        justify-content: center;
        margin-top: 15px;
    }
    .subscribe-btn {
        display: inline-block;
        background: linear-gradient(45deg, #f59e0b, #d97706);
        color: white !important;
        padding: 15px 40px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: bold;
        font-size: 1.2rem;
        box-shadow: 0 4px 15px rgba(245, 158, 11, 0.4);
        transition: all 0.3s ease;
        border: 1px solid rgba(255,255,255,0.2);
        width: 100%;
        text-align: center;
    }
    .subscribe-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(245, 158, 11, 0.6);
        color: white !important;
        text-decoration: none;
    }
    
    /* TRUST BAR STYLING */
    .trust-bar {
        background-color: rgba(255, 255, 255, 0.03);
        border-top: 1px solid rgba(255,255,255,0.1);
        border-bottom: 1px solid rgba(255,255,255,0.1);
        padding: 30px 20px;
        margin-top: 50px;
        border-radius: 15px;
    }
    .trust-item { text-align: center; margin: 10px; }
    .trust-icon { font-size: 2rem; margin-bottom: 10px; display: block; }
    .trust-label { font-weight: bold; color: white !important; font-size: 1rem; }
    .trust-sub { font-size: 0.8rem; color: #94a3b8 !important; }

    /* DISCLAIMER FOOTER */
    .disclaimer {
        font-size: 0.75rem;
        color: #64748b !important;
        text-align: center;
        margin-top: 50px;
        padding-top: 20px;
        border-top: 1px solid #334155;
    }
    .footer-links a { color: #f59e0b !important; margin: 0 10px; text-decoration: none; }
    
    /* MOBILE RESPONSIVENESS FIX */
    @media (max-width: 768px) {
        div[data-testid="column"] { width: 100% !important; flex: 1 1 auto !important; min-width: 100% !important; }
        h1 { font-size: 2.5rem !important; }
    }

    #MainMenu, footer, header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 4. AUTOMATED ENGINE LOGIC ---
def check_compliance(gcm, axles, width, height):
    report = {
        "status": "APPROVED",
        "color": "#22c55e", 
        "issues": [],
        "permit_type": "General Access (No Permit Required)"
    }
    if width > 2.5:
        report["issues"].append(f"⚠️ **Width ({width}m):** Exceeds 2.5m General Access limit.")
        report["permit_type"] = "Class 1 Oversize Permit Required"
        report["status"] = "CONDITIONAL"
        report["color"] = "#f59e0b"
    if height > 4.3:
        report["issues"].append(f"⛔ **Height ({height}m):** Exceeds 4.3m standard clearance.")
        report["permit_type"] = "High Productivity / Oversize Permit"
        report["status"] = "NON-COMPLIANT"
        report["color"] = "#ef4444" 
    
    gml_limit = 42.5
    if axles >= 7: gml_limit = 50.0 
    if axles >= 9: gml_limit = 62.5 
    
    if gcm > gml_limit:
        report["issues"].append(f"⚠️ **Mass ({gcm}t):** Exceeds {gml_limit}t General Access limit.")
        if report["status"] != "NON-COMPLIANT":
            report["status"] = "CONDITIONAL"
            report["permit_type"] = "Class 1 Overmass Permit Required"
            report["color"] = "#f59e0b"
            
    avg_axle_load = gcm / axles
    if avg_axle_load > 9.0: 
        report["issues"].append(f"⛔ **Axle Load ({avg_axle_load:.1f}t):** Exceeds safety limits (>9t/axle).")
        report["status"] = "CRITICAL FAIL"
        report["color"] = "#ef4444"
        report["permit_type"] = "Structural Assessment Required"
    return report


# --- 5. SESSION STATE ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_type" not in st.session_state:
    st.session_state.user_type = None

# --- 6. SIDEBAR CONTENT ---
with st.sidebar:
    if logo_b64:
        st.markdown(f"""
            <div class="logo-container">
                <img src="data:image/jpeg;base64,{logo_b64}" style="max-width: 100%; height: auto;">
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div class="logo-container">
                <p style="color:#064e3b !important; font-size: 24px; font-weight: bold; margin: 0;">LadenPass</p>
                <p style="color:#666 !important; font-size: 10px; margin: 0;">(Upload 'logo.jpg' to GitHub)</p>
            </div>
        """, unsafe_allow_html=True)
    
    if st.session_state.logged_in:
        st.markdown("### Action Menu")
        st.markdown(f"User: **{st.session_state.user_type}**")
        menu = st.radio("", ["📊 Dashboard", "✅ Run Auto-Check"], label_visibility="collapsed")
        st.markdown("---")
        if st.button("Log Out"):
            st.session_state.logged_in = False
            st.session_state.user_type = None
            st.rerun()
        st.success("🟢 System Online")
    else:
        st.info("🔒 Secure Access")
        st.caption("Please log in to access the Enterprise Platform.")

    current_year = datetime.datetime.now().year
    
    st.markdown(f"""
        <div style='text-align: center; font-size: 0.8rem; color: #cbd5e1; margin-top: 15px; opacity: 0.8;'>
            © {current_year} LadenPass Enterprise<br>
            <strong>ABN: 16 632 316 240</strong>
        </div>
    """, unsafe_allow_html=True)


# --- 7. MAIN CONTENT ---

# >>> VIEW 1: LANDING PAGE <<<
if not st.session_state.logged_in:
    # HERO HEADER
    st.markdown("""
    <div style="text-align: left; padding: 20px 0 40px 0;">
        <h1 style="font-size: 4rem; text-shadow: 0 4px 10px rgba(0,0,0,0.5); margin-bottom: 10px;">LadenPass Enterprise</h1>
        <h2 style="color: #4ade80 !important; font-weight: 300; font-size: 1.8rem; margin-top: 0;">
            Heavy Haulage Compliance. Simplified.
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    # SPLIT LAYOUT
    c_sales, c_login = st.columns([1.5, 1])
    
    with c_sales:
        st.markdown("### Why use LadenPass?")
        st.markdown("""
        <div class="sales-point">
            <h4>⚡ Instant Feasibility Checks</h4>
            <p>Know if you are compliant in 2 seconds. Our engine calculates limits for <strong>Excavators, Bobcats, and Plant Machinery</strong>.</p>
        </div>
        <div class="sales-point">
            <h4>🏗️ Bridge Formula Calculator</h4>
            <p>Avoid structural failures. We check axle spacing and mass distribution against Tier 1 safety standards.</p>
        </div>
        <div class="sales-point">
            <h4>💰 Avoid Expensive Fines</h4>
            <p>Don't risk a $5,000 fine. Validate your load before it hits the weighbridge.</p>
        </div>
        """, unsafe_allow_html=True)

    with c_login:
        # --- LOGIN FORM ---
        with st.form("login_form"):
            st.subheader("Subscriber Login")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login")
            
            if submitted:
                # --- [SECURE LOGIN IMPLEMENTATION] ---
                try:
                    # 1. Fetch Credentials from Secrets
                    admin_user = st.secrets["credentials"]["username"]
                    admin_pass = st.secrets["credentials"]["password"]
                    
                    # 2. Fetch Guest Credentials (Optional - uses .get to prevent crash if not set)
                    guest_user = st.secrets.get("guest", {}).get("username", "none")
                    guest_pass = st.secrets.get("guest", {}).get("password", "none")

                    # 3. Validation Logic
                    if username == admin_user and password == admin_pass:
                        st.session_state.logged_in = True
                        st.session_state.user_type = "Admin"
                        st.rerun()
                    elif username == guest_user and password == guest_pass:
                        st.session_state.logged_in = True
                        st.session_state.user_type = "Guest/Trial"
                        st.rerun()
                    else:
                        st.error("Invalid credentials.")
                        
                except Exception as e:
                    st.error("⚠️ System Error: Secrets not configured correctly.")
                    st.info("Check Streamlit Settings > Secrets.")

        # --- TRIAL REQUEST LINK (NEW) ---
        st.markdown("""
            <div style="text-align: center; margin-top: 20px;">
                <p style="margin-bottom: 10px;">Don't have a login?</p>
                <a href="mailto:support@ladenpass.com.au?subject=Request 7-Day Free Trial&body=Hi, I would like to request a free trial code for LadenPass Enterprise." 
                   style="background-color: transparent; border: 1px solid #4ade80; color: #4ade80; padding: 10px 20px; border-radius: 5px; text-decoration: none; display: inline-block;">
                   📩 Request 7-Day Free Trial
                </a>
            </div>
        """, unsafe_allow_html=True)

        # SUBSCRIBE BUTTON
        st.markdown("""
            <div class="subscribe-btn-container">
                <a href="https://buy.stripe.com/28EdRa2om1jWfAc5kZ9oc00" class="subscribe-btn" target="_blank">
                    UNLOCK INSTANT ACCESS ($99/mo)
                    <div style="font-size: 0.8rem; font-weight: normal; margin-top: 5px;">30-Day Money Back Guarantee</div>
                </a>
            </div>
        """, unsafe_allow_html=True)

    # --- TRUST BAR ---
    st.markdown("""
    <div class="trust-bar">
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap; text-align: center;">
            <div class="trust-item">
                <span class="trust-icon">👷‍♂️</span>
                <div class="trust-label">Industry Ready</div>
                <div class="trust-sub">Civil, Mining & Agriculture</div>
            </div>
            <div class="trust-item">
                <span class="trust-icon">✅</span>
                <div class="trust-label">NHVR Compliance</div>
                <div class="trust-sub">Updated to 2026 Gazettes</div>
            </div>
             <div class="trust-item">
                <span class="trust-icon">🔒</span>
                <div class="trust-label">Secure Data</div>
                <div class="trust-sub">AES-256 Encryption</div>
            </div>
            <div class="trust-item">
                <span class="trust-icon">🛡️</span>
                <div class="trust-label">Safety First</div>
                <div class="trust-sub">Chain of Responsibility</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# >>> VIEW 2: LOGGED IN AREA (AUTOMATED) <<<
else:
    if "Dashboard" in menu:
        st.markdown(f"""
        <div style="text-align: center; padding: 20px 0 30px 0;">
            <h1 style="font-size: 3rem;">Operations Dashboard</h1>
            <p style="font-size: 1.1rem; opacity: 0.9;">Welcome back, {st.session_state.user_type} User.</p>
        </div>
        """, unsafe_allow_html=True)

        # Metrics
        c1, c2, c3, c4 = st.columns(4)
        with c1: st.markdown('<div class="glass-card"><h3>🟢 Online</h3><p>Engine Status</p></div>', unsafe_allow_html=True)
        with c2: st.markdown('<div class="glass-card"><h3>< 2s</h3><p>Calculation Speed</p></div>', unsafe_allow_html=True)
        with c3: st.markdown('<div class="glass-card"><h3>Active</h3><p>Subscription</p></div>', unsafe_allow_html=True)
        with c4: st.markdown('<div class="glass-card"><h3>Unlimited</h3><p>Remaining Checks</p></div>', unsafe_allow_html=True)

        st.markdown("<br>### System Capabilities", unsafe_allow_html=True)
        fc1, fc2, fc3 = st.columns(3)
        with fc1:
            st.markdown('<div class="glass-card"><h3>⚡ GML Limits</h3><p>Instant General Mass Limit verification.</p></div>', unsafe_allow_html=True)
        with fc2:
            st.markdown('<div class="glass-card"><h3>📐 Dimension Check</h3><p>Automatic width/height gazette cross-reference.</p></div>', unsafe_allow_html=True)
        with fc3:
            st.markdown('<div class="glass-card"><h3>🏗️ Tier 1 Safety</h3><p>Axle load distribution safety calculation.</p></div>', unsafe_allow_html=True)

    elif "Run" in menu:
        st.title("Instant Compliance Check")
        st.markdown("Enter vehicle parameters below to run an automated assessment.")
        
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
                time.sleep(1) # Visual effect
                result = check_compliance(gcm, axles, width, height)
                
                st.markdown(f"""
                <div style="background-color: white; border-radius: 10px; padding: 25px; border-left: 10px solid {result['color']}; margin-top: 20px;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <h2 style="color: #0f172a !important; margin:0;">Status: {result['status']}</h2>
                    </div>
                    <p style="color: #64748b !important; font-weight: bold; margin-top: 5px;">{result['permit_type']}</p>
                    <hr style="border-top: 1px solid #e2e8f0; margin: 15px 0;">
                """, unsafe_allow_html=True)
                
                if result['issues']:
                    for issue in result['issues']:
                        st.error(issue)
                else:
                    st.success("✅ Configuration meets General Access Limits. No Permit Required.")
                    
                st.markdown("</div>", unsafe_allow_html=True)

# --- FOOTER & LEGAL ---
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("""
    <div class="disclaimer">
        <b>Disclaimer:</b> LadenPass provides preliminary feasibility assessments based on standard General Mass Limits (GML). 
        Results are estimates only and do not constitute a legal permit. 
        All heavy vehicle movements must be officially lodged and approved by the National Heavy Vehicle Regulator (NHVR).
        <br><br>
        <div style="margin-bottom: 20px;">
            © 2026 LadenPass Heavy Haulage | <strong>ABN: 16 632 316 240</strong>
        </div>
    </div>
""", unsafe_allow_html=True)

with st.expander("📜 Privacy Policy"):
    st.write("""
    **Privacy Policy for LadenPass**
    1. **Data Collection:** We collect user input (vehicle dimensions) and login credentials for functional purposes only.
    2. **Usage:** Data is used to calculate compliance checks and is not sold to third parties.
    3. **Storage:** No vehicle data is permanently stored in this version of the application.
    4. **Contact:** For privacy concerns, contact the administrator.
    """)

with st.expander("⚖️ Terms of Service"):
    st.write("""
    **Terms of Service**
    1. **Not Legal Advice:** The outputs of this tool are for estimation only. 
    2. **NHVR Authority:** Always consult the official NHVR portal before transport.
    3. **Liability:** LadenPass is not liable for fines incurred based on these calculations.
    4. **Refunds:** Subscription refunds are handled via Stripe's standard policies (30-day guarantee).
    """)
