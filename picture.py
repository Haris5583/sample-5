import streamlit as st
from PIL import Image, ImageOps, ImageFilter
import numpy as np
import time
import os

st.set_page_config(page_title="Ye Lay Bahi Khosh Hoja", layout="centered")
st.title("🎨  Your Sweet pussy  ")

# Path to your default image
image_path = "default.jpg"  # change this to your file name

if os.path.exists(image_path):
    # Open and convert to grayscale
    image = Image.open(image_path).convert("RGB")
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
        time.sleep(0.05)

    st.success("✨ Drawing complete!")

else:
    st.error(f"Image file '{image_path}' not found. Please add it to the project folder.")



    


