import streamlit as st
from PIL import Image
import src.manage_data as dat
import plotly.express as px
import pandas as pd
import folium
from streamlit_folium import folium_static
import codecs
import streamlit.components.v1 as components
import seaborn as sns


def app():

    data = dat.carga_data()

    #--------------------------------------
    # Fuel type
    #--------------------------------------

    st.title("""Consume by Fuel type""")

    fuel =  dat.ft_value(st.selectbox("""
    What kind of fuel type do you want to check?
    """, dat.ft_keys()))

    if fuel == 1:
        dfuel = data[data["gas_type"] == "E10"]
        fig = px.histogram(dfuel, x="consume", title = "Consume by fuel type = E10", color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig)

    if fuel == 2:
        dfuel = data[data["gas_type"] == "SP98"]
        fig = px.histogram(dfuel,x="consume", title = "Consume by fuel type = SP98", color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig)

    if fuel == 3:
        
        fig = px.histogram(data, x="consume", title = "Consume by fuel type = SP98", color="gas_type", barmode="group")
        st.plotly_chart(fig)

    #--------------------------------------
    # Price by distance
    #--------------------------------------

    st.title("""Consume by speed""")

    ##To Do cambiar grafico para que muestre la distancia/precio por tipo de combustible

    fuel2 =  dat.ft_value(st.selectbox("""
    What kind of fuel do you want to check?
    """, dat.ft_keys()))

    if fuel2 == 1:
        dfuel = data[data["gas_type"] == "E10"]
        fig = px.scatter(dfuel, x="consume", y="speed", title = "Consume by fuel type = E10", color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig)

    if fuel2 == 2:
        dfuel = data[data["gas_type"] == "SP98"]
        fig = px.scatter(dfuel,x="consume", y="speed", title = "Consume by fuel type = SP98", color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig)

    if fuel2 == 3:
        
        fig = px.scatter(data, x="consume", y="speed", title = "Consume by fuel type = SP98", color="gas_type")
        st.plotly_chart(fig)







