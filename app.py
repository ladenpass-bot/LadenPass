# --- 6. SIDEBAR CONTENT ---
with st.sidebar:
    # UPDATED LOGIC:
    # 1. Checks for 'ladenpass-logo.png'
    # 2. Uses 'image/png' (correct for your file type)
    # 3. Fallback text uses <p> tag to avoid White-on-White text conflict
    if logo_b64:
        st.markdown(f"""
            <div class="logo-container">
                <img src="data:image/png;base64,{logo_b64}" style="max-width: 100%; height: auto;">
            </div>
        """, unsafe_allow_html=True)
    else:
        # This shows if the file is missing. 
        # We used <p> instead of <h2> to ensure the text is Green, not White.
        st.markdown("""
            <div class="logo-container">
                <p style="color:#064e3b !important; font-size: 24px; font-weight: bold; margin: 0;">LadenPass</p>
                <p style="color:#666 !important; font-size: 10px; margin: 0;">(Upload logo to fix)</p>
            </div>
        """, unsafe_allow_html=True)
    
    # Login Status & Menu
    if st.session_state.logged_in:
        st.markdown("### Action Menu")
        menu = st.radio("", ["📊 Dashboard", "✅ Run Auto-Check"], label_visibility="collapsed")
        st.markdown("---")
        if st.button("Log Out"):
            st.session_state.logged_in = False
            st.rerun()
        st.success("🟢 System Online")
    else:
        st.info("🔒 Secure Access")
        st.caption("Please log in to access the Enterprise Platform.")

    current_year = datetime.datetime.now().year
    
    # Footer
    st.markdown(f"""
        <div style='text-align: center; font-size: 0.8rem; color: #cbd5e1; margin-top: 15px; opacity: 0.8;'>
            © {current_year} LadenPass Enterprise<br>
            <strong>ABN: 16 632 316 240</strong>
        </div>
    """, unsafe_allow_html=True)
