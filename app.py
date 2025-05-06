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

    # Step 6: Sliders for position (X, Y) and font size
    col1, col2 = st.columns([1, 2])  # Create two columns for input fields
    with col1:
        x = st.slider("Position X:", min_value=0, max_value=1000, value=780)
    with col2:
        x_input = st.text_input("X Position Manual:", value=str(x))  # Text input for Position X
    
    with col1:
        y = st.slider("Position Y:", min_value=0, max_value=1000, value=128)
    with col2:
        y_input = st.text_input("Y Position Manual:", value=str(y))  # Text input for Position Y
    
    with col1:
        font_size = st.slider("Font Size:", min_value=10, max_value=100, value=20)
    with col2:
        font_size_input = st.text_input("Font Size Manual:", value=str(font_size))  # Text input for Font Size

    # If user manually edits the input fields, update the variables
    try:
        x = int(x_input) if x_input else x
        y = int(y_input) if y_input else y
        font_size = int(font_size_input) if font_size_input else font_size
    except ValueError:
        st.warning("Please enter valid numeric values in the manual input fields!")

    # Step 7: Draw passport number on image with updated position and font size
    # Always recreate the image each time to ensure the changes are reflected
    image = Image.open(uploaded_file)  # Reload the image from uploaded file to preserve it

    draw = ImageDraw.Draw(image)
    
    # Try using a default font or load a custom one if available
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()  # Fallback to default font if custom font is unavailable

    # Clear the area where the text will go (optional)
    draw.rectangle([x-5, y-5, x+200, y+font_size+10], fill="white")
    draw.text((x, y), st.session_state.passport_number, fill="black", font=font)

    # Step 8: Display the modified image
    st.image(image, caption="Modified Passport", use_container_width=True)
