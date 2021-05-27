   
# Import libraries

import streamlit as st
from PIL import Image
import pickle 
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import src.manage_data as dat

def app():

    st.title("""
    Here we help you to check it, please enter the desired information in the boxes.
    """)

    m2 = st.text_input("""
    Enter the square metres of your home:
    """)

    habit = st.text_input("""
    How many rooms does your home have?:
    """)

    banos = st.text_input("""
    How many bathrooms does your home have?:
    """)

    piso = st.text_input("""
    What floor is your home on?:
    """)

    nueva = dat.sn_bool(st.selectbox("""
    Is it a new development?:
    """, dat.si_no()))

    reforma = dat.sn_bool(st.selectbox("""
    Does it need to be reformed?:
    """, dat.si_no()))

    park = dat.sn_bool(st.selectbox("""
    Do you have a parking space?:
    """, dat.si_no()))

    exter = dat.sn_bool(st.selectbox("""
    is exterior?:
    """, dat.si_no()))

    tipo= dat.ht_value(st.selectbox("""
    What type of housing is it?:
    """, dat.ht_keys()))

    distr = st.selectbox("""
    Select a district:
    """, dat.d_keys())


    barr = dat.b_values(distr, st.selectbox("""
    Select a neighborhood:
    """, dat.b_keys(distr)))


    cert = dat.ec_value(st.selectbox("""
    What kind of energy certificate do you have?
    """, dat.ec_keys()))



    market = {
        "sq_mt_built": [m2],
        "n_rooms": [habit],
        "n_bathrooms" : [banos], 
        "floor" : [piso],
        "is_new_development" : [nueva],
        "is_renewal_needed" : [reforma],
        "has_parking": [park],
        "is_exterior" : [exter],
        "tipo" : [tipo],
        "barrio_pm2" : [barr], 
        "e_certificate" : [cert],
        #"rent_price" : [1800]
        
    }

    try:
        market_test = pd.DataFrame(market)
        ren_tree = pickle.load(open("Tools/parameters/rent_price/rp_rfr_md9_mf075_ms2", 'rb'))
        precio = ren_tree.predict(market_test)
        #st.write(precio)

        market["rent_price"] = [precio]
        market_test = pd.DataFrame(market)
        best_tree = pickle.load(open("Tools/parameters/rfr_md8_mf08_ms3_fun", 'rb'))

        valoracion = best_tree.predict(market_test)

        st.title(f"""The market price of your property is `{round(valoracion[0],-4)}` €""")

        st.title(f"""The rent price of your property is `{round(precio[0], -1)}` €""")
    
    except:
        pass