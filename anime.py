# import requests
# from rauth.service import OAuth2Service
# import json
# class mal:
#     def __init__(self, client_id, client_secret):
#         self.access_token = None
#     def get_access_token(self):
#         data = {'code': 'bar',
#                 'grant_type': 'client_credentials',
#                 'redirect_uri': 'https://api.myanimelist.net/v2'}
#         session = self.service.get_auth_session(data=data, decoder=json.loads)
#         self.access_token = session.access_token
# cid='658f184e4718cff8b149634bad83562a'
# csecret='4807a0e7f604ea408b570aca7e6372ff6313844a16ef66c45778ebf0f307d977'
# m = OAuth2Service(
#         client_id=cid,
#         client_secret=csecret,
#         name='mal',
#         authorize_url='https://myanimelist.net/v1/oauth2/authorize',
#         access_token_url='https://myanimelist.net/v1/oauth2/access_token',
#         base_url='https://myanimelist.net/v2')
# data = {'code': 'bar',
#                 'grant_type': 'client_credentials',
#                 'redirect_uri': 'https://api.myanimelist.net/v2'}
# session = m.get_auth_session(data=data)
# #print('Visit this URL in your browser: ' + m.get_authorize_url())
#     # This is a bit cumbersome, but you need to copy the code=something (just the
#     # `something` part) out of the URL that's redirected to AFTER you login and
#     # authorize the demo application
# #code = input('Enter code parameter (code=something) from URL: ')
#     # create a dictionary for the data we'll post on the get_access_token request
# #data = dict(code=code, redirect_uri='https://github.com/litl/rauth/')
#     # retrieve the authenticated session
# #session = github.get_auth_session(data=data)
#     # make a request using the authenticated session
# user = session.get('user').json()
# print('currently logged in as: ' + user['login'])
# # mal=mal(cid,csecret)
# # mal.access_token()
# # print(mal.access_token)
# url='https://api.myanimelist.net/v2/anime/1'
# result=requests.get(url,auth=(cid,csecret),)
# print(result)

import json
import time
import requests
from bs4 import BeautifulSoup
url="https://myanimelist.net/sitemap/anime-000.xml"
links=[]
id=[]
page=requests.get(url).text
soup = BeautifulSoup(page,features="lxml")
for a in soup.find_all('loc'):
  links.append(a.string)
  id.append(a.string[30:30+a.string[30:].index('/')])
from googlesearch import search
from mal._anime import Anime
import csv
def searchTrailer(query):
    for j in search(query + "anime trailer youtube", num_results=1):
        return j

filename = "anime1.csv"
with open(filename, 'a',newline='') as csvfile:
    temp = csv.writer(csvfile)
    #temp.writerow(['mid', 'title', 'rating', 'rank', 'type', 'genre', 'rdate', 'language', 'cover', 'description', 'trailer', 'released', 'year'])
    for i in range(157,250):
        try:
            anime = Anime(int(i),timeout=41)
            trailer = searchTrailer(anime.title)
            if trailer != None:
                continue
            else:
                trailer='Null'
            print([anime.mal_id,anime.title,anime.rating,anime.rank,'anime',json.dumps(anime.genres),anime.premiered,json.dumps(["Japanese"]),anime.image_url,anime.synopsis,trailer,"TRUE",anime.aired])
            time.sleep(0.5)
            temp.writerow([anime.mal_id,anime.title,anime.rating,anime.rank,'anime',json.dumps(anime.genres),anime.premiered,json.dumps(["Japanese"]),anime.image_url,anime.synopsis,trailer,"TRUE",anime.aired])
        except ValueError:
            print(i,'ValueError: No such id on MyAnimeList')
            time.sleep(0.5)
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# options = Options()
# options.headless = True
# options.add_argument("--window-size=1920,1200")
# driver = webdriver.Chrome(r'C:\Users\USER\Downloads\Compressed\chromedriver.exe',options=options)
# driver.get(url)