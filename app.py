import pandas as pd
import streamlit as st
import numpy as np

# Load data
st.title('Peliculas Data Analysis')
URL = 'peliculas.csv'
# st.write(f'Dataset: ', URL)

def load_data():
    data = pd.read_csv(URL, sep=',', encoding='latin1', error_bad_lines=False)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text('Loading data... done!')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

# Nombre de peliculas, sinopsis y duracion
st.subheader('Nombre de peliculas, sinopsis y duracion (tabla)')
st.write(data[['title', 'synopsis', 'runtime']])

# Número de peliculas por año formato tabla
st.subheader('Número de peliculas por genero (tabla)')
genre_count = data['genre'].value_counts().reset_index()
genre_count.columns = ['genre', 'count']
st.write(genre_count)

# Número de peliculas por año formato grafico de area
st.subheader('Número de películas por año (gráfico de área)')
year_count = data['year'].value_counts()
st.area_chart(year_count)

# Top 10 de directores formato grafico de barras
st.subheader('Top 10 de directores (gráfico de barras)')
director_count = data['director'].value_counts().nlargest(10)
st.bar_chart(director_count)

# Número de rating de peliculas formato tabla
st.subheader('Número de rating de peliculas (tabla)')
rating_count = data['rating'].value_counts()
st.write(rating_count)

# Número de puntaje de criticas formato grafico de area
st.subheader('Número de puntaje de criticas (gráfico de area)')
criticscore_count = data['critic_score'].value_counts()
st.area_chart(criticscore_count)

# Número de total de votos formato grafico de barras
st.subheader('Número de total de votos (gráfico de barras)')
totalvotes_count = data['total_reviews'].value_counts()
st.bar_chart(totalvotes_count)

# Número total de tipo de peliculas formato grafico de barras
st.subheader('Número total de tipo de peliculas (gráfico de barras)')
totalvotes_count = data['type'].value_counts()
st.bar_chart(totalvotes_count)