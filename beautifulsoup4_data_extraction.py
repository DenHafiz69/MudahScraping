from bs4 import BeautifulSoup
import requests
from csv import writer

# function to change url to next page

def url_func(page):
  return "https://www.mudah.my/kuala-lumpur/apartment-condominium-for-rent?o=" + page

# definition of classes in case it does not work again, need to change here

main_class = "sc-cQFLBn jkvPib"
title_class = "sc-fYiAbW infEfr"
price_class = "sc-gHboQg jzKDEN"
location_class = "sc-gqPbQI jcysAz"
outer_class = "sc-eerKOB kYoUWg"
inner_class = "sc-emmjRN jodtUm"

with open('housing.csv', 'w', encoding='utf8', newline='') as f:

  thewriter = writer(f)
  header =['Title', 'Price', 'Location', 'Size', 'Bedroom']

  thewriter.writerow(header)

  for reps in range(1, 20):

    url = url_func(str(reps))
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