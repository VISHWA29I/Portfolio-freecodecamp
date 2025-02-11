# import streamlit as st
# from PIL import Image
# import base64
# from io import BytesIO

# # Function to convert image to base64
# def image_to_base64(image):
#     buffered = BytesIO()
#     image.save(buffered, format="JPEG")
#     return base64.b64encode(buffered.getvalue()).decode()

# # Page Configuration
# st.set_page_config(page_title="Vishwaraj's Portfolio", layout="wide")

# # Custom Styling
# st.markdown(
#     """
#     <style>
#         body {background-color: #f4f4f4;}
#         .title {text-align: center; font-size: 40px; font-weight: bold; color: #333;}
#         .subtitle {text-align: center; font-size: 20px; color: #555; background: linear-gradient(90deg, #0073b1, #00c6ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: bold;}
#         .section-title {font-size: 25px; font-weight: bold; color: #444; margin-top: 20px; background: linear-gradient(90deg, #0073b1, #00c6ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent;}
#         .contact-links a {text-decoration: none; margin-right: 15px; font-size: 18px; color: #0073b1;}
#         .container {padding: 20px;}
#         .navbar {background-color: #0073b1; padding: 10px; text-align: center; border-radius: 10px; margin-bottom: 20px;}
#         .navbar a {color: white; text-decoration: none; font-size: 18px; margin: 0 15px; padding: 8px 15px; transition: all 0.3s ease;}
#         .navbar a:hover {background-color: white; color: #0073b1; border-radius: 5px;}
#         .button {background-color: #0073b1; color: white; padding: 10px 20px; border-radius: 5px; text-align: center; display: inline-block; transition: all 0.3s ease;}
#         .button:hover {background-color: white; color: #0073b1; border: 1px solid #0073b1;}
#         .profile-img {border-radius: 50%; display: block; margin: 0 auto; width: 250px; height: 250px; object-fit: cover;}
#         .highlight {background: linear-gradient(90deg, #0073b1, #00c6ff); color: white; padding: 5px 10px; border-radius: 5px; display: inline-block;}
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Navbar
# st.markdown(
#     """
#     <div class='navbar'>
#         <a href='#about'>About</a>
#         <a href='#skills'>Skills</a>
#         <a href='#projects'>Projects</a>
#         <a href='#contact'>Contact</a>
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# # Load Profile Image
# col1, col2 = st.columns([1, 2])
# with col1:
#     image = Image.open("u.jpg")  # Replace with your image file path
#     st.markdown(f"<img src='data:image/jpeg;base64,{image_to_base64(image)}' class='profile-img'>", unsafe_allow_html=True)
# with col2:
#     st.markdown("<p class='title'>🚀 Vishwaraj's Portfolio</p>", unsafe_allow_html=True)
#     st.markdown("<p class='subtitle'>Aspiring Data Engineer | Big Data Analytics | Open to Collaboration & Learning</p>", unsafe_allow_html=True)

# # About Me Section
# st.markdown("<p class='section-title' id='about'>👨‍💻 About Me</p>", unsafe_allow_html=True)
# st.write("""
# - 🎓 **PG Diploma in Big Data Analytics**
# - 💡 Passionate about **transforming data into insights**
# - 🛠 Skilled in **Python, SQL, Apache Spark, Hadoop, ETL, Tableau, Cloud**
# - 📊 Experience in **Fraud Detection, Energy Analytics**
# """)

# # Skills Section
# st.markdown("<p class='section-title' id='skills'>🛠️ Skills</p>", unsafe_allow_html=True)
# skills = ["Python", "SQL", "Apache Spark", "Hadoop", "ETL Workflows", "Big Data Analytics", "Tableau", "Cloud Technologies"]
# st.write(" | ".join(skills))

# # Projects Section
# st.markdown("<p class='section-title' id='projects'>📂 Projects</p>", unsafe_allow_html=True)
# project = st.selectbox("Select a Project to View Details", ["Fraud Detection Model", "Energy Analytics Dashboard"])
# if project == "Fraud Detection Model":
#     st.write("🔍 Developed a fraud detection model using machine learning techniques with Spark and SQL.")
# elif project == "Energy Analytics Dashboard":
#     st.write("⚡ Designed an interactive Tableau dashboard for analyzing renewable energy trends.")

# # Contact Info with Buttons
# st.sidebar.header("📬 Connect with Me")
# st.sidebar.markdown("""
# [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/your-profile)  
# [![GitHub](https://img.shields.io/badge/GitHub-Profile-lightgray?style=flat&logo=github)](https://github.com/your-profile)  
# 📧 Email: your.email@example.com
# """)

# st.markdown("<p class='section-title' id='contact'>📩 Let's Connect!</p>", unsafe_allow_html=True)
# st.write("I am always open to collaboration and learning new technologies. Let's connect and explore how we can work together! 🚀")

