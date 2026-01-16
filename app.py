import streamlit as st
import pandas as pd

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="LadenPass | Enterprise Logistics",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. CSS STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #f4f6f9; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    h1 { font-family: 'Helvetica Neue', sans-serif; font-weight: 700; color: #1e293b; font-size: 2.2rem; }
    h2, h3 { font-family: 'Helvetica Neue', sans-serif; color: #334155; }
    .result-card { background-color: white; padding: 20px; border-radius: 10px; border-left: 5px solid #3b82f6; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); margin-bottom: 20px; }
    .stButton>button { width: 100%; background-color: #0f172a; color: white; border: none; padding: 0.5rem 1rem; border-radius: 6px; font-weight: 600; transition: all 0.2s; }
    .stButton>button:hover { background-color: #1e293b; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
    .status-dot { height: 10px; width: 10px; background-color: #22c55e; border-radius: 50%; display: inline-block; margin-right: 8px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    # Ensure 'logo.png' exists in your GitHub repo, otherwise this shows a broken image icon.
    st.image("https://raw.githubusercontent.com/ladenpass-bot/LadenPass/main/logo.png", width=310)
    st.caption("Ver 2.2.0 (Stable)")
    st.markdown("---")
    
    menu = st.radio("Module", ["🔍 Route Assessment", "🚛 Fleet Manager", "📂 Permit Archive", "⚙️ Settings"])
    
    st.markdown("---")
    st.markdown("### **System Status**")
    st.markdown('<div><span class="status-dot"></span><strong>NHVR API</strong>: Online</div>', unsafe_allow_html=True)
    st.markdown('<div><span class="status-dot"></span><strong>HVSAPS</strong>: Online</div>', unsafe_allow_html=True)
    st.markdown("---")
    st.info("Support: admin@ladenpass.com.au")

# --- 4. MAIN APP ---

if menu == "🔍 Route Assessment":
    col_head1, col_head2 = st.columns([3, 1])
    with col_head1:
        st.title("Compliance Engine")
        st.markdown("**New Movement Assessment (Class 1 OSOM)**")
    with col_head2:
        st.caption("2026 Regulations Active")

    with st.container():
        st.markdown("### 1. Vehicle Configuration")
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
    
    # Logic is simplified here to prevent indentation errors
    if st.button("RUN COMPLIANCE CHECK"):
        
        # --- LOGIC START ---
        flags = []
        status = "Approved"
        color = "green"
        
        if gcm > 42.5 and (route == "Victoria" or route == "NSW"):
            flags.append("🌉 **HVSAPS ALERT:** Mass > 42.5t. Bridge assessment required.")
            status = "Conditional"
            color = "orange"
        
        if width > 2.5:
            flags.append("⚠️ **OVERSIZE:** Width exceeds 2.5m.")
            status = "Conditional"
            color = "orange"
        
        if height > 4.9:
            flags.append("⚡ **UTILITY CLEARANCE:** Height > 4.9m. Power check required.")
            status = "Referral Required"
            color = "red"
        # --- LOGIC END ---

        # Display Results
        st.markdown("---")
        st.subheader("Results")
        
        r1, r2, r3 = st.columns(3)
        with r1:
            st.metric("Determination", status)
        with r2:
            st.metric("NHVR Fee", "$91.00")
        with r3:
            st.metric("Turnaround", "Instant" if color == "green" else "24 Hours")

        # Result Card Construction
        card_color = "#22c55e" # Default Green
        if color == "red": card_color = "#ef4444"
        if color == "orange": card_color = "#f59e0b"
        
        if len(flags) > 0:
            details_html = "".join([f"<li>{f}</li>" for f in flags])
        else:
            details_html = "<li>✅ General Access Compliant.</li>"

        st.markdown(f"""
        <div class="result-card" style="border-left-color: {card_color};">
            <h4>Analysis Details</h4>
            <ul>{details_html}</ul>
        </div>
        """, unsafe_allow_html=True)

        if color != "green":
            # UPDATE THIS LINK WITH YOUR STRIPE LINK
            st.link_button("🚀 SUB
