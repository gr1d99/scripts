import csv
import requests
from BeautifulSoup import BeautifulSoup
import unicodedata


def scrape():

    url = 'http://localhost:90/locations.html'
    response = requests.get(url)
    html = response.content

    soup = BeautifulSoup(html)
    select = soup.find('select')

    location_list = []

    for opt in select.findAll('option'):
        location_list.append(opt.text)

    with open('./locations.txt', 'wb') as location_file:
        location_file.write("\n".join("('{}','{}'),".format(loc, loc) for loc in location_list))

scrape()