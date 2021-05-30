#Import libraries

import streamlit as st
from multiapp import MultiApp
from Streamlit import Home, calculator, graphics # import your app modules here
from PIL import Image

#Set width
st.set_page_config(layout="wide")


#Creating Multitabs

app = MultiApp()

imagen = Image.open("Tools/Images/logo_cobi.png")
st.sidebar.image(imagen)

st.sidebar.markdown("""
# The best tool for
# `high-end tunned` 
# car fuel prediction
""")

# Add all your application here

app.add_app("Home", Home.app)
app.add_app("Visualization", graphics.app)
app.add_app("Calculator", calculator.app)

# The main app
app.run()