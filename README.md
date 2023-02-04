# Housing Price Data Project

This project focuses on collecting and cleaning housing price data from the website mudah.my using Python and its libraries such as Beautiful Soup and Pandas.

## File Descriptions

* beautifulsoup4_data_extraction.py: Contains the code for web scraping the website using Beautiful Soup library. The data collected includes the name of the housing listing, price, location, size, and the number of bedrooms.
* pandas_data_cleaning.py: Contains the code for cleaning the collected data using pandas.
* housing_price_data.csv: The output file from the web scraping code. It contains the cleaned and organized housing price data.

## Getting Started

To run the code, make sure you have the following libraries installed:

* Beautiful Soup
* Pandas

You can install the libraries by running the following command in your terminal:

```python
pip install beautifulsoup4 pandas
```

After installing the libraries, simply run the beautifulsoup4_data_extraction.py file first to collect the data, and then run the pandas_data_cleaning.py file to clean and organize the data. The cleaned data will be stored in the housing_price_data.csv file.