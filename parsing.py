import urllib.request

from bs4 import BeautifulSoup

tracking = 'np00000000866099npi'
url = 'https://novaposhta.ua/tracking/international/cargo_number/{}'.format(tracking)

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse(html):
    soup = BeautifulSoup(html)
    table = soup.find('table', class_="tracking-int")

    # current_status
    for row in table.find_all('tr')[1:]:
        current_status = row.find_all('td')

    #history_status
    history_statuses = soup.find('tbody', class_="spoiler-content")
    history_statuses.find_all('tr')[1:]
        #history_status = status.find_all('td')


    print(current_status)
    print('__________________________')
    print(history_statuses)




def main():
    parse(get_html(url))

if __name__ == '__main__':
    main()





