import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
st.header('sprint7')
hist_button = st.checkbox('Construir histograma') # crear un boton
        
if hist_button: # al hacer clic en el boton
    # escribir un mensaje
    st.write('Creacion de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    
    # mostrar un grafico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
  
if st.checkbox('Construir grafico de dispersion'):
    st.write('Dispersion de odometro vs. precio')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)