import streamlit as st
import pandas as pd

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="LadenPass",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. CSS STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #f4f6f9; }
    .result-card { background-color: white; padding: 20px; border-radius: 10px; border-left: 5px solid #3b82f6; margin-bottom: 20px; }
    .stButton>button { width: 100%; background-color: #0f172a; color: white; border: none; padding: 0.5rem 1rem; border-radius: 6px; }
    .stButton>button:hover { background-color: #1e293b; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    # Ensure logo.png is in your GitHub. If broken, it displays a placeholder text.
    st.image("https://raw.githubusercontent.com/ladenpass-bot/LadenPass/main/logo.png", width=300)
    st.caption("Ver 2.3.0 (Stable)")
    st.markdown("---")
    menu = st.radio("Menu", ["Assessment", "Fleet", "Settings"])
    st.markdown("---")
    st.info("Support: admin@ladenpass.com.au")

# --- 4. MAIN APP ---

if menu == "Assessment":
    st.title("Compliance Engine")
    st.markdown("**New Movement Assessment (Class 1 OSOM)**")

    # INPUTS
    with st.container():
        c1, c2 = st.columns(2)
        with c1:
            ref = st.text_input("Job Reference", value="JOB-26-004")
            gcm = st.number_input("GCM (Tonnes)", 10.0, 200.0, 42.5)
        with c2:
            route = st.selectbox("State", ["Victoria", "NSW", "QLD", "SA"])
            width = st.number_input("Width (m)", 2.0, 8.0, 2.5)
            height = st.number_input("Height (m)", 2.0, 6.0, 4.3)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # BUTTON & LOGIC
    if st.button("RUN CHECK"):
        
        # LOGIC
        flags = []
        status = "Approved"
        color = "green"
        
        if gcm > 42.5 and (route == "Victoria" or route == "NSW"):
            flags.append("Mass > 42.5t (Bridge Check Req)")
            status = "Conditional"
            color = "orange"
        
        if width > 2.5:
            flags.append("Oversize Width (>2.5m)")
            status = "Conditional" 
            color = "orange"
            
        if height > 4.9:
            flags.append("High Load (>4.9m)")
            status = "Referral"
            color = "red"

        # RESULTS
        st.markdown("---")
        c_res1, c_res2 = st.columns(2)
        with c_res1:
            st.metric("Status", status)
        with c_res2:
            st.metric("Fee", "$91.00")

        # DETAILS CARD
        card_color = "#22c55e"
        if color == "orange": card_color = "#f59e0b"
        if color == "red": card_color = "#ef4444"
        
        if len(flags) > 0:
            html_list = "".join([f"<li>{f}</li>" for f in flags])
        else:
            html_list = "<li>General Access Compliant</li>"

        st.markdown(f"""
        <div class="result-card" style="border-left-color: {card_color};">
            <b>Assessment Details:</b>
            <ul>{html_list}</ul>
        </div>
        """, unsafe_allow_html=True)

        # PAYMENT BUTTON
        if color != "green":
            # This is the line that was breaking. It is now short and safe.
            st.link_button("🚀 PAY & SUBMIT ($140)", "https://buy.stripe.com/test_123")

elif menu == "Fleet":
    st.title("Fleet Registry")
    data = {"ID": ["PM-01", "TR-04"], "Rego": ["XQ-99", "TR-88"], "Status": ["Active", "Active"]}
    st.dataframe(pd.DataFrame(data), use_container_width=True)

elif menu == "Settings":
    st.title("Settings")
    st.text_input("NHVR Email")
    st.button("Save")
