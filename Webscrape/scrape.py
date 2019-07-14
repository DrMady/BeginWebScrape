# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

data = []

page = 'https://www.indeed.fr/jobs?q=developpeur%20web&l=%C3%8Ele-de-France&jt=apprenticeship&sort=date&vjk=bf5d8a0984962637'
parsedPage = urlopen(page)

soup = BeautifulSoup(parsedPage, 'html.parser')
links = soup.findAll('div', attrs={'class': 'result'})

for offer in links:
    childTitle = offer.findChildren('a', recursive=True)
    childCompanies = offer.findChildren('span', attrs={'company'}, recursive=True)
    for child in childTitle:
        title = child.text
        for company in childCompanies:
            companyName = company.text

            if "developpeur" in title.lower():
                print(title)
                print(companyName)
            if "développeur" in title.lower():
                print(title)
                print(companyName)
            if "Alternance Développeur Web H/F" in title:
                print(title)
                print(companyName)
