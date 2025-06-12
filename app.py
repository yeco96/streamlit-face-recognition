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
        "herramientas de jardin", "plantas de interior", "macetas decorativas",
        "bicicleta estatica", "batidos de proteina", "calcetines deportivos",
        "meditacion guiada", "colchoneta yoga", "ropa termica para correr",
        "reloj Garmin", "pesas rusas", "libros de autoayuda",
        "documentales sobre salud", "peliculas de accion", "peliculas romanticas",
        "series policiacas", "juegos de estrategia", "auriculares gamer",
        "teclado mecanico", "mouse gamer", "pantalla 4K",
        "cargador solar portátil", "power bank para viajes", "mochilas de senderismo",
        "zapatos de senderismo", "drone para fotografia", "camara deportiva",
        "accesorios para mascotas", "alimento premium gatos", "correas para perros",
        "decoracion de interiores", "sillas ergonomicas", "escritorios ajustables",
        "pantallas LED decorativas", "luces inteligentes", "robots de limpieza",
        "recetas veganas", "aplicaciones de recetas", "tupper saludables",
        "leggings deportivos", "bandas de resistencia", "guantes de gym",
        "rutinas de cardio", "dietas bajas en carbohidratos", "ejercicios para gluteos",
        "pulsometro deportivo", "gps para correr", "botella de agua reutilizable",
        "esterillas fitness", "cintas de correr", "escaladoras elipticas",
        "peliculas de terror", "documentales de naturaleza", "series de comedia",
        "juegos de aventura", "pc gaming", "sillas gamer",
        "patinetes electricos", "furgonetas camper", "accesorios para coche",
        "viajes de aventura", "campings", "vuelos baratos",
        "semillas para huerto", "fertilizantes", "sistemas de riego",
        "libros de cocina", "ejercicios de respiracion", "cremas hidratantes",
        "mascarillas faciales", "protectores solares", "aceites esenciales",
        "productos para el pelo", "maquillaje natural", "perfumes originales",
        "bicicletas electricas", "monopatines", "surf de remo",
        "esquis", "snowboards", "tiendas de campaña",
        "senderismo con perros", "camas para perros", "juguetes para gatos",
        "comida para peces", "jaulas para pajaros", "terrarios para reptiles",
        "aspiradoras robot", "cafeteras inteligentes", "frigorificos smart",
        "altavoces inteligentes", "camaras de seguridad", "termostatos inteligentes",
        "paneles solares hogar", "bombillas led regulables", "enchufes inteligentes",
        "sensores de movimiento", "cerraduras inteligentes", "alarmas para casa",
        "purificadores de aire", "humidificadores", "deshumidificadores",
        "kits de cultivo indoor", "huertos urbanos", "composteras",
        "cursos de idiomas online", "aplicaciones de productividad", "software de edicion de video",
        "camaras reflex", "objetivos fotograficos", "tripodes",
        "impresoras 3D", "tabletas graficas", "programas de diseño",
        "cursos de programacion", "desarrollo web", "inteligencia artificial",
        "ciberseguridad", "blockchain", "criptomonedas",
        "bolsos de cuero", "carteras elegantes", "joyas de plata",
        "relojes de lujo", "gafas de sol polarizadas", "sombreros de moda",
        "botas de piel", "zapatos de tacon", "sandalias de verano",
        "chaquetas de cuero", "abrigos de lana", "vestidos de fiesta",
        "camisas de vestir", "pantalones vaqueros", "faldas largas",
        "cinturones de marca", "bufandas de seda", "guantes de invierno",
        "ropa de cama", "toallas de bambu", "alfombras persas",
        "cortinas blackout", "espejos decorativos", "cuadros abstractos",
        "floreros de cristal", "velas aromaticas", "cojines de diseño",
        "vajillas de porcelana", "cristalerias finas", "cuberterias de plata",
        "ollas de presion", "sartenes antiadherentes", "robot de cocina",
        "licuadoras de vaso", "exprimidores electricos", "tostadoras de pan",
        "barbacoas de gas", "hornos electricos", "microondas con grill",
        "lavadoras eficientes", "secadoras de ropa", "lavavajillas integrables",
        "kits de herramientas", "taladros inalambricos", "lijadoras electricas",
        "sierras circulares", "medidores laser", "detectores de metales",
        "escaleras telescopicas", "carros de herramientas", "generadores electricos",
        "bombas de agua", "compresores de aire", "hidrolavadoras",
        "muebles de exterior", "hamacas de jardin", "sombrillas de playa",
        "piscinas desmontables", "jacuzzis inflables", "saunas portatiles",
        "aparatos de gimnasia", "pesas ajustables", "bicicletas de spinning",
        "cintas de andar", "maquinas de remo", "elípticas",
        "cursos de cocina", "libros de reposteria", "clases de cocteleria",
        "vinos organicos", "cervezas artesanales", "quesos gourmet",
        "chocolates belgas", "cafes de especialidad", "tes exoticos",
        "masajes relajantes", "spas urbanos", "terapias alternativas",
        "vitaminas y suplementos", "probioticos", "omega 3",
        "proteina en polvo", "creatina", "bcaa",
        "barritas energeticas", "geles energeticos", "bebidas isotónicas",
        "ropa de ciclismo", "cascos de bici", "gafas de sol deportivas",
        "zapatillas de trail running", "bastones de trekking", "mochilas de hidratacion",
        "gafas de natacion", "gorros de piscina", "toallas de microfibra",
        "raquetas de tenis", "pelotas de padel", "palas de playa",
        "patines en linea", "skates", "longboards",
        "equipacion de futbol", "balones de baloncesto", "raquetas de bádminton",
        "discos voladores", "frisbees", "cometas de acrobacia",
        "juegos de mesa", "rompecabezas 3D", "libros para colorear adultos",
        "cursos de fotografia", "edicion de fotos", "diseño grafico",
        "clases de musica", "instrumentos musicales", "software de produccion musical"
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
        "hogar y jardin", "hogar y jardin", "hogar y jardin",
        "fitness", "fitness", "fitness",
        "salud y bienestar", "salud y bienestar", "fitness",
        "tecnologia", "fitness", "salud y bienestar",
        "salud y bienestar", "entretenimiento", "entretenimiento",
        "entretenimiento", "entretenimiento", "tecnologia",
        "tecnologia", "tecnologia", "tecnologia",
        "viajes", "viajes", "deportes al aire libre",
        "deportes al aire libre", "tecnologia", "tecnologia",
        "mascotas", "mascotas", "mascotas",
        "hogar y jardin", "hogar y jardin", "hogar y jardin",
        "hogar y jardin", "hogar y jardin", "hogar y jardin",
        "salud y bienestar", "salud y bienestar", "salud y bienestar",
        "fitness", "fitness", "fitness",
        "fitness", "salud y bienestar", "fitness",
        "tecnologia", "deportes al aire libre", "salud y bienestar",
        "fitness", "fitness", "fitness",
        "entretenimiento", "entretenimiento", "entretenimiento",
        "entretenimiento", "tecnologia", "tecnologia",
        "automovilismo", "automovilismo", "automovilismo",
        "viajes", "viajes", "viajes",
        "hogar y jardin", "hogar y jardin", "hogar y jardin",
        "salud y bienestar", "salud y bienestar", "salud y bienestar",
        "salud y bienestar", "salud y bienestar", "salud y bienestar",
        "salud y bienestar", "salud y bienestar", "salud y bienestar",
        "deportes al aire libre", "deportes al aire libre", "deportes al aire libre",
        "deportes al aire libre", "deportes al aire libre", "viajes",
        "mascotas", "mascotas", "mascotas",
        "mascotas", "mascotas", "mascotas",
        "hogar y jardin", "hogar y jardin", "hogar y jardin",
        "tecnologia", "hogar y jardin", "hogar y jardin",
        "tecnologia", "hogar y jardin", "hogar y jardin",
        "hogar y jardin", "hogar y jardin", "hogar y jardin",
        "salud y bienestar", "salud y bienestar", "salud y bienestar",
        "hogar y jardin", "hogar y jardin", "hogar y jardin",
        "educacion", "educacion", "educacion",
        "tecnologia", "tecnologia", "tecnologia",
        "educacion", "educacion", "tecnologia",
        "tecnologia", "tecnologia", "tecnologia",
        "moda y accesorios", "moda y accesorios", "moda y accesorios",
        "moda y accesorios", "moda y accesorios", "moda y accesorios",
        "moda y accesorios", "moda y accesorios", "moda y accesorios",
        "moda y accesorios", "moda y accesorios", "moda y accesorios",
        "moda y accesorios", "moda y accesorios", "moda y accesorios",
        "moda y accesorios", "moda y accesorios", "moda y accesorios",
        "hogar y jardin", "hogar y jardin", "hogar y jardin",
        "hogar y jardin", "hogar y jardin", "hogar y jardin",
        "hogar y jardin", "hogar y jardin", "hogar y jardin",
        "hogar y jardin", "hogar y jardin", "hogar y jardin",
        "hogar y jardin", "hogar y jardin", "hogar y jardin",
        "hogar y jardin", "hogar y jardin", "hogar y jardin",
        "hogar y jardin", "hogar y jardin", "hogar y jardin",
        "hogar y jardin", "hogar y jardin", "hogar y jardin",
        "hogar y jardin", "hogar y jardin", "hogar y jardin",
        "deportes al aire libre", "deportes al aire libre", "hogar y jardin",
        "hogar y jardin", "hogar y jardin", "hogar y jardin",
        "fitness", "fitness", "fitness",
        "fitness", "fitness", "fitness",
        "salud y bienestar", "salud y bienestar", "salud y bienestar",
        "salud y bienestar", "salud y bienestar", "salud y bienestar",
        "salud y bienestar", "salud y bienestar", "salud y bienestar",
        "salud y bienestar", "salud y bienestar", "salud y bienestar",
        "fitness", "fitness", "fitness",
        "deportes al aire libre", "deportes al aire libre", "deportes al aire libre",
        "deportes al aire libre", "deportes al aire libre", "deportes al aire libre",
        "deportes al aire libre", "deportes al aire libre", "deportes al aire libre",
        "deportes al aire libre", "deportes al aire libre", "deportes al aire libre",
        "deportes al aire libre", "deportes al aire libre", "deportes al aire libre",
        "entretenimiento", "entretenimiento", "entretenimiento",
        "educacion", "educacion", "educacion",
        "educacion", "educacion", "educacion"
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
        "Herramientas de jardinería profesionales", "Plantas exóticas para tu hogar", "Macetas de diseño",
        "Descuento en bicicletas estáticas", "2x1 en batidos de proteína vegana", "Pack de calcetines Nike",
        "App de meditación premium", "Set de yoga con colchoneta ecológica", "Ropa térmica Puma",
        "Ofertas en relojes Garmin", "Pesas rusas con envío gratis", "Top 10 libros de autoayuda",
        "Mejores documentales de salud 2024", "Películas de acción recomendadas", "Clásicos del cine romántico",
        "Maratón de series policiacas", "Steam: descuentos en estrategia", "Auriculares Razer Kraken",
        "Teclado mecánico Logitech", "Mouse gamer RGB", "Pantalla LG 4K de 32 pulgadas",
        "Cargador solar para camping", "Power banks con carga rápida", "Mochilas The North Face",
        "Botas Columbia para senderismo", "Drones DJI con cámara 4K", "GoPro Hero en oferta",
        "Juguetes y accesorios para gatos", "Comida Royal Canin gatos", "Correas resistentes para perros grandes",
        "Decoración estilo escandinavo", "Sillas ergonómicas para home office", "Escritorio regulable eléctrico",
        "Tiras LED con control remoto", "Luces inteligentes Alexa", "Roomba con sensor inteligente",
        "Recetario vegano gratuito", "Apps con más de 10,000 recetas", "Tuppers herméticos y saludables",
        "Leggings deportivos de alta compresión", "Set de bandas elásticas para entrenar", "Guantes de levantamiento de pesas",
        "Programa de cardio online", "Libro de recetas keto", "Guía de ejercicios para tonificar glúteos",
        "Reloj deportivo con pulsómetro integrado", "Oferta en GPS para corredores", "Botellas de agua personalizadas",
        "Esterillas de yoga antideslizantes", "Cintas de correr profesionales", "Elipticas para gimnasio en casa",
        "Estrenos de películas de terror", "Documentales de fauna salvaje", "Series de comedia para toda la familia",
        "Nuevos juegos de aventura para PC", "Ordenadores gaming de última generación", "Sillas gamer ergonómicas",
        "Patinetes eléctricos de Xiaomi", "Alquiler de furgonetas camper", "Accesorios para coche tuning",
        "Viajes de aventura a la montaña", "Campings con piscina en la playa", "Vuelos baratos a Europa",
        "Semillas orgánicas para huerto urbano", "Fertilizantes naturales para plantas", "Sistemas de riego inteligente",
        "Libros de repostería creativa", "Clases de meditación guiada", "Cremas hidratantes antiedad",
        "Mascarillas faciales de arcilla", "Protectores solares para todo tipo de piel", "Sets de aceites esenciales",
        "Productos para el crecimiento del cabello", "Maquillaje ecológico", "Perfumes importados",
        "Bicicletas eléctricas urbanas", "Monopatines de longboard", "Clases de surf de remo",
        "Oferta en esquís Head", "Tablas de snowboard Burton", "Tiendas de campaña Quechua",
        "Arneses para senderismo con perros", "Camas ortopédicas para perros", "Juguetes interactivos para gatos",
        "Alimento premium para peces de acuario", "Jaulas grandes para loros", "Terrarios para reptiles exóticos",
        "Aspiradoras robot Roomba", "Cafeteras inteligentes Nespresso", "Frigoríficos Samsung SmartThings",
        "Altavoces inteligentes Google Home", "Cámaras de seguridad Arlo", "Termostatos inteligentes Nest",
        "Paneles solares para autoconsumo", "Bombillas LED Philips Hue", "Enchufes inteligentes TP-Link Kasa",
        "Sensores de movimiento para el hogar", "Cerraduras inteligentes Yale", "Sistemas de alarma Verisure",
        "Purificadores de aire Dyson", "Humidificadores de aire ultrasónicos", "Deshumidificadores portátiles",
        "Kits de cultivo hidropónico", "Huertos urbanos verticales", "Composteras para residuos orgánicos",
        "Cursos de inglés online con Babbel", "Aplicaciones de organización personal", "Software de edición de video Adobe Premiere",
        "Cámaras réflex Canon EOS", "Objetivos Sigma para fotografía", "Trípodes Manfrotto",
        "Impresoras 3D Ender", "Tabletas gráficas Wacom", "Programas de diseño gráfico CorelDRAW",
        "Cursos de Python para principiantes", "Guía para desarrollo web con React", "Introducción a la Inteligencia Artificial",
        "Cursos de ciberseguridad online", "Explorando la tecnología Blockchain", "Inversión en criptomonedas",
        "Bolsos de cuero artesanales", "Carteras de diseño minimalista", "Joyas de plata con piedras preciosas",
        "Relojes de lujo Rolex", "Gafas de sol polarizadas Ray-Ban", "Sombreros Panamá originales",
        "Botas de piel hechas a mano", "Zapatos de tacón elegantes", "Sandalias de verano para mujer",
        "Chaquetas de cuero auténtico", "Abrigos de lana para invierno", "Vestidos de fiesta largos",
        "Camisas de vestir de seda", "Pantalones vaqueros skinny fit", "Faldas largas bohemias",
        "Cinturones de marca Diesel", "Bufandas de seda estampadas", "Guantes de invierno de lana",
        "Ropa de cama de algodón egipcio", "Toallas de bambú ultrasuaves", "Alfombras persas hechas a mano",
        "Cortinas blackout para el dormitorio", "Espejos decorativos de pared", "Cuadros abstractos modernos",
        "Floreros de cristal soplado", "Velas aromáticas de soja", "Cojines de diseño nórdico",
        "Vajillas de porcelana Bone China", "Cristalerías finas para vino", "Cuberterías de plata de ley",
        "Ollas de presión rápidas", "Sartenes antiadherentes de inducción", "Robot de cocina Thermomix",
        "Licuadoras de vaso de alta potencia", "Exprimidores eléctricos para cítricos", "Tostadoras de pan retro",
        "Barbacoas de gas Weber", "Hornos eléctricos de convección", "Microondas con grill integrado",
        "Lavadoras eficientes de carga frontal", "Secadoras de ropa con bomba de calor", "Lavavajillas integrables Bosch",
        "Kits de herramientas profesionales", "Taladros inalámbricos Bosch", "Lijadoras eléctricas orbitales",
        "Sierras circulares para madera", "Medidores láser de distancia", "Detectores de metales para hobistas",
        "Escaleras telescópicas multiusos", "Carros de herramientas con ruedas", "Generadores eléctricos portátiles",
        "Bombas de agua sumergibles", "Compresores de aire para taller", "Hidrolavadoras de alta presión",
        "Muebles de exterior de ratán", "Hamacas de jardín con soporte", "Sombrillas de playa XXL",
        "Piscinas desmontables Intex", "Jacuzzis inflables Bestway", "Saunas portátiles de vapor",
        "Aparatos de gimnasia multifuncionales", "Pesas ajustables para entrenamiento", "Bicicletas de spinning con monitor",
        "Cintas de andar plegables", "Máquinas de remo de agua", "Elípticas magnéticas silenciosas",
        "Cursos de cocina internacional", "Libros de repostería vegana", "Clases de coctelería molecular",
        "Vinos orgánicos sin sulfitos", "Cervezas artesanales IPA", "Quesos gourmet europeos",
        "Chocolates belgas de alta calidad", "Cafés de especialidad de Colombia", "Tés exóticos de la India",
        "Masajes relajantes con aceites esenciales", "Spas urbanos con tratamientos faciales", "Terapias alternativas de acupuntura",
        "Vitaminas y suplementos para deportistas", "Probióticos para la digestión", "Omega 3 de aceite de pescado",
        "Proteína en polvo de suero", "Creatina monohidrato", "BCAA para la recuperación muscular",
        "Barritas energéticas sin gluten", "Geles energéticos para corredores", "Bebidas isotónicas deportivas",
        "Ropa de ciclismo transpirable", "Cascos de bicicleta de montaña", "Gafas de sol deportivas polarizadas",
        "Zapatillas de trail running Salomon", "Bastones de trekking telescópicos", "Mochilas de hidratación para senderismo",
        "Gafas de natación antivaho", "Gorros de piscina de silicona", "Toallas de microfibra de secado rápido",
        "Raquetas de tenis Babolat", "Pelotas de pádel Head", "Palas de playa para niños",
        "Patines en línea de velocidad", "Skates para principiantes", "Longboards para carving",
        "Equipación de fútbol Adidas", "Balones de baloncesto Spalding", "Raquetas de bádminton Yonex",
        "Discos voladores Ultimate Frisbee", "Frisbees profesionales", "Cometas de acrobacia para adultos",
        "Juegos de mesa estratégicos", "Rompecabezas 3D de edificios famosos", "Libros para colorear antiestrés",
        "Cursos de fotografía digital", "Software de edición de fotos Lightroom", "Diseño gráfico con Photoshop",
        "Clases de guitarra para principiantes", "Instrumentos musicales Yamaha", "Software de producción musical Ableton Live"
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
