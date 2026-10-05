import streamlit as st
import os
from dotenv import load_dotenv
from openai import AsyncOpenAI

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenRouter API Key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Initialize OpenRouter Client using OpenAI SDK with Custom Base URL
client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

# Page Configuration
st.set_page_config(
    page_title="Happy Teachers Day - Umexo Labs",
    page_icon="🎓",
    layout="centered"
)

# Custom CSS for VIP styling, Cursive typography, and Animated Balloons
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Poppins:wght@300;400;600;700&display=swap');

    .main {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #311042 100%);
        color: #ffffff;
    }
    
    .cursive-title {
        font-family: 'Pacifico', cursive;
        font-size: 3.2rem;
        color: #f43f5e;
        text-align: center;
        text-shadow: 2px 2px 15px rgba(244, 63, 94, 0.6);
        margin-bottom: 0px;
    }

    .subtitle {
        font-family: 'Poppins', sans-serif;
        font-size: 1.4rem;
        color: #38bdf8;
        text-align: center;
        font-weight: 600;
        margin-top: 10px;
        margin-bottom: 25px;
    }

    .card-box {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        margin-bottom: 20px;
    }

    .project-title {
        font-family: 'Poppins', sans-serif;
        color: #a78bfa;
        font-weight: 700;
        font-size: 1.2rem;
    }

    .mentor-credit {
        font-family: 'Poppins', sans-serif;
        text-align: center;
        font-size: 1.15rem;
        color: #34d399;
        font-weight: 600;
        background: rgba(52, 211, 153, 0.1);
        padding: 18px;
        border-radius: 12px;
        border: 1px dashed #34d399;
        margin-top: 20px;
        line-height: 1.6;
    }

    /* CSS Floating Balloons Animation */
    @keyframes bounceBalloon {
        0%, 100% { transform: translateY(0) scale(1); }
        50% { transform: translateY(-15px) scale(1.1); }
    }
    .animated-balloons {
        font-size: 2.8rem;
        text-align: center;
        animation: bounceBalloon 1.5s infinite ease-in-out;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Session state initialization
if 'entered' not in st.session_state:
    st.session_state.entered = False

if not st.session_state.entered:
    # --- LANDING SCREEN ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    st.markdown('<div class="animated-balloons">🎈 🎈 🎈 🎉 🎈 🎈 🎈</div>', unsafe_allow_html=True)
    st.markdown('<p class="cursive-title">Sir Umar & Miss Umm-e-Habiba</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Happy Teacher\'s Day! Specially You ✨</p>', unsafe_allow_html=True)
    
    st.markdown("""
        <div style="text-align: center; color: #cbd5e1; font-family: 'Poppins', sans-serif; font-size: 1.1rem; margin-bottom: 40px;">
            A small token of appreciation for the finest mentors at Umexo Labs, who equipped me with the skills to code on my own. 🚀
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎁 Open Tribute Website", use_container_width=True):
            st.session_state.entered = True
            st.rerun()

else:
    # --- MAIN PROJECTS & WISHES SCREEN ---
    st.markdown('<div class="animated-balloons">🎉 🎈 🌟 🎈 🎉</div>', unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: center; font-family: \"Poppins\", sans-serif; color: #f43f5e;'>Happy Teacher's Day to My Mentors! 🌟</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-family: \"Poppins\", sans-serif; color: #94a3b8;'>Dedicated with utmost respect and gratitude to Umexo Labs</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Mentor Credit Box
    st.markdown("""
        <div class="mentor-credit">
            👑 None other than our esteemed mentors, <b>Sir Umar</b> and <b>Miss Umm-e-Habiba</b>, made me capable of building all these projects and writing code! Thank you both so much for your relentless hard work and guidance. 🙏
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("🛠️ My Projects & Creations (Built under your guidance)")

    # Project 1: Voice Command Software
    st.markdown("""
        <div class="card-box">
            <span class="project-title">🎙️ Voice Command Software</span>
            <p style="color: #cbd5e1; margin-top: 8px;">Advanced speech recognition applications built to execute system and utility commands seamlessly through voice input.</p>
        </div>
    """, unsafe_allow_html=True)

    # Project 2: Python Programming
    st.markdown("""
        <div class="card-box">
            <span class="project-title">🐍 Python Programming & Logic</span>
            <p style="color: #cbd5e1; margin-top: 8px;">Mastering core Python programming concepts, environment management, and developing robust backend logic.</p>
        </div>
    """, unsafe_allow_html=True)

    # Project 3: Autonomous Coding & AI Agents
    st.markdown("""
        <div class="card-box">
            <span class="project-title">🤖 Autonomous Coding & AI Agents</span>
            <p style="color: #cbd5e1; margin-top: 8px;">Building next-generation autonomous coding workflows, custom AI agents, and intelligent developer tools.</p>
        </div>
    """, unsafe_allow_html=True)

    # Project 4: Mini-Devin AI Engineer
    st.markdown("""
        <div class="card-box">
            <span class="project-title">⚡ Mini-Devin AI Engineer</span>
            <p style="color: #cbd5e1; margin-top: 8px;">An advanced AI engineering tool built using Streamlit and agentic workflows to autonomously manage and assist in development tasks.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔄 Back to Welcome Screen", use_container_width=True):
            st.session_state.entered = False
            st.rerun()