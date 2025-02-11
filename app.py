import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


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

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Pujan :wave:")
    st.title("An AI Engineer Intern From Nepal")
    st.write(
        "I am a computer science undergraduate passionate about leveraging AI, machine learning, and computer vision technologies to enhance traffic management systems, develop autonomous vehicles, and create innovative solutions for pedestrian safety."
    )
    st.write("[Learn More >](https://www.linkedin.com/in/pujan-pant/)")

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
        st.write("[View Portfolio >](https://github.com/pantpujan017)")
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
        st.subheader("Emergency-Vehicle-Route-Optimization-using-SUMO")
        st.write(
            """
            Optimizing emergency vehicle routes using SUMO! 🚑⚡
This project focuses on reducing response times by simulating and optimizing traffic flow for emergency vehicles.
Explore the code and implementation on GitHub!.
            """
        )
        st.markdown("[More on...](https://github.com/pantpujan017/Emergency-Vehicle-Route-Optimization-using-SUMO.git)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/pantpujan017@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()