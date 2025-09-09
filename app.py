import streamlit as st
import pickle
import numpy as np
import pandas as pd
import joblib

# Load the trained model

model = joblib.load('models/laptop_price_model.pkl')
st.title('Laptop Price Predictor')
st.write('Enter the specifications of the laptop to predict its price:')
# Add all required input fields
company = st.selectbox('Company', ['Dell', 'HP', 'Lenovo', 'Apple', 'Acer', 'Asus', 'MSI', 'Other'], key='company')
typename = st.selectbox('TypeName', ['Notebook', 'Ultrabook', 'Gaming', '2 in 1', 'Workstation', 'Netbook', 'Other'], key='typename')
inches = st.slider("Screen Size (inches)", 10.0, 20.0, 15.6, 0.1)
screenwidth = st.number_input('Screen Width (cm)', value=35.0, key='screenwidth')
screenheight = st.number_input('Screen Height (cm)', value=20.0, key='screenheight')
weight = st.number_input('Weight (kg)', value=2.0, key='weight')
cpu_speed = st.number_input('CPU Speed (GHz)', min_value=1.0, max_value=5.0, value=2.5, key='cpu_speed')
ram = st.slider("RAM (GB)", 2, 128, 8, 2)
ssd = st.number_input("SSD Size (GB)", min_value=0, value=256, step=128)
hdd = st.number_input("HDD Size (GB)", min_value=0, value=0, step=500)
hybrid = st.number_input('Hybrid (GB)', min_value=0, max_value=2048, value=0, key='hybrid')
flash_storage = st.number_input('Flash Storage (GB)', min_value=0, max_value=2048, value=0, key='flash_storage')
gpu = st.selectbox('GPU', ['Integrated', 'NVIDIA', 'AMD', 'Other'], key='gpu')
opsys = st.selectbox('Operating System', ['Windows', 'MacOS', 'Linux', 'Other'], key='opsys')

# Example input fields (customize based on your model's features)
cpu_brand = st.selectbox('Cpu Brand', ['Intel Core i3', 'Intel Core i5', 'Intel Core i7', 'Intel Core i9', 'AMD Ryzen 3', 'AMD Ryzen 5', 'AMD Ryzen 7', 'Other'])



# Prepare input for model (example encoding, adjust as per your model)

# Prepare input for model with all required columns
input_dict = {
	'Company': company,
	'TypeName': typename,
	'Inches': inches,
	'ScreenWidth': screenwidth,
	'ScreenHeight': screenheight,
	'Weight': weight,
	'Cpu_brand': cpu_brand,
	'Cpu_speed': cpu_speed,
	'Ram': ram,
	'HDD': hdd,
	'SSD': ssd,
	'Hybrid': hybrid,
	'Flash_Storage': flash_storage,
	'Gpu': gpu,
	'OpSys': opsys
}
input_df = pd.DataFrame([input_dict])

if st.button('Predict Price'):
	try:
		prediction = model.predict(input_df)[0]
		st.success(f'Estimated Laptop Price: ₹{prediction:,.0f}')
	except Exception as e:
		st.error(f'Error in prediction: {e}')
