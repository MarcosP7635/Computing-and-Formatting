from tkinter.ttk import Separator
import streamlit as st
import pandas as pd
import numpy as np
import itertools as IT
import altair as alt
from PIL import Image

def load_data(nrows):
    data = pd.read_csv('C:/Users/engin/Documents/GitHub/Computing-and-Formatting/amazonData/amazon-final.csv', 
    delimiter = ';')
    #data['date first available'] = pd.to_datetime(data['date first available'])
    #data = data.sort_values(by=['date first available'])
    #data = data.set_index(data['date first available'])
    #data['discount percentage'] = (data['discount percentage'].str.replace("%",'')). astype(int) 
    #lowercase = lambda x: str(x).lower()
    #data.rename(lowercase, axis='columns', inplace=True)
    return data


for key in load_data(10).keys():
    print(key + "\n")
