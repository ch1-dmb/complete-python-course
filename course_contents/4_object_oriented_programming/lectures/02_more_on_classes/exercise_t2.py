# Define a Movie class that has two properties: name and director

class Movie:
    def __init__(self, name, director):
        self.movie_name = name
        self.director_name =  director

    def show_detail(self):
        print("{} is directed by {}".format(self.movie_name, self.director_name))

# You should be able to create Movie objects like this one:
my_movie = Movie('The Matrix', 'Wachowski')
her_movie = Movie('Oppenheimer', 'Christopher Nolan')
my_movie.show_detail()
her_movie.show_detail()
my_movie.movie_name
my_movie['movie_name']