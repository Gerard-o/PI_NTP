import streamlit as st
import pandas as pd

# Agrega un encabezado en la aplicación web
st.header("Proyecto Integrador")

# Crea un diccionario con información sobre personas
datos = {"Nombre": ["Ana", "Juan", "Pedro"],
         "Edad": [25, 30, 35],
         "Ciudad": ["Madrid", "Barcelona", "Sevilla"]}

# Convierte el diccionario a un DataFrame
df_datos = pd.DataFrame(datos)

# Muestra el DataFrame como una tabla en la aplicación web
st.table(df_datos)

# Muestra un gráfico de barras usando el DataFrame, configurando 'Nombre' como el índice
st.bar_chart(df_datos.set_index('Nombre'))

# Crea otro diccionario con información sobre diferentes tipos de animales y sus cantidades
data = {
    'Tipo': ['Perro', 'Gato', 'Pájaro', 'Conejo', 'Hamster'],
    'Cantidad': [50, 30, 20, 10, 5]
}

# Convierte el diccionario a un DataFrame
df = pd.DataFrame(data)

# Muestra el DataFrame en la aplicación web
st.write(df)

# Muestra un gráfico de barras usando el DataFrame, configurando 'Tipo' como el índice
st.bar_chart(df.set_index('Tipo'))

#musica=[["Canción","Hips Don't Lie","Mi Gente","La Bicicleta","Felices los 4","Tusa","Traicionera","De Donde Vengo Yo","Te Mando Flores","Día tras Día","Una Lady Como Tú"],
 #        ["Discográfica","Epic Records","Universal Music Latin","Sony Music Latin","Sony Music Latin","Universal Music Latin","Universal Music Latino","Sony Music Latin","EMI","La Industria Inc"],
  #       ["Productor y mezcla","Shakira, Wyclef Jean, Jerry 'Wonder' Duplessis, Clive Davis"," DJ Snake, Willy William","Andrés Castro, Shakira","Rude Boyz (Kevin ADG y Chan El Genio)","Mauricio Rengifo, Andrés Torres","Andrés Castro","Ovy On The Drums","Fonseca, Bernardo Ossa","Andrés Cepeda y Freddy Camelo","Julián Turizo y Sergio George"],
   #      ["Género","Pop- Reguetón","Reguetón","Vallenato, Pop Latino","Reguetón, Pop Latino","Reguetón, Trap Latino","Reguetón, Pop Latino","Hip Hop, Afro-Colombiano","Pop Latino, Vallenato"," Pop Latino, Balada","Reguetón, Pop Latino"],
    #     ["Lugar de origen","Barranquilla","Medellín","Santa Marta","Medellín","Medellín","Medellín","Quibdó","Bogotá","Bogotá","Montería"],
     #    ["Año de  publicación",[2006,2017,2016,2017,2019,2016,2016,2016,2009,2006]],
      #  ["Duración", ["3:38", "3:16", "3:47", "3:50", "3:20", "3:49", "4:20", "4:11", "4:16", "3:59"]]
#]
#df_musica=pd.DataFrame(musica)

#st.write(df_musica)