# # Add a Call-to-Action Button
# st.markdown("""
#     <a href='mailto:your.email@example.com' class='button'>📩 Contact Me</a>
# """, unsafe_allow_html=True)

import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Function to convert image to base64
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()

# Page Configuration
st.set_page_config(page_title="Vishwaraj Singh", layout="wide")

# Custom Styling
st.markdown(
    """
    <style>
        body {background-color: #f4f4f4;}
        .title {text-align: center; font-size: 40px; font-weight: bold; color: #555;}
        .subtitle {text-align: center; font-size: 20px; color: #555; background: linear-gradient(90deg, #0073b1, #00c6ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: bold;}
        .section-title {font-size: 25px; font-weight: bold; color: #444; margin-top: 20px; background: linear-gradient(90deg, #0073b1, #00c6ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent;}
        .contact-links a {text-decoration: none; margin-right: 15px; font-size: 18px; color: #0073b1;}
        .container {padding: 20px;}
        .navbar {background-color: #0073b1; padding: 10px; text-align: center; border-radius: 10px; margin-bottom: 20px;}
        .navbar a {color: white; text-decoration: none; font-size: 18px; margin: 0 15px; padding: 8px 15px; transition: all 0.3s ease;}
        .navbar a:hover {background-color: white; color: #0073b1; border-radius: 5px;}
        .button {background-color: #0073b1; color: white; padding: 10px 20px; border-radius: 5px; text-align: center; display: inline-block; transition: all 0.3s ease;}
        .button:hover {background-color: white; color: #0073b1; border: 1px solid #0073b1;}
        .profile-img {border-radius: 50%; display: block; margin: 0 auto; width: 250px; height: 250px; object-fit: cover;}
        .social-links {text-align: center; margin-top: 10px;}
        .social-links a {text-decoration: none; margin: 0 10px;}
        .social-links img {width: 30px; height: 30px;}
    </style>
    """,
    unsafe_allow_html=True
)

# Navbar
st.markdown(
    """
    <div class='navbar'>
        <a href='#about'>About</a>
        <a href='#skills'>Skills</a>
        <a href='#projects'>Projects</a>
        <a href='#contact'>Contact</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Load Profile Image
col1, col2 = st.columns([1, 2])
with col1:
    image = Image.open("u.jpg")  # Replace with your image file path
    st.markdown(f"<img src='data:image/jpeg;base64,{image_to_base64(image)}' class='profile-img'>", unsafe_allow_html=True)
with col2:
    st.markdown("<p class='title'>🚀 Hey There  I am Vishwaraj Singh   ", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Aspiring Data Engineer | Big Data Analytics | Open to Collaboration & Learning</p>", unsafe_allow_html=True)
    
   

# About Me Section
st.markdown("<p class='section-title' id='about'>👨‍💻 About Me</p>", unsafe_allow_html=True)
st.write("""
- 🎓 **PG Diploma in Big Data Analytics**
- 💡 Passionate about **transforming data into insights**
- 🛠 Skilled in **Python, SQL, Apache Spark, Hadoop, ETL, Tableau, Cloud**
- 📊 Experience in **Fraud Detection, Energy Analytics**
""")

# Skills Section
st.markdown("<p class='section-title' id='skills'>🛠️ Skills</p>", unsafe_allow_html=True)
skills = ["Python", "SQL", "Apache Spark", "Hadoop", "ETL Workflows", "Big Data Analytics", "Tableau", "Cloud Technologies"]
st.write(" | ".join(skills))

# Projects Section
st.markdown("<p class='section-title' id='projects'>📂 Projects</p>", unsafe_allow_html=True)
project = st.selectbox("Select a Project to View Details", ["Fraud Detection Model", "Energy Analytics Dashboard"])
if project == "Fraud Detection Model":
    st.write("🔍 Developed a fraud detection model using machine learning techniques with Spark and SQL.")
elif project == "Energy Analytics Dashboard":
    st.write("⚡ Designed an interactive Tableau dashboard for analyzing renewable energy trends.")

# Contact Info with Buttons
st.sidebar.header("📬 Connect with Me")
st.sidebar.markdown("""
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/vishwaraj2011/)  
[![GitHub](https://img.shields.io/badge/GitHub-Profile-lightgray?style=flat&logo=github)](https://github.com/vishwaraj14)  
📧 Email: your.email@example.com
""")

st.markdown("<p class='section-title' id='contact'>📩 Let's Connect!</p>", unsafe_allow_html=True)
st.write("I am always open to collaboration and learning new technologies. Let's connect and explore how we can work together! 🚀")

# Add a Call-to-Action Button
st.markdown("""
    <a href='mailto:your.email@example.com' class='button'>📩 Contact Me</a>
""", unsafe_allow_html=True)