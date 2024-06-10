import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="wide")

st.title("Simulador Cesde")

df = pd.read_csv('static/datasets/cesde.csv')

gruposU = sorted(df['GRUPO'].unique())
momentosU = sorted(df['MOMENTO'].unique())

# -----------------------------------------------------------------------------------

def filtro1():
    st.header("Notas por Grupo y Momento")
    col1, col2 = st.columns(2)
    with col1:
        grupo = st.selectbox("Grupo", gruposU)
    with col2:
        momento = st.selectbox("Momento", momentosU)
    resultado = df[(df['GRUPO'] == grupo) & (df['MOMENTO'] == momento)]
    mostrar_resultados(resultado)

def filtro_notas_mas_bajas():
    st.header("Notas Más Bajas por Estudiante")
    notas_mas_bajas = df.loc[df[['CONOCIMIENTO', 'DESEMPEÑO', 'PRODUCTO']].idxmin(axis=0)]
    mostrar_resultados(notas_mas_bajas)

def filtro_docentes_varias_materias():
    st.header("Docentes que Imparten Varias Materias")
    materias_por_docente = df.groupby('DOCENTE')['SUBMODULO'].nunique()
    docentes_varias_materias = materias_por_docente[materias_por_docente > 1]
    
    if not docentes_varias_materias.empty:
        fig = go.Figure(go.Bar(x=docentes_varias_materias.index, y=docentes_varias_materias.values))
        fig.update_layout(
            xaxis_title='Docente',
            yaxis_title='Cantidad de Materias',
            title='Docentes que Imparten Varias Materias'
        )
        st.plotly_chart(fig, use_container_width=True)
        st.table(docentes_varias_materias.reset_index().rename(columns={'index': 'Docente', 'SUBMODULO': 'Cantidad de Materias'}))
    else:
        st.write("No hay docentes que impartan varias materias.")

def filtro_horario():
    st.header("Gráfico de Horarios")
    horario_conteo = df['HORARIO'].value_counts()
    mostrar_grafico(horario_conteo, 'Horario', 'Conteo')

def filtro_jornada():
    st.header("Gráfico de Pareto de Jornadas")
    jornada_conteo = df['JORNADA'].value_counts().sort_values(ascending=False)
    mostrar_grafico(jornada_conteo, 'Jornada', 'Conteo')

# -----------------------------------------------------------------------------------

def mostrar_grafico(data, x_label, y_label):
    fig = go.Figure(data=[go.Scatter(x=data.index, y=data.values, mode='lines+markers')])
    fig.update_layout(xaxis_title=x_label, yaxis_title=y_label, margin=dict(l=0, r=0, b=0, t=0))
    st.plotly_chart(fig, use_container_width=True)
    st.table(data.reset_index().rename(columns={'index': x_label, data.name: y_label}))

def mostrar_resultados(data):
    fig = go.Figure(data=[
        go.Line(name='CONOCIMIENTO', x=data['NOMBRE'], y=data['CONOCIMIENTO']),
        go.Line(name='DESEMPEÑO', x=data['NOMBRE'], y=data['DESEMPEÑO']),
        go.Line(name='PRODUCTO', x=data['NOMBRE'], y=data['PRODUCTO'])
    ])
    st.plotly_chart(fig, use_container_width=True)
    st.table(data[["NOMBRE", "CONOCIMIENTO", "DESEMPEÑO", "PRODUCTO"]])

# -----------------------------------------------------------------------------------

filtros = {
    "Notas por Grupo y Momento": filtro1,
    "Notas Más Bajas por Estudiante": filtro_notas_mas_bajas,
    "Docentes que Imparten Varias Materias": filtro_docentes_varias_materias,
    "Gráfico de Horarios": filtro_horario,
    "Gráfico de Pareto de Jornadas": filtro_jornada
}

filtro_seleccionado = st.selectbox("Filtros", list(filtros.keys()))
if filtro_seleccionado:
    filtros[filtro_seleccionado]()
