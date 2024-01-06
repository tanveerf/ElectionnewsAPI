import requests
import streamlit as st

api_url = 'https://bdelectionnews.b4a.app/electionnews'

response = requests.get(api_url)
if response.status_code == 200:
    data = response.json()
    # Process and display the data
else:
    st.error(f"Failed to retrieve data: {response.status_code}")
