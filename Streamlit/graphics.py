import streamlit as st
from PIL import Image
import src.manage_data as dat
import plotly.express as px
import pandas as pd
import folium
from streamlit_folium import folium_static
import codecs
import streamlit.components.v1 as components


def app():

    data = dat.carga_data()

    #--------------------------------------
    # Price/m2

    st.title("""Price per m2 depending on the district.""")

    distr = st.selectbox("""
    Choose a district.
    """, dat.lista_barrios())

    datagraf = dat.grafico(distr)

    fig = px.bar(datagraf,x="sq_mt_built", y="buy_price", title = f"Price / m2 ratio in the district: {distr}")
    st.plotly_chart(fig)


    #--------------------------------------
    # Valores medios

    st.title("""Average values of the different variables according to district.""")

    medio = data.groupby("distr").mean()

    variable = dat.col_value(st.selectbox("""
    Which average value do you want to check?
    """, dat.col_keys()))

    fig = px.bar(medio, y=f"{variable}", title = "Average values for each district.", color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig)

    #--------------------------------------
    # Max values

    st.title("""Max values of the different variables according to district.""")

    max = data.groupby("distr").max()

    variable1 = dat.col_value(st.selectbox("""
    Which max value do you want to check?
    """, dat.col_keys()))

    fig = px.bar(max, y=f"{variable1}", title = "Max values for each district.", color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig)

        #--------------------------------------
    # Min values

    st.title("""Min values of the different variables according to district.""")

    min = data.groupby("distr").min()

    variable2 = dat.col_value(st.selectbox("""
    Which min value do you want to check?
    """, dat.col_keys()))

    fig = px.bar(min, y=f"{variable2}", title = "Min values for each district.", color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig)


