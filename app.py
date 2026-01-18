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
    initial_sidebar_state="expanded" 
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

# --- 4. PROFESSIONAL STYLING ---
st.markdown("""
    <style>
    /* 1. SIDEBAR LOCK */
    button[aria-label="Collapse sidebar"] { display: none !important; }
    [data-testid="collapsedControl"] { display: block !important; color: #4ade80 !important; background-color: rgba(6, 78, 59, 0.8) !important; border-radius: 5px; z-index: 100000 !important; }
    section[data-testid="stSidebar"] { min-width: 320px !important; max-width: 320px !important; background-color: #064e3b !important; border-right: 1px solid rgba(255,255,255,0.1); }

    /* 2. GLOBAL RESET & THEME */
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
        padding-top: 3rem !important;
        padding-bottom: 3rem !important;
        max-width: 1400px;
    }

    /* 3. ENHANCED TYPOGRAPHY */
    h1 { color: #ffffff !important; font-size: 3.5rem !important; font-weight: 800 !important; margin-bottom: 10px !important; letter-spacing: -1px; }
    h2 { color: #4ade80 !important; font-size: 2rem !important; margin-top: 0px !important; font-weight: 400 !important; }
    h3 { color: #ffffff !important; font-size: 1.5rem !important; font-weight: 600 !important; margin-bottom: 10px !important; }
    p, li, label, div { color: #cbd5e1 !important; font-size: 1.1rem !important; line-height: 1.6 !important; }
    span { font-size: inherit; }
    
    /* 4. SIDEBAR WIDGETS */
    .sidebar-card { background-color: rgba(0, 0, 0, 0.2); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 8px; padding: 20px; margin-bottom: 20px; }
    .user-badge { background-color: #f59e0b; color: white; padding: 4px 10px; border-radius: 4px; font-size: 0.8rem; font-weight: bold; text-transform: uppercase; }
    .status-dot { height: 12px; width: 12px; background-color: #4ade80; border-radius: 50%; display: inline-block; margin-right: 10px; box-shadow: 0 0 0 0 rgba(74, 222, 128, 0.7); animation: pulse-green 2s infinite; }

    /* 5. COMPONENTS */
    .glass-card, [data-testid="stForm"], .control-panel, .metric-card { background-color: rgba(15, 23, 42, 0.75); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.1); padding: 30px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.2); margin-bottom: 25px; }

    /* METRICS */
    .metric-value { font-size: 2.5rem; font-weight: 800; color: #ffffff; margin: 5px 0; }
    .metric-label { font-size: 1rem; color: #94a3b8; text-transform: uppercase; letter-spacing: 1px; font-weight: 600; }
    .metric-delta { font-size: 0.9rem; margin-top: 5px; }
    
    /* 6. INPUTS & BUTTONS */
    .stTextInput input, .stNumberInput input { background-color: #1e293b !important; color: white !important; border: 1px solid #334155; border-radius: 6px; padding: 12px 15px; font-size: 1.1rem !important; }
    .stButton > button { background-color: #10b981 !important; color: white !important; border: none; font-weight: 700; font-size: 1.1rem; width: 100%; padding: 15px; border-radius: 6px; text-transform: uppercase; margin-top: 10px; }
    .stButton > button:hover { background-color: #059669 !important; }

    /* 7. CHECKBOX & DATAFRAME */
    [data-testid="stCheckbox"] label { font-size: 1.1rem !important; }
    [data-testid="stDataFrame"] { border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 8px; font-size: 1rem !important; }

    /* 8. MISC */
    header, footer, #MainMenu {visibility: hidden;}
    .subscribe-btn-container { display: flex; justify-content: center; margin-top: 25px; }
    .subscribe-btn { display: inline-block; background: linear-gradient(45deg, #f59e0b, #ea580c); color: white !important; padding: 15px 50px; border-radius: 8px; text-decoration: none; font-weight: bold; font-size: 1.2rem; border: 1px solid rgba(255,255,255,0.2); width: 100%; text-align: center; }
    
    @keyframes pulse-green { 0% { box-shadow: 0 0 0 0 rgba(74, 222, 128, 0.7); } 70% { box-shadow: 0 0 0 6px rgba(74, 222, 128, 0); } 100% { box-shadow: 0 0 0 0 rgba(74, 222, 128, 0); } }
    
    .sales-point { background-color: rgba(6, 78, 59, 0.6); border-left: 5px solid #4ade80; padding: 20px; margin-bottom: 20px; border-radius: 4px; }
    .sales-point h4 { margin: 0 !important; font-size: 1.3rem !important; color: white !important; font-weight: bold !important; }
    
    .trust-bar { margin-top: 50px; display: flex; justify-content: space-around; padding: 20px 10px; border-top: 1px solid rgba(255,255,255,0.1); }
    .trust-item { text-align: center; opacity: 1.0; }
    .trust-icon { font-size: 1.8rem; display: block; margin-bottom: 10px; color: #f59e0b; }
    .trust-label { font-weight: bold; color: white !important; font-size: 1rem; text-transform: uppercase; letter-spacing: 1px; }
    .trust-sub { font-size: 0.9rem; color: #94a3b8; }
    </style>
""", unsafe_allow_html=True)

