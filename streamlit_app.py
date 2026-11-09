import streamlit as st
import joblib
import pandas as pd
import datetime
def render_credits(profile_url: str, repo_url: str):
    """
    Renders the credits footer mimicking the credits.tsx component.
    """
    html_content = f"""
    <footer style="padding: 1.5rem; text-align: center; border-top: 1px solid #e5e7eb; margin-top: 2rem; color: #4b5563;">
        <p style="font-size: 0.875rem;">Made by bruzz-bruzz</p>
        <div style="display: flex; justify-content: center; gap: 1rem; margin-top: 0.5rem;">
            <a style="color: #2563eb; text-decoration: underline;" href="{profile_url}" target="_blank">GitHub Profile</a>
            <a style="color: #2563eb; text-decoration: underline;" href="{repo_url}" target="_blank">GitHub Repository</a>
        </div>
    </footer>
    """
    st.markdown(html_content, unsafe_allow_html=True)
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
render_credits(
    profile_url="https://github.com/bruzz-bruzz", 
    repo_url="https://github.com/bruzz-bruzz/gold-price-predictor"
)
