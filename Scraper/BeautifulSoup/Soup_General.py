import requests
from bs4 import BeautifulSoup


headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 "
            "Safari/537.36 Edge/12.246"}


#terminal based scraping
#params: site to scrape
#return: req(content and meta data) 
#   soup(just content)
def Access_Site(site):
    req = requests.get(site,headers=headers) 
    soup = BeautifulSoup(req.content,'html5lib')
    return req,soup