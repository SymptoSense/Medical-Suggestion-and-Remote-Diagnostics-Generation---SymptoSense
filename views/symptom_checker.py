import os
import pickle
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

import base64
from streamlit_option_menu import option_menu

# Set page configuration
def symptomcheck():
        current_directory = os.getcwd()

        title_html = '''
            <div class="title">
                <h1 class="custom-title" style= "color: white;padding-top: 10px;">Check your symptoms</h1>
            </div>
            '''
        st.markdown(title_html, unsafe_allow_html=True)

        # Creating a DataFrame

       # csv_relative_path = os.path.relpath(r'../dataset/symptom_checker.csv', current_directory)
        #print("sadneep path", csv_relative_path, "current", current_directory)
        #df = pd.read_csv(csv_relative_path)
        df = pd.read_csv(r'views/symptom_checker.csv')
    # Preprocessing: Split the symptoms and replace underscores with spaces
        df['Symptoms'] = df['Symptoms'].str.replace('_', ' ').str.split(',')

    # Create a pipeline with CountVectorizer and Multinomial Naive Bayes
        model = make_pipeline(CountVectorizer(tokenizer=' '.join, preprocessor=' '.join), MultinomialNB())

    # Fit the model
        model.fit(df['Symptoms'].apply(' '.join), df['Disease'])


    # Preprocessing
    # df['symptoms'] = df['symptoms'].apply(lambda x: x.replace('_', ' ').split(','))
        st.markdown('  ')

    # Dropdown for selecting symptoms
        selected_symptoms = st.multiselect("Select Symptoms", df['Symptoms'].explode().unique())

        if st.button("Predict"):
            input_symptoms = ' '.join(selected_symptoms)
            predicted_probabilities = model.predict_proba([input_symptoms])
            
            # Sort predictions by probability in descending order
            sorted_predictions = sorted(zip(model.classes_, predicted_probabilities[0], df[df['Disease'].isin(model.classes_)]['Cures']), key=lambda x: x[1], reverse=True)
            
            # Display the top 5 predictions
            st.success("Top 5 predicted diseases, probabilities, and cures:")
            for Disease, probability, Cures in sorted_predictions[:5]:
                st.write(f"{Disease}: {probability*100:.2f}% - Cures: {Cures}")

        st.markdown('---')
        st.markdown('  ')
        # Footer
        st.markdown('''
                <div class="para"><p class="custom-para" style="text-align:bottom; text-indent: 70px; position: absolute; bottom: 0; padding-left: 200px; color: white; font-size: 18px border-top: 2px solid white; padding-top: 10px;"> Your Personal Medical Guide. A Medical Suggestion and Remote Generation System.</p></div>''',
                unsafe_allow_html=True)
        st.markdown('  ')
        st.markdown('  ')
        st.markdown('''
                <div class="para"><p class="custom-para" style="text-align:bottom; text-indent: 40px; position: absolute; bottom: 0; padding-left: 200px; color: white; font-size: 18px "> © 2024 Centre of Development of Advanced Computing (C-DAC). All rights reserved.</p></div>''',
                unsafe_allow_html=True)




