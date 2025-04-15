# 🚀 NASA APOD Archive Headings Scraper

This Python script scrapes all the `<b>` tag headings from the [NASA Astronomy Picture of the Day (APOD) archive page](https://apod.nasa.gov/apod/archivepix.html) and stores the results in a pandas DataFrame. It also displays the page title and provides an optional feature to export the data to an Excel file.

## 📌 Features

- Extracts all bold (<b>) tag text from the APOD archive.
- Uses requests and BeautifulSoup for web scraping.
- Displays the page title and a preview of the scraped data.
- Stores results in a pandas DataFrame.
- (Optional) Save to Excel or CSV.

## 🛠️ Requirements

- Python 3.x
- pandas
- beautifulsoup4
- requests

Install them with:

'''bash
pip install pandas beautifulsoup4 requests

📝 Output
Prints the title of the page.

Displays a preview of the headings scraped from the archive.
