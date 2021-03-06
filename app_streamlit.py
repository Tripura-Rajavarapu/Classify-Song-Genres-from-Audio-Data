# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 16:56:44 2021

@author: tripu
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
def predict_note_authentication(acousticness,danceability,energy,instrumentalness,liveness,speechiness,tempo,valence):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[acousticness,danceability,energy,instrumentalness,liveness,speechiness,tempo,valence]])

    print(prediction)
    return prediction



def main():
    st.title("Song Genre Classifier")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Song Genre Classifier ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    acousticness = st.text_input("Acousticness")
    danceability = st.text_input("Danceability")
    energy = st.text_input("Energy")
    instrumentalness = st.text_input("Instrumentalness")
    liveness = st.text_input("Liveness")
    speechiness = st.text_input("Speechiness")               
    tempo = st.text_input("Tempo")
    valence = st.text_input("Valence")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(acousticness,danceability,energy,instrumentalness,liveness,speechiness,tempo,valence)
    st.success('The output is {}'.format(result))
    
    
if __name__=='__main__':
    main()
    
    
    