import streamlit as st
import cv2
from PIL import Image
import numpy as np

st.title("Hinata Pencil Sketch 🎨")

# Upload your image
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Open the image
    image = Image.open(uploaded_file).convert("RGB")
    img_array = np.array(image)

    # Convert to grayscale
    gray_image = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

    # Invert the image
    inverted = 255 - gray_image

    # Blur the image
    blurred = cv2.GaussianBlur(inverted, (21, 21), 0)

    # Invert the blurred image
    inverted_blur = 255 - blurred

    # Create the pencil sketch
    sketch = cv2.divide(gray_image, inverted_blur, scale=256.0)

    # Show original and sketch
    st.image(image, caption="Original Image", use_column_width=True)
    st.image(sketch, caption="Pencil Sketch", use_column_width=True, channels="GRAY")
