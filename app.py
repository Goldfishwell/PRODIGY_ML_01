import pandas as pd
import pickle as pk
import streamlit as st


model = pk.load(open('C:/Users/Umesh/Downloads/Prodigy tasks/House_Prediction_Model.pkl','rb'))
st.header('Mumbai House Prediction Model.')
data=pd.read_csv('C:/Users/Umesh/Downloads/Prodigy tasks/Cleaned_Dataset.csv')

loc= st.selectbox('Choose the Location:',data['locality'].unique())
sqft = st.number_input('Choose your Square Ft:')
bed = st.number_input('Enter number of Bedrooms:')
bathroom = st.number_input('Enter number of Bathrooms:')
balc = st.number_input('Enter number of Balcony:')

input1 = pd.DataFrame([[sqft,loc,bed,bathroom,balc]],columns=['area','locality','bedroom_num','bathroom_num','balcony_num'])

if st.button('Predict Price'):
    output = model.predict(input1)
    st.write('Price of Flat is: ',output[0]*100000)
    st.write('price per square ft is: ',(output[0]*100000)/sqft)
    