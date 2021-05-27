import streamlit as st
from PIL import Image


def app():
    
    # Front Page
    logo = Image.open("Tools/Images/logo.png")
    st.image(logo)

    imagen = Image.open("Tools/Images/Portada2.jpg")
    st.image(imagen)

    st.title("""
    How much is your house worth?
    Have you ever wondered what the **`current value`** of your home is?

    Are you interested in buying a new property but don't know if its value is in line with the **`market value`**?

    Have you ever tried to **`rent a property`** and didn't know if the price was right?

    Here we help you to check it, please enter the desired information in the boxes.
    """)

    st.write("""
    # Real estate market
    After the brick crisis of 2008 the real estate market suffered a very sharp fall, but nowadays prices are increasing.
    """)

    st.image(Image.open("Tools/Images/Madrid-overall-property-prices.png"))
