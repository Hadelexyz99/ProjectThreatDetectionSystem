# -*- coding: utf-8 -*-

"""
Created on Tue May 16 08:55:44 2023

@author: Usman Adeleye
"""

import numpy as np
import pickle
import streamlit as st

from tensorflow.keras.models import load_model
classifier = load_model('model.h5')

# pickle_in = open("classifier.pkl", "rb")
# classifier = pickle.load(pickle_in)


# @app.route('/')
def welcome():
    return "Welcome All"


# @app.route('/predict',methods=["Get"])
def predict_fraud(V4, V8, V10, V13, V14, V16, V21, V22, V23, V27):
    prediction = classifier.predict([[V4, V8, V10, V13, V14, V16, V21, V22, V23, V27]])
    return prediction


def main():
    st.title("Network Intrusion Detection System")
    html_temp = """
    <div style="background-color:green;padding:10px">
    <h2 style="color:white;text-align:center;">Usman's Network Intrusion Detection ML App</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    V4 = st.number_input("V4 ('Values -6 and 20')", step=1)
    V8 = st.number_input("V8 ('Values between -73 and 20')", step=1)
    V10 = st.number_input("V10 ('Values between -25 and 25')", step=1)
    V13 = st.number_input("V13 ('Values -6 and 8')", step=1)
    V14 = st.number_input("V14 ('Values -20 and 12')", step=1)
    V16 = st.number_input("V16 ('Values -15 and 18')", step=1)
    V21 = st.number_input("V21 ('Values -35 and 30')", step=1)
    V22 = st.number_input("V22 ('Values -11 and 11')", step=1)
    V23 = st.number_input("V23 ('Values -45 and 25')", step=1)
    V27 = st.number_input("V27 ('Values -23 and 31')", step=1)
    
    

    # Code for Prediction
    result = ""
    if st.button("Predict Fraud"):
        result = predict_fraud(V4, V8, V10, V13, V14, V16, V21, V22, V23, V27)
        if result >= 0.9:
            result = "This is a fraudulent transaction"
            print(result)
        else:
            result = "This is a normal transaction "
            print(result)
        
    st.success(result)


if __name__ == '__main__':
    main()
