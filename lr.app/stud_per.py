import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler, LabelEncoder


def load_model():
    with open('linear_regression_model.pkl', 'rb') as file:
        model, scaler, le = pickle.load(file)
    return model, scaler, le

def preprocessing_input_data(data, scaler, le):
    data['Extracurricular Activities'] = le.transform([data['Extracurricular Activities']])[0]
    df = pd.DataFrame([data])
    df_transformed = scaler.transform(df)
    return df_transformed

def predict_data(data):
    model, scaler, le = load_model()
    preprocessed_data = preprocessing_input_data(data, scaler, le)
    prediction = model.predict(preprocessed_data)
    return round(prediction[0], 2)

def main():
    st.title('Student performance predication')
    st.write('Enter your detail for get predication on your input')

    hour_studied = st.number_input('Hours studied', min_value=1, max_value=10, value=5)
    previous_score = st.number_input('Previous Scores', min_value=40, max_value=100, value=70)
    Extracurricular_Activities = st.selectbox('Extracurricular Activities', ['Yes', 'No'])
    Sleep_hours = st.number_input('Sleep Hours', min_value=4, max_value=10, value=7)
    Question_papers = st.number_input('Question Papers', min_value=0, max_value=10, value=5)

    if st.button('Predict_Your_Score'):
        user_data = {
            'Hours Studied': hour_studied,
            'Previous Scores': previous_score,
            'Extracurricular Activities': Extracurricular_Activities,
            'Sleep Hours': Sleep_hours,
            'Sample Question Papers Practiced': Question_papers
        }
        prediction = predict_data(user_data)
        st.success(f'Your predication result is: {prediction}')
if __name__ == '__main__':
    main()




