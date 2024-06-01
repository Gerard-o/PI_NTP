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

# La lista de listas
musica = [
    ["Hips Don't Lie", "Epic Records", "Shakira, Wyclef Jean, Jerry 'Wonder' Duplessis, Clive Davis", "Pop- Reguetón", "Barranquilla", 2006, "3:38"],
    ["Mi Gente", "Universal Music Latin", "DJ Snake, Willy William", "Reguetón", "Medellín", 2017, "3:16"],
    ["La Bicicleta", "Sony Music Latin", "Andrés Castro, Shakira", "Vallenato, Pop Latino", "Santa Marta", 2016, "3:47"],
    ["Felices los 4", "Sony Music Latin", "Rude Boyz (Kevin ADG y Chan El Genio)", "Reguetón, Pop Latino", "Medellín", 2017, "3:50"],
    ["Tusa", "Universal Music Latin", "Mauricio Rengifo, Andrés Torres", "Reguetón, Trap Latino", "Medellín", 2019, "3:20"],
    ["Traicionera", "Universal Music Latino", "Andrés Castro", "Reguetón, Pop Latino", "Medellín", 2016, "3:49"],
    ["De Donde Vengo Yo", "Sony Music Latin", "Ovy On The Drums", "Hip Hop, Afro-Colombiano", "Quibdó", 2016, "4:20"],
    ["Te Mando Flores", "EMI", "Fonseca, Bernardo Ossa", "Pop Latino, Vallenato", "Bogotá", 2006, "4:11"],
    ["Día tras Día", "La Industria Inc", "Andrés Cepeda y Freddy Camelo", "Pop Latino, Balada", "Bogotá", 2009, "4:16"],
    ["Una Lady Como Tú", "Universal Music Latino", "Julián Turizo y Sergio George", "Reguetón, Pop Latino", "Montería", 2016, "3:59"]
]

# Nombres de las columnas
columnas = ["Canción", "Discográfica", "Productor y mezcla", "Género", "Lugar de origen", "Año de publicación", "Duración"]

# Crear el DataFrame
df_musica = pd.DataFrame(musica, columns=columnas)

# Configurar la aplicación de Streamlit
st.title('Lista de Canciones')

# Mostrar el DataFrame en la aplicación
st.dataframe(df_musica)
