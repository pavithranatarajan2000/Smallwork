import imdb
ia=imdb.IMDb()
search=ia.get_top250_movies()
for i in range(100):
  print("{}){}".format(i+1,search[i]))
