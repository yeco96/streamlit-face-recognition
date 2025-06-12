import streamlit as st
import face_recognition
import numpy as np
import cv2
from PIL import Image

st.set_page_config(page_title="Reconocimiento Facial en Vivo", layout="centered")
st.title("🎭 ¿Qué tan bien te reconoce una máquina?")

st.markdown("Sube una imagen de una persona conocida y luego otra imagen para ver si la puede reconocer.")

# Cargar imagen de referencia
known_image_file = st.file_uploader("📷 Sube una imagen conocida (rostro de referencia)", type=["jpg", "jpeg", "png"])
# Cargar imagen para analizar
unknown_image_file = st.file_uploader("🔍 Sube una imagen donde buscar (puede haber más de un rostro)", type=["jpg", "jpeg", "png"])

if known_image_file and unknown_image_file:
    # Cargar las imágenes
    known_image = face_recognition.load_image_file(known_image_file)
    unknown_image = face_recognition.load_image_file(unknown_image_file)

    # Obtener encoding del rostro conocido
    known_encodings = face_recognition.face_encodings(known_image)
    if not known_encodings:
        st.error("⚠️ No se detectó ningún rostro en la imagen conocida.")
    else:
        known_encoding = known_encodings[0]

        # Detectar rostros en la imagen desconocida
        face_locations = face_recognition.face_locations(unknown_image)
        face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

        # Convertir imagen para mostrar con OpenCV
        image_to_show = unknown_image.copy()

        found = False
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            match = face_recognition.compare_faces([known_encoding], face_encoding)[0]
            color = (0, 255, 0) if match else (0, 0, 255)
            text = "Encontrado ✅" if match else "Desconocido ❌"
            found = found or match

            # Dibujar recuadro
            cv2.rectangle(image_to_show, (left, top), (right, bottom), color, 2)
            cv2.putText(image_to_show, text, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

        # Mostrar resultado
        st.image(image_to_show, channels="RGB", caption="Resultado del reconocimiento")
        if found:
            st.success("🎉 ¡El rostro fue encontrado en la imagen!")
        else:
            st.warning("👀 El rostro no fue encontrado.")

