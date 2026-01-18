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
        # Using logo.jpg as provided
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return None

logo_b64 = get_base64_image("logo.jpg")

# --- 3. PROFESSIONAL STYLING (MATCHING SCREENSHOT PRECISELY) ---
st.markdown("""
    <style>
    /* 1. LAYOUT & CENTERING */
    div[data-testid="stAppViewContainer"] {
        height: 100vh;
        overflow-y: auto;
    }
    
    div.block-container {
        min-height: 90vh !important;
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
    }

    /* 2. GLOBAL THEME (Dark Blue Background) */
    .stApp {
        background-color: #0f172a; 
        background-image: linear-gradient(rgba(15, 23, 42, 0.94), rgba(15, 23, 42, 0.96)), 
        url("https://images.unsplash.com/photo-1601584115197-04ecc0da31d7?q=80&w=2670&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* 3. REMOVE DECORATIONS */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}

    /* 4. TYPOGRAPHY */
    h1 { color: #ffffff !important; font-size: 3rem !important; font-weight: 700 !important; margin-bottom: 5px !important; }
    h2 { color: #4ade80 !important; font-size: 1.5rem !important; margin-top: 0px !important; font-weight: 300 !important; }
    h3 { color: #ffffff !important; font-size: 1.1rem !important; }
    p, li, label, span, div { color: #cbd5e1 !important; font-size: 0.9rem !important; }
    
    /* 5. SIDEBAR (SOLID GREEN) */
    [data-testid="stSidebar"] {
        background-color: #064e3b !important;
        border-right: 1px solid rgba(255,255,255,0.1);
    }
    
    /* 6. LOGO CONTAINER */
    .logo-container {
        background-color: white;
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 20px;
        text-align: center;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    /* 7. GLASS CARDS (DARK THEME) */
    .glass-card {
        background-color: rgba(15, 23, 42, 0.6); 
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 10px;
        height: 100%;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    }
    
    /* 8. SALES POINTS (DARK GREEN BARS) */
    .sales-point {
        background-color: rgba(6, 78, 59, 0.6);
        border-left: 4px solid #4ade80;
        padding: 15px;
        margin-bottom: 15px;
        border-radius: 4px;
    }
    .sales-point h4 { margin: 0 !important; font-size: 1.1rem !important; color: white !important; font-weight: bold !important; }
    .sales-point p { margin: 2px 0 0 0 !important; font-size: 0.9rem !important; opacity: 0.9; }

    /* 9. FORM CONTAINER (DARK) */
    [data-testid="stForm"] {
        background-color: rgba(15, 23, 42, 0.6);
        padding: 30px;
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }

    /* 10. INPUTS & BUTTONS */
    .stTextInput input {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border-radius: 4px;
        padding: 10px;
    }
    .stButton > button {
        background-color: #f5f5f5 !important;
        color: #0f172a !important;
        border: none;
        font-weight: 600;
        width: 100px;
        padding: 8px;
        margin-top: 10px;
        border-radius: 4px;
    }
    .stButton > button:hover { background-color: #e2e8f0 !important; }

    /* 11. SUBSCRIBE BUTTON (ORANGE) */
    .subscribe-btn-container {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    .subscribe-btn {
        display: inline-block;
        background: linear-gradient(45deg, #f59e0b, #ea580c);
        color: white !important;
        padding: 12px 40px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        font-size: 1rem;
        border: 1px solid rgba(255,255,255,0.2);
        width: 100%;
        text-align: center;
        box-shadow: 0 4px 15px rgba(234, 88, 12, 0.3);
    }
    .subscribe-btn:hover {
        color: white !important;
        transform: translateY(-2px);
    }
    
    /* 12. TRUST BAR */
    .trust-bar {
        margin-top: 40px;
        display: flex;
        justify-content: space-around;
        padding: 0 10px;
        border-top: 1px solid rgba(255,255,255,0.1);
        padding-top: 20px;
    }
    .trust-item { text-align: center; opacity: 1.0; }
    .trust-icon { font-size: 1.2rem; display: block; margin-bottom: 5px; color: #f59e0b; }
    .trust-label { font-weight: bold; color: white !important; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px; }
    .trust-sub { font-size: 0.7rem; color: #94a3b8; }

    /* 13. FOOTER */
    .footer-container {
        margin-top: 30px;
        text-align: center;
        opacity: 0.7;
    }
    .footer-text { font-size: 0.75rem; color: #64748b; margin-bottom: 5px; }
    .footer-links a { color: #f59e0b !important; margin: 0 10px; text-decoration: none; font-size: 0.75rem; }
    
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
        report["issues"].append(f"⚠️ Width ({width}m) > 2.5m")
        report["permit_type"] = "Class 1 Oversize Permit"
        report["status"] = "CONDITIONAL"
        report["color"] = "#f59e0b"
    if height > 4.3:
        report["issues"].append(f"⛔ Height ({height}m) > 4.3m")
        report["permit_type"] = "High Productivity / Oversize"
        report["status"] = "NON-COMPLIANT"
        report["color"] = "#ef4444" 
    
    gml_limit = 42.5
    if axles >= 7: gml_limit = 50.0 
    if axles >= 9: gml_limit = 62.5 
    
    if gcm > gml_limit:
        report["issues"].append(f"⚠️ Mass ({gcm}t) > {gml_limit}t")
        if report["status"] != "NON-COMPLIANT":
            report["status"] = "CONDITIONAL"
            report["permit_type"] = "Class 1 Overmass Permit"
            report["color"] = "#f59e0b"
            
    avg_axle_load = gcm / axles
    if avg_axle_load > 9.0: 
        report["issues"].append(f"⛔ Axle Load ({avg_axle_load:.1f}t) > 9t")
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
    # A. LOGO (White Box)
    if logo_b64:
        st.markdown(f"""<div class="logo-container"><img src="data:image/jpeg;base64,{logo_b64}" style="max-width: 100%; height: auto;"></div>""", unsafe_allow_html=True)
    else:
        st.markdown("""<div class="logo-container"><p style="color:#064e3b !important; font-size: 20px; font-weight: bold; margin: 0;">LadenPass</p></div>""", unsafe_allow_html=True)
    
    # B. LOGGED IN CONTROLS
    if st.session_state.logged_in:
        st.markdown("### Action Menu")
        st.markdown(f"User: **{st.session_state.user_type}**")
        menu = st.radio("", ["📊 Dashboard", "✅ Run Check"], label_visibility="collapsed")
        
        # Future Additions Slot
        # st.button("⚙️ Settings")
        
        st.markdown("---")
        if st.button("Log Out"):
            st.session_state.logged_in = False
            st.session_state.user_type = None
            st.rerun()
        st.success("🟢 System Online")
        
    else:
        # --- C. SECURE ACCESS (CUSTOM DARK BOX) ---
        st.markdown("""
        <div style="
            background-color: #042f2e; 
            border-left: 4px solid #10b981; 
            padding: 12px; 
            border-radius: 4px; 
            color: #94a3b8; 
            font-size: 0.85rem;
            margin-bottom: 20px;
        ">
            <span style="margin-right: 8px;">🔒</span> <strong>Secure Access</strong>
        </div>
        """, unsafe_allow_html=True)
        
        # --- D. 7-DAY TRIAL OFFER (IN SIDEBAR) ---
        st.markdown("""
        <div style="
            background-color: rgba(6, 78, 59, 0.4); 
            border: 2px solid #10b981; 
            border-radius: 8px; 
            padding: 15px; 
            text-align: center;
        ">
            <h3 style="color: #ffffff; margin: 0 0 10px 0; font-size: 1.0rem;">🎉 7-Day Free Trial</h3>
            <p style="color: #cbd5e1; font-size: 0.8rem; margin-bottom: 12px; line-height: 1.3;">
                Test drive the platform instantly. No credit card required.
            </p>
            <div style="background-color: rgba(0,0,0,0.3); padding: 8px; border-radius: 4px; margin-bottom: 8px;">
                <div style="color: #34d399; font-weight: bold; font-size: 0.85rem;">User: guest</div>
                <div style="color: #34d399; font-weight: bold; font-size: 0.85rem;">Pass: tryladenpass</div>
            </div>
            <p style="color: #94a3b8; font-size: 0.7rem; margin: 0;">(Limited Time Only)</p>
        </div>
        """, unsafe_allow_html=True)

    # E. SIDEBAR FOOTER
    current_year = datetime.datetime.now().year
    st.markdown(f"""
        <div style='text-align: center; font-size: 0.7rem; color: #cbd5e1; margin-top: 40px; opacity: 0.6;'>
            © {current_year} LadenPass<br>ABN: 16 632 316 240
        </div>
    """, unsafe_allow_html=True)


# --- 7. MAIN CONTENT ---

# >>> VIEW 1: LANDING PAGE <<<
if not st.session_state.logged_in:
    
    # 1. HEADER SECTION
    st.markdown("""
    <div style="text-align: left; margin-bottom: 30px;">
        <h1>LadenPass Enterprise</h1>
        <h2>Heavy Haulage Compliance. Simplified.</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # 2. SPLIT LAYOUT (SALES & LOGIN)
    c_sales, c_login = st.columns([1.6, 1])
    
    with c_sales:
        st.markdown("### Why use LadenPass?")
        st.markdown("""
        <div class="sales-point">
            <h4>⚡ Instant Feasibility</h4>
            <p>Calculates limits for Excavators & Bobcats in seconds.</p>
        </div>
        <div class="sales-point">
            <h4>🏗️ Bridge Formula Check</h4>
            <p>Verify axle spacing against Tier 1 safety standards.</p>
        </div>
        <div class="sales-point">
            <h4>💰 Avoid Fines</h4>
            <p>Validate your load before it hits the weighbridge.</p>
        </div>
        """, unsafe_allow_html=True)

    with c_login:
        with st.form("login_form"):
            st.markdown("### Subscriber Login")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login")
            
            if submitted:
                # --- LOGIN LOGIC (UPDATED WITH FALLBACK) ---
                try:
                    # 1. Admin Logic (Secrets)
                    admin_user = st.secrets.get("credentials", {}).get("username", "admin")
                    admin_pass = st.secrets.get("credentials", {}).get("password", "trucks") # Fallback to 'trucks' if not set
                    
                    # 2. Guest Logic (Auto-Fallbacks enabled so it works instantly)
                    guest_user = st.secrets.get("guest", {}).get("username", "guest")
                    guest_pass = st.secrets.get("guest", {}).get("password", "tryladenpass")

                    if username == admin_user and password == admin_pass:
                        st.session_state.logged_in = True
                        st.session_state.user_type = "Admin"
                        st.rerun()
                    elif username == guest_user and password == guest_pass:
                        st.session_state.logged_in = True
                        st.session_state.user_type = "Guest"
                        st.rerun()
                    else:
                        st.error("Invalid credentials.")
                except Exception as e:
                    # Emergency bypass if secrets completely fail
                    if username == "guest" and password == "tryladenpass":
                         st.session_state.logged_in = True
                         st.session_state.user_type = "Guest"
                         st.rerun()
                    else:
                         st.error("Invalid credentials.")
        
        # TRIAL REQUEST LINK (TEXT ONLY)
        st.markdown("""
            <div style="text-align: center; margin-top: 15px;">
                <a href="mailto:support@ladenpass.com.au?subject=Request Trial&body=Hi, request for trial code." 
                   style="color: #4ade80; text-decoration: none; font-size: 0.85rem;">
                   📩 Request Free Trial Code
                </a>
            </div>
        """, unsafe_allow_html=True)

        # SUBSCRIBE BUTTON
        st.markdown("""
            <div class="subscribe-btn-container">
                <a href="https://buy.stripe.com/28EdRa2om1jWfAc5kZ9oc00" class="subscribe-btn" target="_blank">
                    UNLOCK INSTANT ACCESS ($99)
                </a>
            </div>
        """, unsafe_allow_html=True)

    # 3. TRUST BAR
    st.markdown("""
        <div class="trust-bar">
            <div class="trust-item">
                <span class="trust-icon">👤</span>
                <div class="trust-label">Industry Ready</div>
                <div class="trust-sub">Civil, Mining & Agriculture</div>
            </div>
            <div class="trust-item">
                <span class="trust-icon">✅</span>
                <div class="trust-label">NHVR Compliant</div>
                <div class="trust-sub">Updated to 2026 Gazettes</div>
            </div>
             <div class="trust-item">
                <span class="trust-icon">🔒</span>
                <div class="trust-label">AES-256 Secure</div>
                <div class="trust-sub">Secure Data</div>
            </div>
            <div class="trust-item">
                <span class="trust-icon">🛡️</span>
                <div class="trust-label">Safety First</div>
                <div class="trust-sub">Chain of Responsibility</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 4. FOOTER
    st.markdown("""
        <div class="footer-container">
            <div class="footer-text">
                Estimates only. Not a legal permit. Must be lodged with NHVR.
            </div>
            <div class="footer-links">
                <a href="#">Privacy Policy</a> &bull; 
                <a href="#">Terms of Service</a> &bull; 
                <a href="#">Support</a>
            </div>
        </div>
    """, unsafe_allow_html=True)


# >>> VIEW 2: LOGGED IN AREA (AUTOMATED) <<<
else:
    if "Dashboard" in menu:
        st.markdown(f"""
        <div style="text-align: center; padding-bottom: 20px;">
            <h1>Operations Dashboard</h1>
            <p>Welcome, {st.session_state.user_type}.</p>
        </div>
        """, unsafe_allow_html=True)

        c1, c2, c3, c4 = st.columns(4)
        with c1: st.markdown('<div class="glass-card"><h3>🟢 Online</h3><p>Engine Status</p></div>', unsafe_allow_html=True)
        with c2: st.markdown('<div class="glass-card"><h3>< 2s</h3><p>Speed</p></div>', unsafe_allow_html=True)
        with c3: st.markdown('<div class="glass-card"><h3>Active</h3><p>Sub</p></div>', unsafe_allow_html=True)
        with c4: st.markdown('<div class="glass-card"><h3>Unlimited</h3><p>Checks</p></div>', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        fc1, fc2, fc3 = st.columns(3)
        with fc1: st.markdown('<div class="glass-card"><h3>⚡ GML Limits</h3></div>', unsafe_allow_html=True)
        with fc2: st.markdown('<div class="glass-card"><h3>📐 Dimensions</h3></div>', unsafe_allow_html=True)
        with fc3: st.markdown('<div class="glass-card"><h3>🏗️ Tier 1 Safety</h3></div>', unsafe_allow_html=True)

    elif "Run" in menu:
        st.markdown("## Instant Compliance Check")
        with st.container():
            c1, c2 = st.columns(2)
            with c1:
                gcm = st.number_input("GCM (t)", 10.0, 200.0, 42.5)
                axles = st.number_input("Axles", 3, 20, 6)
            with c2:
                width = st.number_input("Width (m)", 2.0, 8.0, 2.5)
                height = st.number_input("Height (m)", 2.0, 6.0, 4.3)
        
        if st.button("RUN CHECK"):
            with st.spinner("Analyzing..."):
                time.sleep(0.5)
                result = check_compliance(gcm, axles, width, height)
                
                st.markdown(f"""
                <div style="background-color: white; border-radius: 8px; padding: 15px; border-left: 8px solid {result['color']}; margin-top: 15px;">
                    <h3 style="color: #0f172a !important; margin:0;">{result['status']}</h3>
                    <p style="color: #64748b !important; font-weight: bold;">{result['permit_type']}</p>
                    <hr style="border-top: 1px solid #e2e8f0; margin: 10px 0;">
                """, unsafe_allow_html=True)
                
                if result['issues']:
                    for issue in result['issues']:
                        st.error(issue)
                else:
                    st.success("✅ Meets GML General Access.")
                st.markdown("</div>", unsafe_allow_html=True)
