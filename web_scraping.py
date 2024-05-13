from bs4 import BeautifulSoup
import requests
from csv import writer

# Function to change url to next page

def new_page_url(page):
  '''A function to get the next page url

  Parameter(s)
  ----------
  page : int
    The page number intended to go
  
  Returns
  -------
  url : str
    The new url to load
  '''

  return "https://www.mudah.my/kuala-lumpur/apartment-condominium-for-rent?o=" + page

# Definition of classes in case it does not work again, need to change here

main_class = "sc-cQFLBn jkvPib"
title_class = "sc-fYiAbW infEfr"
price_class = "sc-gHboQg jzKDEN"
location_class = "sc-gqPbQI jcysAz"
outer_class = "sc-eerKOB kYoUWg"
inner_class = "sc-emmjRN jodtUm"

# Maximum pages that want to be travelled
max_page = 20

with open('housing_price_data.csv', 'w', encoding='utf8', newline='') as f:

  thewriter = writer(f)
  header =['title', 'price', 'location', 'size', 'bedroom']

  thewriter.writerow(header)

  for reps in range(1, max_page):

    url = new_page_url(str(reps))
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    lists = soup.find_all('div', {"class": main_class})

    for i in lists:

      title = i.find('a', {"class": title_class}).text
      price = i.find('div', {"class": price_class}).text
      location = i.find('span', {"class": location_class}).text
      sqft = i.find('div', {"class": outer_class}).find('div', {"class": inner_class, "title": "Size"}).text
      bedroom = i.find('div', {"class": outer_class}).find('div', {"class": inner_class, "title": "Bedrooms"}).text

      info = [title, price, location, sqft, bedroom]

      thewriter.writerow(info)