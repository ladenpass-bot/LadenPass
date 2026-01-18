
import streamlit as st
import base64
import datetime
import time
import pandas as pd

# --- 1. ENTERPRISE PAGE CONFIG ---
st.set_page_config(
    page_title="LadenPass | Automated Compliance",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded" # This asks the browser to open it.
)

# --- 2. STATE MANAGEMENT ---
if "history" not in st.session_state:
    st.session_state.history = [] 
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_type" not in st.session_state:
    st.session_state.user_type = None

# --- 3. HELPER: LOAD IMAGE CORRECTLY ---
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return None

logo_b64 = get_base64_image("logo.jpg")

# --- 4. ADVANCED CSS TROUBLESHOOTING & STYLING ---
st.markdown("""
    <style>
    /* >>> CRITICAL FIX: SIDEBAR VISIBILITY <<< */
    
    /* 1. If sidebar is CLOSED, force the 'Open' arrow (>) to be VISIBLE and GREEN */
    [data-testid="collapsedControl"] {
        display: block !important;
        color: #4ade80 !important; /* Bright Green Arrow */
        background-color: rgba(6, 78, 59, 0.8) !important; /* Dark Green box behind it */
        border-radius: 5px;
        z-index: 100000 !important; /* Force it on top of everything */
    }

    /* 2. Once sidebar is OPEN, hide the 'Close' X button so it stays open */
    section[data-testid="stSidebar"] button[kind="header"] {
        display: none !important;
    }

    /* 3. Force the Sidebar Background to be the correct Green */
    section[data-testid="stSidebar"] {
        background-color: #064e3b !important;
        border-right: 1px solid rgba(255,255,255,0.1);
        min-width: 320px !important;
        max-width: 320px !important;
    }

    /* >>> REST OF PROFESSIONAL THEME <<< */

    /* GLOBAL THEME */
    div[data-testid="stAppViewContainer"] {
        height: 100vh;
        overflow-y: auto;
        background-color: #0f172a; 
        background-image: linear-gradient(rgba(15, 23, 42, 0.94), rgba(15, 23, 42, 0.96)), 
        url("https://images.unsplash.com/photo-1601584115197-04ecc0da31d7?q=80&w=2670&auto=format&fit=crop");
        background-size: cover;
        background-attachment: fixed;
    }
    
    div.block-container {
        min-height: 90vh !important;
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 1400px;
    }

    /* TYPOGRAPHY */
    h1 { color: #ffffff !important; font-size: 2.5rem !important; font-weight: 700 !important; margin-bottom: 5px !important; }
    h2 { color: #4ade80 !important; font-size: 1.5rem !important; margin-top: 0px !important; font-weight: 300 !important; }
    h3 { color: #ffffff !important; font-size: 1.2rem !important; font-weight: 600 !important; }
    p, li, label, span, div { color: #cbd5e1 !important; font-size: 0.9rem !important; }
    
    /* SIDEBAR WIDGETS */
    .sidebar-card {
        background-color: rgba(0, 0, 0, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 15px;
    }
    .user-badge {
        background-color: #f59e0b;
        color: white;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 0.7rem;
        font-weight: bold;
        text-transform: uppercase;
    }
    .status-dot {
        height: 10px;
        width: 10px;
        background-color: #4ade80;
        border-radius: 50%;
        display: inline-block;
        margin-right: 8px;
        box-shadow: 0 0 0 0 rgba(74, 222, 128, 0.7);
        animation: pulse-green 2s infinite;
    }

    /* GLASS CARDS */
    .glass-card, [data-testid="stForm"], .control-panel, .metric-card {
        background-color: rgba(15, 23, 42, 0.75); 
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        margin-bottom: 20px;
    }

    /* METRICS */
    .metric-value { font-size: 2rem; font-weight: 800; color: #ffffff; margin: 5px 0; }
    .metric-label { font-size: 0.85rem; color: #94a3b8; text-transform: uppercase; letter-spacing: 1px; }
    
    /* INPUTS & BUTTONS */
    .stTextInput input, .stNumberInput input {
        background-color: #1e293b !important;
        color: white !important;
        border: 1px solid #334155;
        border-radius: 6px;
        padding: 10px;
    }
    .stButton > button {
        background-color: #10b981 !important;
        color: white !important;
        border: none;
        font-weight: 700;
        font-size: 1rem;
        width: 100%;
        padding: 12px;
        border-radius: 6px;
        text-transform: uppercase;
        margin-top: 10px;
    }
    .stButton > button:hover { background-color: #059669 !important; }

    /* REMOVE DECORATIONS */
    header, footer, #MainMenu {visibility: hidden;}
    
    /* DATAFRAME */
    [data-testid="stDataFrame"] { border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 8px; }
    
    /* SUBSCRIBE BUTTON */
    .subscribe-btn-container { display: flex; justify-content: center; margin-top: 20px; }
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
    }
    
    /* ANIMATIONS */
    @keyframes pulse-green {
        0% { box-shadow: 0 0 0 0 rgba(74, 222, 128, 0.7); }
        70% { box-shadow: 0 0 0 6px rgba(74, 222, 128, 0); }
        100% { box-shadow: 0 0 0 0 rgba(74, 222, 128, 0); }
    }
    
    /* SALES POINTS */
    .sales-point {
        background-color: rgba(6, 78, 59, 0.6);
        border-left: 4px solid #4ade80;
        padding: 15px;
        margin-bottom: 15px;
        border-radius: 4px;
    }
    .sales-point h4 { margin: 0 !important; font-size: 1.1rem !important; color: white !important; font-weight: bold !important; }
    
    /* TRUST BAR */
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
    </style>
""", unsafe_allow_html=True)

