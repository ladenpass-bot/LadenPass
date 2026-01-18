import streamlit as st

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="LadenPass | Heavy Haulage",
    page_icon="🚚",
    layout="wide"
)

# --- 2. CUSTOM CSS (Styling) ---
# Enforces the Black & Safety Yellow (Heavy Hauler) theme
st.markdown("""
    <style>
    /* Main Background & Text */
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    
    /* Headers (Safety Yellow) */
    h1, h2, h3 {
        color: #f4b400 !important;
    }
    
    /* Buttons (Yellow with Black Text) */
    div.stButton > button {
        background-color: #f4b400;
        color: black;
        font-weight: bold;
        width: 100%;
        border-radius: 5px;
        border: none;
        padding: 10px;
    }
    div.stButton > button:hover {
        background-color: #d49b00;
        color: white;
        border-color: #d49b00;
    }

    /* Input Fields (Dark Grey background for contrast) */
    .stTextInput > div > div > input, 
    .stSelectbox > div > div > div, 
    .stTextArea > div > div > textarea {
        background-color: #262730;
        color: white;
    }
    
    /* Footer Styling */
    .footer-text {
        text-align: center; 
        color: #888; 
        padding: 20px; 
        font-size: 14px;
        border-top: 1px solid #333;
    }
    .footer-text a {
        color: #f4b400;
        text-decoration: none;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. HEADER & LOGO ---
col1, col2 = st.columns([1, 5])

with col1:
    # This tries to find the logo file in your GitHub repo root
    try:
        st.image("ladenpass-logo.png", width=120)
    except:
        # Fallback if image upload is forgotten
        st.warning("⚠️ Upload ladenpass-logo.png to GitHub")

with col2:
    st.title("LADENPASS")
    st.markdown("### Heavy Haulage & Machinery Transport | Sydney & Regional NSW")

# --- 4. HERO SECTION ---
# Display the heavy hauler background
try:
    st.image("heavy-hauler-bg.jpg", use_container_width=True)
except:
    st.info("ℹ️ Upload heavy-hauler-bg.jpg to GitHub to see the banner here.")

# --- 5. SERVICES SECTION ---
st.write("---")
st.header("Our Services")
st.write("Based in Padstow, serving the Greater Sydney Area and Regional NSW.")

serv1, serv2, serv3 = st.columns(3)

with serv1:
    st.subheader("🏗️ Excavator Transport")
    st.write("Specialized transport for excavators (up to 20t). Safe loading protocols and chaining.")

with serv2:
    st.subheader("🚜 Plant Machinery")
    st.write("Bobcats, bulldozers, forklifts, and industrial plant equipment.")

with serv3:
    st.subheader("🛣️ Regional Haulage")
    st.write("Long-distance heavy towing across NSW. (Sydney to Newcastle, Wollongong, Dubbo).")

# --- 6. QUOTE FORM ---
st.write("---")
st.header("Request a Transport Quote")

# Use a form container so the page doesn't reload on every keystroke
with st.form("quote_form"):
    c1, c2 = st.columns(2)
    
    with c1:
        name = st.text_input("Contact Name")
        phone = st.text_input("Phone Number")
        pickup = st.text_input("Pickup Suburb (e.g. Yagoona)")
    
    with c2:
        email = st.text_input("Email Address")
        machinery = st.selectbox("Machinery Type", ["Excavator", "Bobcat", "Vehicle/Car", "Container", "Other"])
        dropoff = st.text_input("Dropoff Suburb")
    
    details = st.text_area("Additional Details (Dimensions, Weight, Preferred Date)")
    
    # Submit Button
    submitted = st.form_submit_button("Send Request")
    
    if submitted:
        if not phone or not name:
            st.error("Please provide your Name and Phone Number.")
        else:
            # SUCCESS MESSAGE
            st.success(f"✅ Request Sent! Thank you {name}. We will call you on {phone} shortly to quote your {machinery} transport.")
            st.info("Note: This is a demo form. In a live version, this would email you directly.")

# --- 7. FOOTER (COMPLIANCE) ---
st.markdown("---")
st.markdown("""
    <div class='footer-text'>
        <p>&copy; 2026 LadenPass Heavy Haulage.</p>
        <p><strong>ABN:</strong> 16 632 316 240</p>
        <p>
            <a href='#'>Privacy Policy</a> | 
            <a href='#'>Terms of Service</a>
        </p>
    </div>
""", unsafe_allow_html=True)
