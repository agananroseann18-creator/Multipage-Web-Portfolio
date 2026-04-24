import streamlit as st

def apply_style():
    st.markdown("""
    <style>
    /* Modern Dark Theme Background */
    .stApp {
        background: linear-gradient(135deg, #1a1a1a 0%, #1a1a1a 100%) !important;
    }
    
    /* Main content area */
    .main .block-container {
        background: transparent !important;
        padding-top: 2rem !important;
    }
    
    /* Sidebar styling - dark modern */
    .stSidebar {
        background: linear-gradient(180deg, #2a2a2a 0%, #1f1f1f 100%) !important;
        border-right: 1px solid #404040 !important;
        box-shadow: 2px 0 12px rgba(0, 0, 0, 0.1) !important;
    }
    
    .stSidebar .stMarkdown, 
    .stSidebar .stRadio label {
        color: #f5f5f5 !important;
    }
    
    .glass {
        background: #2d2d2d !important;
        padding: 24px !important;
        border-radius: 10px !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2), 0 1px 2px rgba(0, 0, 0, 0.1) !important;
        margin-bottom: 20px !important;
        border: 1px solid #404040 !important;
        transition: all 0.2s ease !important;
    }
    
    .glass:hover {
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3) !important;
        transform: translateY(-2px) !important;
    }
    
    h1 {
        color: #00d4aa !important;
        font-weight: 600 !important;
        font-size: 2.5rem !important;
        letter-spacing: -0.02em !important;
    }
    
    h2 {
        color: #f5f5f5 !important;
        font-weight: 600 !important;
        font-size: 1.8rem !important;
        letter-spacing: -0.01em !important;
    }
    
    h3 {
        color: #00d4aa !important;
        font-weight: 500 !important;
    }
    
    p, li, .stMarkdown {
        color: #f5f5f5 !important;
        line-height: 1.6 !important;
    }
    
    .stTextInput label, 
    .stTextArea label, 
    .stSelectbox label {
        color: #f5f5f5 !important;
        font-weight: 500 !important;
    }
    
    .stTextInput input, 
    .stTextArea textarea, 
    .stSelectbox select {
        border: 1px solid #404040 !important;
        border-radius: 8px !important;
        background-color: #2d2d2d !important;
        color: #f5f5f5 !important;
        appearance: none !important;
        -webkit-appearance: none !important;
        -moz-appearance: none !important;
    }
    
    select option {
        color: #000000 !important;
        background-color: #ffffff !important;
        background: #ffffff !important;
        padding: 5px !important;
    }
    
    select option:checked {
        background: linear-gradient(#00d4aa, #00d4aa) !important;
        background-color: #00d4aa !important;
        color: #000000 !important;
    }
    
    .stTextInput input:focus, 
    .stTextArea textarea:focus {
        border-color: #00d4aa !important;
        box-shadow: 0 0 0 2px rgba(0, 212, 170, 0.1) !important;
        outline: none !important;
    }
    
    .stProgress > div > div > div > div {
        background-color: #00d4aa !important;
        border-radius: 10px !important;
    }
    
    .stProgress > div {
        background-color: #404040 !important;
        border-radius: 10px !important;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #00d4aa 0%, #00b894 100%) !important;
        color: #1a1a1a !important;
        font-weight: 500 !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.5rem 1.5rem !important;
        transition: all 0.2s ease !important;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #00b894 0%, #00a085 100%) !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 12px rgba(0, 212, 170, 0.25) !important;
    }
    
    .stAlert {
        border-radius: 10px !important;
        border-left: 4px solid !important;
        background-color: #2d2d2d !important;
        color: #f5f5f5 !important;
    }
    
    .stAlert > div {
        background-color: #2d2d2d !important;
    }
    
    [data-testid="stMetric"] {
        background: #2d2d2d !important;
        padding: 1rem !important;
        border-radius: 10px !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2) !important;
        border: 1px solid #404040 !important;
    }
    
    [data-testid="stMetric"] label {
        color: #b0b0b0 !important;
        font-weight: 500 !important;
    }
    
    [data-testid="stMetric"] .stMetricValue {
        color: #f5f5f5 !important;
        font-weight: 700 !important;
        font-size: 1.8rem !important;
    }
    
    .streamlit-expanderHeader {
        background-color: #2d2d2d !important;
        border-radius: 8px !important;
        color: #f5f5f5 !important;
        font-weight: 500 !important;
    }
    
    .streamlit-expanderContent {
        background-color: #1f1f1f !important;
        border-radius: 0 0 8px 8px !important;
        border: 1px solid #404040 !important;
        border-top: none !important;
    }
    
    hr {
        margin: 2rem 0 !important;
        border: none !important;
        height: 1px !important;
        background: linear-gradient(90deg, transparent, #404040, transparent) !important;
    }
    
    .stImage figcaption {
        color: #b0b0b0 !important;
        font-size: 0.8rem !important;
        text-align: center !important;
    }
    
    .stRadio > div {
        gap: 0.5rem !important;
    }
    
    .stRadio label {
        background: transparent !important;
        padding: 8px 12px !important;
        border-radius: 8px !important;
        transition: background 0.2s ease !important;
        color: #f5f5f5 !important;
    }
    
    .stRadio label:hover {
        background: #404040 !important;
    }
    
    .stRadio [data-testid="stMarkdown"] p {
        font-weight: 500 !important;
        color: #00d4aa !important;
    }
    
    .footer {
        text-align: center;
        padding: 2rem;
        color: white;
        font-size: 0.8rem;
        border-top: 1px solid #404040;
        margin-top: 3rem;
    }
    </style>
    """, unsafe_allow_html=True)
    