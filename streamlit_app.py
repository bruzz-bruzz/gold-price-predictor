import streamlit as st
import joblib
import pandas as pd
import datetime

# Load the model
model = joblib.load('predictor.pkl')

st.set_page_config(page_title="Gold Price Predictor", page_icon="💰")
st.title("💰 Gold Price Predictor")
st.write("Enter a date to predict the gold price (USD).")

# Date input
selected_date = st.date_input("Select Date", datetime.date.today())

if st.button("Predict Price", type="primary"):
    # Convert date to timestamp as per main.py logic
    # The model was trained with 'Date' as a column, and the values are timestamps in seconds
    timestamp = (pd.Timestamp(selected_date) - pd.Timestamp('1970-01-01')) // pd.Timedelta('1s')
    
    # The model expects a DataFrame with the same structure as the training data
    input_data = pd.DataFrame({'Date': [timestamp]})
    
    # Predict
    prediction = model.predict(input_data)[0]
    
    st.success(f"The predicted gold price for {selected_date} is ${prediction:,.2f}")
