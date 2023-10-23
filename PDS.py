import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Load the dataset with predictions for all time intervals
data = pd.read_csv("dataset_with_predictions.csv")

# Define the input features for prediction and their upper limits
features = ['a (AU)', 'Eccentricity', 'Inclination (deg)', 'Argument of Perihelion (deg)',
            'Longitude of Ascending Node (deg)', 'Mean Anomaly (deg)', 'Perihelion Distance (AU)',
            'Aphelion Distance (AU)', 'Orbital Period (yr)']

# Create a machine learning model (Random Forest Regressor) for each time interval
model_3_months = RandomForestRegressor(n_estimators=500, random_state=42)
model_6_months = RandomForestRegressor(n_estimators=500, random_state=42)
model_1_year = RandomForestRegressor(n_estimators=500, random_state=42)

# Train the models for each time interval
model_3_months.fit(data[features], data[['x (3rd Month)', 'y (3rd Month)', 'z (3rd Month)']])
model_6_months.fit(data[features], data[['x (6th Month)', 'y (6th Month)', 'z (6th Month)']])
model_1_year.fit(data[features], data[['x (1 Year)', 'y (1 Year)', 'z (1 Year)']])

# Streamlit app
st.title("Satellite Coordinate Prediction Model")

st.sidebar.header("User Input")
a = st.sidebar.number_input('Semi-Major Axis (AU)', min_value=0.0)
eccentricity = st.sidebar.number_input('Eccentricity', min_value=0.0, max_value=1.0)
inclination = st.sidebar.number_input('Inclination (deg)', min_value=0.0, max_value=180.0)
arg_perihelion = st.sidebar.number_input('Argument of Perihelion (deg)', min_value=0.0, max_value=360.0)
asc_node = st.sidebar.number_input('Longitude of Ascending Node (deg)', min_value=0.0, max_value=360.0)
mean_anomaly = st.sidebar.number_input('Mean Anomaly (deg)', min_value=0.0, max_value=360.0)
p_dist = st.sidebar.number_input('Perihelion Distance (AU)', min_value=0.0)
a_dist = st.sidebar.number_input('Aphelion Distance (AU)', min_value=0.0)
oy = st.sidebar.number_input('Orbital Period (yr)', min_value=0.0)

if st.sidebar.button('Predict'):
    input_data = [a, eccentricity, inclination, arg_perihelion, asc_node, mean_anomaly, p_dist, a_dist, oy]
    predictions_3_months = model_3_months.predict([input_data])
    predictions_6_months = model_6_months.predict([input_data])
    predictions_1_year = model_1_year.predict([input_data])
    st.subheader('Predicted Satellite Orbit:')

    st.write('Coordinates for 3rd Month:')
    st.write(f'X: {predictions_3_months[0][0]:.4f}')
    st.write(f'Y: {predictions_3_months[0][1]:.4f}')
    st.write(f'Z: {predictions_3_months[0][2]:.4f}')

    st.write('Coordinates for 6th Month:')
    st.write(f'X: {predictions_6_months[0][0]:.4f}')
    st.write(f'Y: {predictions_6_months[0][1]:.4f}')
    st.write(f'Z: {predictions_6_months[0][2]:.4f}')

    st.write('Coordinates for 1 Year:')
    st.write(f'X: {predictions_1_year[0][0]:.4f}')
    st.write(f'Y: {predictions_1_year[0][1]:.4f}')
    st.write(f'Z: {predictions_1_year[0][2]:.4f}')