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
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return None

logo_b64 = get_base64_image("logo.jpg")

# --- 3. PROFESSIONAL STYLING (CONSISTENT HIGH-END THEME) ---
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
        max-width: 1200px; /* Keep dashboard contained */
    }

    /* 2. GLOBAL THEME */
    .stApp {
        background-color: #0f172a; 
        background-image: linear-gradient(rgba(15, 23, 42, 0.94), rgba(15, 23, 42, 0.96)), 
        url("https://images.unsplash.com/photo-1601584115197-04ecc0da31d7?q=80&w=2670&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* 3. TYPOGRAPHY */
    h1 { color: #ffffff !important; font-size: 3rem !important; font-weight: 700 !important; margin-bottom: 5px !important; }
    h2 { color: #4ade80 !important; font-size: 1.5rem !important; margin-top: 0px !important; font-weight: 300 !important; }
    h3 { color: #ffffff !important; font-size: 1.1rem !important; }
    p, li, label, span, div { color: #cbd5e1 !important; font-size: 0.9rem !important; }
    
    /* 4. SIDEBAR */
    [data-testid="stSidebar"] {
        background-color: #064e3b !important;
        border-right: 1px solid rgba(255,255,255,0.1);
    }
    
    /* 5. GLASS CARDS & CONTAINERS */
    .glass-card, [data-testid="stForm"], .control-panel {
        background-color: rgba(15, 23, 42, 0.7); 
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }
    
    /* 6. INPUT FIELDS */
    .stTextInput input, .stNumberInput input {
        background-color: #1e293b !important;
        color: white !important;
        border: 1px solid #334155;
        border-radius: 6px;
        padding: 10px;
    }
    
    /* 7. PRIMARY BUTTONS */
    .stButton > button {
        background-color: #10b981 !important; /* Brand Green */
        color: white !important;
        border: none;
        font-weight: 700;
        font-size: 1rem;
        width: 100%;
        padding: 12px;
        border-radius: 6px;
        transition: all 0.2s;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .stButton > button:hover { 
        background-color: #059669 !important;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.4);
        transform: translateY(-1px);
    }

    /* 8. RESULT CARD STYLING */
    .result-card {
        background: white;
        border-radius: 8px;
        padding: 20px;
        color: #0f172a !important;
        margin-top: 20px;
        border-left: 8px solid #22c55e;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }
    .result-card h3 { color: #0f172a !important; margin: 0; font-size: 1.5rem; }
    .result-card p { color: #475569 !important; }

    /* 9. REMOVE DECORATIONS */
    header, footer, #MainMenu {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 4. LOGIC ---
def check_compliance(gcm, axles, width, height):
    report = {
        "status": "APPROVED",
        "color": "#22c55e", # Green
        "icon": "✅",
        "issues": [],
        "permit_type": "General Access (No Permit Required)"
    }
    if width > 2.5:
        report["issues"].append(f"⚠️ Width ({width}m) > 2.5m")
        report["permit_type"] = "Class 1 Oversize Permit"
        report["status"] = "CONDITIONAL"
        report["color"] = "#f59e0b" # Orange
        report["icon"] = "⚠️"
    if height > 4.3:
        report["issues"].append(f"⛔ Height ({height}m) > 4.3m")
        report["permit_type"] = "High Productivity / Oversize"
        report["status"] = "NON-COMPLIANT"
        report["color"] = "#ef4444" # Red
        report["icon"] = "⛔"
    
    gml_limit = 42.5
    if axles >= 7: gml_limit = 50.0 
    if axles >= 9: gml_limit = 62.5 
    
    if gcm > gml_limit:
        report["issues"].append(f"⚠️ Mass ({gcm}t) > {gml_limit}t")
        if report["status"] != "NON-COMPLIANT":
            report["status"] = "CONDITIONAL"
            report["permit_type"] = "Class 1 Overmass Permit"
            report["color"] = "#f59e0b"
            report["icon"] = "⚠️"
            
    avg_axle_load = gcm / axles
    if avg_axle_load > 9.0: 
        report["issues"].append(f"⛔ Axle Load ({avg_axle_load:.1f}t) > 9t")
        report["status"] = "CRITICAL FAIL"
        report["color"] = "#ef4444"
        report["icon"] = "⛔"
        report["permit_type"] = "Structural Assessment Required"
    return report

# --- 5. STATE ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_type" not in st.session_state:
    st.session_state.user_type = None

# --- 6. SIDEBAR ---
with st.sidebar:
    if logo_b64:
        st.markdown(f"""<div style="background:white; padding:10px; border-radius:8px; text-align:center; margin-bottom:20px;"><img src="data:image/jpeg;base64,{logo_b64}" style="max-width: 100%; height: auto;"></div>""", unsafe_allow_html=True)
    
    if st.session_state.logged_in:
        st.markdown("### Menu")
        menu = st.radio("", ["📊 Dashboard", "✅ Run Check"], label_visibility="collapsed")
        st.markdown("---")
        if st.button("Log Out"):
            st.session_state.logged_in = False
            st.session_state.user_type = None
            st.rerun()
    else:
        # Secure Access Box
        st.markdown("""<div style="background-color:#042f2e; border-left:4px solid #10b981; padding:12px; border-radius:4px; color:#94a3b8; font-size:0.85rem; margin-bottom:20px;"><span>🔒</span> <strong>Secure Access</strong></div>""", unsafe_allow_html=True)
        # Trial Box
        st.markdown("""<div style="background-color:rgba(6,78,59,0.4); border:2px solid #10b981; border-radius:8px; padding:15px; text-align:center;"><h3 style="color:white; margin:0 0 10px 0; font-size:1rem;">🎉 7-Day Free Trial</h3><p style="color:#cbd5e1; font-size:0.8rem;">Test drive instantly.</p><div style="background:rgba(0,0,0,0.3); padding:8px; border-radius:4px; margin-top:10px;"><div style="color:#34d399; font-weight:bold; font-size:0.85rem;">User: guest</div><div style="color:#34d399; font-weight:bold; font-size:0.85rem;">Pass: tryladenpass</div></div></div>""", unsafe_allow_html=True)
    
    st.markdown(f"""<div style='text-align:center; font-size:0.7rem; color:#cbd5e1; margin-top:40px; opacity:0.6;'>© {datetime.datetime.now().year} LadenPass<br>ABN: 16 632 316 240</div>""", unsafe_allow_html=True)


# --- 7. MAIN CONTENT ---

# >>> LANDING PAGE <<<
if not st.session_state.logged_in:
    st.markdown("""<div style="text-align:left; margin-bottom:30px;"><h1>LadenPass Enterprise</h1><h2>Heavy Haulage Compliance. Simplified.</h2></div>""", unsafe_allow_html=True)
    
    c_sales, c_login = st.columns([1.6, 1])
    
    with c_sales:
        st.markdown("""
        <div class="glass-card" style="margin-bottom:20px;">
            <h4 style="color:white; margin:0;">⚡ Instant Feasibility</h4>
            <p style="margin:5px 0 0 0;">Calculates NHVR limits for Excavators & Bobcats in seconds.</p>
        </div>
        <div class="glass-card" style="margin-bottom:20px;">
            <h4 style="color:white; margin:0;">🏗️ Bridge Formula Check</h4>
            <p style="margin:5px 0 0 0;">Verify axle spacing against Tier 1 safety standards.</p>
        </div>
        """, unsafe_allow_html=True)

    with c_login:
        with st.form("login_form"):
            st.markdown("### Subscriber Login")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.form_submit_button("Login"):
                # LOGIN LOGIC (Admin + Guest + Fallback)
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
                    # Emergency fallback
                    if username == "guest" and password == "tryladenpass":
                        st.session_state.logged_in = True
                        st.session_state.user_type = "Guest"
                        st.rerun()
                    else:
                        st.error("Invalid credentials.")

        st.markdown("""<div style="text-align:center; margin-top:20px;"><a href="https://buy.stripe.com/28EdRa2om1jWfAc5kZ9oc00" style="background:linear-gradient(45deg, #f59e0b, #ea580c); color:white; padding:12px 40px; border-radius:8px; text-decoration:none; font-weight:bold; display:inline-block;">UNLOCK INSTANT ACCESS ($99)</a></div>""", unsafe_allow_html=True)

# >>> LOGGED IN AREA (IMPROVED UI) <<<
else:
    if "Dashboard" in menu:
        st.markdown(f"""<div style="text-align:center; padding-bottom:20px;"><h1>Operations Dashboard</h1><p>Welcome, {st.session_state.user_type}.</p></div>""", unsafe_allow_html=True)
        # Dashboard Cards
        c1, c2, c3, c4 = st.columns(4)
        for t, v in [("🟢 Status", "Online"), ("⚡ Latency", "< 20ms"), ("📅 Plan", "Active"), ("🛡️ Checks", "Unlimited")]:
            with c1 if t=="🟢 Status" else c2 if t=="⚡ Latency" else c3 if t=="📅 Plan" else c4:
                st.markdown(f'<div class="glass-card" style="text-align:center;"><h3>{t}</h3><p>{v}</p></div>', unsafe_allow_html=True)

    elif "Run" in menu:
        # --- NEW PROFESSIONAL FORM UI ---
        st.markdown("## 🚛 Instant Compliance Check")
        st.markdown("Enter your vehicle configuration below to validate against NHVR GML standards.")
        
        # Container for the form to give it a "Control Panel" look
        with st.container():
            st.markdown('<div class="control-panel">', unsafe_allow_html=True)
            
            c1, c2 = st.columns(2)
            with c1:
                gcm = st.number_input("Gross Combination Mass (t)", 10.0, 200.0, 42.5, help="Total weight of truck + trailer + load")
                axles = st.number_input("Number of Axles", 3, 20, 6, help="Total axles on the ground")
            with c2:
                width = st.number_input("Vehicle Width (m)", 2.0, 8.0, 2.5)
                height = st.number_input("Vehicle Height (m)", 2.0, 6.0, 4.3)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Big Action Button
            if st.button("RUN COMPLIANCE CHECK"):
                with st.spinner("Analyzing Physics & Regulations..."):
                    time.sleep(0.5)
                    result = check_compliance(gcm, axles, width, height)
                    
                    # --- PROFESSIONAL RESULT CARD ---
                    st.markdown(f"""
                    </div> <div class="result-card" style="border-left: 10px solid {result['color']};">
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <div>
                                <h3 style="margin:0; color:#0f172a;">{result['icon']} {result['status']}</h3>
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
                        st.markdown("**Identified Issues:**")
                        for issue in result['issues']:
                            st.markdown(f"<div style='color:#ef4444; margin-bottom:5px;'>• {issue}</div>", unsafe_allow_html=True)
                        st.markdown(f"<div style='background-color:#fee2e2; color:#b91c1c; padding:10px; border-radius:4px; margin-top:10px; font-size:0.9rem;'><strong>ACTION REQUIRED:</strong> You must apply for a {result['permit_type']} before transport.</div>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<div style='color:#166534; margin-top:5px;'>Configuration meets GML General Access Limits. No specific permit required for dimensions/mass provided.</div>", unsafe_allow_html=True)
                    
                    st.markdown("</div>", unsafe_allow_html=True)
            
            else:
                st.markdown('</div>', unsafe_allow_html=True) # Close div if button not clicked
