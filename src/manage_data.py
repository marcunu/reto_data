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
