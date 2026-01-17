import streamlit as st
import pandas as pd
import numpy as np
import base64

# --- 1. ENTERPRISE PAGE CONFIG ---
st.set_page_config(
    page_title="LadenPass | Command Center",
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
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
    }

    /* GLOBAL THEME */
    .stApp {
        background-color: #0f172a; 
        background-image: linear-gradient(rgba(15, 23, 42, 0.95), rgba(15, 23, 42, 0.95)), 
        url("https://images.unsplash.com/photo-1601584115197-04ecc0da31d7?q=80&w=2670&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* TYPOGRAPHY */
    h1, h2, h3, h4, h5, h6 { color: #ffffff !important; font-family: 'Segoe UI', sans-serif; }
    p, li, label, span, div { color: #cbd5e1 !important; }
    
    /* SIDEBAR */
    [data-testid="stSidebar"] {
        background-color: #064e3b !important;
        border-right: 1px solid rgba(255,255,255,0.05);
    }
    
    /* LOGO CONTAINER */
    .logo-container {
        background-color: white;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 20px;
        text-align: center;
        display: flex;
        justify-content: center;
        align-items: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .logo-container img { max-width: 100%; height: auto; }

    /* NAVIGATION BUTTONS */
    [data-testid="stRadio"] > div { gap: 10px; }
    [data-testid="stRadio"] label {
        background-color: rgba(255, 255, 255, 0.05) !important;
        padding: 12px 15px !important;
        border-radius: 6px !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        transition: all 0.2s ease !important;
        cursor: pointer !important;
    }
    [data-testid="stRadio"] label:hover {
        background-color: rgba(255, 255, 255, 0.15) !important;
        border-color: #4ade80 !important;
    }
    [data-testid="stRadio"] label[data-checked="true"] {
        background-color: rgba(34, 197, 94, 0.2) !important;
        border-color: #22c55e !important;
        color: white !important;
        font-weight: 600 !important;
    }

    /* DASHBOARD CARDS (METRICS) */
    .metric-card {
        background-color: rgba(30, 41, 59, 0.7);
        border-left: 4px solid #22c55e;
        padding: 15px;
        border-radius: 6px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .metric-card h2 { font-size: 1.8rem !important; margin: 0 !important; font-weight: 700; }
    .metric-card p { margin: 0 !important; opacity: 0.8; font-size: 0.9rem; }

    /* TABLE STYLING */
    [data-testid="stDataFrame"] {
        background-color: rgba(30, 41, 59, 0.5);
        border-radius: 8px;
        padding: 10px;
    }

    /* INPUTS & BUTTONS */
    .stTextInput input, .stNumberInput input, .stSelectbox div[data-baseweb="select"] {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border-radius: 4px;
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
    
    #MainMenu, footer, header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR NAVIGATION ---
with st.sidebar:
    if logo_b64:
        st.markdown(f"""<div class="logo-container"><img src="data:image/jpeg;base64,{logo_b64}"></div>""", unsafe_allow_html=True)
    else:
        st.markdown("""<div class="logo-container"><h2 style="color:#064e3b !important; margin:0;">LadenPass</h2></div>""", unsafe_allow_html=True)
    
    st.markdown("### Operations")
    menu = st.radio(
        "", 
        ["📊 Command Center", "✅ Compliance Engine", "🚛 Fleet Assets"], 
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("### Quick Stats")
    st.caption("Network Status: 🟢 Online")
    st.caption("Active Movements: 12")
    st.caption("Pending Approvals: 0")


# --- 5. MAIN CONTENT ---

if "Command" in menu:
    # --- HEADER ---
    c1, c2 = st.columns([3, 1])
    with c1:
        st.title("LadenPass Command Center")
        st.markdown("Real-time network access monitoring and compliance overview.")
    with c2:
        # Date Display
        st.markdown(f"<div style='text-align:right; font-size:1.2rem; padding-top:10px;'>{pd.Timestamp.now().strftime('%d %b %Y')}</div>", unsafe_allow_html=True)

    st.markdown("---")

    # --- ROW 1: KEY METRICS (KPIs) ---
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    with kpi1:
        st.markdown("""<div class="metric-card"><h2>98.2%</h2><p>Auto-Approval Rate</p></div>""", unsafe_allow_html=True)
    with kpi2:
        st.markdown("""<div class="metric-card"><h2>142</h2><p>Movements Today</p></div>""", unsafe_allow_html=True)
    with kpi3:
        st.markdown("""<div class="metric-card" style="border-color:#f59e0b;"><h2>3</h2><p>Pending Reviews</p></div>""", unsafe_allow_html=True)
    with kpi4:
        st.markdown("""<div class="metric-card" style="border-color:#3b82f6;"><h2>$12,450</h2><p>Permit Fees Saved</p></div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- ROW 2: SPLIT VIEW (MAP + CHART) ---
    col_map, col_chart = st.columns([3, 2])
    
    with col_map:
        st.subheader("📍 Live Network Activity (Active Jobs)")
        # Simulating random truck locations in NSW/VIC for the map
        map_data = pd.DataFrame(
            np.random.randn(20, 2) / [20, 20] + [-36.5, 145.0],
            columns=['lat', 'lon']
        )
        st.map(map_data, zoom=6, use_container_width=True)
        
    with col_chart:
        st.subheader("📈 Compliance Trend (30 Days)")
        # Simulating approval data
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['Approved', 'Conditional', 'Referral']
        )
        st.area_chart(chart_data, color=["#22c55e", "#f59e0b", "#ef4444"])

    st.markdown("<br>", unsafe_allow_html=True)

    # --- ROW 3: RECENT ACTIVITY LOG ---
    st.subheader("📋 Recent Permit Requests")
    
    # Fake Data for the table
    recent_jobs = pd.DataFrame({
        "Job Ref": ["JOB-2044", "JOB-2043", "JOB-2042", "JOB-2041", "JOB-2040"],
        "Route": ["Melbourne -> Sydney", "Brisbane -> Gold Coast", "Dubbo -> Newcastle", "Geelong -> Ballarat", "Perth -> Kalgoorlie"],
        "Vehicle": ["Prime Mover + Low Loader", "B-Double", "Oversize Load", "Mobile Crane", "Road Train"],
        "Status": ["✅ Approved", "✅ Approved", "⚠️ Conditional", "✅ Approved", "🔴 Rejected"],
        "Time": ["2 mins ago", "14 mins ago", "1 hour ago", "3 hours ago", "5 hours ago"]
    })
    
    # Display table without index
    st.dataframe(recent_jobs, use_container_width=True, hide_index=True)


elif "Compliance" in menu:
    st.title("New Movement Assessment")
    st.markdown("Enter vehicle parameters to check network feasibility.")
    
    with st.container():
        c1, c2, c3 = st.columns(3)
        with c1:
            ref = st.text_input("Job Reference", value="JOB-2026-X88")
            route = st.selectbox("Jurisdiction", ["Victoria (VIC)", "New South Wales (NSW)", "Queensland (QLD)"])
        with c2:
            gcm = st.number_input("Gross Mass (t)", 10.0, 250.0, 42.5)
            axles = st.number_input("Axle Count", 2, 20, 6)
        with c3:
            width = st.number_input("Width (m)", 2.0, 10.0, 2.5)
            height = st.number_input("Height (m)", 2.0, 8.0, 4.3)

    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("RUN ANALYSIS"):
        with st.spinner(" querying NHVR Structural Database..."):
            import time
            time.sleep(0.8)
            
            flags = []
            status = "APPROVED"
            color = "#22c55e"
            
            if gcm > 42.5:
                flags.append(f"⚠️ Mass ({gcm}t) exceeds General Access limits (>42.5t)")
                status = "CONDITIONAL"
                color = "#f59e0b"
            if width > 2.5:
                flags.append(f"⚠️ Width ({width}m) requires 'Oversize' signage")
                status = "CONDITIONAL"
                color = "#f59e0b"
            if height > 4.6:
                flags.append(f"⛔ Height ({height}m) exceeds clearway max.")
                status = "REFERRAL"
                color = "#ef4444"
                
            if len(flags) == 0: flags.append("✅ General Access Compliant")

            st.markdown(f"""
            <div style="background-color: white; padding: 20px; border-radius: 8px; border-left: 8px solid {color}; margin-top: 20px;">
                <h2 style="color: #0f172a !important; margin:0;">Status: {status}</h2>
                <hr style="margin: 10px 0;">
                <ul style="color: #334155 !important; padding-left: 20px;">
                    {''.join([f'<li style="color:#334155;">{f}</li>' for f in flags])}
                </ul>
            </div>
            """, unsafe_allow_html=True)


elif "Fleet" in menu:
    st.title("Fleet Assets")
    st.markdown("Manage your prime movers and trailers.")
    
    # Just a simple stylized table
    st.markdown("""<style>[data-testid="stDataFrame"] { background-color: white !important; color: black !important; }</style>""", unsafe_allow_html=True)
    
    data = {
        "Asset ID": ["PM-104", "PM-105", "TR-882", "TR-991", "CR-001"],
        "Registration": ["XJ-44-KL", "AB-22-ZZ", "TR-55-PL", "TR-11-QQ", "CR-99-XX"],
        "Type": ["Prime Mover", "Prime Mover", "Low Loader", "Dolly", "Franna Crane"],
        "Status": ["Active", "Maintenance", "Active", "Active", "Active"]
    }
    st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)
