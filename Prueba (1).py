#Importar la libreria streamlit para el funcionamiento de codigo
import streamlit as st

#Para el titulo
st.title("Test Non es Solus")

#Para escribir texto en la pagina
st.write("""En esta sección podras realizar el test N.S, antes de iniciar necesitamos algunos datos
esenciales para mejor tu experiencia como usuario humano.
""")

#Variable para el nombre en la pagina
name = st.text_input("Ingresa tu nombre")

#Para poder avanzar en el test se necesita elegir uno de estos nombres gracias a esta linea
if name == "Daniel" or name == "Matias" or name == "Mori" or name == "Maxi" or name == "Gonzalo" or name =="Yonakleison":

    #Variable para edad y elegirla con una barra interactuable
    age = st.slider("Cuanto tiempo(años) has estado sin incidentes mortales?", 0, 100, 0)
    #Para escribir texto en la pagina con la variable edad
    st.write("tengo ", age, "años")

    #Para poder avanzar elegir la edad entre 16 y 34 en la pagina 
    if 15 < age and 35 > age:
        #Para escribir texto en la pagina
        st.write("Evacua la zona inmediatamente")
        
        #Para poder elegir entre varias opciones con radio y la variable region
        region = st.radio(
        "En que región vives",
        ["Tarapaca", "Antofagasta", "Atacama", "Coquimbo","Valparaiso","Region metropolitana", "O'Higgins", "Maule", "Bió-Bió","Araucanía", "Los lagos", "Aisén", "Magallanes"],
        index = None

    )
        #Al elegir la Region metropolitana se podra avanzar, con otra no
        if region == "Region metropolitana":
            
            #Para escribir texto en la pagina, un titulo y otro texto
            st.write("No puedes escapar")
            st.title("Inicio")
            st.write("Antes de comenzar con el verdadero test te realizaremos una preguntas de rutina, ten paciencia", name, ".")

            
            #Pregunta para el usuario con solo dos respuestas y una correcta
            dios = st.radio(
                "¿Crees en D̶̡̛̟̙̥̋̈ḯ̷̮͔̥̱̯̅̓̎̉͜͞o̷̢̳̬̗̜̰̓̓̓͠s҈̨̰̤̌̅͝?",
                ["Si", "No"],
                index = None
            #condicional que hace al usuario avanzar a la siguiente a la pregunta
            )
            #Pregunta para el usuario con solo dos respuestas y una correcta
            if dios == "Si" or dios == "No":
                #Pregunta para el usuario con solo dos respuestas y una correcta
                armas = st.radio(
                    "¿Tienes armas en tu casa?",
                    ["Si", "No"],
                    index = None
            
            )
                #condicional que hace al usuario avanzar a la siguiente a la pregunta
                if armas == "No" or armas == "Si":
                    #Pregunta para el usuario con solo dos respuestas y una correcta
                    melancolia = st.radio(
                "¿Vives solo?",
                ["No", "Si"],
                index = None
            
            )
                    #condicional que hace al usuario avanzar a la siguiente a la pregunta
                    if melancolia == "Si" or melancolia == "No":
                        #Pregunta para el usuario con solo dos respuestas y una correcta
                              o = st.radio(
                "¿̵̭̲҇̍͜?҈̨͇͍̤͒̓͞",
                ["?¿", "¿?"],
                index = None
            
            )
                              #condicional que hace al usuario avanzar a la siguiente a la pregunta ademas de comenzar a reproducir un audio en bucle
                              if o == "¿?" or o == "?¿":
                                  #Pregunta para el usuario con solo dos respuestas y una correcta
                                st.audio("1A.mp3", autoplay = True, loop = True)
                                #Pregunta para el usuario con solo dos respuestas y una correcta
                                vida = st.radio(
                "¿̴̨̳͎̥҇͐͒E҈̢̪̖͈̯҇̇̿͑̚s̴̨̗̳̤̣̦̾͆̄͝t̷̨̫̠͔͛̈́̿̈̐͡a̷̰͙͆̉̊̀̈͢͞s̴̯̪͗̃̕͢ v̴̡̭̥̩̠҇̃̂̽i̷̧̳̬̙̙̇͌̈́̌͠ṽ̵̢̞̙͗̕o҈̛̖̥͕̃̑͜?҉͔͙̣̃̐̓͢͡",
                ["No", "Si"],
                index = None
            
        )
                                #condicional que hace al usuario avanzar a la siguiente a la pregunta junto a una imagen y texto
                                if vida == "Si" or vida == "No":
                                    st.write("¡Has pasado el test inicial, felicidades por lograr llegar hasta aca, ahora comenzaremos con el test real!")
                                    st.image("1.png")                            
                                    st.divider()
                                    st.write("Comenzemos con algo facil, ¿cual es el alterno?")
                                    #Pregunta para el usuario con solo dos respuestas y una correcta
                                    Prueba1 = st.radio(
                                        "Decide",
                                        ["Imagen 1", "Imagen 2"],
                                        index = None
                                        )
                                    st.divider()
                                    #condicional que hace al usuario avanzar a la siguiente a la pregunta, junto a columnas, imegenes, textos y divisiones en la pagina
                                    if Prueba1 == "Imagen 2" or Prueba1 == "Imagen 1":
                                        col1, col2 = st.columns(2)
                                        col1.image("alt2.jpg")
                                        col2.image("22.jpeg")
                                        st.divider()
                                        st.write("¿Cual es la amenaza?")
                                        #Pregunta para el usuario con solo dos respuestas y una correcta
                                        Prueba2 = st.radio(
                                        "Selecciona",
                                        ["Imagen 1", "Imagen 2"],
                                        index = None
                                        )
                                        st.divider()
                                        #condicional que hace al usuario avanzar a la siguiente a la pregunta junto a columnas, imagenes y textos, aparte de una division
                                        if Prueba2 == "Imagen 1" or Prueba2 =="Imagen 2":
                                            col1, col2 = st.columns(2)
                                            col1.image("alt 3.png")
                                            col2.image("Muta.png")
                                            st.divider()
                                            st.write("¿Quien ha aparecido en tus sueños?")
                                            #Pregunta para el usuario con solo dos respuestas y una correcta
                                            Prueba3 = st.radio(
                                        "Haz tu elección",
                                        ["Imagen 1", "Imagen 2"],
                                        index = None
                                        )
                                            st.divider()
                                            #condicional que hace al usuario avanzar a la siguiente a la pregunta, junto a columnas, imegenes, textos y divisiones en la pagina
                                            if Prueba3 == "Imagen 1" or Prueba3 == "Imagen 2":
                                                
                                                col1, col2 = st.columns(2)
                                                col1.image("proto.png")
                                                col2.image("pc.png")
                                                st.divider()
                                                st.write("¿Quien ha irrumpido en tu casa?")
                                                #Pregunta para el usuario con solo dos respuestas y una correcta
                                                Prueba4 = st.radio(
                                        "....",
                                        ["Imagen 1", "Imagen 2"],
                                        index = None
                                        )
                                                st.divider()
                                               #condicional que hace al usuario avanzar a la siguiente a la pregunta, junto a columnas, imegenes, textos y divisiones en la pagina
                                                if Prueba4 == "Imagen 1" or Prueba4 == "Imagen 2":
                                                    col1,col2 = st.columns(2)
                                                    col1.image("negro.jpg")
                                                    col2.image("negro.jpg")
                                                    st.divider()
                                                    st.write("¿Quien es el culpable?")
                                                   #Pregunta para el usuario con solo dos respuestas y una correcta
                                                    Prueba5 = st.radio(
                                        "Admitelo",
                                        ["Yo", "..."],
                                        index = None
                                        )
                                                    #condicional que hace al usuario avanzar al final del test donde dependiendo de las opciones se muestre un mensaje u otro
                                                    if Prueba5 == "Yo" or Prueba5 =="...":
                                                        st.title("Haz terminado el test Non es Solus!, un poco más abajo podras saber tus resultados")
                                                        if dios == "Si" and armas == "Si" and melancolia == "No" and vida == "Si" and Prueba1 == "Imagen 2" and Prueba2 == "Imagen 1" and Prueba3 == "Imagen 2" and Prueba4 == "Imagen 1":
                                                            st.title("¡Estas totalmente preparado para sobrevivir, eres increible!")
                                                            st.write("Solo el 0,0000000000000000001 de la población Chilena ha pasado este test exitosamente, ¡eres más habil que un militar!, si quieres seguir explorando la pagina revisa nuestra función de calculo de grasa")
                                                            st.image("yepi.png")
                                                        else:
                                                            st.title("Muy mal, no serías capaz de identificar a un alterno!")
                                                            st.write("Es importante para tu seguridad que realizes el test nuevamente para responderlo correctamente y asi sobrevivir, no abras la puerta.")
      

        
        #linea encarga de mostrar un mensaje cuando el usuario ponga una opción distinta
        else:
            st.write("Aun estas a tiempo, contacta con tu institución gubernamental más cercana")
    #linea encargada de mostrar un mensaje cuando el valor no sea la requerida        
    else:
        st.write("Estas en peligro")
    

        
#linea que muestra un mensaje cuando el usuario ponga un nombre no permitido    
else:
    st.write("¿Por qué estas aqui", name,"?")