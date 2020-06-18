# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 15:27:32 2020

@author: Rohan Jacob
"""


import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(loan,empvarrate,conspriceidx,euribor3m,nremployed):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: loan
        in: query
        type: number
        required: true
      - name: empvarrate
        in: query
        type: number
        required: true
      - name: conspriceidx
        in: query
        type: number
        required: true
      - name: euribor3m
        in: query
        type: number
        required: true
    -   name: nremployed
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[loan,empvarrate,conspriceidx,euribor3m,nremployed]])
    print(prediction)
    return prediction



def main():
    st.title("Bank Subscription Analysis")
    html_temp = """
    <div style="background-color:blue;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Subscription ML Application </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    loan = st.text_input("loan","Type Here")
    empvarrate = st.text_input("empvarrate","Type Here")
    conspriceidx= st.text_input("conspriceidx","Type Here")
    euribor3m = st.text_input("euribor3m","Type Here")
    nremployed = st.text_input("nremployed","Type Here")

    result=""
    if st.button("Predict"):
        result=predict_note_authentication(loan,empvarrate,conspriceidx,euribor3m,nremployed)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Bank Churn Analyis")
        st.text("0- Customer Doesn't Subscribes'; 1- Customer Subscribes")

if __name__=='__main__':
    main()