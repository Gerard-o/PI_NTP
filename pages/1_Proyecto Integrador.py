import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.header("BomMusic")

df = pd.read_csv('static/datasets/musica.csv')

artist_col = 'artists'.strip()
duration_col = 'duration_ms'.strip()
valence_col = 'valencia'.strip()
release_year_col = 'release_year'.strip()
plays_col = 'plays'.strip()
popularity_col = 'popularity'.strip()  

np.random.seed(42)
genres = ['Pop', 'Rock', 'Hip-Hop', 'Jazz', 'Classical']
if 'genre' not in df.columns:
    df['genre'] = np.random.choice(genres, size=len(df))

if valence_col not in df.columns:
    df[valence_col] = np.random.uniform(0, 1, size=len(df))

cities = ['New York', 'Los Angeles', 'London', 'Tokyo', 'Paris']
if 'city' not in df.columns:
    df['city'] = np.random.choice(cities, size=len(df))

if release_year_col not in df.columns:
    df[release_year_col] = np.random.randint(1950, 2023, size=len(df))

if plays_col not in df.columns:
    df[plays_col] = np.random.randint(1000, 1000000, size=len(df))  

unique_genres = df['genre'].unique()
selected_genre = st.selectbox('Selecciona un género musical', options=["Todos"] + list(unique_genres), key='genre_selectbox')

unique_cities = df['city'].unique()[:5]
selected_city = st.selectbox('Selecciona una ciudad', options=["Todos"] + list(unique_cities), key='city_selectbox')

filtered_popularity_df = df.copy()
if selected_genre != "Todos":
    filtered_popularity_df = filtered_popularity_df[filtered_popularity_df['genre'] == selected_genre]
if selected_city != "Todos":
    filtered_popularity_df = filtered_popularity_df[filtered_popularity_df['city'] == selected_city]

st.subheader("Artistas por Popularidad")
top_popularity_artists = filtered_popularity_df.groupby(artist_col)[popularity_col].sum().sort_values(ascending=False).head(40)

if not top_popularity_artists.empty:
    plt.figure(figsize=(10, 8), facecolor='orange')
    colors = plt.cm.viridis(np.linspace(0, 1, len(top_popularity_artists)))
    top_popularity_artists.plot(kind='bar', color=colors)
    plt.title('Artistas por Popularidad', fontsize=16, color='blue')
    plt.xlabel('Artistas', fontsize=12, color='green')
    plt.ylabel('Popularidad', fontsize=12, color='green')
    plt.xticks(rotation=90, fontsize=10, color='purple')
    plt.yticks(color='purple')
    plt.tight_layout()
    st.pyplot(plt)

selected_duration_artist = st.selectbox('Selecciona un artista para el gráfico de duraciones', options=["Todos"] + list(df[artist_col].unique()), key='duration_artist_selectbox')

filtered_duration_df = df.copy()
if selected_duration_artist != "Todos":
    filtered_duration_df = filtered_duration_df[filtered_duration_df[artist_col] == selected_duration_artist]
if selected_genre != "Todos":
    filtered_duration_df = filtered_duration_df[filtered_duration_df['genre'] == selected_genre]
if selected_city != "Todos":
    filtered_duration_df = filtered_duration_df[filtered_duration_df['city'] == selected_city]

num_songs_to_show = st.slider('Selecciona el número de canciones más largas a mostrar:', 1, 40, 10, key='num_songs_slider')

st.subheader("Duraciones de Canciones")
top_durations = filtered_duration_df.nlargest(num_songs_to_show, duration_col)

if not top_durations.empty:
    top_durations[artist_col] = top_durations[artist_col].apply(lambda x: x if len(x) <= 10 else x[:7] + '...')
    plt.figure(figsize=(10, 8), facecolor='lightblue')
    plt.scatter(top_durations[artist_col], top_durations[duration_col], c='blue', alpha=0.5)
    plt.title(f'Top {num_songs_to_show} Duraciones de Canciones', fontsize=16, color='blue')
    plt.xlabel('Artistas', fontsize=12, color='green')
    plt.ylabel('Duración (ms)', fontsize=12, color='green')
    plt.xticks(rotation=90, fontsize=10, color='purple')
    plt.yticks(color='purple')
    plt.tight_layout()
    st.pyplot(plt)

