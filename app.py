import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Detective de Datos: Detección de Fraude", layout="wide")

st.title("🕵️‍♂️ El Detective de Datos: Desvelando Patrones de Fraude")

st.write(
    "Imagina que somos un banco y queremos detectar transacciones sospechosas. "
    "Usaremos la Ciencia de Datos para encontrar patrones 'extraños' en nuestros datos."
)

st.sidebar.header("Configuración de la Detección")

# --- Generación de Datos Simulados ---
@st.cache_data
def generate_data(num_transactions=1000, num_fraud=30):
    np.random.seed(42) # Para reproducibilidad

    # Transacciones normales
    normal_monto = np.random.normal(loc=50, scale=20, size=num_transactions)
    normal_frecuencia = np.random.normal(loc=3, scale=1, size=num_transactions)
    df_normal = pd.DataFrame({
        'Monto_Transaccion': np.clip(normal_monto, 1, 100), # Monto entre 1 y 100
        'Frecuencia_Compra_Dia': np.clip(normal_frecuencia, 0.5, 5), # Frecuencia entre 0.5 y 5
        'Tipo': 'Normal'
    })

    # Transacciones fraudulentas (simulamos que son de montos muy altos y/or frecuencias muy bajas)
    fraud_monto = np.random.normal(loc=150, scale=30, size=num_fraud)
    fraud_frecuencia = np.random.normal(loc=0.8, scale=0.3, size=num_fraud)
    df_fraud = pd.DataFrame({
        'Monto_Transaccion': np.clip(fraud_monto, 100, 200),
        'Frecuencia_Compra_Dia': np.clip(fraud_frecuencia, 0.1, 1.5),
        'Tipo': 'Fraude'
    })

    df = pd.concat([df_normal, df_fraud], ignore_index=True)
    df = df.sample(frac=1, random_state=42).reset_index(drop=True) # Mezclar los datos
    return df

df = generate_data()

st.subheader("Simulación de Transacciones Bancarias")
st.write(f"Hemos generado {len(df)} transacciones para nuestro análisis.")
st.dataframe(df.head())

# --- Gráfico de Dispersión Interactivo ---
st.subheader("Análisis Visual de Transacciones")
st.write(
    "Observa cómo se agrupan las transacciones por su **Monto** y **Frecuencia de Compra**. "
    "Las transacciones de fraude (en rojo) suelen ser 'puntos atípicos' que se desvían de lo normal."
)

fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x='Frecuencia_Compra_Dia',
    y='Monto_Transaccion',
    hue='Tipo', # Colorear por tipo (Normal/Fraude)
    palette={'Normal': 'blue', 'Fraude': 'red'},
    s=100,
    alpha=0.7,
    ax=ax
)
ax.set_title("Monto vs. Frecuencia de Compra por Transacción")
ax.set_xlabel("Frecuencia de Compra por Día")
ax.set_ylabel("Monto de Transacción ($)") # CORRECTED LINE
st.pyplot(fig)

# --- Detector de Fraude con Umbral Interactivo ---
st.sidebar.subheader("Ajuste del Umbral de Detección")
st.sidebar.write(
    "Ajusta el umbral del **Monto de Transacción** para ver cuántas transacciones "
    "sospechosas podemos 'detectar'. Una transacción será marcada como fraude si su monto supera este umbral."
)

umbral_monto = st.sidebar.slider(
    "Monto Mínimo para Fraude ($)",
    min_value=50.0,
    max_value=200.0,
    value=100.0, # Umbral por defecto
    step=5.0
)

st.sidebar.write(
    "Ajusta el umbral de la **Frecuencia de Compra** para afinar la detección. "
    "Una transacción será marcada como fraude si su frecuencia es *inferior* a este umbral."
)
umbral_frecuencia = st.sidebar.slider(
    "Frecuencia Máxima para Fraude (por día)",
    min_value=0.1,
    max_value=5.0,
    value=1.5, # Umbral por defecto
    step=0.1
)

# Aplicar el umbral y contar detecciones
df['Detectado_como_Fraude'] = (df['Monto_Transaccion'] > umbral_monto) & \
                             (df['Frecuencia_Compra_Dia'] < umbral_frecuencia)

num_detectado = df['Detectado_como_Fraude'].sum()
num_fraude_real = df[df['Tipo'] == 'Fraude'].shape[0]

st.subheader("Resultados de la Detección")
col1, col2 = st.columns(2)

with col1:
    st.metric(label="Transacciones Marcadas como Sospechosas", value=num_detectado)
with col2:
    st.metric(label="Transacciones de Fraude Real (en nuestros datos)", value=num_fraude_real)

st.write(
    f"Al aplicar los umbrales de Monto > ${umbral_monto:.2f} y Frecuencia < {umbral_frecuencia:.2f} compras/día, "
    f"hemos marcado **{num_detectado}** transacciones como potencialmente fraudulentas."
)

st.write("---")
st.write(
    "**Conclusión para tus compañeros:**"
    "Como ven, la Ciencia de Datos nos permite ir más allá de lo obvio. "
    "Al visualizar y ajustar parámetros, podemos entrenar a nuestros 'detectives de datos' "
    "para identificar patrones que, de otra forma, pasarían desapercibidos. "
    "Esto es crucial para proteger el dinero de los clientes y la salud financiera del banco."
)
