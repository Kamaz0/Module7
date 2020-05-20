import random 

class FilmSeriesList:

    def __init__(self):
        self.full_list = []
      
    def add(self, movie):
        self.full_list.append(movie)

    def show_all(self):
        for x in self.full_list:
            print(x)

    def get_series(self):
        seriale = [i for i in self.full_list if isinstance(i, Series)]
        return seriale

    def get_movies(self):
        movies = [i for i in self.full_list if isinstance(i, Film) and not isinstance(i, Series)]
        return movies

    def search(self, title):
        movies = [i for i in self.full_list if i.title == title]
        return movies
        #movies = [i for i in self.full_list if i.title.lower() == title.lower()]

    def generate_views(self):
        i = random.randint(0,len(self.full_list)-1)        
        views = random.randint(1,100)
        self.full_list[i].times_played = views
        
    def generate_views_tentimes(self):
        for i in range(10):
            self.generate_views()

    def top_titles(self, n=3, content_type=None):
        if content_type == "movies":
            movies = self.get_movies()
        elif content_type == "series":
            movies = self.get_series() 
        else: 
            movies = self.full_list
        movies = sorted(movies, key=lambda x: x.times_played,reverse=True)
        return movies[:n]
        
     
    # parametr content_type, którym wybierzesz czy mają zostać pokazane filmy, czy seriale


class Film:
    def __init__(self, title, year, genre, times_played):
        self.title = title
        self.year = year
        self.genre = genre
        self.times_played = times_played

    def play(self, play_one=1):
        self.times_played += play_one

    def __str__(self):
        return f'{self.title} ({self.year})'

    def __repr__(self):
        return str(self)


class Series(Film):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f'{self.title} S{self.season}{self.episode}'


lista_lista = FilmSeriesList()


film1 = Film("Pulp Fiction", "1994", "crime", times_played=0)
film2 = Film("Crouching Tiger, Hidden Dragon", "2000", "fantasy", times_played=0)
film3 = Film("Lincz", "2010", "dramat", times_played=0)
series1_1 = Series(title="X Files", year="1990", genre="crime", season="01", episode="01", times_played=0)
series1_2 = Series(title="X Files", year="1990", genre="crime", season="01", episode="02", times_played=0)
series1_3 = Series(title="X Files", year="1990", genre="crime", season="01", episode="03", times_played=0)

print("Biblioteka Filmów")

lista_lista.add(film1)
lista_lista.add(film2)
lista_lista.add(film3)
lista_lista.add(series1_1)
lista_lista.add(series1_2)
lista_lista.add(series1_3)


print(film1)
lista_lista.show_all()
film1.play()
print(film1.times_played)


print(lista_lista.get_movies())
print(lista_lista.get_series())

 # jest_filmem = [isinstance(i, Film) for i in self.full_list] pierwsza proba


print(lista_lista.search("Lincz"))

lista_lista.generate_views()
lista_lista.generate_views_tentimes()

for movie in lista_lista.full_list: 
    print(movie.title,movie.times_played)

print(lista_lista.top_titles())
print(lista_lista.top_titles(2,"series"))

