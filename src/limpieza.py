import os
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def download_kaggle():
    '''
    This function downloads, unzip, delet zip file and move to data folder, a dataset from kaggle.
    Finally returns the dataset.
    Arg:
         
    '''
    #Firs of all, download the file

    os.system("kaggle datasets download -d anderas/car-consume")
    print("Kaggle file downloaded.")

    #we need to unzip the file
    os.system("unzip car-consume.zip")
    print("Kaggle file unzipped.")

    #Delete the zip file and the old version
    os.system("rm -rf car-consume.zip")
    os.system("rm -rf measurements2.xlsx")
    print("zip file deleted.")

    #Move to data folder
    os.system("mv measurements.csv data/measurements.csv")
    print("Files moved to data folder.")

    return "DataFrame downloaded correctly as madrid-real-estate-market."


def heat_map_triangle(df):
    '''
    This function creates a heat map from a selected dataframe
    '''
    sns.set_theme(style="white")

    # Compute the correlation matrix
    corr = df.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(11, 9))

    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(230, 20, as_cmap=True)

    # Draw the heatmap with the mask and correct aspect ratio
    return sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0, square=True, linewidths=.5,annot=True, cbar_kws={"shrink": .5})


def dot_comma(fila):
    '''
    This function replace ","" with ".".
    Args:
        - fila: the string where we want to remove the comma.
    '''

    return fila.replace(',','.')


def str_to_float(df_columna):
    '''
    This function convert a object type column into a float.
    Args:
        -columna: The column we want to convert.
    '''


    return  df_columna.str.replace(",",".").astype(float) 
