import streamlit as st
import pandas as pd

# --- Conjunto de Datos de Búsquedas y Temas de Interés ---
# Este es nuestro "historial" de búsquedas y los temas de interés asociados.
# En un sistema real, esto provendría de una base de datos o un data lake.
data = {
    "busqueda": [
        "zapatillas deportivas", "ropa de ejercicio", "suplementos fitness",
        "recetas saludables", "entrenamiento en casa", "yoga principiantes",
        "smartwatch deportivo", "auriculares inalambricos gym",
        "camisetas running", "mancuernas ajustables",
        "peliculas de ciencia ficcion", "series de fantasia", "libros de misterio",
        "videojuegos de rol", "consolas de nueva generacion",
        "coches electricos", "motos deportivas", "bicicletas de montaña",
        "viajes a la playa", "hoteles baratos",
        "herramientas de jardin", "plantas de interior", "macetas decorativas"
    ],
    "tema_interes": [
        "fitness", "fitness", "fitness",
        "salud y bienestar", "fitness", "salud y bienestar",
        "tecnologia", "tecnologia",
        "fitness", "fitness",
        "entretenimiento", "entretenimiento", "entretenimiento",
        "entretenimiento", "tecnologia",
        "automovilismo", "automovilismo", "deportes al aire libre",
        "viajes", "viajes",
        "hogar y jardin", "hogar y jardin", "hogar y jardin"
    ],
    "anuncio_sugerido": [
        "Oferta de zapatillas Nike", "Descuento en ropa Adidas", "Promo en proteínas",
        "Curso de cocina saludable online", "App de entrenamiento personalizado", "Clases de yoga en línea",
        "Nuevo Apple Watch", "Audífonos Bluetooth JBL",
        "Ropa deportiva Under Armour", "Mancuernas ajustables PowerBlock",
        "Estrenos en Netflix", "Sagas literarias épicas", "Novelas de suspense",
        "Juegos para PlayStation 5", "Ofertas en consolas Xbox",
        "Test drive de Tesla", "Motos Ducati a tu medida", "Bicicletas de montaña Trek",
        "Paquetes turísticos a Cancún", "Hoteles con descuento en Punta Cana",
        "Herramientas de jardinería profesionales", "Plantas exóticas para tu hogar", "Macetas de diseño"
    ]
}

df_busquedas = pd.DataFrame(data)

# --- Función para Sugerir Anuncios ---
def sugerir_anuncios(busqueda_usuario):
    # Convertir la búsqueda del usuario a minúsculas para una comparación insensible a mayúsculas
    busqueda_usuario_lower = busqueda_usuario.lower()

    # Buscar temas de interés relacionados con la búsqueda del usuario
    temas_relacionados = df_busquedas[df_busquedas["busqueda"].str.contains(busqueda_usuario_lower, case=False)]["tema_interes"].unique()

    sugerencias = []
    if len(temas_relacionados) > 0:
        # Si encontramos temas relacionados, sugerimos anuncios basados en esos temas
        for tema in temas_relacionados:
            anuncios_posibles = df_busquedas[df_busquedas["tema_interes"] == tema]["anuncio_sugerido"].tolist()
            sugerencias.extend(anuncios_posibles)
    else:
        # Si no hay coincidencias directas, se podría implementar una lógica más compleja
        # (por ejemplo, buscar palabras clave, usar modelos de embeddings, etc.)
        # Para este ejemplo simple, si no hay coincidencia directa, sugerimos anuncios generales
        sugerencias = ["Anuncios generales: ¡Descubre ofertas en productos variados!", "Prueba nuestros servicios premium", "Explora nuevas categorías"]

    # Eliminar duplicados y devolver una muestra limitada
    return list(set(sugerencias))[:5] # Limitar a 5 sugerencias para no abrumar

# --- Interfaz de Usuario con Streamlit ---
st.set_page_config(page_title="Emulación de Anuncios Sugeridos", layout="centered")

st.title("🔎 Emulación de Sugerencia de Anuncios Basada en Búsquedas")
st.markdown("""
Este ejemplo simula cómo las búsquedas de un usuario en una plataforma
podrían influir en los anuncios que se le muestran.
Introduce algunas palabras clave en el buscador y mira qué anuncios se sugieren.
""")

st.subheader("Simulador de Búsqueda")
user_input = st.text_input("¿Qué estás buscando hoy?", placeholder="Ej: zapatillas deportivas, peliculas de ciencia ficcion, viajes")

if user_input:
    st.subheader("Anuncios Sugeridos para ti:")
    sugerencias_anuncios = sugerir_anuncios(user_input)

    if sugerencias_anuncios:
        for anuncio in sugerencias_anuncios:
            st.info(f"👉 {anuncio}")
    else:
        st.write("No hay sugerencias de anuncios en este momento para tu búsqueda específica. ¡Intenta con otras palabras clave!")

st.markdown("---")
st.subheader("Cómo funciona (Detrás de Escena):")
st.markdown("""
1.  **Conjunto de Datos:** Tenemos un conjunto de datos simple que asocia palabras clave de búsqueda con "temas de interés" (por ejemplo, 'fitness', 'entretenimiento', 'viajes').
2.  **Mapeo:** Cuando ingresas una búsqueda, el sistema intenta mapear tus palabras clave a uno o más de estos temas de interés.
3.  **Sugerencia:** Una vez que se identifica un tema de interés, se muestran anuncios que están pre-asociados con ese tema en nuestro conjunto de datos.
""")

st.subheader("Datos de Ejemplo Utilizados:")
st.dataframe(df_busquedas)

st.caption("Nota: Este es un ejemplo simplificado. Un sistema de sugerencia de anuncios real sería mucho más complejo, utilizando algoritmos de machine learning, análisis de comportamiento del usuario, historial de clics, datos demográficos, etc.")
