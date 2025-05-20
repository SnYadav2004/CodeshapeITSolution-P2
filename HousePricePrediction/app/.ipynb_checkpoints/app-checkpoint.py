import streamlit as st
import pandas as pd
import numpy as np
import joblib
# from sqlalchemy import create_engine
import pymysql


# Load the trained model
model = joblib.load(r"C:\Users\snyad\project\HousePricePrediction\models\house_price_model.pkl")
# Connect to MySQL database (update with your password)
# engine = create_engine("mysql+pymysql://root:8005130826@localhost/house_price")

st.set_page_config(page_title="House Price Prediction", layout="centered")
st.title("🏠 House Price Predictor")
st.markdown("Fill in the details below to estimate your house's price:")

# Input fields (match with model features)
overall_qual = st.slider("Overall Quality (1-10)", 1, 10, 5)
gr_liv_area = st.number_input("Above Ground Living Area (sq ft)", min_value=300, max_value=10000)
garage_cars = st.slider("Garage Capacity (cars)", 0, 5, 2)
total_bsmt_sf = st.number_input("Total Basement Area (sq ft)", min_value=0, max_value=3000)
first_flr_sf = st.number_input("1st Floor Area (sq ft)", min_value=0, max_value=3000)
year_built = st.slider("Year Built", 1900, 2024, 2000)

# Create DataFrame for prediction
input_data = pd.DataFrame({
    'OverallQual': [overall_qual],
    'GrLivArea': [gr_liv_area],
    'GarageCars': [garage_cars],
    'TotalBsmtSF': [total_bsmt_sf],
    '1stFlrSF': [first_flr_sf],
    'YearBuilt': [year_built]
})

# Prediction button
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Estimated House Price: ₹{int(prediction):,}")
    
    # # ✅ Save prediction to MySQL
    # input_data['predicted_price'] = prediction
    # input_data.to_sql('prediction_log', con=engine, if_exists='append', index=False)
    # st.info("✅ Prediction logged to MySQL database.")
