# pip install streamlit
# streamlit --help
# streamlit run app.py

#########################################################################

import streamlit as st

# Title-Text
st.header("Its Header")
st.subheader("Its Subheader")
st.markdown("#### It also support markdown")
st.text("Normal Text")
st.caption("Small text")


# Warning
st.success("Success-completion block")
st.warning("Warning block")
st.info("Information Block")
st.error("Error Block")
st.exception("Name Error-pdf not defined")

# Help Function
# import pandas

# st.help(range)
# st.help(pandas)

# Writing Text-super function
st.write("Text with write")
st.write(range(10))
st.write("Hello World")
3 + 9
True
False
729


########################################################################
## Image
from PIL import Image

img = Image.open("static/flipkart.ico")
st.image(img)
import os

st.image(os.path.join(os.getcwd(), "static", "flipkart.ico"))
#######################################################################

# Video adding
# vid_file = open("job.mov", "rb")
# vid_bytes = vid_file.read()
# st.video(vid_bytes)  # 10m

# Audio
# audio_file = open("pop.mp3", "rb").read()
# st.audio(audio_file)


#######################################################################

# Buttons
pressed = st.button("Press me")
print("First : ", pressed)
pressed = st.button("Second Button")
print("Second: ", pressed)


#######################################################################
# Code
code_example = """
def greet(name):
    print("hello",name)
"""
st.code(code_example, language="python")

#######################################################################


# Checkbox
# ML(Gender,M/F)
if st.checkbox("show/Hide"):
    st.text("showing or Hiding widget")

# Radio Buttons
status = st.radio("What is your status", ("Active", "Inactive"))


#######################################################################


# Link with some function
if status == "Active":
    st.success("You are Active")

# Else Function

if status == "Active":
    st.success("You are active")
else:
    st.warning("Inactive, Activate it")


#######################################################################
