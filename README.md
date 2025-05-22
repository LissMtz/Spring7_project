# Spring7_project
Proyecto Spring 7 Tripleten (Data Scientist)


# Análisis de Anuncios de Vehículos Usados
Este proyecto es una aplicación en Python que permite visualizar de forma interactiva información del conjunto de datos `vehicles_us.csv`.


## Descripción

La aplicación permite al usuario seleccionar entre diferentes tipos de gráficos para analizar los datos:

- Histograma: muestra la distribución del kilometraje (`odometer`) de los vehículos.
- Gráfico de dispersión: visualiza la relación entre el kilometraje y el precio (`odometer` vs `price`).

El usuario puede marcar una casilla para seleccionar qué gráfico desea visualizar.

## Funcionalidad

- Interfaz interactiva.
- Visualización de datos directamente desde el archivo `vehicles_us.csv`.
- Gráficos generados con Plotly Express.
- Permite comparar visualmente diferentes aspectos del dataset de manera sencilla.

## Paquetes utilizados
- Pandas
- Plotly Express
- Streamlit