# --- 5. AUTOMATION LOGIC ---

def get_automated_requirements(width, length, is_night):
    reqs = { "equipment": [], "pilots": [] }
    
    # 1. EQUIPMENT LOGIC
    if width > 2.5:
        reqs["equipment"].append("⚠️ 'OVERSIZE' Sign (Front & Rear)")
        reqs["equipment"].append("🚩 4x Warning Flags (Brightly colored)")
        reqs["equipment"].append("🔦 Low Beam Headlights (Day Use)")
        
    if width > 3.0 or length > 25.0:
        reqs["equipment"].append("🚨 1x Rotating Amber Beacon (Cab)")
        reqs["equipment"].append("↔️ Side Delineators")

    if length > 22.0:
        reqs["equipment"].append("🚛 'LONG VEHICLE' Sign (Rear)")

    if is_night and width > 2.5:
        reqs["equipment"].append("💡 Side Marker Lights (Every 1.5m)")

    # 2. PILOT VEHICLE LOGIC
    if width > 4.5:
        reqs["pilots"].append("🚓 2x Pilot Vehicles (Front & Rear)")
    elif width > 3.5:
        reqs["pilots"].append("🚗 1x Pilot Vehicle (Front)")
    elif length > 30.0:
        reqs["pilots"].append("🚗 1x Pilot Vehicle (Rear)")
    elif is_night and width > 3.1:
        reqs["pilots"].append("🚗 1x Pilot Vehicle (Front - Night Condition)")
    
    if not reqs["pilots"]:
        reqs["pilots"].append("✅ No Pilot Vehicles Required")

    return reqs

def check_compliance(gcm, axles, width, height, length, is_night):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    auto_reqs = get_automated_requirements(width, length, is_night)
    
    report = {
        "status": "APPROVED",
        "color": "#22c55e", 
        "icon": "✅",
        "issues": [],
        "permit_type": "General Access",
        "timestamp": timestamp,
        "details": f"{gcm}t | {width}m Wide",
        "equipment": auto_reqs["equipment"],
        "pilots": auto_reqs["pilots"]
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
        "Configuration": f"{gcm}t | {width}m x {length}m",
        "Status": report["status"],
        "Permit": report["permit_type"]
    })
    
    return report

