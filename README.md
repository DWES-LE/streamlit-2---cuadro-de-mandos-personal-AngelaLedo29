# 📈 Cuadro de mandos personal 📊
 
> Usa este repositorio para crear un cuadro de mandos personal con Streamlit. Documenta los siguientes apartados del README.
> Incluye en tu README la url de donde has publicado tu aplicación. Pon la `url` también en el `About` de tu repositorio.

## Objetivo
Diseño de un cuadro de mandos personal para visualización e interacción con un conjunto de datos.

## Los datos
Elige un conjunto de datos que te interese: educación, deportes, trabajo, música, econocomía, etc. 

## Búsqueda de los datos
Busca una fuente para tus datos. Puedes usar una API de un portal de datos abiertos, un conjunto ya publicado, recopilar personalmente datos por scraping, etc.

## Documentación de los datos
Documenta los datos que vas a usar y su origen. De dónde los has sacado, fuentes, etc. Describe los campos, los valores, las unidades, etc.

> Voy a usar los datos de peliculas que los he sacado de la web https://zenodo.org/record/5898454#.ZAjcW3bMLIV. Lo que he hecho es descargar el archivo csv y subirlo a mi repositorio. Los datos son de peliculas de la web IMDB. Los campos que tiene son: id, title, synopsis, critic_score, people_score, consensus, total_reviews, total_ratings, type, rating, genre, director. etc... Los valores y las unidades son numeros y texto.
La descripción de los campos son los datos que tiene cada pelicula.

## Prepara tu aplicación.
La aplicación se llamará `app.py`. Añade un `requirements.txt` con las dependencias de tu aplicación. Ve actualizándolo a medida que vayas añadiendo librerías.

## Carga y análisis de conjunto de dato con pandas
Carga el conjunto de datos en un dataframe de pandas y realiza un análisis exploratorio de los datos.

## Visualización de los datos
Prepara visualizaciones diferentes del dataframe en texto (tablas) o gráficas (histogramas, barras, etc.). Puedes usar matplotlib, seaborn, plotly, etc.

## Diseña la interacción que van a tener tus datos
Qué inputs y outputs tendrán tus datos. 

## Prepara la aplicación (cuadro de mandos) con Streamlit
Prepara y prueba la aplicación.

## Publica la aplicación.
Publica la aplicación en Streamlit Cloud, en Heroku o en el servicio que prefieras https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app
