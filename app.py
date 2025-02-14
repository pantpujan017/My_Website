import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

linkedin_img = Image.open("images/linkedin.png")
github_img = Image.open("images/github.png")
mail_img = Image.open("images/mail.png")

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/emergency.png")
img_lottie_animation = Image.open("images/IMG_5651.jpg")

# Load social media icons
linkedin_icon = Image.open("images/linkedin.png")  # Make sure to add these images
github_icon = Image.open("images/github.png")      # to your images folder

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Pujan :wave:")
    st.title("An AI Engineer Intern From Nepal")
    st.write(
        "I am a computer science undergraduate passionate about leveraging AI, machine learning, and computer vision technologies to enhance traffic management systems, develop autonomous vehicles, and create innovative solutions for pedestrian safety."
    )

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            As an AI Engineer Intern, I work on:
            - Building self-driving car systems with computer vision for lane and sign detection
            - Developing smart traffic solutions and emergency vehicle routing systems
            - Creating medical imaging AI for brain tumor detection
            - Designing recommendation engines and automated chatbot systems
            - Building custom language models for financial applications

            If you're interested in AI innovations that solve real-world problems, check out my projects below.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Self Driving Car")
        st.write(
            """
            Check out my self-driving car project using Raspberry Pi and image processing! 🚗💡
            This project uses a YOLOv4-tiny model for real-time object detection, enabling autonomous navigation.
            Explore the code and implementation on GitHub!
            """
        )
        st.markdown("[More on...](https://github.com/pantpujan017/Self-Driving-Car.git)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Emergency Vehicle Route Optimization using SUMO")
        st.write(
            """
            Optimizing emergency vehicle routes using SUMO! 🚑⚡
            This project focuses on reducing response times by simulating and optimizing traffic flow for emergency vehicles.
            Explore the code and implementation on GitHub!.
            """
        )
        st.markdown("[More on...](https://github.com/pantpujan017/Emergency-Vehicle-Route-Optimization-using-SUMO.git)")


# ---- CONNECT WITH ME ----
with st.container():
    st.write("---")
    st.header("Connect with me")

    # Using columns with smaller spacing
    col1, col2, col3 = st.columns([1, 1,1])

    # Define CSS for clickable icons with hover effect
    icon_style = """
    <style>
        .icon-container {
            display: flex;
            justify-content: center;
            gap: 40px;  /* Adjust spacing between icons */
        }
        .icon-container a img {
            width: 45px; /* Adjust size */
            transition: transform 0.2s ease-in-out;
        }
        .icon-container a:hover img {
            transform: scale(1.1); /* Slight zoom effect */
            cursor: pointer; /* Changes cursor to pointer on hover */
        }
    </style>
    """
    st.markdown(icon_style, unsafe_allow_html=True)

    # Display social icons in a row with spacing
    st.markdown(
        """
        <div class="icon-container">
            <a href="https://www.linkedin.com/in/pujan-pant/" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png">
            </a>
            <a href="https://github.com/pantpujan017" target="_blank">
                <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png">
            </a>
            <a href="mailto:pantpujan017@gmail.com">
                <img src="https://upload.wikimedia.org/wikipedia/commons/7/7e/Gmail_icon_%282020%29.svg">
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
