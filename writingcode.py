"""
NASA APOD Archive Headings Scraper

This script scrapes all <b> tag headings from the NASA Astronomy Picture of the Day (APOD) archive page
and stores them in a pandas DataFrame. Optionally, it saves the data to an Excel file.

"""

import pandas as pd
from bs4 import BeautifulSoup
import requests
# URL of the APOD archive
url = "https://apod.nasa.gov/apod/archivepix.html"
# Send a GET request to the page
response = requests.get(url)
html_content = response.content
# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")
# Get and print the page title
title = soup.title
print("Page Title:", title.string)
# Find all <b> tags
tags = soup.find_all("b")
# Extract the text content from each <b> tag
headings = [tag.get_text() for tag in tags]
# Create a DataFrame
df = pd.DataFrame(headings, columns=["Headings"])
# Preview the first few rows
print(df.head())



