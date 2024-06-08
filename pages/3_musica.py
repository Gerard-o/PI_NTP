import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.header("Simulador Música")

df = pd.read_csv('static/datasets/musica.csv')

artist_col = 'artists'.strip()
duration_col = 'duration_ms'.strip()
valence_col = 'valencia'.strip()

np.random.seed(42)  
genders = ['female', 'male', 'non-binary']
if 'gender' not in df.columns:
    df['gender'] = np.random.choice(genders, size=len(df))

if valence_col not in df.columns:
    df[valence_col] = np.random.uniform(0, 1, size=len(df))

cities = ['New York', 'Los Angeles', 'London', 'Tokyo', 'Paris']
if 'city' not in df.columns:
    df['city'] = np.random.choice(cities, size=len(df))

unique_artists = df[artist_col].unique()
selected_artist = st.selectbox('Selecciona un artista para el gráfico de artistas', options=["Todos"] + list(unique_artists))

unique_genders = df['gender'].unique()
selected_gender = st.selectbox('Selecciona un género', options=["Todos"] + list(unique_genders))

unique_cities = df['city'].unique()[:5]  # Obtener las primeras 5 ciudades únicas
selected_city = st.selectbox('Selecciona una ciudad', options=["Todos"] + list(unique_cities))

filtered_artist_df = df.copy()
if selected_artist != "Todos":
    filtered_artist_df = filtered_artist_df[filtered_artist_df[artist_col] == selected_artist]
if selected_gender != "Todos":
    filtered_artist_df = filtered_artist_df[filtered_artist_df['gender'] == selected_gender]
if selected_city != "Todos":
    filtered_artist_df = filtered_artist_df[filtered_artist_df['city'] == selected_city]

st.subheader("Top 40 Artistas")
artist_counts = filtered_artist_df[artist_col].value_counts()
top_artists = artist_counts.head(40)

plt.figure(figsize=(10, 8), facecolor='orange')

colors = plt.cm.tab10(np.arange(len(top_artists)))
top_artists.plot(kind='bar', color=colors)
plt.title('Top 40 Artistas')
plt.xlabel('Artistas')
plt.ylabel('Número de Canciones')
plt.xticks(rotation=90)
plt.tight_layout()
st.pyplot(plt)

selected_duration_artist = st.selectbox('Selecciona un artista para el gráfico de duraciones', options=["Todos"] + list(unique_artists))

filtered_duration_df = df.copy()
if selected_duration_artist != "Todos":
    filtered_duration_df = filtered_duration_df[filtered_duration_df[artist_col] == selected_duration_artist]
if selected_gender != "Todos":
    filtered_duration_df = filtered_duration_df[filtered_duration_df['gender'] == selected_gender]
if selected_city != "Todos":
    filtered_duration_df = filtered_duration_df[filtered_duration_df['city'] == selected_city]

st.subheader("Top 40 Duraciones de Canciones")
duration_counts = filtered_duration_df[duration_col].value_counts()
top_durations = duration_counts.head(40)

plt.figure(figsize=(10, 8), facecolor='orange')

colors = plt.cm.tab10(np.arange(len(top_durations)))
top_durations.plot(kind='bar', color=colors)
plt.title('Top 40 Duraciones de Canciones')
plt.xlabel('Duración (ms)')
plt.ylabel('Número de Canciones')
plt.tight_layout()
st.pyplot(plt)

female_artists_df = df[df['gender'] == 'female']
selected_female_city = st.selectbox('Selecciona una ciudad para las artistas femeninas', options=["Todos"] + list(unique_cities))
if selected_female_city != "Todos":
    female_artists_df = female_artists_df[female_artists_df['city'] == selected_female_city]

st.subheader("Top 40 Mujeres Artistas")
female_artist_counts = female_artists_df[artist_col].value_counts()
top_female_artists = female_artist_counts.head(40)

plt.figure(figsize=(10, 8), facecolor='orange')

colors = plt.cm.tab10(np.arange(len(top_female_artists)))
top_female_artists.plot(kind='bar', color=colors)
plt.title('Top 40 Mujeres Artistas')
plt.xlabel('Artistas')
plt.ylabel('Número de Canciones')
plt.xticks(rotation=90)
plt.tight_layout()
st.pyplot(plt)

st.subheader("Filtro ciudad de Valencia")
unique_valences = df[valence_col].unique()
selected_valence = st.selectbox('Selecciona un valor de valencia', options=["Todos"] + list(unique_valences))

filtered_valence_df = df.copy()
if selected_valence != "Todos":
    filtered_valence_df = filtered_valence_df[filtered_valence_df[valence_col] == selected_valence]

st.subheader("Top 40 Artistas de Valencia")
valence_artist_counts = filtered_valence_df[artist_col].value_counts()
top_valence_artists = valence_artist_counts.head(40)

plt.figure(figsize=(10, 8), facecolor='orange')

colors = plt.cm.tab10(np.arange(len(top_valence_artists)))
top_valence_artists.plot(kind='bar', color=colors)
plt.title('Top 40 Artistas de Valencia')
plt.xlabel('Artistas')
plt.ylabel('Número de Canciones')
plt.xticks(rotation=90)
plt.tight_layout()
st.pyplot(plt)