import streamlit as st
import time
import pandas as pd
import datetime

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="LadenPass | Enterprise Logistics",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. PROFESSIONAL STYLING (CSS) ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #f4f6f9;
    }
    /* Hide Streamlit Header/Footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Custom Header Styling */
    h1 {
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 700;
        color: #1e293b;
        font-size: 2.2rem;
    }
    h2, h3 {
        font-family: 'Helvetica Neue', sans-serif;
        color: #334155;
    }
    
    /* Card Styling for Results */
    .result-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #3b82f6;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    
    /* Button Styling */
    .stButton>button {
        width: 100%;
        background-color: #0f172a; /* Navy Blue */
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 6px;
        font-weight: 600;
        transition: all 0.2s;
    }
    .stButton>button:hover {
        background-color: #1e293b;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    
    /* Status Indicators */
    .status-dot {
        height: 10px;
        width: 10px;
        background-color: #22c55e;
        border-radius: 50%;
        display: inline-block;
        margin-right: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    # --- LOGO DISPLAY ---
    # This URL points to the raw image in your GitHub. 
    # If the image doesn't load, ensure 'logo.png' is in your repo and spellings match.
    st.image("https://raw.githubusercontent.com/ladenpass-bot/LadenPass/main/logo.png", width=280)
    
    st.caption("Ver 2.1.0 (Enterprise)")
    
    st.markdown("---")
    
    # Navigation
    menu = st.radio("Module", ["🔍 Route Assessment", "🚛 Fleet Manager", "📂 Permit Archive", "⚙️ Settings"])
    
    st.markdown("---")
    
    # "Live" Status Mockup
    st.markdown("### **System Status**")
    st.markdown('<div><span class="status-dot"></span><strong>NHVR Portal API</strong>: Online</div>', unsafe_allow_html=True)
    st.markdown('<div><span class="status-dot"></span><strong>HVSAPS (VIC/NSW)</strong>: Online</div>', unsafe_allow_html=True)
    st.markdown('<div><span class="status-dot"></span><strong>Gazette Database</strong>: Synced</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.info("ℹ️ **Support:** 1800 555 000\n\nadmin@ladenpass.com.au")

# --- 4. MAIN CONTENT LOGIC ---

if menu == "🔍 Route Assessment":
    # Header
    col_head1, col_head2 = st.columns([3, 1])
    with col_head1:
        st.title("Compliance Engine")
        st.markdown("**New Movement Assessment (Class 1 OSOM)**")
    with col_head2:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Infobox_info_icon.svg/480px-Infobox_info_icon.svg.png", width=40)
        st.caption("2026 Regulations Active")

    # The Input Dashboard
    with st.container():
        st.markdown("### 1. Vehicle Configuration")
        with st.expander("📝 Enter Load Details", expanded=True):
            c1, c2, c3, c4 = st.columns(4)
            with c1:
                ref = st.text_input("Job Reference", value="JOB-26-004")
            with c2:
                make = st.selectbox("Configuration", ["Prime Mover + Low Loader", "Crane (All Terrain)", "Platform Trailer"])
            with c3:
                gcm = st.number_input("GCM (Tonnes)", 10.0, 200.0, 42.5, step=0.5)
            with c4:
                route = st.selectbox("Jurisdiction", ["Victoria", "NSW", "Queensland", "South Australia"])

            c5, c6, c7, c8 = st.columns(4)
            with c5:
                length = st.number_input("Length (m)", 10.0, 40.0, 19.0)
            with c6:
                width = st.number_input("Width (m)", 2.0, 8.0, 2.5)
            with c7:
                height = st.number_input("Height (m)", 2.0, 6.0, 4.3)
            with c8:
                axles = st.number_input("Total Axles", 2, 20, 6)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Action Button
    assess_btn = st.button("RUN COMPLIANCE CHECK (HVSAPS)")

    # The Logic Engine
    if assess_btn:
        # Simulate Processing
        with st.spinner("Querying NHVR Gazette Notices..."):
            time.sleep(0.8)
        with st.spinner("Running HVSAPS Structural Analysis (DTP API)..."):
            time.sleep(1.2)

        # Logic
        flags = []
        status = "Approved"
        color = "green"
        
        # 1. HVSAPS Check (The 2026 Feature)
        if gcm > 42.5 and (route == "Victoria" or route == "NSW"):
            flags.append("🌉 **HVSAPS ALERT:** Mass > 42.5t. Structural bridge assessment required.")
            status = "Conditional"
            color = "orange"
        
        # 2. Dimensions
        if width > 2.5:
            flags.append("⚠️ **OVERSIZE:** Width exceeds General Access (2.5m).")
            status = "Conditional" if status != "Critical" else "Critical"
            color = "orange"
        
        if height > 4.3:
            flags.append("⚠️ **HIGH LOAD:** Height exceeds General Access (4.3m).")
            color = "orange"
        
        if height > 4.9:
            flags.append("⚡ **UTILITY CLEARANCE:** Height > 4.9m. Essential Energy/Rail check mandatory.")
            status = "Referral Required"
            color = "red"

        # Results Display
        st.markdown("---")
        st.subheader("📋 Assessment Results")
        
        r1, r2, r3 = st.columns(3)
        with r1:
            st.metric("Determination", status, delta="Action Required" if color != "green" else "Clear", delta_color="inverse" if color=="red" else "normal")
        with r2:
            st.metric("NHVR Fee", "$91.00", "Statutory")
        with r3:
            st.metric("Turnaround", "Instant" if color == "green" else "24 Hours")

        # The "Card" for details
        st.markdown(f"""
        <div class="result-card" style="border-left-color: {'#ef4444' if color=='red' else '#f59e0b' if color=='orange' else '#22c55e'};">
            <h4>Analysis Details</h4>
            <ul>
                {''.join([f'<li>{f}</li>' for f in flags]) if flags else '<li>✅ Vehicle is General Access compliant. No permit required.</li>'}
            </ul>
        </div>
        """, unsafe_allow_html=True)

        # Call to Action
        if color != "green":
            col_cta1, col_cta2 = st.columns([1, 2])
            with col_cta1:
                # Replace the link below with your actual Stripe Payment Link
                st.link_button("🚀 SUBMIT APPLICATION ($140.00)", "https://buy.stripe.com/test_123")
            with col_cta2:
                st.info("Clicking submit will auto-fill the NHVR application and append the HVSAPS report.")

elif menu == "🚛 Fleet Manager":
    st.title("Fleet Registry")
    st.markdown("Manage your assets for rapid permitting.")
    
    # Professional Table
    data = {
        "Asset ID": ["PM-001", "TR-LOW-04", "CR-50T"],
        "Registration": ["XQ-99-ZZ", "TR-88-AA", "HV-55-CC"],
        "Make/Model": ["Kenworth K200", "Drake 4x4", "Liebherr LTM"],
        "Status": ["Active", "Active", "Maintenance"],
        "Last Permit": ["2 days ago", "Yesterday", "N/A"]
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.button("+ Add New Asset")

elif menu == "📂 Permit Archive":
    st.title("Permit Library")
    st.warning("Please log in to view historical documents.")

elif menu == "⚙️ Settings":
    st.title("System Configuration")
    st.text_input("Company Name", value="LadenPass Demo Account")
    st.text_input("NHVR Portal Email")
    st.text_input("API Key (Hidden)", type="password")
    st.button("Save Configuration")

# --- 5. PROFESSIONAL FOOTER ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #64748b; font-size: 0.8rem;'>
        © 2026 LadenPass Technologies. All rights reserved. <br>
        Built for compliance with the <strong>Heavy Vehicle National Law (HVNL)</strong> and <strong>HVSAPS 2026</strong> standards.<br>
        <a href="#">Privacy Policy</a> | <a href="#">Terms of Service</a> | <a href="#">Status</a>
    </div>
    """, unsafe_allow_html=True
)
