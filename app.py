import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression

# Dataset simulado con y sin sesgo
def get_dataset(biased=True):
    if biased:
        # Modelo sesgado: rechaza sistemáticamente ciertos perfiles
        data = {
            'income': [50000, 60000, 30000, 40000, 80000, 35000],
            'gender': [0, 1, 0, 1, 0, 1],  # 0: Masculino, 1: Femenino
            'race':   [0, 0, 1, 1, 0, 1],  # 0: Blanco, 1: Negro
            'approved': [1, 1, 0, 0, 1, 0]
        }
    else:
        # Modelo justo: decisiones basadas solo en ingresos, no en género/raza
        data = {
            'income': [50000, 60000, 30000, 40000, 80000, 35000],
            'gender': [0, 1, 0, 1, 0, 1],
            'race':   [0, 0, 1, 1, 0, 1],
            'approved': [1, 1, 0, 1, 1, 0]  # Más balanceado y justo
        }
    return pd.DataFrame(data)

# Entrena un modelo simple
def train_model(biased=True):
    df = get_dataset(biased)
    X = df[['income', 'gender', 'race']]
    y = df['approved']
    model = LogisticRegression()
    model.fit(X, y)
    return model

# Predicción
def predict(model, income, gender, race):
    X_new = pd.DataFrame([[income, gender, race]], columns=['income', 'gender', 'race'])
    return model.predict(X_new)[0]

# ==============================
# Interfaz de Streamlit
# ==============================

st.title("⚖️ ¿Y si el algoritmo es racista?")
st.markdown("### Simulación de sesgo en un modelo de aprobación de crédito")
st.markdown("Este ejemplo muestra cómo un modelo puede tomar decisiones injustas si los datos con los que fue entrenado contienen sesgos.")

# Entrada de usuario
income = st.number_input("💵 Ingreso anual (USD)", min_value=10000, max_value=100000, step=5000)
gender = st.selectbox("🧍 Género", ["Masculino", "Femenino"])
race = st.selectbox("🧑 Raza", ["Blanco", "Negro"])

# Convertir a valores numéricos
gender_val = 0 if gender == "Masculino" else 1
race_val = 0 if race == "Blanco" else 1

# Entrenar modelos
biased_model = train_model(biased=True)
fair_model = train_model(biased=False)

# Realizar predicciones
biased_result = predict(biased_model, income, gender_val, race_val)
fair_result = predict(fair_model, income, gender_val, race_val)

# Mostrar resultados
st.markdown("## 🧪 Resultados:")
st.write(f"🔴 **Modelo con sesgo:** {'✅ Aprobado' if biased_result else '❌ Rechazado'}")
st.write(f"🟢 **Modelo justo:** {'✅ Aprobado' if fair_result else '❌ Rechazado'}")

# Análisis ético
if biased_result != fair_result:
    st.warning("⚠️ El modelo sesgado tomó una decisión distinta influenciada por género o raza.")
else:
    st.success("✅ Ambos modelos llegaron a la misma decisión.")

# Detalles opcionales
with st.expander("🔎 Ver datos de entrenamiento"):
    st.markdown("#### Modelo Sesgado")
    st.dataframe(get_dataset(biased=True))
    st.markdown("#### Modelo Justo")
    st.dataframe(get_dataset(biased=False))
