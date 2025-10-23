import streamlit as st
import math

# datos de entrada
st.header("Ingresa tus datos")
sexo = st.radio("Sexo", ["Hombre", "Mujer"])
edad = st.slider("Edad (años)", 18, 65, 25)
peso = st.number_input("Peso (kg)", min_value=40.0, max_value=150.0, value=70.0)
altura = st.number_input("Altura (cm)", min_value=140, max_value=220, value=170)

# --- SECCIÓN DE CONTORNOS REQUERIDOS ---
st.subheader("Contornos corporales (cm)")
contorno_brazo = st.number_input("Contorno Brazo (Relajado)", min_value=10.0, max_value=80.0, value=30.0)
contorno_cintura = st.number_input("Contorno Cintura (Mínimo)", min_value=40.0, max_value=150.0, value=80.0)
contorno_cadera = st.number_input("Contorno Cadera (Máximo)", min_value=50.0, max_value=150.0, value=95.0)

# ----------------------------------------
# titulo de %
st.subheader("Pliegues subcutáneos (mm)")
pliegue_biceps = st.number_input("Pliegue bíceps", min_value=2.0, max_value=150.0, value=5.0)
pliegue_triceps = st.number_input("Pliegue tríceps", min_value=2.0, max_value=150.0, value=10.0)
pliegue_subescapular = st.number_input("Pliegue subescapular", min_value=2.0, max_value=150.0, value=8.0)
pliegue_suprailiaco = st.number_input("Pliegue suprailiaco", min_value=2.0, max_value=150.0, value=12.0)

# nivel de actividad fisica
actividad = st.selectbox("Nivel de actividad física",
    ["Sedentario", "Ligero", "Moderado", "Activo", "Muy activo"])

# Tabla de factores de actividad
factores_actividad = {
    "Sedentario": 1.2,
    "Ligero": 1.375,
    "Moderado": 1.55,
    "Activo": 1.725,
    "Muy activo": 1.9
}

# Función para calcular densidad corporal (Durnin-Womersley) CORREGIDA
def calcular_densidad_corporal(sexo, edad, suma_pliegues):
    if sexo == "Hombre":
        if edad < 20:
            C, M = 1.1620, 0.0630
        elif 20 <= edad < 30:
            C, M = 1.1631, 0.0632
        elif 30 <= edad < 40:
            C, M = 1.1422, 0.0544
        elif 40 <= edad < 50:
            C, M = 1.1620, 0.0700
        else:  # 50+
            C, M = 1.1715, 0.0779
    else:  # Mujer
        if edad < 20:
            C, M = 1.1549, 0.0678
        elif 20 <= edad < 30:
            C, M = 1.1599, 0.0717
        elif 30 <= edad < 40:
            C, M = 1.1423, 0.0632
        elif 40 <= edad < 50:
            C, M = 1.1333, 0.0612
        else:  # 50+
            C, M = 1.1339, 0.0645
    densidad = C - (M * math.log10(suma_pliegues))
    return densidad

# Función para calcular % graso CORREGIDA
def calcular_porcentaje_grasa(densidad):
    grasa = (495 / densidad) - 450
    return max(grasa, 0.0)

# Función para calcular metabolismo basal (Harris-Benedict)
def calcular_metabolismo_basal(sexo, peso, altura, edad):
    if sexo == "Hombre":
        mb = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * edad)
    else:
        mb = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * edad)
    return mb

# Botón de calculo y MUESTRA DE RESULTADOS
if st.button("Calcular"):
    suma_pliegues = pliegue_biceps + pliegue_triceps + pliegue_subescapular + pliegue_suprailiaco

    if suma_pliegues <= 0:
        st.error("La suma de los pliegues debe ser mayor que cero para calcular la densidad corporal.")
    else:
        densidad = calcular_densidad_corporal(sexo, edad, suma_pliegues)
        grasa = calcular_porcentaje_grasa(densidad)
        mb = calcular_metabolismo_basal(sexo, peso, altura, edad)
        gasto_total = mb * factores_actividad[actividad]

        st.success(f"""
            **Resultados del Análisis:**

            - **Porcentaje de Grasa Corporal:** `{grasa:.2f}%`
            - **Metabolismo Basal (MB):** `{mb:.2f} kcal/día`
            - **Gasto Calórico Total Diario:** `{gasto_total:.2f} kcal/día`

            *Nota: Los contornos de brazo, cintura y cadera se registraron, pero no se usaron en los cálculos de densidad (Durnin-Womersley) o metabolismo (Harris-Benedict).*
            """)
