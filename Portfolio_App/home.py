import streamlit as st
import os
from style import apply_style

apply_style()

st.set_page_config(page_title="Portfolio", layout="wide")

st.markdown("""
<div class="hero-section">
    <h1 class="hero-title">Hi, I'm Rose-ann Aganan</h1>
    <p class="hero-subtitle">Future Web Developer & Graphic Designer</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

col1, col2 = st.columns([1,2], gap="small")

with col1:
    if os.path.exists("Portfolio_App/photo.png"):
        st.image("Portfolio_App/photo.png", width=300)
    else:
        st.markdown("<div class='placeholder-image'>📸 Profile Photo</div>", unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
        <div class="glass" style="text-align: center; padding: 40px; margin-top: 50px;">
            <h3>Welcome to My Portfolio! 🌟</h3>
            <p>I'm a computer science student passionate about web development and graphic design.
            With expertise in both areas and a love for learning, I'm always excited
            to take on new challenges and collaborate with creative teams.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
st.markdown("---")

st.markdown("## 📍 What You'll Find Here")

feat_col1, feat_col2, feat_col3, feat_col4 = st.columns(4, gap="medium")

with feat_col1:
    st.markdown("""
    <div class="feature-card">
        <h3>👩 About</h3>
        <p>Learn about my background, education, and interests</p>
    </div>
    """, unsafe_allow_html=True)

with feat_col2:
    st.markdown("""
    <div class="feature-card">
        <h3>📁 Projects</h3>
        <p>Explore the projects I've built and my certifications</p>
    </div>
    """, unsafe_allow_html=True)

with feat_col3:
    st.markdown("""
    <div class="feature-card">
        <h3>👩‍💻 Skills</h3>
        <p>Check out my technical and soft skills</p>
    </div>
    """, unsafe_allow_html=True)

with feat_col4:
    st.markdown("""
    <div class="feature-card">
        <h3>📬 Contact</h3>
        <p>Get in touch or connect with me online</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("## 📊 Quick Stats")

stat_col1, stat_col2, stat_col3 = st.columns(3, gap="medium")

with stat_col1:
    st.metric(label="Projects Completed", value="5+", delta="Growing")

with stat_col2:
    st.metric(label="Certifications", value="6", delta="Learning")

with stat_col3:
    st.metric(label="Skills", value="10+", delta="Developing")

st.markdown("---")

st.markdown("""
<div class="cta-section">
    <h3>Ready to Connect? </h3>
    <p>Navigate using the sidebar menu to learn more about my work, skills, and how to reach me!</p>
</div>
""", unsafe_allow_html=True)
