from imdb import IMDb
import glob
import os

cwd = os.getcwd()
ia = IMDb()
for movie_file in glob.glob("*.mp4") + glob.glob("*.mkv") + glob.glob("*.avi"):
    print(movie_file)
    movie_name = ""
    for word in movie_file.replace("_", " ").split():
        if word.isnumeric():
            movie_name += word
            break
        else:
            movie_name += word + " "
    print(movie_name)
    movies = ia.search_movie(movie_name)
    if len(movies) > 0:
        print("    id: ", movies[0].movieID)
        movie = ia.get_movie(movies[0].movieID)
        print("    title: ", movie['title'])
        print("    year: ", movie['year'])
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

