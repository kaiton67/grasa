# Importar streamlit
import streamlit as st

# Configurar la pagina
st.set_page_config(
    page_title="Test Alternos grasosos :V",
    page_icon=":blue_heart:", # Usar el comando python -m rich.emoji para ver lista de emojis
    layout="centered",
)


#Crear las multipaginas
pg = st.navigation(["Inicio.py", "Prueba.py","grasas.py","contacto.py"])
pg.run()