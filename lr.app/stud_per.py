import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler



def load_model():
    with open('linear_regression_model.pkl', 'rb') as file:
        model, scaler, le = pickle.load(file)
    return model, scaler, le

def preprocessing_input_data(data, scaler, le):
    data['Extracurricular Activities'] = le.fit_transform(data['Extracurricular Activities'])
    df_transformed = scaler.transform(data)
    return df_transformed



