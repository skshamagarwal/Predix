#import mysql.connector as connector
from googlesearch import search
import imdb
# class PredixDB:
#     def __init__(self, tablename):
#         # Initialize Connection
#         self.con = connector.connect(host='localhost',
#                                      user='predixweb',
#                                      password='predixdb_password',
#                                      database='predixweb')
#         self.tablename = tablename
#         query = f'CREATE TABLE IF NOT EXISTS {self.tablename}(mrank int(3), id int(7), title varchar(100), rating numeric(4,2), \
#             type varchar(100), rdate varchar(100), lan varchar(100), year varchar(50), fcover varchar(200), descr varchar(200), trailer varchar(200));'
#         cur = self.con.cursor()
#         cur.execute(query)
#         print(f'Table successfully created...')
#
#     # Insert
#     def insertVal(self, mid, title, rating, type, genre, rdate, language, cover, description, sequal, trailer):
#         query = f"INSERT INTO {self.tablename}(mid, title, rating, type, genre, rdate, language, cover, description, sequal, trailer) VALUES\
#             ('{mid}', '{title}', '{rating}', '{type}', '{genre}', '{rdate}', '{language}', '{cover}', '{description}', '{sequal}', '{trailer}')"
#         cur = self.con.cursor()
#         cur.execute(query)
#         self.con.commit()
#         print("Insertion successful...")
#
#     # Read
#     def fetchAll(self):
#         query = f'SELECT * FROM {self.tablename}'
#         cur = self.con.cursor()
#         cur.execute(query)
#         for row in cur:
#             print(row)
#
#     # Delete
#     def deleteVal(self, movieID):
#         query = f'DELETE FROM {self.tablename} WHERE id={movieID}'
#         cur = self.con.cursor()
#         cur.execute(query)
#         self.con.commit()
#         print('Deletion successful...')
#
#     # DROP Table
#     def dropTable(self):
#         query = f'DROP TABLE {self.tablename}'
#         cur = self.con.cursor()
#         cur.execute(query)
def searchTrailer(query):
    for j in search(query + " movie trailer youtube", num_results=1):
        return j
import csv
import json
si = imdb.IMDb()
# for i in range(9999999):
#     mov=si.get_movie(i)
with open('tv.csv','a', newline='') as file:
    print("done")
    temp=csv.writer(file)
    #temp.writerow(['mid', 'title', 'rating', 'ranking', 'type', 'genre', 'rdate', 'language', 'cover', 'description', 'trailer' ,'released','year'])
    movies = si.get_top250_tv()
    t=121
    for i in movies[120:]:
        mov = si.get_movie(i.movieID)
        s = ['genres', 'rating', 'imdbID', 'languages', 'title', 'year', 'kind', 'series years',
             'akas', 'seasons', 'writer', 'production companies', 'distributors', 'other companies', 'plot', 'canonical title',
             'long imdb title', 'long imdb canonical title', 'smart canonical title', 'smart long imdb canonical title', 'full-size cover url']
        md = {}
        trailer = searchTrailer(mov['title'])
        print(trailer)
        if trailer!=None:
            md.update({'trailer': trailer})
        else:
            md.update({'trailer': 'Null'})
        for i in s:
            try:
                md.update({i: mov[i]})
            except:
                # print (i,None)
                md.update({i: 'Null'})
        print([md['imdbID'], md['title'], md['rating'],str(t), 'tv series', json.dumps(md['genres']), md['series years'],
                      json.dumps(md['languages']), md['full-size cover url'], md['plot'][0], md['trailer'],'TRUE',md['year']])
        temp.writerow([md['imdbID'], md['title'], md['rating'],str(t), 'tv series', json.dumps(md['genres']), md['series years'],
                      json.dumps(md['languages']), md['full-size cover url'], md['plot'][0], md['trailer'],'TRUE',md['year']])
        t=t+1
    # mid, title, rating, rank, type, genre, rdate, language, cover, description, trailer ,released
    # if trailer:
    #     print(mid, title, rating, type,  rdate, language,  description, sequal, trailer)
    # else:
    #     print(mid, title, rating, type,  rdate, language,  description, sequal)
# Temp DRIVER

# Table Init
# movies = PredixDB("movies")
# trending = PredixDB("trending")
# latest = PredixDB("latest")
# top = PredixDB("top")


# Insert Syntax
# movies.insertVal(14, 18, 'title', 4.0, 'type', '15/08/2012', 'hindi', '2012', 'cover.jpg', 'MovieDesc', 'xyz.youtube.com')

# Delete Syntax
# movies.deleteVal(1)

# # GetData Syntax
# movies.fetchAll()

# Drop Table Syntax
# movies.dropTable()
# trending.dropTable()
# latest.dropTable()
# top.dropTable()