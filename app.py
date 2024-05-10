# -*- coding: utf-8 -*-

"""
Created on Sat 27 Apr 08:55:44 2024

@author: Usman Adeleye
"""

import numpy as np
import pickle
import streamlit as st
import altair as alt
from tensorflow.keras.models import load_model

classifier = load_model('model.h5')

# Define the prediction function
def predict_threat(ts, uid, orig_h, orig_p, resp_h, resp_p, conn_state,
                   history, orig_pkts, orig_ip_bytes, resp_pkts, resp_ip_bytes,
                   PartOfAHorizontalPortScan, n, tcp, udp):
    # You might need to preprocess the input data here, depending on the model requirements
    # Assuming the model expects numpy arrays, you might need to convert the input to numpy arrays
    input_data = np.array([ts, uid, orig_h, orig_p, resp_h, resp_p, conn_state,
                           history, orig_pkts, orig_ip_bytes, resp_pkts, resp_ip_bytes,
                           PartOfAHorizontalPortScan, n, tcp, udp]).reshape(1, -1)
    # Make prediction
    prediction = classifier.predict(input_data)
    return prediction

# Define the main Streamlit app
def main():
    # Set page title and icon
    st.set_page_config(page_title="Intrusion Detection System", page_icon="🔒")

    # Header
    st.title("Network Intrusion Detection System")
    st.write("Welcome to Usman's Network Intrusion Detection ML App")
    st.markdown("---")

    # Collect user inputs
    st.sidebar.title("Input Parameters")
    ts = st.sidebar.number_input("Timestamp", min_value=1500000000, max_value=2000000000, value=1526000000, step=1)
    uid = st.sidebar.number_input("Unique Identifier", min_value=0, max_value=196565, value=100, step=1)
    orig_h = st.sidebar.number_input("Source IP", min_value=0, max_value=57, value=10, step=1)
    orig_p = st.sidebar.number_input("Source Port", min_value=23, max_value=61000, value=10000, step=1)
    resp_h = st.sidebar.number_input("Destination IP", min_value=0, max_value=172516, value=20, step=1)
    resp_p = st.sidebar.number_input("Destination Port", min_value=1, max_value=65535, value=80, step=1)
    conn_state = st.sidebar.number_input("Connection State", min_value=0, max_value=9, value=5, step=1)
    history = st.sidebar.number_input("History", min_value=0, max_value=73, value=10, step=1)
    orig_pkts = st.sidebar.number_input("Packets from Destination to Port", min_value=0, max_value=48, value=5, step=1)
    orig_ip_bytes = st.sidebar.number_input("Bytes from Source to Destination", min_value=0, max_value=2990, value=200, step=1)
    resp_pkts = st.sidebar.number_input("Packets from Destination to Source", min_value=0, max_value=66, value=10, step=1)
    resp_ip_bytes = st.sidebar.number_input("Bytes from Destination to Source", min_value=0, max_value=4202, value=400, step=1)
    PartOfAHorizontalPortScan = st.sidebar.number_input("Horizontal Port Scan", min_value=0, max_value=1, value=0, step=1)
    tcp = st.sidebar.number_input("TCP", min_value=0, max_value=1, value=1, step=1)
    udp = st.sidebar.number_input("UDP", min_value=0, max_value=1, value=0, step=1)
    n = st.sidebar.number_input("Not Horizontal Port Scan", min_value=0, max_value=1, value=1, step=1)
    
    # Code for Prediction
    if st.sidebar.button("Predict Threat"):
        result = predict_threat(ts, uid, orig_h, orig_p, resp_h, resp_p, conn_state, history, orig_pkts, orig_ip_bytes, resp_pkts, resp_ip_bytes, PartOfAHorizontalPortScan, n, tcp, udp)
        if result >= 0.9:
            st.error("Threat Detected!")
        else:
            st.success("Normal Activity Detected")

if __name__ == '__main__':
    main()
