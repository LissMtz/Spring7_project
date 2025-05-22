import streamlit as st
import pandas as pd
import plotly.express as px


car_data = pd.read_csv('vehicles_us.csv')


st.header('Anuncios de venta de coches')

hist_button = st.button('Construir histograma')  # crear un botón


if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig_1 = px.histogram(car_data,
                         x="odometer",
                         title="Anuncios de venta de coches",
                         color_discrete_sequence=["orange"])

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_1, use_container_width=True)

scat_button = st.button('Construir gráfico de dispersión')  # crear un botón


if scat_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un gráfico de dispersión
    fig_2 = px.scatter(car_data,
                       x="odometer", y="price",
                       title="Anuncios de venta de coches",
                       color_discrete_sequence=["green"])

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_2, use_container_width=True)
