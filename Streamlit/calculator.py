   
# Import libraries

import streamlit as st
from PIL import Image
import pickle 
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import src.manage_data as dat
import requests
import json

def app():

    st.title("""
    Below I help you to choose the best type of fuel depending on the situation.
    In short, what the calculator does is to calculate the consumption according to the different parameters for the two types of fuel, once it has calculated them, it compares them and gives you back which is the most efficient fuel for each case.
    Depending on the location, it collects weather information for the city via an API call to a weather page, and fills in the values within the algorithm.
    """)

    dist = st.number_input("""
    how far you plan to go:
    """)

    speed = st.number_input("""
    How fast do you plan to go?:
    """)

    ac = dat.sn_bool(st.selectbox("""
    Are you going to use the AC??:
    """, dat.si_no()))

    ciudad = st.text_input("""
    Where are you?
    """)

    url = "http://api.weatherapi.com/v1/current.json?key=75da7270adbc40d6b58154057213005&q={ciudad}&aqi=no"

    response = requests.get(url).json()

    temp_o = response["current"]["temp_c"]
    nubes = response["current"]["cloud"]

    if nubes >=  50:
        sun = 0
    else:
        sun = 1

    lluvia = response["current"]["precip_mm"]

    if lluvia > 0 :
        rain = 1
    else:
        rain = 0

    st.markdown(f"""### In `{ciudad}`, a temperature of `{temp_o} ºC` is forecast, there will be `{nubes}%` of clouds and the precipitation will be `{lluvia} mm`.""")
    st.write(f"""This information has been obtained from weather API""")

    fuel_sp = {
        "distance": [dist],
        "speed": [speed],
        "temp_inside" : 21.9295, 
        "temp_outside" : [temp_o],
        "AC" : [ac],
        "rain" : [rain],
        "sun": [sun],
        "Fuel_price" : 1.46  
    }

    fuel_e = {
        "distance": [dist],
        "speed": [speed],
        "temp_inside" : 21.9295, 
        "temp_outside" : [temp_o],
        "AC" : [ac],
        "rain" : [rain],
        "sun": [sun],
        "Fuel_price" : 1.38  
    }

    try:
        fuel_test_sp = pd.DataFrame(fuel_sp)
        ren_tree = pickle.load(open("Tools/parameters/cars", 'rb'))
        consume_sp = ren_tree.predict(fuel_test_sp)
        fuel_test_sp["consume"] = consume_sp
        

        precio_sp =  round(fuel_test_sp["distance"] * (fuel_test_sp["consume"]/100) * fuel_test_sp["Fuel_price"],2)

        fuel_test_e = pd.DataFrame(fuel_e)
        ren_tree = pickle.load(open("Tools/parameters/cars", 'rb'))
        consume_e = ren_tree.predict(fuel_test_e)
        fuel_test_e["consume"] = consume_e

        precio_e =  round(fuel_test_e["distance"] * (fuel_test_e["consume"]/100) * fuel_test_e["Fuel_price"],2)    

    

        st.markdown(f"""## The price if you use SP98 fuel is:  `{precio_sp[0]} €`""")

        st.markdown(f"""## The price if you use E10 fuel is:  `{precio_e[0]} €` """)
    
        

    except:
        pass
    

    try:
        dc={"SP98":precio_sp[0],"E10":precio_e[0]}

        mejor = min(dc, key=dc.get)

        st.markdown(f"""# The best fuel for this travel is {mejor}""")
    except:
        pass

    