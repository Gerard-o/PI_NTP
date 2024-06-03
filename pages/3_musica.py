import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.header("Simulador Música")

# Cargar el conjunto de datos
df = pd.read_csv('static/datasets/musica.csv')

# Asignar nombres de columnas basados en los resultados proporcionados
artist_col = 'artists'.strip()  # Asegurarse de que no haya espacios en blanco alrededor del nombre
duration_col = 'duration_ms'.strip()  # Duración de las canciones

# Crear select box para el filtro del artista
unique_artists = df[artist_col].unique()
selected_artist = st.selectbox('Selecciona un artista', options=["Todos"] + list(unique_artists))

# Filtrar el DataFrame basado en la selección del artista
filtered_df = df.copy()
if selected_artist != "Todos":
    filtered_df = filtered_df[filtered_df[artist_col] == selected_artist]

# Mostrar los datos filtrados
st.write("Datos filtrados", filtered_df)

# Contar la frecuencia de cada artista
artist_counts = df[artist_col].value_counts()

# Obtener los top 40 artistas
top_artists = artist_counts.head(40)

# Crear un gráfico de barras para mostrar los top 40 artistas
plt.figure(figsize=(10, 8))
top_artists.plot(kind='bar')
plt.title('Top 40 Artistas')
plt.xlabel('Artistas')
plt.ylabel('Número de Canciones')
plt.xticks(rotation=90)
plt.tight_layout()

# Mostrar el gráfico en la aplicación Streamlit
st.pyplot(plt)

# Contar la frecuencia de duración de las canciones
duration_counts = df[duration_col].value_counts()

# Obtener las top 40 duraciones de canciones
top_durations = duration_counts.head(40)

# Crear un gráfico de barras para mostrar las top 40 duraciones de canciones
plt.figure(figsize=(10, 8))
top_durations.plot(kind='bar')
plt.title('Top 40 Duraciones de Canciones')
plt.xlabel('Duración (ms)')
plt.ylabel('Número de Canciones')
plt.tight_layout()

# Mostrar el gráfico en la aplicación Streamlit
st.pyplot(plt)