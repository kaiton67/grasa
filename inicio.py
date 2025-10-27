#Linea para importar la biblioteca streamlit
import streamlit as st
#linea para escribir un titulo
st.title("TEST DE ALTERNOS")
#linea de subtitulo
st.markdown("Proyecto inspirado en el universo del Mandela Catalogue, no apto para asustadisos, niños, tontitos, personas de bajo intelecto, enfermos cardiacos, enfermos terminales y loquitos, ademas de estar dirigido especialmente para las personas(especificamente:danieles, matias y maximilianos) de la region metropólitana pero tambien para el resto de Chile como precaucion. ")

# Imagen de portada
st.image("mand.jpg", caption="**Ellos se ven como nosotros...**")

# Sección descriptiva
st.header("¿Qué es esta aplicación?")
st.write(
    """
    Esta aplicación es una **experiencia interactiva de terror psicológico**, inspirada en el universo del *Mandela Catalogue*.  
    Aquí pondremos a prueba tu **percepción**, tu **capacidad para distinguir la realidad**, y tu **resistencia mental** ante lo desconocido.

    El **Test de Alternos** no busca solo asustarte, sino **evaluar tu reacción** frente a estímulos ambiguos y señales de suplantación.

    *Advertencia: algunas imágenes, sonidos o decisiones podrían resultar perturbadoras.*
    """
)
st.image("visto2.png", caption="**Ellos observan, siempre al acecho...**")

# Presentación del objetivo
st.subheader("Objetivo del Proyecto")
st.write(
    """
    El objetivo de esta aplicación es simular un **entrenamiento del Departamento de Defensa** del Condado de Mandela,
    diseñado para identificar **Alternos**: entidades que **imitan la forma humana** pero carecen de empatía y racionalidad.

    En versiones futuras, podrás:
    - Realizar un **test visual** con fotografías de humanos y alternos.
    - Escuchar **grabaciones distorsionadas** y decidir si provienen de una persona o una entidad.
    - Participar en **simulaciones interactivas** donde tus decisiones determinarán tu destino.
    """
)

