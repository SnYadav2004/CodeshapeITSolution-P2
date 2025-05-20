import streamlit as st
import pandas as pd
import joblib
import os

# ✅ Load model using absolute path resolution (works on any platform)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "house_price_model.pkl")
model = joblib.load(MODEL_PATH)

# ✅ Streamlit UI
st.set_page_config(page_title="House Price Prediction", layout="centered")
st.title("🏠 House Price Predictor")
st.markdown("Fill in the details below to estimate your house's price:")

# Inputs
overall_qual = st.slider("Overall Quality (1-10)", 1, 10, 5)
gr_liv_area = st.number_input("Above Ground Living Area (sq ft)", 300, 10000)
garage_cars = st.slider("Garage Capacity (cars)", 0, 5, 2)
total_bsmt_sf = st.number_input("Total Basement Area (sq ft)", 0, 3000)
first_flr_sf = st.number_input("1st Floor Area (sq ft)", 0, 3000)
year_built = st.slider("Year Built", 1900, 2024, 2000)

input_df = pd.DataFrame({
    "OverallQual": [overall_qual],
    "GrLivArea": [gr_liv_area],
    "GarageCars": [garage_cars],
    "TotalBsmtSF": [total_bsmt_sf],
    "1stFlrSF": [first_flr_sf],
    "YearBuilt": [year_built]
})

if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    st.success(f"💰 Estimated House Price: ₹{int(prediction):,}")
