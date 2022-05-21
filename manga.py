import time
import requests
from bs4 import BeautifulSoup
url="https://myanimelist.net/sitemap/manga-000.xml"
links=[]
id=[]
page=requests.get(url).text
soup = BeautifulSoup(page,features="lxml")
for a in soup.find_all('loc'):
  links.append(a.string)
  id.append(a.string[30:30+a.string[30:].index('/')])
from googlesearch import search
from mal._manga import Manga
import json
import csv
def searchTrailer(query):
    for j in search(query + "anime trailer youtube", num_results=1):
        return j
filename = "manga.csv"
with open(filename, 'a',newline='') as csvfile:
    temp = csv.writer(csvfile)
    #temp.writerow(['mid', 'title', 'rating', 'rank', 'type', 'genre', 'rdate', 'language', 'cover', 'description', 'trailer', 'released', 'year'])
    for i in range(5,250):
        try:
            anime = Manga(int(i),timeout=41)
            trailer = searchTrailer(anime.title)
            if trailer != None:
                continue
            else:
                trailer='Null'
            x=[]
            for i in anime.genres:
                x.append(i[17:])
            print([anime.mal_id,anime.title,anime.score,anime.rank,'manga',json.dumps(x),anime.published,
				   json.dumps(["Japanese"]),anime.image_url,anime.synopsis,trailer,"TRUE",anime.published])
            time.sleep(0.5)
            temp.writerow([anime.mal_id,anime.title,anime.score,anime.rank,'manga',json.dumps(x),
						   anime.published,json.dumps(["Japanese"]),anime.image_url,anime.synopsis,trailer,"TRUE",anime.published])
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