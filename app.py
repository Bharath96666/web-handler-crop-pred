import streamlit as st 
import pickle 

st.title('Crop Predicition System ')
modal=pickle.load(open('modal.pkl','rb'))

col1,col2=st.columns(2)
n=col1.number_input('Enter Nitrogen')
p=col2.number_input('Enter Phosphorous')
k=col1.number_input('Enter potassium')
t=col2.number_input('Enter Temperature')
h=col1.number_input('Enter Humidity')
ph=col1.number_input('Enter pH')
r=col2.number_input('Enter Rainfall')

if st.button('predict'):
    data=[[n,p,k,t,h,ph,r]]
    result=modal.predict(data)[0]
    st.success(result)