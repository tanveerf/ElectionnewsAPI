import streamlit as st
import requests

# Streamlit webpage layout
st.title('Election News in Bangladesh - Daily Star, TBS, New Age, BdNews, Prothom Alo')

# Endpoint of your Node.js API
api_url = 'https://bdelectionnews.b4a.app/electionnews'

# Fetching data from the Node.js API
try:
    response = requests.get(api_url)
    if response.status_code == 200:
        news_data = response.json()
        if news_data:
            for item in news_data:
                st.subheader(item.get('title', 'No Title'))
                st.write(f"URL: {item.get('url', 'No URL')}")
                st.write(f"Keyword: {item.get('keyword', 'No Keyword')}")
                st.write(f"Source: {item.get('site', 'No Source')}")
                st.write("---")
        else:
            st.write("No news data found.")
    else:
        st.error(f"Failed to retrieve data: HTTP Status Code {response.status_code}")
except Exception as e:
    st.error(f"An error occurred: {e}")
