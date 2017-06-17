import requests #requests library from pip install request(s?) 
import urllib3 #urllib3 from brew install python3 (I think, if not, its pip install urllib3)
from bs4 import BeautifulSoup #IF YOU DON't HAVE ANY OF THESE PACKAGES, GOOGLE HOMEBREW, DOWNLOAD IT, THEN in Terminal, 
                              # brew install python3 and then do brew install pip(3?) or brew install python3 
                              # OR DO THIS vvv (hopefully does everything for u. if this program does not compile after doing this message me.) 
                              # https://stackoverflow.com/questions/20082935/how-to-install-pip-for-python-3-on-mac-os-x
                              # OR DO THIS ^^^ (hopefully does everything for u. if this program does not compile after doing this message me.) 
def main():
    urllib3.disable_warnings() #because RL-Trades is a secured (https rather than http) website 
    cookies = { # YOUR REAL COOKIES STRAIGHT UP FROM GOOGLE CHROME -> INSPECT (ELEMENT) -> APPLICATION -> COOKIES (or something close to this). Need Google Chrome!
        'PYPF': '3OyMLS2-xJlxKilWEOSvMQXAhyCgIhvAxYfbB8S_5lGBxxAS18Z7I8Q', #Exact Copy Paste. http://i.imgur.com/FJp7p9a.jpg
        '_ga': 'GA1.2.227320333.1496647453', #http://i.imgur.com/FJp7p9a.jpg
        '_gat': '1', #http://i.imgur.com/FJp7p9a.jpg
        '_gid': 'GA1.2.75815641.1496647453' #http://i.imgur.com/FJp7p9a.jpg
    }
    params = { #a guess at what probably needs to be passed into params to fix '/#pf=xbox' from not being read...
        'platform': 'xbox' # does not have to be here to work the same as it does. 
    }
    page = requests.get("http://www.rl-trades.com/#pf=xbox", headers={'Platform': 'Xbox'}, verify=False, cookies=cookies, params=params).text
    page # okay above ^ verify = False has to be there, otherwise it doesnt work. verify=False though might be causing the URL to be read as http://www.rl-trades.com rather than http://www.rl-trades.com/#pf=xbox
    soup = BeautifulSoup(page, 'html.parser') # the rest (i.e. headers={'Platform': 'Xbox'}, cookies=cookies, params=params).text does not have to be there to work the same way. 
    #print(soup.prettify()) #uncomment to see what HTML is being read in right here
    tag = soup.td #not needed (tag lines to reference later) 
    type(tag) #not needed
    tag.name = "td" #not needed
    print(soup.prettify()) #print HTML for PC Trades in between <td> and </td> 
main()
