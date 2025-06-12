import streamlit as st
import pandas as pd

st.set_page_config(page_title="¿Cómo me espía el algoritmo?", layout="centered")
st.title("🧠 ¿Cómo me espía el algoritmo?")
st.subheader("Simulación de un sistema de recomendación")

st.markdown("""
Esta demo simula cómo un algoritmo de recomendación analiza los gustos de diferentes usuarios y genera sugerencias personalizadas.
""")

# Dataset ficticio de contenido
catalogo = pd.DataFrame([
    {"Nombre": "Stranger Things", "Género": "Ciencia Ficción"},
    {"Nombre": "Dark", "Género": "Ciencia Ficción"},
    {"Nombre": "Breaking Bad", "Género": "Drama"},
    {"Nombre": "Narcos", "Género": "Crimen"},
    {"Nombre": "Mindhunter", "Género": "Crimen"},
    {"Nombre": "The Office", "Género": "Comedia"},
    {"Nombre": "Brooklyn Nine-Nine", "Género": "Comedia"},
    {"Nombre": "Game of Thrones", "Género": "Fantasía"},
    {"Nombre": "The Witcher", "Género": "Fantasía"},
    {"Nombre": "Black Mirror", "Género": "Ciencia Ficción"},
])

# Perfiles simulados de usuarios
usuarios = {
    "Usuario 1 - Crimen": ["Narcos", "Mindhunter"],
    "Usuario 2 - Comedia": ["The Office", "Brooklyn Nine-Nine"],
    "Usuario 3 - Fantasía": ["The Witcher", "Game of Thrones"],
    "Usuario 4 - Ciencia Ficción": ["Stranger Things", "Dark"],
    "Usuario 5 - Drama + Crimen": ["Breaking Bad", "Narcos"]
}

usuario_seleccionado = st.selectbox("👤 Elige un usuario para simular", list(usuarios.keys()))
gustos = usuarios[usuario_seleccionado]

# Mostrar gustos
st.markdown(f"**Contenido visto por {usuario_seleccionado}:**")
for titulo in gustos:
    st.markdown(f"- {titulo}")

# Inferencia de género preferido
gustos_df = catalogo[catalogo["Nombre"].isin(gustos)]
generos = gustos_df["Género"].value_counts()
genero_preferido = generos.idxmax()

# Mostrar resultado
st.markdown(f"🔍 El algoritmo ha detectado que este usuario prefiere el género **{genero_preferido}**.")

# Recomendaciones
sugerencias = catalogo[~catalogo["Nombre"].isin(gustos)]
recomendadas = sugerencias[sugerencias["Género"] == genero_preferido]

st.markdown("🎯 **Recomendaciones generadas automáticamente:**")
for nombre in recomendadas["Nombre"].sample(min(3, len(recomendadas))):
    st.markdown(f"- {nombre}")
