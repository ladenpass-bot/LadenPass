import streamlit as st

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="LadenPass | Automated Compliance",
    page_icon="🚛",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. ADVANCED STYLING (Background & Glassmorphism) ---
st.markdown("""
    <style>
    /* 1. BACKGROUND IMAGE WITH DARK OVERLAY */
    .stApp {
        /* We use a linear-gradient to put a dark tint (70% opacity) over the image */
        background-image: linear-gradient(rgba(15, 23, 42, 0.8), rgba(15, 23, 42, 0.8)), 
        url("http://googleusercontent.com/image_collection/image_retrieval/14116698006579212757_0");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* 2. FORCE TEXT TO BE WHITE (For contrast against dark background) */
    .main h1, .main h2, .main h3, .main h4, .main p, .main li, .main span, .main div, .main label {
        color: #ffffff !important;
    }
    
    /* 3. SIDEBAR (Keep Brand Green) */
    [data-testid="stSidebar"] {
        background-color: #0e3b28 !important;
        border-right: 1px solid #064e3b;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* 4. GLASSMORPHISM CARDS (See-through boxes) */
    .feature-card {
        background-color: rgba(255, 255, 255, 0.05); /* 5% White Transparency */
        padding: 20px;
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        margin-bottom: 10px;
        backdrop-filter: blur(5px); /* Blurs the background behind the card */
    }
    .feature-card h3 {
        color: #22c55e !important; /* Bright Green Text for Headers */
        margin-top: 0;
    }
    .feature-card p {
        color: #e2e8f0 !important; /* Light Grey for body text */
    }

    /* 5. INPUT FIELDS (Clean White for usability) */
    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div>div {
        background-color: rgba(255, 255, 255, 0.9) !important;
        color: #0f172a !important;
        border: none;
    }
    
    /* 6. BUTTONS */
    .stButton>button {
        width: 100%;
        background-color: #22c55e !important;
        color: white !important;
        border: none;
        padding: 0.6rem 1rem;
        font-weight: bold;
        text-shadow: 0 1px 2px rgba(0,0,0,0.2);
    }
    .stButton>button:hover { background-color: #16a34a !important; }

    /* HIDE MENU */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    # Looking for logo.jpg
    try:
        st.image("logo.jpg", use_container_width=True)
    except:
        st.error("Logo not found. Ensure 'logo.jpg' is in GitHub.")
    
    st.markdown("---")
    menu = st.radio("Navigation", ["🏠 Home", "🛠️ Start Assessment", "🚛 My Fleet"])
    st.markdown("---")
    st.caption("© 2026 LadenPass Australia")
    st.caption("Support: admin@ladenpass.com.au")

# --- 4. MAIN CONTENT ---

if menu == "🏠 Home":
    # HERO SECTION
    st.markdown("""
    <div style="text-align: center; padding: 60px 0;">
        <h1 style="font-size: 3.5rem; text-shadow: 0 4px 6px rgba(0,0,0,0.3);">Move Heavy Loads, <span style="color: #22c55e !important;">Faster.</span></h1>
        <p style="font-size: 1.3rem; opacity: 0.9;">
            The automated compliance tool for Class 1 Heavy Vehicles. <br>
            Instant bridge checks. 100% Compliant.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # FEATURES
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""
        <div class="feature-card">
            <h3>⚡ Instant Checks</h3>
            <p>Stop waiting 28 days. Get instant feasibility checks for VIC & NSW.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown("""
        <div class="feature-card">
            <h3>🛡️ NHVR Compliant</h3>
            <p>Synced daily with National Heavy Vehicle Regulator gazettes.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with c3:
        st.markdown("""
        <div class="feature-card">
            <h3>📍 Route Planning</h3>
            <p>Avoid low bridges and powerlines automatically.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # CTA
    col_cta1, col_cta2, col_cta3 = st.columns([1, 2, 1])
    with col_cta2:
        st.info("👈 Select 'Start Assessment' in the sidebar to begin.")


elif menu == "🛠️ Start Assessment":
    st.title("New Movement Assessment")
    
    # Transparent Container for Inputs
    with st.container():
        st.markdown("### 1. Vehicle Configuration")
        c1, c2 = st.columns(2)
        with c1:
            ref = st.text_input("Job Reference", value="JOB-26-004")
            gcm = st.number_input("GCM (Tonnes)", 10.0, 200.0, 42.5)
        with c2:
            route = st.selectbox("Jurisdiction", ["Victoria", "NSW", "QLD", "SA"])
            width = st.number_input("Width (m)", 2.0, 8.0, 2.5)
            height = st.number_input("Height (m)", 2.0, 6.0, 4.3)
            
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("RUN COMPLIANCE ENGINE"):
        # LOGIC
        flags = []
        status = "Approved"
        color = "#
