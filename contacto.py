import streamlit as st

def contact_page():
    """
    Define el contenido y la lógica de la página de contacto.
    """
    st.title("📞 Contáctanos")
    st.markdown("---") # Separador visual

    st.write(
        "¿Quienes somos? Somos una organizacion gubernamental encargada de la seguridad mundial que busca garantizar la paz y erradicar a los inmigrantes ilegales"
    " ¿Tienes alguna pregunta, sugerencia o acaso tu vecino tiene acento medio raro? "
        "¡Estaremos encantados de leer tu caso! Por favor, llena el siguiente formulario."
    )
#Formulario de Contacto
#Usamos st.form para agrupar los elementos del formulario
    with st.form(key='contact_form', clear_on_submit=True):
# Campos del formulario
        name = st.text_input('👤 Tu Nombre', placeholder='Ej: Juan Pérez')
        email = st.text_input('📧 Tu Correo Electrónico', placeholder='Ej: tu.correo@dominio.com')
        message = st.text_area('📝 Mensaje', placeholder='Escribe tu mensaje aquí...', height=150)

# Botón de enviar (debe estar dentro del bloque with st.form)
        submit_button = st.form_submit_button(label='Enviar Mensaje')

        if submit_button:
            if not name or not email or not message:
                st.error("🚨 **Error:** Por favor, completa todos los campos para enviar el mensaje.")
            else:

#Para este ejemplo, solo mostramos un mensaje de éxito
                st.success(f"✅ ¡Mensaje enviado con éxito, **{name}**! Te responderemos pronto a **{email}**.")
#st.write(f"Datos recibidos - Nombre: {name}, Email: {email}, Mensaje: {message}")

#Información de Contacto Adicional
    st.markdown("---")
    st.subheader("Otras formas de contacto")
    st.info(
        "También puedes encontrarnos en:\n\n"
        "* **Correo Directo:** reytilinJhandeimer@hotmail.com\n"
        "* **Teléfono:** +335 456 7890 (Lunes a Viernes, 9am - 5pm)"
    )

if __name__ == "__main__":
    contact_page()