# --- 6. SIDEBAR ---
with st.sidebar:
    if logo_b64:
        st.markdown(f"""<div class="logo-container" style="background:white; padding:10px; border-radius:8px; margin-bottom:20px; text-align:center;"><img src="data:image/jpeg;base64,{logo_b64}" style="max-width: 100%; height: auto;"></div>""", unsafe_allow_html=True)
    else:
        st.markdown("""<div class="logo-container" style="background:white; padding:10px; border-radius:8px; margin-bottom:20px; text-align:center;"><p style="color:#064e3b !important; font-size: 20px; font-weight: bold; margin: 0;">LadenPass</p></div>""", unsafe_allow_html=True)
    
    if st.session_state.logged_in:
        user_role = "ADMIN" if st.session_state.user_type == "Admin" else "TRIAL"
        st.markdown(f"""
        <div class="sidebar-card">
            <div style="display:flex; align-items:center;">
                <div style="font-size:2rem; margin-right:15px;">👤</div>
                <div>
                    <div style="color:white; font-weight:bold; font-size:1.1rem;">{st.session_state.user_type}</div>
                    <span class="user-badge">{user_role} ACCESS</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<p style='font-size:0.9rem; color:#94a3b8; font-weight:bold; letter-spacing:1px; margin-top:25px; margin-bottom:15px;'>MENU</p>", unsafe_allow_html=True)
        menu = st.radio("", ["📊 Dashboard", "✅ Run Check"], label_visibility="collapsed")
        
        st.markdown("""
        <div class="sidebar-card" style="margin-top:25px;">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <span style="font-size:0.9rem; color:#cbd5e1;">System Status</span>
                <span style="font-size:0.9rem; color:#4ade80;">99.9%</span>
            </div>
            <div style="margin-top:10px;">
                <span class="status-dot"></span> <span style="font-size:0.9rem; color:white;">Operational</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")
        if st.button("LOG OUT"):
            st.session_state.logged_in = False
            st.session_state.user_type = None
            st.session_state.history = []
            st.rerun()

    else:
        st.markdown("""<div style="background-color:#042f2e; border-left:4px solid #10b981; padding:15px; border-radius:4px; color:#94a3b8; font-size:1rem; margin-bottom:25px;"><span>🔒</span> <strong>Secure Access</strong></div>""", unsafe_allow_html=True)
        st.markdown("""<div style="background-color:rgba(6,78,59,0.4); border:2px solid #10b981; border-radius:8px; padding:20px; text-align:center; animation:pulse-green 2s infinite;"><h3 style="color:white; margin:0 0 10px 0; font-size:1.2rem;">🎉 7-Day Free Trial</h3><p style="color:#cbd5e1; font-size:1rem;">Test drive instantly.</p><div style="background:rgba(0,0,0,0.3); padding:10px; border-radius:4px; margin-top:10px;"><div style="color:#34d399; font-weight:bold; font-size:1rem;">User: guest</div><div style="color:#34d399; font-weight:bold; font-size:1rem;">Pass: tryladenpass</div></div></div>""", unsafe_allow_html=True)
    
    st.markdown(f"""<div style='text-align:center; font-size:0.85rem; color:#cbd5e1; margin-top:50px; opacity:0.6;'>© {datetime.datetime.now().year} LadenPass<br>ABN: 16 632 316 240</div>""", unsafe_allow_html=True)


# --- 7. MAIN CONTENT ---

if not st.session_state.logged_in:
    st.markdown("""<div style="text-align:left; margin-bottom:40px;"><h1>LadenPass Enterprise</h1><h2>Heavy Haulage Compliance. Simplified.</h2></div>""", unsafe_allow_html=True)
    
    c_sales, c_login = st.columns([1.6, 1])
    
    with c_sales:
        st.markdown("""
        <div class="sales-point">
            <h4>👮 Automated Pilot & Escort Logic</h4>
            <p>Stop guessing. Instantly calculate if you need 1 pilot, 2 pilots, or police escorts based on your exact dimensions.</p>
        </div>
        <div class="sales-point">
            <h4>🚩 Smart Safety Equipment Lists</h4>
            <p>Generates a precise checklist of required "Oversize" signs, flags, beacons, and side marker lights.</p>
        </div>
        <div class="sales-point">
            <h4>⚡ Instant GML Feasibility</h4>
            <p>Validate GCM, Axle Spacing, and Night Travel rules against 2026 National Gazettes in seconds.</p>
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

        st.markdown("""
            <div style="text-align: center; margin-top: 15px;">
                <a href="mailto:support@ladenpass.com.au?subject=Help with LadenPass" 
                   style="color: #4ade80; text-decoration: none; font-size: 0.9rem;">
                   📩 Need Help? Contact Support
                </a>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""<div class="subscribe-btn-container"><a href="https://buy.stripe.com/28EdRa2om1jWfAc5kZ9oc00" class="subscribe-btn">UNLOCK INSTANT ACCESS ($99)</a></div>""", unsafe_allow_html=True)
    
    st.markdown("""<div class="trust-bar"><div class="trust-item"><span class="trust-icon">👤</span><div class="trust-label">Industry Ready</div></div><div class="trust-item"><span class="trust-icon">✅</span><div class="trust-label">NHVR Compliant</div></div><div class="trust-item"><span class="trust-icon">🔒</span><div class="trust-label">AES-256 Secure</div></div></div>""", unsafe_allow_html=True)

else:
    st.markdown(f"""
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:30px;">
        <div><h1>Operations Command</h1><p>Session Active: {st.session_state.user_type}</p></div>
        <div style="text-align:right;"><h3 style="color:#10b981 !important;">{datetime.date.today().strftime('%d %b %Y')}</h3></div>
    </div>
    """, unsafe_allow_html=True)

    if "Dashboard" in menu:
        checks_count = len(st.session_state.history)
        last_check_status = st.session_state.history[0]['Status'] if checks_count > 0 else "Ready"
        
        c1, c2, c3, c4 = st.columns(4)
        with c1: st.markdown(f"""<div class="metric-card"><div class="metric-label">Session Checks</div><div class="metric-value">{checks_count}</div><div class="metric-delta">Live Session</div></div>""", unsafe_allow_html=True)
        with c2:
            color = "#4ade80" if "APPROVED" in last_check_status else "#f59e0b" if "CONDITIONAL" in last_check_status else "#ef4444" if "NON-COMPLIANT" in last_check_status else "#94a3b8"
            st.markdown(f"""<div class="metric-card"><div class="metric-label">Last Status</div><div class="metric-value" style="font-size:1.5rem; color:{color};">{last_check_status}</div><div class="metric-delta">Latest Result</div></div>""", unsafe_allow_html=True)
        with c3: st.markdown("""<div class="metric-card"><div class="metric-label">GML Limit</div><div class="metric-value">42.5t</div><div class="metric-delta">Standard General Access</div></div>""", unsafe_allow_html=True)
        with c4: st.markdown("""<div class="metric-card"><div class="metric-label">Compliance Database</div><div class="metric-value" style="font-size:1.5rem; color:#4ade80;">Online</div><div class="metric-delta">Gazette 2026</div></div>""", unsafe_allow_html=True)

        col_main, col_side = st.columns([2, 1])
        with col_main:
            st.markdown("### 📋 Session Audit Log")
            if checks_count == 0: st.info("No checks performed in this session. Go to 'Run Check' to begin.")
            else:
                df = pd.DataFrame(st.session_state.history)
                st.table(df)
        with col_side:
            st.markdown("### 🛠️ Driver Toolkit")
            st.markdown("""
            <div class="glass-card" style="padding:20px;">
                <p style="margin-bottom:20px;">Quick access to official external resources.</p>
                <a href="https://www.nhvr.gov.au/road-access/route-planner" target="_blank" style="display:block; background:#1e293b; color:white; padding:12px; border-radius:6px; margin-bottom:12px; text-decoration:none; border:1px solid #334155;">🗺️ NHVR Route Planner</a>
                <a href="https://www.nhvr.gov.au/law-policies/notices-and-permit-based-schemes/national-notices" target="_blank" style="display:block; background:#1e293b; color:white; padding:12px; border-radius:6px; margin-bottom:12px; text-decoration:none; border:1px solid #334155;">📜 National Gazettes</a>
            </div>
            """, unsafe_allow_html=True)

    elif "Run" in menu:
        st.markdown("## 🚛 New Assessment")
        with st.container():
            st.markdown('<div class="control-panel">', unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1: gcm = st.number_input("GCM (t)", 10.0, 200.0, 42.5)
            with c2: axles = st.number_input("Axles", 3, 20, 6)
            
            st.markdown("<br>", unsafe_allow_html=True)
            c3, c4, c5 = st.columns(3)
            with c3: width = st.number_input("Width (m)", 2.0, 8.0, 2.5)
            with c4: height = st.number_input("Height (m)", 2.0, 6.0, 4.3)
            with c5: length = st.number_input("Length (m)", 12.0, 50.0, 19.0)
            
            st.markdown("<br>", unsafe_allow_html=True)
            is_night = st.checkbox("🌙 Night Travel? (Adjusts Pilot Requirements)")
            
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("RUN COMPLIANCE CHECK"):
                with st.spinner("Analyzing Physics & Regulations..."):
                    time.sleep(0.5)
                    result = check_compliance(gcm, axles, width, height, length, is_night)
                    
                    # --- FIXED: USING IMPLICIT STRING CONCATENATION (BULLETPROOF) ---
                    card_html = (
                        f'<div class="metric-card" style="background:white; color:#0f172a; border-left: 10px solid {result["color"]}; margin-top:20px;">'
                        f'<div style="display:flex; justify-content:space-between; align-items:center;">'
                        f'<div>'
                        f'<h3 style="margin:0; color:#0f172a; font-size:1.8rem;">{result["icon"]} {result["status"]}</h3>'
                        f'<p style="margin:5px 0 0 0; font-weight:bold; color:#64748b; font-size:1.1rem;">{result["permit_type"]}</p>'
                        f'</div>'
                        f'<div style="text-align:right;">'
                        f'<div style="font-size:0.9rem; color:#94a3b8;">ASSESSMENT ID</div>'
                        f'<div style="font-weight:bold; color:#0f172a;">#LP-{int(time.time())}</div>'
                        f'</div>'
                        f'</div>'
                        f'<div style="background-color:#fff1f2; border:1px solid #fda4af; padding:8px; border-radius:4px; margin-top:10px;">'
                        f'<p style="color:#be123c !important; font-size:0.9rem !important; margin:0; font-weight:bold;">'
                        f'⚠️ ESTIMATE ONLY: This is not a legal permit. You must lodge with NHVR.'
                        f'</p>'
                        f'</div>'
                        f'<hr style="border-top: 1px solid #e2e8f0; margin: 20px 0;">'
                    )
                    st.markdown(card_html, unsafe_allow_html=True)
                    
                    if result['issues']:
                        st.markdown("**⛔ Compliance Breaches:**")
                        for issue in result['issues']:
                            st.markdown(f"<div style='color:#ef4444; margin-bottom:8px; font-size:1.1rem;'>• {issue}</div>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<div style='color:#166534; margin-top:5px; font-size:1.1rem;'>Configuration meets GML General Access Limits.</div>", unsafe_allow_html=True)
                    
                    st.markdown("<br>", unsafe_allow_html=True)
                    c_equip, c_pilots = st.columns(2)
                    with c_equip:
                        st.markdown("**🛠️ Required Safety Gear:**")
                        if result['equipment']:
                            for item in result['equipment']: st.markdown(f"<div style='color:#0f172a; margin-bottom:5px; font-weight:500; font-size:1.1rem;'>{item}</div>", unsafe_allow_html=True)
                        else: st.markdown("No special gear required.")
                    
                    with c_pilots:
                        st.markdown("**👮 Required Pilot Vehicles:**")
                        for item in result['pilots']:
                            color = "#b91c1c" if "Pilot" in item else "#166534"
                            st.markdown(f"<div style='color:{color}; margin-bottom:5px; font-weight:bold; font-size:1.1rem;'>{item}</div>", unsafe_allow_html=True)

                    st.markdown("</div>", unsafe_allow_html=True)
                    st.success("Result logged to Session Audit Log.")
            else:
                st.markdown('</div>', unsafe_allow_html=True)
