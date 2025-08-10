import streamlit as st
from sketchpy import canvas
import os

st.title("Sketchpy Drawing Demo 🎨")

image_path = "hinata.png"  # Place this in the same folder as app.py

if os.path.exists(image_path):
    # Draw the sketch and save it
    obj = canvas.sketch_from_image(image_path)
    obj.draw()  # This will still try to open a turtle window locally
    
    # Instead of displaying turtle window, just show original image
    st.image(image_path, caption="Hinata Sketch", use_column_width=True)
else:
    st.error(f"Image not found: {image_path}")
