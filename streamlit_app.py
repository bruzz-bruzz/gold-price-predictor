import streamlit as st
import joblib
import pandas as pd
import datetime
model = joblib.load('predictor.pkl')
st.set_page_config(page_title="Gold Price Predictor", page_icon="💰")
st.title("💰 Gold Price Predictor")
st.write("Enter a date to predict the gold price (USD).")
selected_date = st.date_input("Select Date", datetime.date.today())
if st.button("Predict Price", type="primary"):
    timestamp = (pd.Timestamp(selected_date) - pd.Timestamp('1970-01-01')) // pd.Timedelta('1s')
    input_data = pd.DataFrame({'Date': [timestamp]})
    prediction = model.predict(input_data)[0]
    st.success(f"The predicted gold price for {selected_date} is ${prediction:,.2f}")
