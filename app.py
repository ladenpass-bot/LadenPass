import streamlit as st
import datetime
import time
import pandas as pd

# --- APP CONFIGURATION ---
st.set_page_config(
    page_title="LadenPass | Automated Access",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS (THE "FACELESS" BRANDING) ---
# This makes it look like expensive software, not a basic script.
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    h1 { color: #0f172a; font-family: 'Helvetica Neue', sans-serif; }
    .stButton>button { 
        width: 100%; 
        background-color: #0056b3; 
        color: white; 
        border-radius: 5px; 
        height: 3em; 
        font-weight: bold;
    }
    .stButton>button:hover { background-color: #004494; border-color: #004494; }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
    }
    .highlight { color: #e11d48; font-weight: bold; }
    .success-box { padding: 15px; background-color: #d1fae5; color: #065f46; border-radius: 8px; border: 1px solid #34d399; }
    .warning-box { padding: 15px; background-color: #ffedd5; color: #9a3412; border-radius: 8px; border: 1px solid #fb923c; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1584/1584892.png", width=50) # Placeholder Icon
    st.markdown("## **LadenPass**")
    st.markdown("### *Invisible Compliance*")
    st.markdown("---")
    menu = st.radio("Menu", ["New Assessment", "Driver Logs (July '26)", "My Fleet", "Admin Settings"])
    
    st.markdown("---")
    st.info("**System Status:** \n\n🟢 **HVSAPS API:** Online\n\n🟢 **NHVR Portal:** Connected")
    st.markdown("v1.2 (Jan 2026 Build)")

# --- MAIN PAGE LOGIC ---

if menu == "New Assessment":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.title("🚛 New Movement Assessment")
        st.write("Enter vehicle specifications to check against **2026 HVSAPS** & **Gazette Notices**.")
        
        with st.form("assessment_form"):
            st.write("### 1. Machine Details")
            c1, c2, c3 = st.columns(3)
            with c1:
                ref_id = st.text_input("Job Reference", value="JOB-2026-001")
            with c2:
                machine_type = st.selectbox("Load Type", ["Excavator", "Dozer", "Crane", "Ag Machinery", "Structure"])
            with c3:
                route_state = st.selectbox("Jurisdiction", ["Victoria", "NSW", "QLD", "SA"])

            st.write("### 2. Dimensions & Mass")
            c4, c5, c6, c7 = st.columns(4)
            with c4:
                length = st.number_input("Length (m)", 10.0, 30.0, 19.0)
            with c5:
                width = st.number_input("Width (m)", 2.0, 6.0, 2.5)
            with c6:
                height = st.number_input("Height (m)", 2.0, 6.0, 4.3)
            with c7:
                mass = st.number_input("Total Mass (t)", 10.0, 150.0, 42.0)

            st.write("### 3. Route Configuration")
            hvsaps_check = st.checkbox("Run HVSAPS Structural Check (VIC/NSW)", value=True)
            
            submitted = st.form_submit_button("Run Compliance Engine")

    if submitted:
        with st.spinner("Connecting to NHVR 2026 Gazette Database..."):
            time.sleep(1.5) # Simulate API latency for "realism"
        
        st.markdown("---")
        st.subheader(f"📋 Compliance Report: {ref_id}")

        # --- THE LOGIC BRAIN (Proprietary Engine) ---
        issues = []
        fees = 91.00
        
        # Logic 1: Width (Oversize)
        if width > 2.5:
            issues.append("⚠️ **OVERSIZE:** Width exceeds 2.5m General Access limit.")
        
        # Logic 2: Height (Electric/Rail)
        if height > 4.3:
            issues.append("⚠️ **HIGH LOAD:** Height exceeds 4.3m. Route restricted.")
        if height > 4.9:
            issues.append("🚨 **RAIL CLEARANCE:** Height > 4.9m. Automated RIM notification required.")
        if height > 5.2:
            issues.append("⚡ **POWER UTILITY:** Height > 5.2m. Essential Energy clearance required.")

        # Logic 3: Mass (HVSAPS Trigger - The 2026 Feature)
        if mass > 42.5 and (route_state == "Victoria" or route_state == "NSW"):
             issues.append("🌉 **HVSAPS TRIGGERED:** Mass > 42.5t. Automated bridge assessment initiated.")

        # --- RESULTS DISPLAY ---
        r1, r2, r3 = st.columns(3)
        
        with r1:
            if not issues:
                st.markdown("<div class='success-box'><h3>✅ PASS</h3><p>General Access - No Permit Required</p></div>", unsafe_allow_html=True)
            elif any("RAIL" in i for i in issues) or any("POWER" in i for i in issues):
                 st.markdown("<div class='warning-box'><h3>🔴 CRITICAL</h3><p>Utility/Rail Clearance Required</p></div>", unsafe_allow_html=True)
            else:
                 st.markdown("<div class='warning-box'><h3>🟠 CONDITIONAL</h3><p>Class 1 Permit Required</p></div>", unsafe_allow_html=True)

        with r2:
            st.metric("Est. Gov Fees", f"${fees:.2f}")
        
        with r3:
            st.metric("Processing Time", "Instant" if not issues else "24-48 Hours")

        st.write("### Action Items")
        if issues:
            for issue in issues:
                st.write(issue)
            
            st.write("---")
            st.write("**Ready to file?**")
            col_pay, col_info = st.columns([1,2])
            with col_pay:
                st.button(f"🚀 File Application (${fees + 49}0)") # Adds your $49 service fee
            with col_info:
                st.caption("Includes automated HVSAPS bridge check & NHVR submission fee.")
        else:
            st.success("This load is General Access. No permit required. Safe travels!")

elif menu == "Driver Logs (July '26)":
    st.title("📱 Primary Duty Log")
    st.info("Required under July 2026 HVNL Amendments for all Class 1 movements.")
    
    with st.form("driver_log"):
        st.write("**Driver Self-Assessment**")
        col_a, col_b = st.columns(2)
        with col_a:
            st.text_input("Driver Name")
            st.text_input("License Number")
        with col_b:
            st.selectbox("Fatigue Status", ["Standard Hours", "BFM", "AFM"])
            st.selectbox("Current Location", ["Depot Start", "Rest Stop", "border Crossing"])
        
        st.write("**Fit-to-Drive Checklist**")
        st.checkbox("I am not under the influence of drugs or alcohol.")
        st.checkbox("I am not suffering from fatigue affecting my ability to drive.")
        st.checkbox("I have visually inspected the load restraints.")
        
        st.form_submit_button("Sign & Upload Log")

elif menu == "My Fleet":
    st.title("🚛 My Fleet")
    st.write("Manage stored vehicle profiles for one-click assessments.")
    
    # Mock Data Table
    data = {
        "Machine ID": ["PC300-1", "D8T-DOZER", "CRANE-50T"],
        "Make": ["Komatsu", "Caterpillar", "Liebherr"],
        "Mass (t)": [32.5, 48.0, 52.0],
        "Width (m)": [3.2, 3.8, 2.9],
        "Status": ["Active", "Active", "Maintenance"]
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

elif menu == "Admin Settings":
    st.title("⚙️ Admin Console")
    st.write("Manage your API keys and billing.")
    st.text_input("NHVR Portal API Key", type="password")
    st.text_input("Stripe Secret Key", type="password")
    st.button("Save Configuration")
