import streamlit as st
import pandas as pd

# Agrega un encabezado en la aplicación web
st.markdown("<h1 style='text-align: center;'>Informacion</h1>", unsafe_allow_html=True)


# Crea un diccionario con información sobre personas
datos = {"Nombre": ["Ana", "Juan", "Pedro"],
         "Edad": [25, 30, 35],
         "Ciudad": ["Madrid", "Barcelona", "Sevilla"]}

# Convierte el diccionario a un DataFrame
df_datos = pd.DataFrame(datos)

# Muestra el DataFrame como una tabla en la aplicación web
st.table(df_datos)

st.markdown("<h1 style='text-align: center;'>Gráfico</h1>", unsafe_allow_html=True)
# Muestra un gráfico de barras usando el DataFrame, configurando 'Nombre' como el índice
st.bar_chart(df_datos.set_index('Nombre'))
st.markdown("<h1 style='text-align: center;'>Cantidad de animales</h1>", unsafe_allow_html=True)

# Crea otro diccionario con información sobre diferentes tipos de animales y sus cantidades
animales = {"Tipo": ['Perro', 'Gato', 'Pájaro', 'Conejo', 'Hamster'],
        "Cantidad": [50, 30, 20, 10, 5],
        "Dieta": ["Omnívoro ","Carnívoro ","Granívoros","Herbívoro ","Omnívoro "]}
# Convierte el diccionario a un DataFrame
df = pd.DataFrame(animales)

# Muestra el DataFrame en la aplicación web
st.table(df)

st.markdown("<h1 style='text-align: center;'>Gráfico</h1>", unsafe_allow_html=True)
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
st.markdown("<h1 style='text-align: center;'>listas de Canciones</h1>", unsafe_allow_html=True)

# Mostrar el DataFrame en la aplicación
st.dataframe(df_musica)

# Convertir la columna 'Año de publicación' a string para que sea categórica en el gráfico de barras
df_musica['Año de publicación'] = df_musica['Año de publicación'].astype(str)


st.markdown("<h1 style='text-align: center;'>Gráfico</h1>", unsafe_allow_html=True)
# Opción alternativa: gráfico de barras agrupando por año de publicación y género
st.bar_chart(df_musica.groupby(['Año de publicación', 'Género']).size().unstack().fillna(0))