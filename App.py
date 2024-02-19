import os
import pickle
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from streamlit_option_menu import option_menu
import base64
from views import medblog, contact_us, about_us, symptom_checker, heart, diabetes

# Set page title and icon
st.set_page_config(page_title="SymptoSense", layout="wide", page_icon="🩺")

st.markdown('<link rel="stylesheet" type="text/css" href="sty.css">', unsafe_allow_html=True)

working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models
heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/trained_model.sav', 'rb'))  
diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model (1).sav', 'rb'))

# Define the main page layout
def inject_custom_css():
    def add_bg_from_local(image_file):
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url(data:image/{"jpeg"};base64,{encoded_string.decode()});
                background-size: cover;
            }}
            .css-1aumxhk {{
                background-color: black !important;
                color: black !important;
            }}
            .st-ba {{
                background-color: black !important;
                color: black !important;
            }}
            .sidebar.sidebar-content {{
                position: fixed;
                background-color: black;
                overflow-y: auto;
                z-index: 999;
            }}
            [data-testid="stHeader"] {{
                position: fixed;
                top: 0px;
                left: 0px;
                right: 0px;
                height: 2.875rem;
                background: rgb(9 9 9);
                outline: none;
                z-index: 999990;
                display: block;
            }}

            [data-testid="stSidebarUserContent"]{{
                position: fixed;
                background-color: rgb(34, 34, 34);
            
            }}

            [data-testid="stSidebarContent"]{{
                background-color: rgb(34, 34, 34);
            
            }}
            .sidebar.accordion {{
                background-color: black !important;
            }}
            .custom-title {{
                color: white !important;
                text-align: center;
            }}
            .custom-para {{
                color: white !important;
            }}
            .bg-image {{
                background-image: url("mainb.jpg");
                position: relative;
                overflow: hidden;
                background-size: cover;
                filter: blur(10px);
                -webkit-filter: blur(8px);
                height: 100%;
                background-position: center;
                background-repeat: no-repeat;
                background-size: cover;
            }} 
            .bg-text {{
                background-color: rgb(0,0,0);
                background-color: rgba(0,0,0, 0.4);
                color: white;
                font-weight: bold;
                border: 3px solid #f1f1f1;
                position: absolute;
                top: 0;
                right: 0;
                transform: translate(0%, 0%);
                z-index: 2;
                width: 100%;
                padding: 50px;
                text-align: right;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

    add_bg_from_local('images/Untitled.jpeg')

    # Function to add logo to top-right corner
    def add_logo_to_home_page(logo_path):
        # Open the logo file
        with open(logo_path, "rb") as logo_file:
            # Encode the logo file to base64
            encoded_logo = base64.b64encode(logo_file.read()).decode('utf-8')

        # Add HTML to display the logo in the top-right corner
        st.markdown(
            f"""
            <div style="position: absolute; top: 0px; right: 0px; z-index: 999;">
                <img src='data:image/png;base64,{encoded_logo}' alt="logo" width="200" height="200">
            </div>
            """,
            unsafe_allow_html=True
        )

    add_logo_to_home_page('images/sympto-logo.png')

inject_custom_css()


def title_component():
    title_html = '''
        <div class="title">
            <h1 class="custom-title" style= "color: white;">SymptoSense: Unveiling Health Tomorrow, Today – Your Personal Medical Guide</h1>
        </div>
    '''
    st.markdown(title_html, unsafe_allow_html=True)

# sidebar for navigation
with st.sidebar:    
    selected = option_menu('SymptoSense',
                           ['Home', 'General Checkup','Check for Diabetes', 'Check for Heart Disease','Med-Blog', 'About Us', 'Contact Us'],
                           menu_icon='hospital-fill',
                           icons=['house', 'activity', 'thermometer','heart','book','mask', 'phone'],
                           default_index=0)
    # Home button
    st.sidebar.markdown('---')
    st.markdown('''<p style="color:white;">A Project Work by DBDA-10.</p>''',unsafe_allow_html=True)

    st.markdown('''<p style="color:white;">© 2024 Centre of Development of<br> Advanced Computing (C-DAC).<br>All rights reserved.</p>''',unsafe_allow_html=True)



if selected == 'Home':
    st.write(' ')
    st.markdown('   ')

    para_html = '''
            <div class="bg-image"></div>

            <div class="bg-text">
                <h1 class="custom-title" style= "color: white;">SymptoSense: Unveiling Health Tomorrow, Today – Your Personal Medical Guide</h1>
                <p class="custom-para" style="text-align:justify; text-indent: 40px; padding-left: 60px; color: white; font-size: 24px"> Welcome to SymptoSense, your innovative and personalized medical guide designed to unveil health insights for a better tomorrow, today. SymptoSense empowers users to explore and understand their health through a comprehensive suite of features. From a Symptom Checker helping you assess and understand potential health issues, to an extensive MedBlog providing information on various diseases, our app is your one-stop destination for health-related queries. Connect with us through the Contact Us form for personalized assistance and delve into the story behind SymptoSense in our About Us section. Join us in this journey toward informed health decisions, where SymptoSense becomes your trusted companion in navigating the complexities of well-being</p>
            </div>
            <div class="para"><p class="custom-para" style="text-align:bottom; text-indent: 70px; position: absolute; bottom: 0; padding-left: 200px; color: white; font-size: 18px"> Your Personal Medical Guide. A Medical Suggestion and Remote Generation System.</p></div>
    '''
    st.markdown(para_html, unsafe_allow_html=True)
    st.markdown("       ")
    st.markdown('---')
    #st.markdown('<div class="para"><p class="custom-para" style="text-align:center; text-indent: 70px; position: absolute; bottom: 100; padding-left: 100px; color: white; font-size: 18px"> Your Personal Medical Guide. A Medical Suggestion and Remote Generation System.</p></div>', unsafe_allow_html=True)


if selected == 'General Checkup':
    symptom_checker.symptomcheck()

# Diabetes Prediction Page
if selected == 'Check for Diabetes':
    diabetes.diabetes_check(diabetes_model)        
    
# Heart Disease Prediction Page
if selected == 'Check for Heart Disease':
    heart.heart_check(heart_disease_model)

if selected == 'Med-Blog':
    medblog.medblog_page()

if selected == 'About Us':
    about_us.about_us_page()

if selected == 'Contact Us':
    contact_us.load_view()
