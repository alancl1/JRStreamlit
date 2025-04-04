import streamlit as st
import pandas as pd
import random
import string
#from PIL import Image
#import streamlit.components.v1 as components
import sqlite3


# Read CSV files
#jeepNews = pd.read_csv('rss-app-csv-2024-11-03.csv')
#jeepEvents = pd.read_csv('JeepRallyEvents.csv')

# Layout
st.title("JeepRally.com")
st.subheader("Find your next Jeep® adventure!")
st.subheader("Latest News and Event Listings:")

st.divider()

#st.header("Latest News:")

# Function to display news
#def display_news(row):
#    st.subheader(row["Title"])
#    col1, col2 = st.columns([3, 1])
#    with col1:
#        st.caption(f"Date: {row['Date']}")
#        st.caption(f"News provided by: {row['Author']}")
#        st.write(row["Plain Description"])
#        with st.expander("Read more..."):
#            st.caption(f"Date: {row['Date']}")
#            st.caption(f"News provided by: {row['Author']}")
#            st.write(row["Plain Description"])
#            st.caption(row["Link"])
#    with col2:
#        image_url = row["Image"]
#        try:
#            st.image(image_url, caption=image_url)
#            st.write("image caption here...")
#        except Exception as e:
#            st.error(f"Error loading image: {e}")
#    st.write("")
#    st.write("")
#    st.divider()
#    st.write("")

# Display news
#for index, row in jeepNews.iterrows():
#    display_news(row)

#st.divider()
#st.write('© 2010-2020 JeepRall.com | Add-ons © by ©')
#st.write('Terms of use  Sponsors  Contact us  Terms of Service / DMCA Policy  Privacy policy  Help  Home')
#st.divider()




# Connect to SQLite database
conn = sqlite3.connect('JeepRallyPostsJan2025.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS entries
             (id INTEGER PRIMARY KEY, url TEXT, author TEXT, date TEXT, title TEXT, 
              short_description TEXT, body TEXT, image_link TEXT, rating REAL)''')
conn.commit()

# Function to fetch entries from the database
def fetch_entries():
    c.execute("SELECT * FROM entries")
    rows = c.fetchall()
    return rows

# Streamlit app
#st.title("Blog Posts Viewer")

# Fetch entries from the database
entries = fetch_entries()

# Convert entries to a DataFrame for easier display
df = pd.DataFrame(entries, columns=['ID', 'URL', 'Author', 'Date', 'Title', 'Short Description', 'Body', 'Image Link', 'Rating'])

# Display individual blog posts
for index, row in df.iterrows():
    st.write(f"## {row['Title']}")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(f"**Author:** {row['Author']}")
        st.write(f"**Date:** {row['Date']}")
        st.write(f"**Short Description:** {row['Short Description']}")
        with st.expander("Read more..."):
            st.write(f"**Body:** {row['Body']}")
            st.write(f"**URL:** {row['URL']}")
            st.write(f"**Rating:** {row['Rating']}")
    with col2:
        if row['Image Link']:
            st.image(row['Image Link'], use_container_width=True)
            st.caption(row['Image Link'])
    st.write("---")

# Close the database connection
conn.close()

# Footer
st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding: 10px;
    }
    </style>
    <div class="footer">
        <p>Follow us on:
            <a href="https://twitter.com" target="_blank">Twitter</a> |
            <a href="https://facebook.com" target="_blank">Facebook</a> |
            <a href="https://rumble.com/user/JeepRally" target="_blank">Rumble</a> |
            <a href="https://Telegram.com" target="_blank">Telegram</a> |
            <a href="https://truthsocial.com/jeeprally" target="_blank">Truthsocial</a> |
            <a href="https://instagram.com" target="_blank">Instagram</a> |
            <a href="https://instagram.com" target="_blank">Terms of use</a> |
            <a href="/about-us" target="_blank">About Us</a> |
            <a href="/Terms" target="_blank">Terms of use</a> |
            <a href="/affiliate" target="_blank">Affiliate</a>
        </p>
        <p>When you click on an affiliate link on our site and make a purchase, we may receive a commission from the retailer at no additional cost to you. 
    This helps support our site and allows us to continue providing valuable content. 
    We only recommend products and services that we believe will add value to our readers.</p>
    </div>
    """, unsafe_allow_html=True)


