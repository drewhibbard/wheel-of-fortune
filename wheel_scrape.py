'''
Module that scrapes wheeloffortuneanswer.com for every puzzle (~80,000) in their database.
You only have to put through 50 http requests to get all of them so don't feel bad.
'''


import requests
from bs4 import BeautifulSoup


def get_links():
    '''
    Get links to each puzzle category sub-page, from the home page.
    '''

    page = requests.get('https://wheeloffortuneanswer.com/')
    soup = BeautifulSoup(page.content)
    table = soup.find_all('td',class_='column-1')

    links = []
    for item in table:
        link = item.find('a').get('href')
        links.append(link)

    return links

def get_puzzles(links):
    '''
    Using the links from get_links, get all puzzles for that category.
    '''
    
    puzzles = []

    for link in links:
        page = requests.get(link)
        soup = BeautifulSoup(page.content)
        table = soup.find_all('td',class_='column-1')
        category = soup.find('th').text
        
        for item in table:
            d = {}
            puzzle = item.text
            d['category'] = category
            d['puzzle'] = puzzle
            puzzles.append(d)

    return puzzles