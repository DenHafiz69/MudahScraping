from bs4 import BeautifulSoup

with open("index.html") as fp:
    soup = BeautifulSoup(fp)

url = "https://www.mudah.my/kuala-lumpur/apartment-condominium-for-rent?q=studio"

