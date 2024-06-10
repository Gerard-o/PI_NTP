import streamlit as st
import matplotlib.pyplot as plt

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://img.freepik.com/foto-gratis/fondo-musica-flat-lay-guitarra-acustica_169016-21058.jpg");
        background-size: cover;
    }
    .center {
        display: block;
        margin-left: auto;
        margin-right: auto;
        border-radius: 50%;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #fc5500;  
    }
    p, li .stMarkdown p  {
        color: #FFFFFF;  
        font-size: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título de la página y encabezado
st.title("Proyecto Integrador")
st.header("BomMusic")


st.image("imgproyecto12.png", width=600)

# Pie de página con los miembros del equipo e información del proyecto
st.subheader("Equipo y Contacto")
st.write("**Miembros del equipo:**")
st.write("- GERARDO DE JESUS IDARRAGA CIRO")
st.write("- FREDY ALBERTO POSADA YARCE")
st.write("- JUAN SEBASTIAN ROMERO ")

st.write("""Información de contacto:[Enlace Información de contacto](https://outlook.office365.com/mail/)""")

st.write("Correo electrónico: [Enlace al correo electrónico de contacto](https://outlook.office365.com/mail/)")
#----------------------------------------

st.subheader("Descripción del proyecto")
st.write('''
<p class="custom-text">
Nuestra plataforma BomMusic tiene como objetivo conectar a los amantes de la música 
con nuevos artistas, géneros y canciones. Proporcionamos una experiencia personalizada
donde los usuarios pueden explorar, escuchar y compartir música de manera fácil y divertida.
</p>
''', unsafe_allow_html=True)

st.subheader("Objetivos")
st.write('''
<p class="custom-text">
- <strong>Descubrimiento Personalizado:</strong> Utilizamos algoritmos de recomendación para ofrecer a los usuarios canciones y artistas basados en sus preferencias musicales. Cuanto más interactúan con la plataforma, más precisa se vuelve la recomendación.
</p>
<p class="custom-text">
- <strong>Promoción de Artistas Emergentes:</strong> Damos visibilidad a artistas independientes y emergentes. Nuestra plataforma ofrece un espacio para que los músicos compartan su trabajo y lleguen a nuevos oyentes.
</p>
<p class="custom-text">
- <strong>Comunidad Musical:</strong> Fomentamos la interacción entre los usuarios. Los usuarios pueden crear listas de reproducción, seguir a otros amantes de la música y comentar sobre canciones y álbumes.
</p>
''', unsafe_allow_html=True)

st.subheader("Impacto")
st.write('''
<p class="custom-text">
- <strong>Para los Usuarios:</strong> Proporcionamos una experiencia musical enriquecedora y diversa. Los usuarios pueden descubrir joyas ocultas, conectarse con otros amantes de la música y expandir sus horizontes musicales.
</p>
<p class="custom-text">
- <strong>Para los Artistas:</strong> Nuestra plataforma es una oportunidad para que los artistas emergentes lleguen a una audiencia más amplia. Pueden recibir comentarios directos de los oyentes y construir una base de seguidores leales.
</p>
<p class="custom-text">
- <strong>Para la Industria Musical:</strong> Contribuimos al crecimiento y la diversidad de la industria musical al promover una mayor exploración y apoyo a artistas independientes.
</p>
''', unsafe_allow_html=True)

# Resumen del Proyecto
st.subheader("Resumen del Proyecto")
st.write('''
<p class="custom-text">
- <strong>Punto 1:</strong> Proporcionar recomendaciones personalizadas basadas en las preferencias del usuario. Promover a artistas emergentes y darles visibilidad. Fomentar una comunidad musical activa.
</p>
<p class="custom-text">
- <strong>Punto 2:</strong> Para los Usuarios: Experiencia musical enriquecedora y descubrimiento de nuevas canciones. Para los Artistas: Oportunidad de llegar a una audiencia más amplia y recibir comentarios directos. Para la Industria Musical: Contribución al crecimiento y diversidad de la música.
</p>
<p class="custom-text">
- <strong>Punto 3:</strong> lenguaje de programación Python, la biblioteca Pandas, el sistema de control de versiones Git y la plataforma de alojamiento de código GitHub. Estas herramientas nos pemiten trabajar de forma eficiente en proyectos de análisis de datos, ya sea solo o en equipo. bases de datos para almacenar preferencias y algoritmos de recomendación. Este proyecto tiene el potencial de enriquecer la vida de los amantes de la música y apoyar a artistas emergentes.
</p>
''', unsafe_allow_html=True)

# Características y Beneficios
st.subheader("Características y Beneficios")
st.write('''
<p class="custom-text">
<strong>Característica 1: Biblioteca de Música Extensa</strong>
</p>
<p class="custom-text">
<strong>Descripción:</strong>
Una web musical con una biblioteca extensa ofrece una vasta colección de canciones, álbumes y géneros musicales. Esto puede incluir música de diferentes épocas, estilos y culturas, accesible para los usuarios en cualquier momento.
</p>
<p class="custom-text">
<strong>Beneficios:</strong>
</p>
<p class="custom-text">
- <strong>Variedad y Diversidad:</strong> Los usuarios pueden descubrir y explorar una amplia gama de música, ampliando sus gustos y conocimientos musicales.
</p>
<p class="custom-text">
- <strong>Conveniencia:</strong> Acceso instantáneo a una gran colección de música desde cualquier dispositivo con conexión a internet.
</p>
<p class="custom-text">
- <strong>Descubrimiento de Nuevos Artistas:</strong> Facilita el descubrimiento de nuevos artistas y géneros, promoviendo la diversidad musical.
</p>
<p class="custom-text">
<strong>Característica 2: Recomendaciones Personalizadas</strong>
</p>
<p class="custom-text">
<strong>Descripción:</strong>
Una característica de recomendaciones personalizadas utiliza algoritmos y datos del usuario (como historial de reproducción, preferencias y calificaciones) para sugerir música que probablemente le gustará.
</p>
<p class="custom-text">
<strong>Beneficios:</strong>
</p>
<p class="custom-text">
- <strong>Experiencia Personalizada:</strong> Los usuarios reciben sugerencias adaptadas a sus gustos individuales, mejorando su experiencia de escucha.
</p>
<p class="custom-text">
- <strong>Ahorro de Tiempo:</strong> Reduce el tiempo que los usuarios pasan buscando nueva música, presentándoles opciones que se alinean con sus preferencias.
</p>
<p class="custom-text">
- <strong>Mayor Satisfacción:</strong> Aumenta la satisfacción del usuario al descubrir música que realmente disfruta y que de otra manera podría no haber encontrado.
</p>
<p class="custom-text">
<strong>Característica 3: Interacción y Comunidad</strong>
</p>
<p class="custom-text">
<strong>Descripción:</strong>
La integración de funciones de interacción y comunidad permite a los usuarios conectarse, compartir y discutir música. Esto puede incluir foros, grupos de discusión, comentarios, y la posibilidad de crear y compartir listas de reproducción.
</p>
<p class="custom-text">
<strong>Beneficios:</strong>
</p>
<p class="custom-text">
- <strong>Conexión Social:</strong> Fomenta la interacción social y la creación de comunidades en torno a intereses musicales compartidos.
</p>
<p class="custom-text">
- <strong>Intercambio de Conocimientos:</strong> Los usuarios pueden compartir conocimientos, recomendaciones y opiniones, enriqueciendo la experiencia musical de todos.
</p>
<p class="custom-text">
- <strong>Compromiso y Fidelización:</strong> Las características de comunidad aumentan el Compromiso y la lealtad de los usuarios, ya que se sienten parte de una sociedad centrada en la música.
</p>
''', unsafe_allow_html=True)
# Gráfico interactivo o visualización (Opcional)
# Reemplaza con tus datos y visualización específicos

# Datos de ejemplo de los géneros musicales más escuchados en todo el mundo
data = [30, 25, 20, 15, 10]
labels = ["Pop", "Hip-Hop", "Rock", "EDM", "Reggaetón"]

# Crear la figura y el eje
fig, ax = plt.subplots()

# Dibujar el gráfico de barras
ax.bar(labels, data, color=["#ff9999","#66b3ff","#99ff99","#ffcc99","#c2c2f0"])

# Añadir títulos y etiquetas
ax.set_title("Géneros Musicales Más Escuchados en Todo el Mundo")
ax.set_xlabel("Géneros Musicales")
ax.set_ylabel("Porcentaje de Audiencia (%)")

# Mostrar el gráfico
plt.show()
# Quitar el fondo
fig.patch.set_facecolor('none')
ax.patch.set_facecolor('none')
st.pyplot(fig)

# Llamado a la acción
st.subheader("¡Toma Acción!")
st.write("**Visite nuestro sitio web:** [Enlace al sitio web del proyecto](https://g7qyxwvy2fxpgtigncgkmf.streamlit.app/)")
st.write("**Contáctenos:** [Enlace al correo electrónico de contacto](https://outlook.office365.com/mail/)")

