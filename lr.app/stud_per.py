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

def predict_data(data):
    model, scaler, le = load_model()
    preprocessed_data = preprocessing_input_data(data, scaler, le)
    prediction = model.predict(preprocessed_data)
    return prediction[0]

def main():
    st.title('Student performance predication')
    st.write('Enter your detail for get predication on your input')

    hour_studied = st.number_input('Hours studied', min_value=1, max_value=10, value=5)

if __name__ == '__main__':
    main()



