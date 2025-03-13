import  streamlit as st

# funtion
def convert_units(Value, unit_from , unit_to):

    # Dictionary / Object
    conversions = {
        'meter_kilometer' : 0.001,   # 1 meter = 0.001 kilometer
         'kilometer_meter' : 1000,   # 1 kilometer = 1000 meter
         'gram_kilogram' : 0.001,    # 1 gram = 0.001 kilogram
         'kilogram_gram' : 1000,     # 1 kilogram = 1000 gram   
    }    


    key = f"{unit_from}_{unit_to}"  # Generate a unique key based no the input & output units   

    if key in conversions :
        conversion = conversions[key]
        return Value * conversion
    
    else:
        return 'Invalid Value to Convert'
    
st.title("Unit Converter")
 
value = st.number_input('Enter the Value')

unit_from = st.selectbox("Convert From:", ["Meter" , "Kilometer" , "Gram" , "Kilogram"])

unit_to = st.selectbox("Convert to:", ["Meter" , "Kilometer" , "Gram" , "Kilogram"])

