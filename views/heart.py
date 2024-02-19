import os
import pickle
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from streamlit_option_menu import option_menu
import base64

# working_dir = os.path.dirname(os.path.abspath(__file__))

def heart_check(heart_disease_model):

        
        # page title
        
    title_html = '''
        <div class="title">
            <h1 class="custom-title" style= "color: white;padding-top: 10px;border-bottom: 2px solid white; padding-bottom: 10px;">Heart Disease Prediction using ML</h1>
        </div>
        '''
    st.markdown(title_html, unsafe_allow_html=True)
    st.markdown(' ')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        gender_mapping = {'Male': 1, 'Female': 0}
        selected_gender = st.selectbox('Gender', ('Male', 'Female'), format_func=lambda x: x)
        sex = gender_mapping[selected_gender]

    with col3:
        cp_mapping = {'Asymptomatic': 3,'Non-aginal Pain': 2,'Atypical Agina': 1, 'Typical Agina': 0}
        selected_cp = st.selectbox('Chest Pain Type', ('Asymptomatic','Non-aginal Pain','Atypical Agina','Typical Agina'), format_func=lambda x: x)
        cp = cp_mapping[selected_cp]

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs_mapping = {'Yes': 1, 'No': 0}
        selected_fbs = st.selectbox('Fasting Blood Sugar', ('Yes', 'No'), format_func=lambda x: x)
        fbs = fbs_mapping[selected_fbs]

    with col1:
        restecg_mapping = {'Left Ventricular - Hypertrophy': 2,'ST-T Wave Abnormality': 1, 'Normal': 0}
        selected_restecg = st.selectbox('Resting Electrocardiographic results', ('Left Ventricular - Hypertrophy','ST-T Wave Abnormality','Normal'), 
        format_func=lambda x: x)
        restecg = restecg_mapping[selected_restecg]

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang_mapping = {'Yes': 1, 'No': 0}
        selected_exang = st.selectbox('Exercise Induced Angina', ('Yes', 'No'), format_func=lambda x: x)
        exang = exang_mapping[selected_exang]

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope_mapping = {'Downsloping': 2,'Flat': 1, 'Unsloping': 0}
        selected_slope = st.selectbox('Slope of the peak exercise ST segment', ('Downsloping','Flat', 'Unsloping'), 
        format_func=lambda x: x)
        slope = slope_mapping[selected_slope]

    with col3:
        ca = st.text_input('Major vessels (0-3) colored by flouroscopy')

    with col1:
        thal_mapping = {'Reversable Defect': 3,'Normal': 2, 'Fixed Defect': 1, 'Value not given': 0}
        selected_thal = st.selectbox('Thalassemia', ('Reversable Defect','Normal','Fixed Defect','Value not given'), 
        format_func=lambda x: x)
        thal = thal_mapping[selected_thal]

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        try:
            user_input = [float(x) for x in user_input]
            heart_prediction = heart_disease_model.predict([user_input])
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'
            st.success(heart_diagnosis)
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