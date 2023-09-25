import streamlit as st
import boto3
from dotenv import load_dotenv
load_dotenv()


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('EG4102')
# Function to create the login page
def login():
    st.title('My Streamlit Login App')
    #st.image('path_to_logo.png', width=200)  # Replace 'path_to_logo.png' with your logo file path

    # Center-align the title and logo
    st.markdown("<h1 style='text-align: center;'>My Streamlit Login App</h1>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center;'><img src='path_to_logo.png' width='200'></div>", unsafe_allow_html=True)

    # Username and Password input fields
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    # Login button
    if st.button('Login'):
        if username == '123' and password == '123':
            st.session_state.login_success = True  # Store login status in session state
            st.experimental_rerun()  # Rerun the app to navigate to the success page

# Function to create the success page
def success():
    st.title('Hello Nurse')  # Replace 'Name' with the user's name
    st.write('Welcome to W@H. Here is your schedule for today:')
    
    # Provide the correct primary key values to retrieve the item
    user_id = 1  # Replace with the actual user ID you want to retrieve
    special_key = 'RTCL183A'  # Replace with the actual special key

    response = table.get_item(
        Key={
            'userId': user_id,  # Convert to string as the primary key is Number
            'specialKey': special_key
        }
    )

    # Check if the item was found
    if 'Item' in response:
        item = response['Item']
        print(response)
        # Access and display the item attributes as needed
        st.write(f'User ID: {item["userId"]}')
        st.write(f'Special Key: {item["specialKey"]}')
        st.write(f'Age: {item["Particulars"]["age"]}')
        st.write(f'DOB: {item["Particulars"]["DOB"]}')
        # Access other attributes and display them similarly
    else:
        st.write('User not found in the DynamoDB table.')



# Check login status using session state
if not hasattr(st.session_state, 'login_success'):
    st.session_state.login_success = False

# Display login or success page based on login status
if not st.session_state.login_success:
    login()
else:
    success()
