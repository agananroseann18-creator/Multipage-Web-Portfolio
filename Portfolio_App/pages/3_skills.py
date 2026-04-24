import streamlit as st
from style import apply_style

apply_style()

st.set_page_config(page_title="Skills", page_icon="👩‍💻", layout="wide")

st.markdown("""
<div class="glass">
    <h1> My Skills</h1>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("## 💻 Technical Skills")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("<h3>Programming Languages</h3>", unsafe_allow_html=True)
    st.progress(85, text="Python - 85%")
    st.progress(80, text="HTML - 80%")
    st.progress(75, text="CSS - 75%")
    st.progress(60, text="MySQL - 60%")

with col2:
    st.markdown("<h3>Web & Frameworks</h3>", unsafe_allow_html=True)
    st.progress(85, text="Streamlit - 85%")
    st.progress(80, text="Git & GitHub - 80%")
    st.progress(75, text="Database Management - 75%")
    st.progress(70, text="Bootstrap - 70%")

st.markdown("---")

st.markdown("## 🌟 Soft Skills")

skill_col1, skill_col2, skill_col3, skill_col4 = st.columns(4, gap="medium")

with skill_col1:
    st.markdown("""
    <div class="feature-card">
        <h3>🧠 Problem Solving</h3>
        <p style="text-align: center; font-size: 1.5rem; color: #667eea; font-weight: bold;">85%</p>
        <p>Analytical thinking and logical approach to challenges</p>
    </div>
    """, unsafe_allow_html=True)

with skill_col2:
    st.markdown("""
    <div class="feature-card">
        <h3>🤝 Team Collaboration</h3>
        <p style="text-align: center; font-size: 1.5rem; color: #667eea; font-weight: bold;">90%</p>
        <p>Excellent communication and teamwork abilities</p>
    </div>
    """, unsafe_allow_html=True)

with skill_col3:
    st.markdown("""
    <div class="feature-card">
        <h3>💬 Communication</h3>
        <p style="text-align: center; font-size: 1.5rem; color: #667eea; font-weight: bold;">80%</p>
        <p>Clear and effective communication skills</p>
    </div>
    """, unsafe_allow_html=True)

with skill_col4:
    st.markdown("""
    <div class="feature-card">
        <h3>⏰ Time Management</h3>
        <p style="text-align: center; font-size: 1.5rem; color: #667eea; font-weight: bold;">85%</p>
        <p>Efficient organization and deadline management</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("## 🎯 Additional Skills & Competencies")

skill_grid_col1, skill_grid_col2, skill_grid_col3 = st.columns(3, gap="medium")

with skill_grid_col1:
    st.markdown("""
    <div class="glass">
        <h4>📊 Database Management</h4>
        <ul style="list-style-type: none; padding: 0;">
            <li>✓ MySQL Database Design</li>
            <li>✓ SQL Queries</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with skill_grid_col2:
    st.markdown("""
    <div class="glass">
        <h4>🎨 UI/UX Design</h4>
        <ul style="list-style-type: none; padding: 0;">
            <li>✓ Responsive Web Design</li>
            <li>✓ User Interface Design</li>
            <li>✓ CSS Styling</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with skill_grid_col3:
    st.markdown("""
    <div class="glass">
        <h4>🔧 Development Tools</h4>
        <ul style="list-style-type: none; padding: 0;">
            <li>✓ VS Code & IDEs</li>
            <li>✓ Project Management Tools</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("## 📈 Interactive Skill Assessment")

st.markdown("""
<div class="glass">
    <p>Test your knowledge by rating skills! This interactive section helps you understand my proficiency levels better.</p>
</div>
""", unsafe_allow_html=True)

assess_col1, assess_col2 = st.columns(2, gap="medium")

with assess_col1:
    skill_to_rate = st.radio(
        "Select a skill to rate:",
        ["Python", "Streamlit", "HTML/CSS", "Problem Solving", "Team Collaboration"],
        horizontal=False
    )

with assess_col2:
    rating = st.slider(f"How would you rate {skill_to_rate}?", 0, 100, 50)

st.progress(rating / 100)

if rating >= 80:
    st.success("🌟 Excellent skill level!")
elif rating >= 60:
    st.info("👍 Good proficiency!")
else:
    st.warning("📚 Room for improvement - always learning!")

st.markdown("---")

# Learning Goals
st.markdown("## 🚀 My Learning Goals")

with st.expander("🔮 Skills I'm Currently Learning"):
    st.markdown("""
    <div class="glass">
        <ul>
            <li><strong>Modern JavaScript Frameworks</strong> - Building interactive web applications</li>
            <li><strong>Full-Stack Development</strong> - Backend and frontend integration</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


st.markdown("---")

st.markdown("## 📊 Proficiency Summary")

col_exp1, col_exp2, col_exp3 = st.columns(3)

with col_exp1:
    st.metric(label="Programming Skills", value="8/10", delta="Improving")

with col_exp2:
    st.metric(label="Web Development", value="8/10", delta="Advancing")

with col_exp3:
    st.metric(label="Problem Solving", value="8.5/10", delta="Excelling")