
import streamlit as st
import matplotlib.pyplot as plt

# Set the page title and header
st.title("Proyecto Integrador")
st.header("BomMusic")

# Hero Section with image and project description
st.image("imgproyecto12.png", width=600)
st.subheader("Descripción del proyecto ")
st.write('''Nuestra plataforma BomMusic tiene como objetivo 
         conectar a los amantes de la música con nuevos artistas, géneros 
         y canciones. Proporcionamos una experiencia personalizada
        donde los usuarios pueden explorar, escuchar y compartir música 
         de manera fácil y divertida''')
st.subheader("Objetivos:")
st.write("- Descubrimiento Personalizado:Utilizamos algoritmos de recomendación para ofrecer a los usuarios canciones y artistas basados en sus preferencias musicales. Cuanto más interactúan con la plataforma, más precisa se vuelve la recomendación.")
st.write("- Promoción de Artistas Emergentes: Damos visibilidad a artistas independientes y emergentes. Nuestra plataforma ofrece un espacio para que los músicos compartan su trabajo y lleguen a nuevos oyentes.")
st.write("- Comunidad Musical: Fomentamos la interacción entre los usuarios. Los usuarios pueden crear listas de reproducción, seguir a otros amantes de la música y comentar sobre canciones y álbumes.")
st.subheader("Impacto:")
st.write("- Para los Usuarios: Proporcionamos una experiencia musical enriquecedora y diversa. Los usuarios pueden descubrir joyas ocultas, conectarse con otros amantes de la música y expandir sus horizontes musicales.")
st.write("- Para los Artistas: Nuestra plataforma es una oportunidad para que los artistas emergentes lleguen a una audiencia más amplia. Pueden recibir comentarios directos de los oyentes y construir una base de seguidores leales.")
st.write("- Para la Industria Musical: Contribuimos al crecimiento y la diversidad de la industria musical al promover una mayor exploración y apoyo a artistas independientes.")
st.subheader("")
# Project Overview
st.subheader("Resumen del Proyecto")
st.write("- Punto 1: Descripción detallada del punto 1 del proyecto.")
st.write("- Punto 2: Descripción detallada del punto 2 del proyecto.")
st.write("- Punto 3: Descripción detallada del punto 3 del proyecto.")

# Features and Benefits
st.subheader("Características y Beneficios")
st.write("**Característica 1:** Descripción de la característica 1 y sus beneficios.")
st.write("**Característica 2:** Descripción de la característica 2 y sus beneficios.")
st.write("**Característica 3:** Descripción de la característica 3 y sus beneficios.")

# Interactive Chart or Visualization (Optional)
# Replace with your specific data and visualization
data = [10, 20, 30, 40, 50]
labels = ["Categoría A", "Categoría B", "Categoría C", "Categoría D", "Categoría E"]
fig, ax = plt.subplots()
ax.pie(data, labels=labels, autopct="%1.1f%%")
st.pyplot(fig)

# Call to Action
st.subheader("¡Toma Acción!")
st.write("**Visite nuestro sitio web:** [Enlace al sitio web del proyecto](https://example.com)")
st.write("**Contáctenos:** [Enlace al correo electrónico de contacto](mailto:info@example.com)")

# Footer with team members and project information
st.subheader("Equipo y Contacto")
st.write("**Miembros del equipo:**")
st.write("- Nombre 1: Cargo en el equipo.")
st.write("- Nombre 2: Cargo en el equipo.")
st.write("- Nombre 3: Cargo en el equipo.")
st.write("**Información de contacto:**")
st.write("Correo electrónico: [Enlace al correo electrónico de contacto](mailto:info@example.com)")