min_year = df[release_year_col].min()
max_year = df[release_year_col].max()
selected_release_year = st.slider('Selecciona un año de lanzamiento:', min_year, max_year, (min_year, max_year), key='release_year_slider')

filtered_release_year_df = df.copy()
filtered_release_year_df = filtered_release_year_df[(filtered_release_year_df[release_year_col] >= selected_release_year[0]) & (filtered_release_year_df[release_year_col] <= selected_release_year[1])]

st.subheader(f"Top 40 Artistas de {selected_release_year[0]}-{selected_release_year[1]}")
release_year_artist_counts = filtered_release_year_df[artist_col].value_counts()
top_release_year_artists = release_year_artist_counts.head(40)

if not top_release_year_artists.empty:
    plt.figure(figsize=(10, 8), facecolor='lightgreen')
    sizes = np.arange(1, len(top_release_year_artists) + 1) * 10
    colors = plt.cm.viridis(np.linspace(0, 1, len(top_release_year_artists)))
    plt.scatter(top_release_year_artists.index, top_release_year_artists.values, s=sizes, c=colors, alpha=0.5)
    plt.title(f'Top 40 Artistas de {selected_release_year[0]}-{selected_release_year[1]}', fontsize=16, color='blue')
    plt.xlabel('Artistas', fontsize=12, color='green')
    plt.ylabel('Número de Canciones', fontsize=12, color='green')
    plt.xticks(rotation=90, fontsize=10, color='purple')
    plt.yticks(color='purple')
    plt.tight_layout()
    st.pyplot(plt)

st.subheader("Género Musical más Escuchado por Ciudad")
selected_country = st.selectbox('Selecciona una ciudad', options=["Todos"] + list(unique_cities), key='genre_city_selectbox')

filtered_country_df = df.copy()
if selected_country != "Todos":
    filtered_country_df = filtered_country_df[filtered_country_df['city'] == selected_country]

genre_counts = filtered_country_df['genre'].value_counts()

if not genre_counts.empty:
    plt.figure(figsize=(10, 8), facecolor='lightyellow')
    genre_counts.plot(kind='bar', color=plt.cm.viridis(np.linspace(0, 1, len(genre_counts))))
    plt.title(f'Género Musical más Escuchado en {selected_country}', fontsize=16, color='blue')
    plt.xlabel('Género Musical', fontsize=12, color='green')
    plt.ylabel('Número de Canciones', fontsize=12, color='green')
    plt.xticks(rotation=45, fontsize=10, color='purple')
    plt.yticks(color='purple')
    plt.tight_layout()
    st.pyplot(plt)

st.subheader("Número de Reproducciones en un Año Determinado")
selected_year = st.slider('Selecciona un año', min_year, max_year, min_year, key='plays_year_slider')

filtered_year_df = df[df[release_year_col] == selected_year]
plays_counts = filtered_year_df.groupby(artist_col)[plays_col].sum().sort_values(ascending=False).head(40)

if not plays_counts.empty:
    plt.figure(figsize=(10, 8), facecolor='lightpink')
    plays_counts.plot(kind='bar', color=plt.cm.plasma(np.linspace(0, 1, len(plays_counts))))
    plt.title(f'Artistas por Número de Reproducciones en {selected_year}', fontsize=16, color='blue')
    plt.xlabel('Artistas', fontsize=12, color='green')
    plt.ylabel('Número de Reproducciones', fontsize=12, color='green')
    plt.xticks(rotation=90, fontsize=10, color='purple')
    plt.yticks(color='purple')
    plt.tight_layout()
    st.pyplot(plt)
