import streamlit as st
import os
from style import apply_style

apply_style()

st.set_page_config(page_title="Projects", page_icon="📁", layout="wide")

st.markdown("""
<div class="glass">
    <h1>My Projects</h1>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="glass">
    <p>Here are some of my projects. Each project represents a learning milestone 
    in my journey as a student developer. Feel free to explore them!</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

projects = [
    {
        "title": "Female Dormitory Management System",
        "desc": "A comprehensive management system for tracking and managing the operations of a female dormitory. This project helped me learn database design and system architecture.",
        "tech": "Microsoft Access, MySQL",
        "image": "images/female.jpeg"
    },
    {
        "title": "StudyMate Homework Tracker",
        "desc": "A simple application to help students track and manage their homework assignments. Perfect for keeping organized during school.",
        "tech": "HTML, CSS, JavaScript",
        "image": "images/studymate.jpeg"
    },
    {
        "title": "My Website",
        "desc": "A personal website to showcase my skills and projects. My first venture into web development.",
        "tech": "HTML, CSS, JavaScript",
        "image": "images/personalsite.png"
    },
    {
        "title": "Bus Data Transfer Demo",
        "desc": "A simulation on how data is transferred across a bus system. An educational project for learning computer architecture.",
        "tech": "HTML5, JavaScript",
        "image": "images/bus_data_transfer_demo.jpg"
    },
    {
        "title": "Personal Portfolio Website",
        "desc": "A multi-page portfolio website using Streamlit to showcase my skills, projects, and contact information. You're viewing it right now!",
        "tech": "Python, Streamlit",
        "image": "images/portfolio.png"
    },
    {
        "title": "GDF Session 5",
        "desc": "A project created during the GDF Session 5 workshop.",
        "tech": "Picsart, Ibispaint",
        "image": "images/GDF S5.jpeg"
    }
    
]

for project in projects:
    col_img, col_info = st.columns([1, 2], gap="large")
    
    with col_img:
        image_path = project.get("image", "")
        if image_path:
            image_path = image_path.replace('\\', '/')
            if not os.path.isabs(image_path) and not image_path.startswith("images/"):
                image_path = os.path.join("images", image_path)

        if image_path and os.path.exists(image_path):
            st.image(image_path, use_container_width=True)
        else:
            st.markdown(f"""
            <div class="feature-card" style="height: 220px; display: flex; align-items: center; justify-content: center;">
                <div style="text-align: center;">
                    <h2>🖼️</h2>
                    <p style="font-weight: bold;">Project Image</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with col_info:
        st.markdown(f"""
        <div class="glass">
            <h3>{project['title']}</h3>
            <p>{project['desc']}</p>
            <p><strong>🛠️ Technologies:</strong> {project['tech']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("")

st.markdown("---")

st.markdown("## 🏅 My Certifications & Achievements")

cert_col1, cert_col2, cert_col3= st.columns(3, gap="small")

with cert_col1:
    try:
        st.image("images/IMG1.png", use_container_width=True)
        st.caption("Python Essentials 1")
    except:
        st.markdown("""
        <div class="feature-card" style="text-align: center;">
            <h3>📜</h3>
            <p>Python Essentials 1</p>
        </div>
        """, unsafe_allow_html=True)

with cert_col2:
    try:
        st.image("images/IMG2.png", use_container_width=True)
        st.caption("Python for Beginners")
    except:
        st.markdown("""
        <div class="feature-card" style="text-align: center;">
            <h3>📜</h3>
            <p>Python for Beginners</p>
        </div>
        """, unsafe_allow_html=True)

with cert_col3:
    try:
        st.image("images/IMG3.png", use_container_width=True)
        st.caption("Web Designing Basics")
    except:
        st.markdown("""
        <div class="feature-card" style="text-align: center;">
            <h3>📜</h3>
            <p>Web Designing Basics</p>
        </div>
        """, unsafe_allow_html=True)
cert_col4, cert_col5, cert_col6= st.columns(3, gap="small")
with cert_col4:
    try:
        st.image("images/IMG4.png", use_container_width=True)
        st.caption("Software Testing")
    except:
        st.markdown("""
        <div class="feature-card" style="text-align: center;">
            <h3>📜</h3>
            <p>Software Testing</p>
        </div>
        """, unsafe_allow_html=True)

with cert_col5:
    try:
        st.image("images/IMG5.png", use_container_width=True)
        st.caption("Project Management 101")
    except:
        st.markdown("""
        <div class="feature-card" style="text-align: center;">
            <h3>📜</h3>
            <p>Project Management 101</p>
        </div>
        """, unsafe_allow_html=True)

with cert_col6:
    try:
        st.image("images/gdf_cert.png", use_container_width=True)
        st.caption("GDF Session 5")
    except:
        st.markdown("""
        <div class="feature-card" style="text-align: center;">
            <h3>📜</h3>
            <p>GDF Session 5</p>
        </div>
        """, unsafe_allow_html=True)
st.markdown("---")

st.markdown("## 💡 Share Your Ideas")

with st.expander("💡 Have a project idea?"):
    st.markdown("""
    <div class="glass">
        <p>I'm always looking for new challenges and opportunities to learn. If you have a project idea,
        I'd love to hear about it!</p>
    </div>
    """, unsafe_allow_html=True)
    
    suggestion = st.text_area(
        "Share your project idea:",
        placeholder="Describe a project you'd like to see me build...",
        height=120
    )
    if st.button("Submit Suggestion", use_container_width=True):
        if suggestion:
            st.success("✅ Thanks for the suggestion! I'll consider adding it to my roadmap.")
        else:
            st.warning("⚠️ Please enter a suggestion before submitting.")