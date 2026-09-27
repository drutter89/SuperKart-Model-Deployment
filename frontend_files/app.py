import streamlit as st
import requests

st.title('SuperKart Sales Forecast')
api_url = st.text_input('Backend URL', 'http://superkart-backend:7860')
with st.form('prediction_form'):
    weight = st.number_input('Product Weight', min_value=0.0, value=12.66)
    sugar = st.selectbox('Sugar Content', ['Low Sugar','Regular','No Sugar'])
    area = st.number_input('Allocated Area', min_value=0.0, value=0.027, format='%.3f')
    mrp = st.number_input('Product MRP', min_value=0.0, value=117.08)
    size = st.selectbox('Store Size', ['Small','Medium','High'])
    city = st.selectbox('City Type', ['Tier 1','Tier 2','Tier 3'])
    store = st.selectbox('Store Type', ['Supermarket Type1','Supermarket Type2','Departmental Store','Food Mart'])
    pid = st.selectbox('Product ID Prefix', ['FD','DR','NC'])
    age = st.number_input('Store Age (Years)', min_value=0, value=16)
    category = st.selectbox('Product Type Category', ['Perishables','Non Perishables'])
    submitted = st.form_submit_button('Predict Sales')
if submitted:
    payload = {'Product_Weight':weight,'Product_Sugar_Content':sugar,'Product_Allocated_Area':area,'Product_MRP':mrp,'Store_Size':size,'Store_Location_City_Type':city,'Store_Type':store,'Product_Id_char':pid,'Store_Age_Years':age,'Product_Type_Category':category}
    r = requests.post(api_url.rstrip('/') + '/v1/predict', json=payload, timeout=30)
    r.raise_for_status()
    st.success(f"Predicted sales: {r.json()['predicted_sales']:,.2f}")
