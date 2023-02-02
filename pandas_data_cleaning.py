import re
import pandas as pd

# import the csv file

df = pd.read_csv("housing.csv")

# define some functions to clean the price, size, and no of bedroom

def extract_price(text):
  return int(text[3:-10].replace(" ", ""))

def extract_size(text):
  return int(text[:-7])

def extract_bed(text):
  return int(text[0:1])

# convert all the data from strings with unnecessary text into integers

df['Price'] = df['Price'].apply(extract_price)
df['Size'] = df['Size'].apply(extract_size)
df['Bedroom'] = df['Bedroom'].apply(extract_bed)