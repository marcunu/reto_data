   
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
        st.markdown("""# The problem of maintenance""")
        st.write(""" E10 petrol is cheaper, but when using SP98 petrol the engine is better preserved, that is why the maintenance cost of the engine is lower when using SP98 petrol. What the comparator does is to calculate this cost depending on the distance to be travelled and add it to the price of the fuel used, calculating if the total price is lower for one petrol or the other taking into account the maintenance and the price of the petrol at the same time. """)
        
        mantenimiento_e = round(dist * 0.0151,2)
        mantenimiento_sp = round(dist * 0.0117,2)

        pf_sp = precio_sp[0] + mantenimiento_sp
        pf_e = precio_e[0] + mantenimiento_e

        st.markdown(f"""## Total price if you use SP98 fuel is:  `{round(pf_sp,2)} €`""")

        st.markdown(f"""## Total price if you use E10 fuel is:  `{round(pf_e,2)} €` """)

        dc={"SP98":pf_sp,"E10":pf_e}

        mejor = min(dc, key=dc.get)

        st.markdown(f"""# The best fuel for this travel is `{mejor}`""")
    except:
        pass

    