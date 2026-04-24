import streamlit as st
from style import apply_style
import re

apply_style()

st.set_page_config(page_title="Contact", page_icon="📬", layout="wide")

st.markdown("""
<div class="glass">
    <h1>Contact Me</h1>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="glass">
    <p>I'd love to hear from you! Whether you have a question, want to collaborate,
    or just want to say hello, feel free to reach out using the form below
    or through my social media accounts.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

col_form, col_social = st.columns([2, 1], gap="large")

with col_form:
    st.markdown("### ✉️ Send Me a Message")

    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input(
            "Your Name *",
            placeholder="Enter your full name",
            key="contact_name"
        )
        email = st.text_input(
            "Your Email *",
            placeholder="example@email.com",
            key="contact_email"
        )
        subject = st.selectbox(
            "Subject *",
            ["General Inquiry", "Project Collaboration", "Job Opportunity", "Feedback", "Other"],
            key="contact_subject"
        )
        message = st.text_area(
            "Your Message *",
            placeholder="Write your message here...",
            height=200,
            key="contact_message"
        )

        submitted = st.form_submit_button("📤 Send Message", use_container_width=True)

        if submitted:
            if not name or not email or not message:
                st.error("❌ Please fill in all required fields (*).")
            elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                st.error("❌ Please enter a valid email address.")
            else:
                st.success(f"✅ Thanks, {name}! Your message has been received. I'll get back to you at {email} soon!")

with col_social:
    st.markdown("### Connect With Me")
    st.markdown("---")
    
    st.markdown("#### Email")
    st.info("agananroseann18@gmail.com")

    st.markdown("#### GitHub")
    st.markdown("[🔗 https://github.com/agananroseann18-creator](https://github.com/agananroseann18-creator)")

    st.markdown("#### Facebook")
    st.markdown("[🔗 facebook.com/roseann.aganan](https://www.facebook.com/roseann.aganan.31)")

    st.markdown("#### Instagram")
    st.markdown("[🔗 @rose.ann3851](https://www.instagram.com/rose.ann3851)")

st.markdown("---")

st.markdown("## 📍 More Information")

info_col1, info_col2, info_col3 = st.columns(3, gap="medium")

with info_col1:
    st.markdown("""
    <div class="feature-card">
        <h3>📍 Location</h3>
        <p>Alba Street, Poblacion East<br>
        Milagros, Masbate<br>
        Philippines</p>
    </div>
    """, unsafe_allow_html=True)

with info_col2:
    st.markdown("""
    <div class="feature-card">
        <h3>⏰ Availability</h3>
        <p>Open to:<br>
        • Internships<br>
        • Freelance Projects<br>
        • Collaborations</p>
    </div>
    """, unsafe_allow_html=True)

with info_col3:
    st.markdown("""
    <div class="feature-card">
        <h3>🚀 Quick Response</h3>
        <p>I typically respond within<br>
        24-48 hours to all<br>
        inquiries</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; color: #b0b0b0; margin-top: 30px;">
    <p style="font-size: 0.85rem; margin-top: 15px;">© 2026 Rose-ann Aganan | All rights reserved </p>
</div>
""", unsafe_allow_html=True)
