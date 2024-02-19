import os
import pickle
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from streamlit_option_menu import option_menu
import base64


def diabetes_check(diabetes_model):
    title_html = '''
        <div class="title">
            <h1 class="custom-title" style= "color: white;padding-top: 10px;border-bottom: 2px solid white; padding-bottom: 10px;">Diabetes Prediction using ML</h1>
        </div>
        '''
    st.markdown(title_html, unsafe_allow_html=True)
 
    st.markdown(' ')
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):
    
        user_input = [ Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        try:
            user_input = [float(x) for x in user_input]
            diab_prediction = diabetes_model.predict([user_input])
            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'
            st.success(diab_diagnosis)
        except ValueError:
            st.error("Please enter valid numerical values for all fields.")

    st.markdown('---')
    st.markdown('  ')
    st.markdown('''
            <div class="para"><p class="custom-para" style="text-align:bottom; text-indent: 70px; position: absolute; bottom: 0; padding-left: 200px; color: white; font-size: 18px border-top: 2px solid white; padding-top: 10px;"> Your Personal Medical Guide. A Medical Suggestion and Remote Generation System.</p></div>''',
            unsafe_allow_html=True)
    st.markdown('  ')
    st.markdown('  ')
    st.markdown('''
            <div class="para"><p class="custom-para" style="text-align:bottom; text-indent: 40px; position: absolute; bottom: 0; padding-left: 200px; color: white; font-size: 18px "> © 2024 Centre of Development of Advanced Computing (C-DAC). All rights reserved.</p></div>''',
            unsafe_allow_html=True)
