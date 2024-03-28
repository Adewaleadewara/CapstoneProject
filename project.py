import streamlit as st
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import joblib
import matplotlib.pyplot as plt
import plotly.express as px

st.markdown("<h4 style = 'margin: -30px; color: #123524; text-align: center; font-family: Cambria'> Built By: JOLAYEMI ADEWALE A.</h4>",unsafe_allow_html = True)
st.image('pngwing.com (19).png', use_column_width=True)
st.markdown("<h1 style = 'color: #2c5f2dff; text-align: center; font-family: Lucida Bright'>CROP RECOMMENDATION SYSTEM</h1>", unsafe_allow_html = True)
st.markdown("<br>", unsafe_allow_html= True)

ds = pd.read_csv('Crop_recommendation (1).csv')
column_names = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
column_name = ['label']
column_names = ds.columns.tolist()
x_column = st.selectbox('Select column for x-axis:', column_name)
y_column = st.selectbox('Select column for y-axis:', column_names)
plt.figure(figsize=(10, 6))

st.markdown("<h1 style = 'color: #2c5f2dff; text-align: center; font-family: Lucida Bright'>PROJECT BACKGROUND INFORMATION</h1>", unsafe_allow_html = True)
st.write("The primary goal of this project is to develop a robust and data-driven machine learning model for crop recommendation. By leveraging historical data on soil characteristics, climate patterns, crop performance, and market demand, the model aims to provide farmers with tailored recommendations for crop selection. This will empower farmers to make informed decisions based on objective insights, leading to improved yields, resource efficiency, and profitability.")



fig1 = px.bar(data_frame = ds,  x = x_column, 
                    y = y_column, width = 1000, height = 450, title = f'{x_column} by {y_column} Crop')
st.plotly_chart(fig1, use_container_width= True)
fig1.update_layout(
            plot_bgcolor='rgb(0, 255, 0)' )
fig1.update_traces(marker_color='#123524')

st.dataframe(ds, use_container_width= True)

st.sidebar.image('agritech.jpg', caption='Welcome User')
st.sidebar.divider()

st.sidebar.subheader('Input Variable', divider=True)

Nitrogen = st.sidebar.number_input('N')
Phosphorus = st.sidebar.number_input('P')
Potassium = st.sidebar.number_input('K')
Temperature = st.sidebar.number_input('temperature')
Humidity = st.sidebar.number_input('humidity')
pH = st.sidebar.number_input('ph')
Rainfall = st.sidebar.number_input('rainfall')

input_var = pd.DataFrame()
input_var['N'] = [Nitrogen]
input_var['P'] = [Phosphorus]
input_var['K'] = [Potassium]
input_var['temperature'] = [Temperature]
input_var['humidity'] = [Humidity]
input_var['ph'] = [pH]
input_var['rainfall'] = [Rainfall]

st.markdown("<br>", unsafe_allow_html= True)
st.divider()
st.subheader('User Input Variables', divider=True)
st.dataframe(input_var, use_container_width=True)

model = joblib.load('Crop_Model.pkl')
label = joblib.load('label_encoder.pkl')


prediction = model.predict(input_var)

# st.button('Check For Crop Recommendation')
if st.button("See the prediction"):
    if prediction == 0:
        st.write(f'The predicted crop for your conditions is Lentil')
    elif prediction == 1:
        st.write(f'The predicted crop for your conditions is Papaya')
    elif prediction == 2:
        st.write(f'The predicted crop for your conditions is Banana')
    elif prediction == 3:
        st.write(f'The predicted crop for your conditions is KidneyBeans')
    elif prediction == 4:
        st.write(f'The predicted crop for your conditions is Chickpea')
    elif prediction == 5:
        st.write(f'The predicted crop for your conditions is WaterMelon')
    elif prediction == 6:
        st.write(f'The predicted crop for your conditions is Mango')
    elif prediction == 7:
        st.write(f'The predicted crop for your conditions is rice')
    elif prediction == 8:
        st.write(f'The predicted crop for your conditions is Muskmelon')
    elif prediction == 9:
        st.write(f'The predicted crop for your conditions is Cotton')
    elif prediction == 10:
        st.write(f'The predicted crop for your conditions is Coffee')
    elif prediction == 11:
        st.write(f'The predicted crop for your conditions is Pomegranate')
    elif prediction == 12:
        st.write(f'The predicted crop for your conditions is Jute')
    elif prediction == 13:
        st.write(f'The predicted crop for your conditions is Grapes')
    elif prediction == 14:
        st.write(f'The predicted crop for your conditions is Coconut')
    elif prediction == 15:
        st.write(f'The predicted crop for your conditions is Maize')
    elif prediction == 16:
        st.write(f'The predicted crop for your conditions is Apple')
    elif prediction == 17:
        st.write(f'The predicted crop for your conditions is Mothbeans')
    elif prediction == 18:
        st.write(f'The predicted crop for your conditions is Blackgram')
    elif prediction == 19:
        st.write(f'The predicted crop for your conditions is Mungbean')
    elif prediction == 20:
        st.write(f'The predicted crop for your conditions is Orange')
    elif prediction == 21:
        st.write(f'The predicted crop for your conditions is PigeonPeas')
    else:
        st.write('Your requirement was not met')
