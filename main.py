import requests
import urllib3
from bs4 import BeautifulSoup

def main():
    urllib3.disable_warnings()
    cookies = {
        'PYPF': '3OyMLS2-xJlxKilWEOSvMQXAhyCgIhvAxYfbB8S_5lGBxxAS18Z7I8Q',
        '_ga': 'GA1.2.227320333.1496647453',
        '_gat': '1',
        '_gid': 'GA1.2.75815641.1496647453'
    }
    params = {
        'platform': 'xbox'
    }
    page = requests.get("http://www.rl-trades.com/#pf=xbox", headers={'Platform': 'Xbox'}, verify=False, cookies=cookies, params=params).text
    page
    soup = BeautifulSoup(page, 'html.parser')
    #print(soup.prettify())
    tag = soup.td
    type(tag)
    tag.name = "td"
    print(soup.prettify())
main()