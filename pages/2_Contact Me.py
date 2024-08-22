import streamlit as st
import os

def load_css():
    # Define the path to the CSS file
    css_path = os.path.join(os.path.dirname(__file__), '../styles/main.css')
    
    # Read and load the CSS file
    with open(css_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load the CSS in Contact Me page
load_css()

st.write("---")
st.write("# Connect with Me!")
contact_form = """
<form action="https://formsubmit.co/engr.marvinbaesa01@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here"></textarea>
    <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)
