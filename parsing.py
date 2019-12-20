import urllib.request
from bs4 import BeautifulSoup

tracking = 'np00000000866099npi'
url = 'https://novaposhta.ua/tracking/international/cargo_number/{}'.format(tracking)


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def parse(html):
    soup = BeautifulSoup(html)
    table = soup.find('table', class_="tracking-int").find_all('tr')

    for row in table:
        columns = row.find_all('td')
        if columns:
            print(columns[0].text + ' --- ' + columns[1].text + ' --- ' + columns[2].text)


def main():
    parse(get_html(url))


if __name__ == '__main__':
    main()
