import scraper
from bs4 import BeautifulSoup


html = scraper.get_url("https://www.kijiji.ca/b-motorcycles/canada/ninja-300/k0c30l0?price=1000__&dc=true")
soup = scraper.ad(html)
#print(soup)

#for i in range(5):
#    print("---------------------------------------")

#print(soup[2])

for i in range(5):
    print("---------------------------------------")

for i in soup:
   print(scraper.link(i))

#print(soup.prettify())