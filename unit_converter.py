import  streamlit as st

# funtion
def convert_units(value, unit_from , unit_to):

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
        return value * conversion
    
    else:
        return 'Invalid Value to Convert'
    
st.title("Unit Converter")
 
value = st.number_input('Enter the Value', min_value=1.0 , step=1.0) 

unit_from = st.selectbox("Convert From:", ["meter" , "kilometer" , "gram" , "kilogram"])

unit_to = st.selectbox("Convert to:", ["meter" , "kilometer" , "gram" , "kilogram"])

if st.button("Convert"):
    res = convert_units(value, unit_from, unit_to) # Invoke the conversion Function
    st.write(f'Converted Value : {res}')  # Display Result On Screen