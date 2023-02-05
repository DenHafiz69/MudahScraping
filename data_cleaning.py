import re
import pandas as pd

# import the csv file

df = pd.read_csv("housing_price_data.csv")

# define some functions to clean the price, size, and no of bedroom

def extract_price(text):
  return int(text[3:-10].replace(" ", ""))

def extract_size(text):
  return int(text[:-7])

def extract_bed(text):
  return int(text[0:1])

# convert all the data from strings with unnecessary text into integers

if df['price'].dtype == str: # check whether data has been converted or not
  df['price'] = df['price'].apply(extract_price)
  df['price'] = df['size'].apply(extract_size)
  df['price'] = df['bedroom'].apply(extract_bed)

# save the modified DataFrame back to the CSV file

df.to_csv("housing_price_data.csv", index=False)