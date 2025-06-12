import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Datos de ejemplo
data = pd.DataFrame({
    'Región': ['Norte', 'Sur', 'Este', 'Oeste'],
    'Producto A': [75, 80, 65, 90],
    'Producto B': [85, 70, 60, 88]
})

st.set_page_config(page_title="Del dato al poder", layout="centered")

st.title("📊 ¿Del dato al poder o a la manipulación?")
st.write("Misma data, distintas visualizaciones. ¿Cuál te convence más?")

st.subheader("🔍 Datos crudos")
st.dataframe(data)

# Selector de tipo de gráfico
chart_type = st.selectbox(
    "Selecciona tipo de gráfico a mostrar:", 
    ["Bar Chart Comparativo", "Área acumulada", "Line Chart con exageración", "Pie Chart por región"]
)

# Gráfico: Barras comparativas
if chart_type == "Bar Chart Comparativo":
    fig, ax = plt.subplots()
    data.plot(x="Región", kind="bar", ax=ax, color=["skyblue", "orange"])
    ax.set_title("Comparación directa entre productos")
    st.pyplot(fig)

# Gráfico: Área acumulada
elif chart_type == "Área acumulada":
    fig, ax = plt.subplots()
    data.set_index("Región").plot.area(ax=ax, alpha=0.6)
    ax.set_title("Percepción acumulada por región")
    st.pyplot(fig)

# Gráfico: Línea con escala exagerada
elif chart_type == "Line Chart con exageración":
    exaggerated = data.copy()
    exaggerated[['Producto A', 'Producto B']] = exaggerated[['Producto A', 'Producto B']] * 10
    fig, ax = plt.subplots()
    exaggerated.set_index("Región").plot(ax=ax, linestyle='--', marker='o')
    ax.set_title("Escala exagerada (¡cuidado con la manipulación!)")
    st.pyplot(fig)

# Gráfico: Pie chart por región
elif chart_type == "Pie Chart por región":
    region = st.selectbox("Selecciona la región:", data["Región"])
    row = data[data["Región"] == region][['Producto A', 'Producto B']].iloc[0]
    fig, ax = plt.subplots()
    ax.pie(row, labels=row.index, autopct='%1.1f%%', startangle=90, colors=["lightgreen", "salmon"])
    ax.set_title(f"Participación en la región {region}")
    st.pyplot(fig)
