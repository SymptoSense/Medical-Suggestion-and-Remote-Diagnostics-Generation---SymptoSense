import streamlit as st

def about_us_page():
    title_html = '''
        <div class="title" style="border-bottom: 2px solid white; padding-bottom: 10px;">
            <h1 class="custom-title" style="color: white;">ABOUT US</h1>
        </div>
    '''
    st.markdown(title_html, unsafe_allow_html=True)

    para_html = '''
        <div style="color: white; font-size: 18px; line-height: 1.6; text-align: justify;">
            <p style="text-align:center;"><br>
                <strong>SYMPTOSENSE - A Medical Recommendation and Remote Diagnostic Generation System</strong><br><br>
                Welcome to SymptoSense, your trusted companion in the realm of health and well-being. SymptoSense is a groundbreaking Medical Recommendation and Remote Diagnostic Generation System designed to empower users with personalized health insights.
            </p>
            <h3 style="color: white; font-size: 20px; line-height: 1.6; text-align: justify;text-decoration: underline;">Organization</h3>
            <ul style="color: white; font-size: 20px; line-height: 1.6; text-align: justify;">
                <li><strong>Organization Name:</strong> <strong><bold><em>Centre of Development of Advanced Computing (C-DAC)</em></strong></bold></li>
                <li><strong>Copyright Year:</strong> 2024</li>
                <li><strong>Group No:</strong> DBDA 10</li>
            </ul>
            <h3 style="color: white; font-size: 18px; line-height: 1.6; text-align: justify;text-decoration: underline;">Developer Team</h3>
            <ul>
                <li><em style="font-family: 'Verdana';text-align: justify;"><strong>Sumedha Singh</strong></em></li>
                <li><em style="font-family: 'Verdana';"><strong>Lokesh Dongre</strong></em></li>
                <li><em style="font-family: 'Verdana';"><strong>Gargi Verma</strong></em></li>
                <li><em style="font-family: 'Verdana';"><strong>Mohan Nagrurkar</strong></em></li>
                <li><em style="font-family: 'Verdana';"><strong>Deshmane Aditya Shrikant</strong></em></li>
            </ul>
            <p style="text-align:center;">
                For any inquiries, feel free to reach out to us: <br>
                <strong>Email: sensesympto@gmail.com </strong>
            </p>
            <p style="text-align:center;border-top: 2px solid white; padding-top: 10px;">
                Thank you for choosing SymptoSense as your Personal Medical Guide!
            </p>
        </div>
    '''
    st.markdown(para_html, unsafe_allow_html=True)


