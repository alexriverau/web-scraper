import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Music'
page = requests.get(URL)
# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)

results = soup.find(class_='noprint Inline-Template Template-Fact')
# print(results.prettify())

citations_needed = results.find_all('i')
# print(citations_needed)

anchors = results('a')
# print(anchors)


def get_citations_needed_count():
    print('Total citations needed: ', len(citations_needed))
    return len(citations_needed)


def get_citations_needed_report():
    pass


if __name__ == '__main__':
    get_citations_needed_count()

