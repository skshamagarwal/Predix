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
with open('tmovie.csv','a', newline='') as file:
    print("done")
    temp=csv.writer(file)
    #temp.writerow(['mid', 'title', 'rating', 'ranking', 'type', 'genre', 'rdate', 'language', 'cover', 'description', 'trailer' ,'released','year'])
    movies = si.get_top250_movies()
    for i in movies[235:]:
        mov = si.get_movie(i.movieID)
        s = [u'rating', u'runtimes', u'year', u'color info', u'votes', u'top 250 rank', u'title',
             u'directors', u'certificates', u'countries', u'country codes', u'language codes', u'cover url', u'genres',
             u'miscellaneous',
             u'director', u'original air date', u'aspect ratio', u'kind', u'languages', u'imdbID', u'plot outline',
             u'plot', u'synopsis', u'box office', u'long imdb title', u'full-size cover url']
        md = {}
        trailer = searchTrailer(mov['title'])
        print(trailer)
        if trailer!=None:
            md.update({'trailer': trailer})
        else:
            md.update({'trailer': 'Null'})
        for i in s:
            #print(i,mov[i])
            try:
                md.update({i: mov[i]})
            except:
                # print (i,None)
                md.update({i: 'Null'})
        print([md['imdbID'], md['title'], md['rating'],md['top 250 rank'], md['kind'], json.dumps(md['genres']), md['original air date'],
                      json.dumps(md['languages']), md['full-size cover url'], md['plot'][0], md['trailer'],'TRUE',md['original air date'][md['original air date'].index('(')-5:md['original air date'].index('(')-1]])
        temp.writerow([md['imdbID'], md['title'], md['rating'],md['top 250 rank'], md['kind'], json.dumps(md['genres']), md['original air date'],
                      json.dumps(md['languages']), md['full-size cover url'], md['plot'][0], md['trailer'],'TRUE',md['original air date'][md['original air date'].index('(')-5:md['original air date'].index('(')-1]])

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