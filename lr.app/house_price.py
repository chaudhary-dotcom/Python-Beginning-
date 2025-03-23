import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Generate a sample dataset
np.random.seed(42)
square_feet = np.random.randint(500, 4000, 100).reshape(-1, 1)
price = square_feet * 150 + np.random.randint(10000, 50000, 100)

# Train a linear Regression model 
X_train, X_test, y_train, y_test = train_test_split(square_feet, price, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Streamlit App 
st.title('House price predication using Linear Regression')

# User input
sqft_input = st.number_input('Enter Square Feet: ', min_value=500, max_value=4000, value= 700, step=50)

if st.button('Predict Price'):
    predicted_price = model.predict([[sqft_input]])[0]
    st.write(f'Predicted Price: **${predicted_price}**')

# Visualizing Predication
y_pred = model.predict(X_test)
fig, ax = plt.subplots()
ax.scatter(X_test, y_test, color='blue', label='Actual Prices')
ax.scatter(X_test, y_pred, color='red', label='Predicated price')
ax.set_xlabel('Square feet')
ax.set_ylabel('Price')
ax.set_title('Actual vs predicated prices')
ax.legend()
st.pyplot(fig)



