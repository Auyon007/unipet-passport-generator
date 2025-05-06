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

# Default values
default_x = 780
default_y = 128
default_font_size = 20

# Step 3: If file is uploaded, display the image and controls
if uploaded_file:
    image = Image.open(uploaded_file)

    st.markdown("### Passport Number Controls")

    # Generate New Passport Number Button
    if st.button("Generate New Passport Number"):
        st.session_state.passport_number = generate_passport_number()
        st.session_state.generated = True

    # Manual input for passport number
    st.session_state.passport_number = st.text_input(
        "Enter a passport number (or leave blank to auto-generate):",
        value=st.session_state.passport_number
    )

    if not st.session_state.passport_number:
        st.session_state.passport_number = generate_passport_number()

    # Side-by-side input fields for X, Y, and Font Size
    col1, col2, col3 = st.columns(3)

    with col1:
        x_input = st.text_input("Position X:", value=str(default_x))
    with col2:
        y_input = st.text_input("Position Y:", value=str(default_y))
    with col3:
        size_input = st.text_input("Font Size:", value=str(default_font_size))

    # Convert input to integers
    try:
        x = int(x_input)
    except ValueError:
        x = default_x

    try:
        y = int(y_input)
    except ValueError:
        y = default_y

    try:
        font_size = int(size_input)
    except ValueError:
        font_size = default_font_size

    # Load font
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        st.warning("Custom font not found. Using default font.")
        font = ImageFont.load_default()

    # Draw on image
    draw = ImageDraw.Draw(image)
    draw.rectangle([x - 5, y - 5, x + 200, y + font_size + 10], fill="white")
    draw.text((x, y), st.session_state.passport_number, fill="black", font=font)

    # Show modified image
    st.image(image, caption="Modified Passport", use_container_width=True)
