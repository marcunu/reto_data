import pandas as pd

data = pd.read_csv("data/cars_limpio.csv")
data.drop("Unnamed: 0", axis=1, inplace=True)

#-------------------------------------------------
#Yes/No
#-------------------------------------------------

def si_no():
    '''
    This function let you choose between yes or no
    '''
    sn = ["No", "Yes"]
    return sn

def sn_bool(resp):
    '''
    This function transforms yes or no into boolean
    '''
    if resp == "No":
        return 0
    if resp == "Yes":
        return 1


#-------------------------------------------------
#Carga data
#-------------------------------------------------

def carga_data():
    '''
    This function loads a dataframe
    '''
    data = pd.read_csv("data/cars_limpio.csv")
    return data

#-------------------------------------------------
#Visualization
#-------------------------------------------------

ft_dicc = {
    "E10":1,
    "SP98":2,
    "Both":3}

def ft_keys():
    '''
    This functions let the user choose between house types.
    '''
    return list(ft_dicc.keys())

def ft_value(key):
    '''
    This function transforms the election of the user into numerical.
    '''
    return ft_dicc[key]