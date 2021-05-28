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

    st.title("""Consume by Fuel type""")

    fuel =  dat.ft_value(st.selectbox("""
    What kind of energy certificate do you have?
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






