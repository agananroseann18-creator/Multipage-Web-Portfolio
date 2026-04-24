# 🚀 Rose-ann's Portfolio Website

A modern, beautifully designed multipage portfolio website built with Streamlit, featuring a professional design with smooth animations, responsive layout, and interactive components.

## 📋 Features

### 🏠 Home Page
- Eye-catching hero section with dark background
- Feature showcase cards highlighting key sections
- Quick statistics about projects and skills
- Professional call-to-action section
- Profile photo showcase

### 👩 About Page
- Personal introduction and background
- Education details
- Career goals and aspirations
- Hobbies and interests with feature cards
- Additional interests (dancing, singing, favorite quote)

### 📁 Projects Page
- 6+ showcase projects with descriptions
- Technology stack for each project
- Professional project cards with hover effects
- Certifications and achievements gallery
- Interactive project idea suggestion box

### 👩‍💻 Skills Page
- Technical skills with progress bars (Python, JavaScript, HTML/CSS, SQL)
- Web & frameworks expertise (Streamlit, GitHub, Database Management, Bootstrap)
- Soft skills visualization (Problem Solving, Team Collaboration, Communication, Time Management)
- Additional skills grid (Database Management, UI/UX Design, Development Tools)
- Interactive skill assessment tool
- Learning goals and future certifications
- Proficiency summary with metrics

### 📬 Contact Page
- Professional contact form with validation
- Social media links (Email, GitHub, Facebook, Instagram)
- Location and availability information
- Call-to-action section

## 🎨 Design Highlights

### Modern Aesthetics
- **Background color**: Dark color
- **Design Pattern**: Glass morphism with smooth transitions
- **Typography**: Professional fonts with proper hierarchy
- **Spacing**: Consistent padding and margins for readability

### Interactive Elements
- Smooth hover effects on cards
- Animated hero section
- Progress bars for skills
- Expandable accordion sections
- Form validation with user feedback
- Responsive buttons with gradients

### Responsive Design
- Works seamlessly on all screen sizes
- Mobile-friendly layout
- Optimized column layouts
- Adaptive images and content

## 🛠️ Tech Stack

- **Framework**: Streamlit (Python web app framework)
- **Styling**: Custom CSS with gradient backgrounds
- **Components**: Streamlit built-in components + custom HTML/CSS
- **Scripting**: Python 3.x
- **Version Control**: Git

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git (optional)

### Installation Steps

1. **Clone or Download the Repository**
   ```bash
   cd Portfolio_App
   ```

2. **Create a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   venv\Scripts\activate  
   source venv/bin/activate
   ```

3. **Install Required Packages**
   ```bash
   pip install streamlit
   ```

4. **Run the Application**
   ```bash
   streamlit run home.py
   ```

5. **View in Browser**
   - The app will automatically open at `http://localhost:8501`
   - Or manually visit the URL shown in the terminal

## 📁 Project Structure

```
Portfolio_App/
├── home.py                
├── style.py              
├── images/               
│   ├── IMG1.png         
│   ├── IMG2.png
│   ├── IMG3.png
│   ├── IMG4.png
│   ├── IMG5.png
│   ├── gdf_cert.png
│   ├── female.jpeg      
│   ├── studymate.jpeg
│   ├── personalsite.png
│   ├── bus_data_transfer_demo.jpg
│   ├── portfolio.png
│   └── GDF S5.jpeg
├── pages/                 
│   ├── 1_about.py        
│   ├── 2_project.py      
│   ├── 3_skills.py       
│   └── 4_contact.py      
├── photo.png             
└── README.md           
```

## 🎯 How to Customize

### Update Personal Information
Edit the following files to add your personal details:

1. **home.py** - Update name, description, and statistics
2. **pages/1_about.py** - Add your education, goals, and interests
3. **pages/2_project.py** - Add your actual projects with descriptions
4. **pages/3_skills.py** - Update your skills and proficiency levels
5. **pages/4_contact.py** - Update your contact information and social links

### Add Images
1. Place your profile photo as `photo.png` in the root directory
2. Add certification images (IMG1.png through IMG5.png) to the `images/` folder

### Change Colors
Edit **style.py** to modify the color scheme:
- Find the hex colors: `#667eea` and `#764ba2`
- Replace with your preferred colors

### Add More Projects
In **pages/2_project.py**, add items to the `projects` list with:
- `title`: Project name with emoji
- `desc`: Project description
- `tech`: Technologies used

## 🚀 Deployment Options

### Streamlit Cloud (Free)
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Deploy with one click!

### Other Hosting Options
- Heroku
- PythonAnywhere
- AWS
- Google Cloud Platform
- Railway
- Render

## 📝 Customization Tips

### Add More Sections
1. Create a new file in `pages/` folder (e.g., `5_blog.py`)
2. Streamlit will automatically add it to the sidebar navigation
3. Use the same styling patterns from other pages

### Enhance Styling
- Edit `style.py` to add custom CSS
- Use the `.glass`, `.feature-card`, `.cta-section` classes in your HTML
- Modify gradients, shadows, and animations

### Add Interactive Features
- Use Streamlit's form components (`st.form`, `st.text_input`, etc.)
- Add charts with `st.chart_data`, `st.bar_chart`
- Use `st.columns` for responsive layouts

## 🐛 Troubleshooting

### Port Already in Use
```bash
streamlit run home.py --server.port 8502
```

### Images Not Loading
- Ensure images are in the correct folder (`images/` for certifications)
- Check file names match exactly (case-sensitive)
- Use `use_container_width=True` for responsive images

### Styling Not Applying
- Clear browser cache (Ctrl+Shift+Del)
- Restart Streamlit server
- Check CSS class names are correct

## 📞 Support & Contact

For issues or questions about the portfolio:
- Email: agananroseann18@gmail.com
- GitHub: [github.com/roseannaganan](https://github.com/roseannaganan)
- Facebook: [facebook.com/roseann.aganan.31](https://www.facebook.com/roseann.aganan.31)

## 📄 License

This portfolio website is created by Rose-ann Aganan. Feel free to use this as a template for your own portfolio!

## 🎓 Learning Resources

If you want to learn more about building with Streamlit:
- [Streamlit Documentation](https://docs.streamlit.io)
- [Streamlit Community](https://discuss.streamlit.io)
- [Python Web Development](https://python.readthedocs.io)

---
