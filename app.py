import streamlit as st
from deepface import DeepFace
from PIL import Image
import numpy as np
import cv2

st.title("🎭 ¿Qué tan bien te reconoce una máquina?")
st.markdown("Compara dos imágenes usando reconocimiento facial con DeepFace.")

img1_file = st.file_uploader("📷 Imagen 1", type=["jpg", "jpeg", "png"])
img2_file = st.file_uploader("📸 Imagen 2", type=["jpg", "jpeg", "png"])

if img1_file and img2_file:
    img1 = Image.open(img1_file)
    img2 = Image.open(img2_file)
    
    st.image([img1, img2], caption=["Imagen 1", "Imagen 2"], width=300)

    try:
        result = DeepFace.verify(img1, img2, enforce_detection=False)
        if result["verified"]:
            st.success("✅ ¡Las imágenes parecen de la misma persona!")
        else:
            st.warning("❌ No parecen ser la misma persona.")
    except Exception as e:
        st.error(f"Error en el análisis: {str(e)}")
