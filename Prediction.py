import pickle
import numpy as np
import streamlit as st
import base64


load_model = pickle.load(open("Calorie_Burned_Prediction.sav", 'rb'))

with open("Fitbit.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
st.markdown(
f"""    
<style>
.stApp {{
    background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center center;
}}
</style>
""",
unsafe_allow_html=True
)

st.title("Counting Calories? AI Does the Math So You Don't Have To!")



Steps = st.number_input("Steps taken (more the merrier!): ",min_value=0, max_value=20000)
Active = st.number_input("Active mins (don't hold back!): ",min_value=0, max_value=100)
Distance = st.number_input("Distance traveled (let's explore!): ",min_value=0, max_value=16)

st.markdown("""
<style>
    .stNumberInput label {
        color: cyan;
    }
</style>
""", unsafe_allow_html=True)

if st.button("Let's Get Cooking!"):
    features = np.array([[Steps, Active, Distance]])
    prediction = load_model.predict(features)
    prediction = int(prediction)
    st.write("Counting Calories? AI Does the Math So You Don't Have To!: ", prediction)
    




