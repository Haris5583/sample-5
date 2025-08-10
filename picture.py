import streamlit as st
from PIL import Image, ImageOps, ImageFilter
import numpy as np
import time

st.set_page_config(page_title="Hinata Sketch Animation", layout="centered")
st.title("🎨 Hinata Pencil Sketch Animation")

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

    st.subheader("Sketch Animation:")
    sketch_placeholder = st.empty()

    # Animation: reveal sketch gradually
    steps = 30  # number of frames
    for i in range(1, steps + 1):
        progress_mask = np.zeros_like(sketch_array)
        rows = int((i / steps) * sketch_array.shape[0])
        progress_mask[:rows, :] = sketch_array[:rows, :]
        sketch_placeholder.image(progress_mask, use_container_width=True, channels="GRAY")
        time.sleep(0.05)  # delay between frames

    st.success("✨ Drawing complete!")




    
