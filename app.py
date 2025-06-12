import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression

# Dataset ficticio con sesgo (simulación)
def get_dataset(biased=True):
    data = {
        'income': [50000, 60000, 30000, 40000, 80000, 35000],
        'gender': [0, 1, 0, 1, 0, 1],  # 0: Male, 1: Female
        'race': [0, 0, 1, 1, 0, 1],    # 0: White, 1: Black
        'approved': [1, 1, 0, 0, 1, 0] if biased else [1, 1, 1, 1, 1, 1]
    }
    return pd.DataFrame(data)

def train_model(biased=True):
    df = get_dataset(biased)
    X = df[['income', 'gender', 'race']]
    y = df['approved']
    model = LogisticRegression()
    model.fit(X, y)
    return model

def predict(model, income, gender, race):
    X_new = pd.DataFrame([[income, gender, race]], columns=['income', 'gender', 'race'])
    return model.predict(X_new)[0]

# UI
st.title("⚖️ ¿Y si el algoritmo es racista?")
st.subheader("Simulación: Aprobación de crédito con y sin sesgo")

income = st.number_input("Ingreso anual (USD)", 10000, 100000, step=5000)
gender = st.selectbox("Género", ["Masculino", "Femenino"])
race = st.selectbox("Raza", ["Blanco", "Negro"])

# Convertir inputs a valores numéricos
gender_val = 0 if gender == "Masculino" else 1
race_val = 0 if race == "Blanco" else 1

# Modelos
biased_model = train_model(biased=True)
fair_model = train_model(biased=False)

# Predicciones
biased_result = predict(biased_model, income, gender_val, race_val)
fair_result = predict(fair_model, income, gender_val, race_val)

st.markdown("### Resultados:")
st.write(f"🔴 **Modelo con sesgo:** {'Aprobado ✅' if biased_result else 'Rechazado ❌'}")
st.write(f"🟢 **Modelo justo:** {'Aprobado ✅' if fair_result else 'Rechazado ❌'}")

if biased_result != fair_result:
    st.warning("⚠️ El modelo sesgado tomó una decisión diferente basada en género o raza.")
else:
    st.success("✅ Ambos modelos llegaron al mismo resultado.")