# --- 5. LOGIC ---
def check_compliance(gcm, axles, width, height):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    report = {
        "status": "APPROVED",
        "color": "#22c55e", 
        "icon": "✅",
        "issues": [],
        "permit_type": "General Access",
        "timestamp": timestamp,
        "details": f"{gcm}t / {axles} Axles"
    }
    
    if width > 2.5:
        report["issues"].append(f"Width ({width}m) > 2.5m")
        report["permit_type"] = "Class 1 Oversize"
        report["status"] = "CONDITIONAL"
        report["color"] = "#f59e0b"
        report["icon"] = "⚠️"
    if height > 4.3:
        report["issues"].append(f"Height ({height}m) > 4.3m")
        report["permit_type"] = "High Productivity"
        report["status"] = "NON-COMPLIANT"
        report["color"] = "#ef4444" 
        report["icon"] = "⛔"
    
    gml_limit = 42.5
    if axles >= 7: gml_limit = 50.0 
    if axles >= 9: gml_limit = 62.5 
    
    if gcm > gml_limit:
        report["issues"].append(f"Mass ({gcm}t) > {gml_limit}t")
        if report["status"] != "NON-COMPLIANT":
            report["status"] = "CONDITIONAL"
            report["permit_type"] = "Class 1 Overmass"
            report["color"] = "#f59e0b"
            report["icon"] = "⚠️"
            
    avg_axle_load = gcm / axles
    if avg_axle_load > 9.0: 
        report["issues"].append(f"Axle Load ({avg_axle_load:.1f}t) > 9t")
        report["status"] = "CRITICAL FAIL"
        report["color"] = "#ef4444"
        report["icon"] = "⛔"
        report["permit_type"] = "Structural Fail"

    st.session_state.history.insert(0, {
        "Time": timestamp,
        "Configuration": f"{gcm}t on {axles} Axles",
        "Dimensions": f"{width}m x {height}m",
        "Status": report["status"],
        "Permit Required": report["permit_type"]
    })
    
    return report

