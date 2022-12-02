import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Music'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

citation = 'citation needed'
results = soup.find_all(text=citation)


def get_citations_needed_count():
    print('citations needed: ', len(results))
    print(' ')
    return len(results)


def get_citations_needed_report():
    for txt in results:
        citation_parent = txt.find_parent('p')
        txt_split = citation_parent.text.split()
        print(' '.join(txt_split))
        print(' ')


if __name__ == '__main__':
    get_citations_needed_count()
    get_citations_needed_report()
