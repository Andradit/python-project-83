from bs4 import BeautifulSoup


def parse_page(page: str):
    result = {}
    soup = BeautifulSoup(page, 'html.parser')
    if soup.title:
        result['title'] = soup.title.string
    else:
        result['title'] = ''
    if soup.find('h1'):
        result['h1'] = soup.find('h1').string
    else:
        result['h1'] = ''
    if soup.find('meta', attrs={'name': 'description'}):
        result['description'] = soup.find(
            'meta', attrs={'name': 'description'})['content']
    else:
        result['description'] = ''
    print(soup.prettify())
    return result