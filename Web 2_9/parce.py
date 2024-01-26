import requests
import json
import os
from bs4 import BeautifulSoup
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker



def parse_data():

    url = 'http://quotes.toscrape.com'
    html_doc = requests.get(url)
    to_file_authors = []
    to_file_quotes = []

    if html_doc.status_code == 200:
        soup = BeautifulSoup(html_doc.content, 'html.parser')
        quots = soup.find_all('div', attrs={'class': 'quote'})
        for quot in quots:

            soup_about = quot.find('a')['href']

            tgs = []
            dict_quotes = {}

            author = quot.find('small').text
            say = quot.find('span', attrs={'class': 'text'}).text.strip('\u201c\u201d')
            tags=quot.find_all('a', attrs={'class': 'tag'})
            
            for tag in tags:
                tgs.append(tag.text)

            dict_quotes['tags'] = tgs
            dict_quotes['author'] = author
            dict_quotes['quote'] = say
            to_file_quotes.append(dict_quotes)

            to_file_authors.append(parse_about_data(soup_about))

    return to_file_authors, to_file_quotes

def parse_about_data(about_url):
    url = 'http://quotes.toscrape.com/' + about_url
    html_doc = requests.get(url)
    if html_doc.status_code == 200:
        dict_authors = {}

        soup = BeautifulSoup(html_doc.content, 'html.parser')
        quots = soup.find('div', attrs={'class': 'author-details'})
        
        author = quots.find('h3', attrs={'class': 'author-title'}).text
        born_date = quots.find('span', attrs={'class': 'author-born-date'}).text
        born_location = quots.find('span', attrs={'class': 'author-born-location'}).text
        description = quots.find('div', attrs={'class': 'author-description'}).text.strip('\n').strip()
        
        dict_authors['fullname'] = author
        dict_authors['born_date'] = born_date
        dict_authors['born_location'] = born_location
        dict_authors['description'] = description
    
    return dict_authors
        

if __name__ == '__main__':
    to_file_authors, to_file_quotes = parse_data()
    to_file_a = json.dumps(to_file_authors, indent=4, sort_keys=True)
    to_file_q = json.dumps(to_file_quotes, indent=4, sort_keys=True)

    if os.path.exists("Web 2_9/parce.py"):
        path_a = os.getcwd() + '\\Web 2_9\\authors.json'
        path_q = os.getcwd() + '\\Web 2_9\\quotes.json'
    elif os.path.exists("parce.py"):
        path_a = 'authors.json'
        path_q = 'quotes.json'

    with open(path_a, 'w') as file:
        file.write(to_file_a)
    with open(path_q, 'w') as file:
        file.write(to_file_q)
