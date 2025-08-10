import streamlit as st
from PIL import Image, ImageOps, ImageFilter
import numpy as np

st.title("Hinata Pencil Sketch 🎨 (No OpenCV)")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Open and convert to grayscale
    image = Image.open(uploaded_file).convert("RGB")
    gray_image = ImageOps.grayscale(image)

    # Invert the image
    inverted_image = ImageOps.invert(gray_image)

    # Blur the inverted image
    blurred_image = inverted_image.filter(ImageFilter.GaussianBlur(21))

    # Create the pencil sketch using dodge blend
    gray_array = np.array(gray_image, dtype=np.float32)
    blur_array = np.array(blurred_image, dtype=np.float32)
    sketch_array = np.clip(gray_array * 255 / (255 - blur_array + 1e-5), 0, 255).astype(np.uint8)

    # Show results
    st.image(image, caption="Original Image", use_column_width=True)
    st.image(sketch_array, caption="Pencil Sketch", use_column_width=True, channels="GRAY")
