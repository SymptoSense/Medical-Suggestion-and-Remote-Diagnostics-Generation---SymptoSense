import streamlit as st
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define a custom CSS style
custom_style = """
<style>
    .contact-us-label {
        color: white !important;
        font-weight: bold;
        padding: 5px;
    }

    .contact-us-input {
        color: white !important;
        background-color: black !important;
        padding: 8px;
        border: 1px solid white !important;
    }

</style>
"""

# Inject the custom style
st.markdown(custom_style, unsafe_allow_html=True)

def create_contact_us_table():
    connection = sqlite3.connect("contact_us.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contact_us (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            message TEXT
        )
    """)
    connection.commit()
    connection.close()

def store_data_in_database(name, email, message):
    connection = sqlite3.connect("contact_us.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO contact_us (name, email, message) VALUES (?, ?, ?)", (name, email, message))
    connection.commit()
    connection.close()

def send_email(name, email, message):
    # Replace these with your actual email credentials
    sender_email = "medhasingh0204@gmail.com"
    sender_password = "dbxl xajq qnzp ajtg"
    receiver_email = "lokeshdongre17@gmail.com"

    subject = "New Contact Us Submission"

    # Email body
    body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

    message = MIMEMultipart()
    message.attach(MIMEText(body, "plain"))
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def load_view():
    title_html = '''
        <div class="title">
            <h1 class="custom-title" style="color: white;">CONTACT US</h1>
        </div>
    '''
    st.markdown(title_html, unsafe_allow_html=True)

    # Create database table if not exists
    create_contact_us_table()

    # Form to collect user data
    st.markdown('<div class="contact-us-label" style="color:white">Your Name</div>', unsafe_allow_html=True)
    name = st.text_input("", key="name_input")

    st.markdown('<div class="contact-us-label" style="color:white">Your Email</div>', unsafe_allow_html=True)
    email = st.text_input("", key="email_input")

    st.markdown('<div class="contact-us-label" style="color:white">Your Message</div>', unsafe_allow_html=True)
    message = st.text_area("", key="message_input", height=200)

    # Center both buttons
    st.markdown('<div style="display: flex; justify-content: center;">', unsafe_allow_html=True)

    # Create "Submit" button
    submit_button = st.button("Submit")

    # Create "Refresh" button
    refresh_button = st.button("Refresh")

    st.markdown('</div>', unsafe_allow_html=True)

    # Process form submission
    if submit_button:
        # Store data in the database
        store_data_in_database(name, email, message)

        # Send email notification
        send_email(name, email, message)

        st.success("Your message has been submitted. We'll get back to you soon!")

    # Process refresh button
    if refresh_button:
        # Clear text boxes
        st.experimental_rerun()

    st.markdown('---')
    st.markdown('<div class="para"><p class="custom-para" style="text-align:bottom; text-indent: 70px; position: absolute; bottom: 0; padding-left: 200px; color: white; font-size: 18px border-top: 2px solid white; padding-top: 10px;"> Your Personal Medical Guide. A Medical Suggestion and Remote Generation System.</p></div>',
                unsafe_allow_html=True)
    st.markdown('  ')
    st.markdown('  ')
    st.markdown('<div class="para"><p class="custom-para" style="text-align:bottom; text-indent: 40px; position: absolute; bottom: 0; padding-left: 200px; color: white; font-size: 18px "> © 2024 Centre of Development of Advanced Computing (C-DAC). All rights reserved.</p></div>',
                unsafe_allow_html=True)
    
# Uncomment the line below if you want to test the Contact Us form
# load_view()
