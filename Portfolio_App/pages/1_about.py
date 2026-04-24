import streamlit as st
import os
from style import apply_style

apply_style()

st.set_page_config(page_title="About", page_icon="👩", layout="wide")

st.markdown("""
<div class="glass">
    <h1>About Me</h1>
</div>
""", unsafe_allow_html=True)

col_photo, col_intro = st.columns([1, 2], gap="large")

with col_photo:
    if os.path.exists("photo.png"):
        st.image("photo.png", use_container_width=True)
    else:
        st.markdown("""
        <div class="placeholder-image">
            📸 Profile Photo
        </div>
        """, unsafe_allow_html=True)

with col_intro:
    st.markdown("""
    <div class="glass">
        <h3>Welcome! 👋</h3>
        <p>I'm Rose-ann Aganan, a computer science student with a strong passion for web development, and graphic design.
        I'm dedicated to continuously learning and growing 
        in this dynamic field of technology.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="glass">
        <h3>🎓 Education</h3>
        <p><strong>Elementary: Milagros East Central School (2009-2017)</strong></p>
        <p><strong>Junior High: Liceo De San Jose INC.(2017-2021)</strong></p>
        <p><strong>Senior High: Liceo De San Jose INC.(2021-2023)</strong></p>
        <p><strong>College: Dr. Emilio B. Espinosa Sr. Memorial State College of Agriculture and Technology (2023-present)</strong></p>
        <p><strong>Degree: Bachelor of Science in Computer Science</strong></p>        
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="glass">
        <h3>🎯 My Goals</h3>
        <ul style="list-style-type: none; padding: 0;">
            <li>✨ Become a skilled and proficient full-stack web developer</li>
            <li>✨ Become a skilled and proficient graphic designer</li>
            <li>✨ Stay updated with latest industry trends</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("## 🌟 Hobbies & Interests")

hobby_col1, hobby_col2, hobby_col3 = st.columns(3, gap="medium")

with hobby_col1:
    st.markdown("""
    <div class="feature-card">
        <h3>📖 Reading</h3>
        <p>I love diving into novels, self-improvement books, and engaging stories. Reading helps me expand my perspective and discover new ideas.</p>
    </div>
    """, unsafe_allow_html=True)

with hobby_col2:
    st.markdown("""
    <div class="feature-card">
        <h3>🎵 Music</h3>
        <p>Pop music is my go-to companion while coding late at night. It keeps me energized and focused on solving problems.</p>
    </div>
    """, unsafe_allow_html=True)

with hobby_col3:
    st.markdown("""
    <div class="feature-card">
        <h3>✍️ Writing</h3>
        <p>I express my creativity through writing spoken word poetry. It's a wonderful way to communicate emotions and thoughts.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("## 🎨 More About Me")

with st.expander("🕺 Dancing"):
    st.markdown("""
    <div class="glass">
        <p>I'm passionate about hip-hop, freestyle, and krumping dance styles. Dance is another creative outlet that keeps me active and expressive.</p>
    </div>
    """, unsafe_allow_html=True)

with st.expander("🎤 Singing"):
    st.markdown("""
    <div class="glass">
        <p>Whether it's in the shower or at karaoke nights with friends, I love singing. It brings joy and laughter to those around me.</p>
    </div>
    """, unsafe_allow_html=True)

with st.expander("💭 My Favorite Quote"):
    st.markdown("""
    <div class="glass" style="border-left: 4px solid #667eea; background: #f8f9ff;">
        <p style="font-size: 1.1rem; font-weight: 500;">
        <em>\"Do it while you're young, do it while you're strong, because someday you'll get old, 
        you'll be weak, so do it now.\"</em></p>
        <p style="text-align: right; color: #94a3b8; margin-top: 10px;">— Geo Ong</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.write("@copyright 2026 Rose-ann Aganan. Built using Python & Streamlit.")
