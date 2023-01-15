from bs4 import BeautifulSoup
import requests

url = "https://www.mudah.my/kuala-lumpur/apartment-condominium-for-rent?q=studio"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

the_lists = soup.find_all('div', class_="sc-ksYbfQ eHFZkE")

for i in the_lists:
    title = i.find('a', class_="sc-uJMKN dQixCO")
    location = i.find('span', class_="sc-caSCKo gabJBv")
    price = i.find('div', class_="sc-jnlKLf bhfbqU")
    posted_date = i.find('span', class_="sc-eqIVtm jQMyrz")