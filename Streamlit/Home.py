import streamlit as st
from PIL import Image


def app():
    


    logo = Image.open("Tools/Images/logo_grand.png")
    st.image(logo)

    imagen = Image.open("Tools/Images/portada.jpg")
    st.image(imagen)



    st.write("""
    Cobify is a company dedicated to transporting people in the style of Uber, Lyft and Cabify itself, which stole its name.

    Cobify was founded in 1992 to coincide with the Barcelona Olympics. We have always been characterised by two things:

    - Operating without a licence of any kind. 💳
    - The use of tricked-out top-of-the-range cars. 🏎

    With the appearance of VTC licences we have been able to come out of the underground and have started to operate legally. But our other hallmark is still the tricked-out high-end cars.
    """)
    st.write("""
    # The fuel Problem

    """)

    st.image(Image.open("Tools/Images/gas_station_orig.jpg"), width=500)

    st.write("""
    
    In case you didn't know, trick cars use high cetane number petrols such as SP98 to avoid fuel injection delays/advancement (avoiding crank pitting), but we have also started to embrace fuels that add ethanol in their formulations, they are cheaper and offer the same cetane number as the more expensive petrols. Without going into more detail (this would be enough for a book) we are beginning to smell that being ecological and modern can be expensive, it seems that cars consume more on journeys.

    """)