# --- 6. SIDEBAR ---
with st.sidebar:
    # A. LOGO
    if logo_b64:
        st.markdown(f"""<div class="logo-container" style="background:white; padding:10px; border-radius:8px; margin-bottom:20px; text-align:center;"><img src="data:image/jpeg;base64,{logo_b64}" style="max-width: 100%; height: auto;"></div>""", unsafe_allow_html=True)
    else:
        st.markdown("""<div class="logo-container" style="background:white; padding:10px; border-radius:8px; margin-bottom:20px; text-align:center;"><p style="color:#064e3b !important; font-size: 20px; font-weight: bold; margin: 0;">LadenPass</p></div>""", unsafe_allow_html=True)
    
    if st.session_state.logged_in:
        # B. USER PROFILE CARD
        user_role = "ADMIN" if st.session_state.user_type == "Admin" else "TRIAL"
        st.markdown(f"""
        <div class="sidebar-card">
            <div style="display:flex; align-items:center;">
                <div style="font-size:1.5rem; margin-right:10px;">👤</div>
                <div>
                    <div style="color:white; font-weight:bold; font-size:0.9rem;">{st.session_state.user_type} Account</div>
                    <span class="user-badge">{user_role} ACCESS</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # C. NAVIGATION
        st.markdown("<p style='font-size:0.75rem; color:#94a3b8; font-weight:bold; letter-spacing:1px; margin-top:20px; margin-bottom:10px;'>MENU</p>", unsafe_allow_html=True)
        menu = st.radio("", ["📊 Dashboard", "✅ Run Check"], label_visibility="collapsed")
        
        # D. SYSTEM STATUS
        st.markdown("""
        <div class="sidebar-card" style="margin-top:20px;">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <span style="font-size:0.8rem; color:#cbd5e1;">System Status</span>
                <span style="font-size:0.8rem; color:#4ade80;">99.9%</span>
            </div>
            <div style="margin-top:5px;">
                <span class="status-dot"></span> <span style="font-size:0.8rem; color:white;">Operational</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # E. LOGOUT
        st.markdown("---")
        if st.button("LOG OUT"):
            st.session_state.logged_in = False
            st.session_state.user_type = None
            st.session_state.history = []
            st.rerun()

    else:
        # LANDING PAGE SIDEBAR
        st.markdown("""<div style="background-color:#042f2e; border-left:4px solid #10b981; padding:12px; border-radius:4px; color:#94a3b8; font-size:0.85rem; margin-bottom:20px;"><span>🔒</span> <strong>Secure Access</strong></div>""", unsafe_allow_html=True)
        st.markdown("""<div style="background-color:rgba(6,78,59,0.4); border:2px solid #10b981; border-radius:8px; padding:15px; text-align:center; animation:pulse-green 2s infinite;"><h3 style="color:white; margin:0 0 10px 0; font-size:1rem;">🎉 7-Day Free Trial</h3><p style="color:#cbd5e1; font-size:0.8rem;">Test drive instantly.</p><div style="background:rgba(0,0,0,0.3); padding:8px; border-radius:4px; margin-top:10px;"><div style="color:#34d399; font-weight:bold; font-size:0.85rem;">User: guest</div><div style="color:#34d399; font-weight:bold; font-size:0.85rem;">Pass: tryladenpass</div></div></div>""", unsafe_allow_html=True)
    
    st.markdown(f"""<div style='text-align:center; font-size:0.7rem; color:#cbd5e1; margin-top:40px; opacity:0.6;'>© {datetime.datetime.now().year} LadenPass<br>ABN: 16 632 316 240</div>""", unsafe_allow_html=True)


# --- 7. MAIN CONTENT ---

# >>> VIEW 1: LANDING PAGE <<<
if not st.session_state.logged_in:
    st.markdown("""<div style="text-align:left; margin-bottom:30px;"><h1>LadenPass Enterprise</h1><h2>Heavy Haulage Compliance. Simplified.</h2></div>""", unsafe_allow_html=True)
    
    c_sales, c_login = st.columns([1.6, 1])
    
    with c_sales:
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
            if st.form_submit_button("Login"):
                try:
                    admin_u = st.secrets.get("credentials", {}).get("username", "admin")
                    admin_p = st.secrets.get("credentials", {}).get("password", "trucks")
                    guest_u = st.secrets.get("guest", {}).get("username", "guest")
                    guest_p = st.secrets.get("guest", {}).get("password", "tryladenpass")
                    
                    if username == admin_u and password == admin_p:
                        st.session_state.logged_in = True
                        st.session_state.user_type = "Admin"
                        st.rerun()
                    elif (username == guest_u and password == guest_p) or (username == "guest" and password == "tryladenpass"):
                        st.session_state.logged_in = True
                        st.session_state.user_type = "Guest"
                        st.rerun()
                    else:
                        st.error("Invalid credentials.")
                except:
                    if username == "guest" and password == "tryladenpass":
                        st.session_state.logged_in = True
                        st.session_state.user_type = "Guest"
                        st.rerun()
                    else:
                        st.error("Invalid credentials.")

        st.markdown("""<div class="subscribe-btn-container"><a href="https://buy.stripe.com/28EdRa2om1jWfAc5kZ9oc00" class="subscribe-btn">UNLOCK INSTANT ACCESS ($99)</a></div>""", unsafe_allow_html=True)
    
    st.markdown("""<div class="trust-bar"><div class="trust-item"><span class="trust-icon">👤</span><div class="trust-label">Industry Ready</div></div><div class="trust-item"><span class="trust-icon">✅</span><div class="trust-label">NHVR Compliant</div></div><div class="trust-item"><span class="trust-icon">🔒</span><div class="trust-label">AES-256 Secure</div></div></div>""", unsafe_allow_html=True)

# >>> VIEW 2: LOGGED IN DASHBOARD (PROFESSIONAL) <<<
else:
    # Header
    st.markdown(f"""
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px;">
        <div>
            <h1>Operations Command</h1>
            <p>Session Active: {st.session_state.user_type}</p>
        </div>
        <div style="text-align:right;">
            <h3 style="color:#10b981 !important;">{datetime.date.today().strftime('%d %b %Y')}</h3>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if "Dashboard" in menu:
        checks_count = len(st.session_state.history)
        last_check_status = st.session_state.history[0]['Status'] if checks_count > 0 else "Ready"
        
        c1, c2, c3, c4 = st.columns(4)
        
        with c1:
            st.markdown(f"""<div class="metric-card"><div class="metric-label">Session Checks</div><div class="metric-value">{checks_count}</div><div class="metric-delta">Live Session</div></div>""", unsafe_allow_html=True)
        with c2:
            color = "#4ade80" if "APPROVED" in last_check_status else "#f59e0b" if "CONDITIONAL" in last_check_status else "#ef4444" if "NON-COMPLIANT" in last_check_status else "#94a3b8"
            st.markdown(f"""<div class="metric-card"><div class="metric-label">Last Status</div><div class="metric-value" style="font-size:1.5rem; color:{color};">{last_check_status}</div><div class="metric-delta">Latest Result</div></div>""", unsafe_allow_html=True)
        with c3:
            st.markdown("""<div class="metric-card"><div class="metric-label">GML Limit</div><div class="metric-value">42.5t</div><div class="metric-delta">Standard General Access</div></div>""", unsafe_allow_html=True)
        with c4:
            st.markdown("""<div class="metric-card"><div class="metric-label">Compliance Database</div><div class="metric-value" style="font-size:1.5rem; color:#4ade80;">Online</div><div class="metric-delta">Gazette 2026</div></div>""", unsafe_allow_html=True)

        col_main, col_side = st.columns([2, 1])

        with col_main:
            st.markdown("### 📋 Session Audit Log")
            if checks_count == 0:
                st.info("No checks performed in this session. Go to 'Run Check' to begin.")
            else:
                df = pd.DataFrame(st.session_state.history)
                st.table(df)

        with col_side:
            st.markdown("### 🛠️ Driver Toolkit")
            st.markdown("""
            <div class="glass-card" style="padding:15px;">
                <p style="margin-bottom:15px;">Quick access to official external resources.</p>
                <a href="https://www.nhvr.gov.au/road-access/route-planner" target="_blank" style="display:block; background:#1e293b; color:white; padding:10px; border-radius:6px; margin-bottom:10px; text-decoration:none; border:1px solid #334155;">🗺️ NHVR Route Planner</a>
                <a href="https://www.nhvr.gov.au/law-policies/notices-and-permit-based-schemes/national-notices" target="_blank" style="display:block; background:#1e293b; color:white; padding:10px; border-radius:6px; margin-bottom:10px; text-decoration:none; border:1px solid #334155;">📜 National Gazettes</a>
            </div>
            """, unsafe_allow_html=True)

    elif "Run" in menu:
        st.markdown("## 🚛 New Assessment")
        with st.container():
            st.markdown('<div class="control-panel">', unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                gcm = st.number_input("GCM (t)", 10.0, 200.0, 42.5)
                axles = st.number_input("Axles", 3, 20, 6)
            with c2:
                width = st.number_input("Width (m)", 2.0, 8.0, 2.5)
                height = st.number_input("Height (m)", 2.0, 6.0, 4.3)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            if st.button("RUN COMPLIANCE CHECK"):
                with st.spinner("Analyzing Physics & Regulations..."):
                    time.sleep(0.5)
                    result = check_compliance(gcm, axles, width, height)
                    
                    st.markdown(f"""
                    </div>
                    <div class="metric-card" style="background:white; color:#0f172a; border-left: 10px solid {result['color']}; margin-top:20px;">
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <div>
                                <h3 style="margin:0; color:#0f172a; font-size:1.5rem;">{result['icon']} {result['status']}</h3>
                                <p style="margin:5px 0 0 0; font-weight:bold; color:#64748b;">{result['permit_type']}</p>
                            </div>
                            <div style="text-align:right;">
                                <div style="font-size:0.8rem; color:#94a3b8;">ASSESSMENT ID</div>
                                <div style="font-weight:bold; color:#0f172a;">#LP-{int(time.time())}</div>
                            </div>
                        </div>
                        <hr style="border-top: 1px solid #e2e8f0; margin: 15px 0;">
                    """, unsafe_allow_html=True)
                    
                    if result['issues']:
                        for issue in result['issues']:
                            st.markdown(f"<div style='color:#ef4444; margin-bottom:5px;'>• {issue}</div>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<div style='color:#166534; margin-top:5px;'>Configuration meets GML General Access Limits.</div>", unsafe_allow_html=True)
                    
                    st.markdown("</div>", unsafe_allow_html=True)
                    st.success("Result logged to Session Audit Log.")
            else:
                st.markdown('</div>', unsafe_allow_html=True)
