import streamlit as st
import webbrowser
import base64


# Sample list of diseases with corresponding Wikipedia links
diseases = {
    'Cancer': 'https://en.wikipedia.org/wiki/Cancer',
    'Diabetes': 'https://en.wikipedia.org/wiki/Diabetes',
    'Asthama': 'https://en.wikipedia.org/wiki/Asthama',
    'Malaria': 'https://en.wikipedia.org/wiki/Malaria',
    'Pneumonia': 'https://en.wikipedia.org/wiki/Pneumonia',
    'Influenza': 'https://en.wikipedia.org/wiki/Influenza',
    'Schizophrenia': 'https://en.wikipedia.org/wiki/Schizophrenia',
    'Diarrhea': 'https://en.wikipedia.org/wiki/Diarrhea',
    'Coronavirus': 'https://en.wikipedia.org/wiki/Coronavirus',
    'Tuberculosis': 'https://en.wikipedia.org/wiki/Tuberculosis',
    'Hepatitis A': 'https://en.wikipedia.org/wiki/Hepatitis A',
    'Alzheimer': 'https://en.wikipedia.org/wiki/Alzheimer',
    # Add more diseases and links as needed
}

def medblog_page():
    # Apply custom styles using HTML and Streamlit
    custom_style = """
        <style>
            .medblog-title {
                color: white !important;
                text-align: center !important;
                font-size: 24px !important;
            }
            .medblog-text {
                color: white !important;
                font-size: 18px !important;
            }
            .explore-button {
                color: white !important;
                background-color: black !important;
                padding: 8px !important;
                border: 1px solid white !important;
                border-radius: 5px !important;
            }
        </style>
    """
    st.markdown(custom_style, unsafe_allow_html=True)

    title_html = '''
        <div class="title" style="border-bottom: 2px solid white; padding-bottom: 10px;">
            <h1 class="custom-title" style="color: white;text-align:center;"><em>MEDICAL BLOG : Know about Diseases before the Disease knows you !</em></h1>
        </div>
    '''
    st.markdown(title_html, unsafe_allow_html=True)

    para_html = '''
        <div style="color: white; font-size: 24px; line-height: 1.6; text-align: center;">
            <p style="text-align:center;"><br>
                <strong>Welcome to MedBlog! Select a disease to learn more from Wikipedia.</strong>
            </p>
        </div>
    '''
    st.markdown(para_html, unsafe_allow_html=True)

    selected_disease = st.selectbox("Choose a Disease", list(diseases.keys()))

    explore_button = st.button("Explore", key="explore_button")

    
    if explore_button:
        # st.success(f"Redirecting to Wikipedia page for {selected_disease}...")
        webbrowser.open(diseases[selected_disease])
    

    st.markdown('  ')
    good_health_text = '''
        <div style="color: white; font-size: 18px; line-height: 1.6; text-align: justify;">
            <p>
                "Good health is the key to unlocking the full potential of life. It serves as the foundation for a vibrant and fulfilling existence, empowering individuals to pursue their aspirations, engage in meaningful relationships, and contribute actively to society. With good health, one can experience the richness of life's joys and navigate its challenges with resilience. It is the cornerstone for personal growth, productivity, and a high quality of life. Embracing a proactive approach to well-being becomes the gateway to unlocking the doors of opportunity and achieving a balanced and purposeful life."
            </p>
        </div>
    '''
    st.markdown(good_health_text, unsafe_allow_html=True)
    st.markdown('  ')
# Test the modified medblog_page

# Test the modified me
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