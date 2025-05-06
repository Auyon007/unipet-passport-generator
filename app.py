import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import random
import string
import warnings

# Suppress deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Function to generate passport number
def generate_passport_number():
    return "TB" + ''.join(random.choices(string.digits, k=6))

# Title
st.title("Passport Number Overlay Tool")

# Step 1: Upload passport image
uploaded_file = st.file_uploader("Upload your passport image", type=["jpg", "jpeg", "png"])

# Step 2: Initialize session state variables if they don't exist
if "passport_number" not in st.session_state:
    st.session_state.passport_number = ""

if "generated" not in st.session_state:
    st.session_state.generated = False

# Step 3: If file is uploaded, display the image and controls
if uploaded_file:
    image = Image.open(uploaded_file)

    # Step 4: Generate new passport number button
    if st.button("Generate New Passport Number"):
        st.session_state.passport_number = generate_passport_number()
        st.session_state.generated = True
        st.write(f"Generated passport number: **{st.session_state.passport_number}**")

    # Step 5: Show manual input field for passport number
    st.session_state.passport_number = st.text_input("Enter a passport number (or leave blank to auto-generate):", value=st.session_state.passport_number)

    if not st.session_state.passport_number:
        st.session_state.passport_number = generate_passport_number()
        st.write(f"Generated passport number: **{st.session_state.passport_number}**")

    # Step 6: Draw passport number on image
    font_size = 20
    x = 780
    y = 128

    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    # Clear the area where the text will go (optional)
    draw.rectangle([x-5, y-5, x+200, y+font_size+10], fill="white")
    draw.text((x, y), st.session_state.passport_number, fill="black", font=font)

    # Step 7: Display the modified image
    st.image(image, caption="Modified Passport", use_container_width=True)
