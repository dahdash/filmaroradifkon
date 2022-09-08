from imdb import Cinemagoer
import glob
import os

def check_movie(movie_file):
    print(movie_file)
    movie_name = ""
    movie_year = ""
    for word in movie_file.replace("_", " ").split():
        if word.startswith("20") or word.startswith("19"):
            movie_year = word
            break
        elif word.startswith("1080") or word.startswith("720") or word.startswith("DVD"):
            break
        else:
            movie_name += word + " "
    print(movie_name, "("+movie_year+")")
    movie_year = int(movie_year)
    movies = ia.search_movie(movie_name)
    if len(movies) > 0:
        for movie in movies:
            if movie_year != movie['year']:
                continue
            print("    id: ", movie.movieID)
            movie = ia.get_movie(movie.movieID)
            print("   ", movie['title'], movie['year'])
            directors = ""
            for director in movie['directors']:
                if directors:
                    directors += ", "
                directors += director['name']
            print("    director(s): ", directors)
            path = cwd + '/' + directors + '/' + str(movie['year']) + ') ' + movie['title']
            if not os.path.exists(path):
                os.makedirs(path)
            os.rename(cwd + '/' + movie_file, path + '/' + movie_file)
            print("    radifshod!")
            return
    print("    radifNAshod!")


cwd = os.getcwd()
ia = Cinemagoer()
for movie_file in glob.glob("*.mp4") + glob.glob("*.mkv") + glob.glob("*.avi"):
    check_movie(movie_file)

