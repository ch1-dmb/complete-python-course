import csv
movies = []
movies_list = [
    {"Title": "The Shawshank Redemption", "Director": "Frank Darabont", "Year": 1994},
    {"Title": "The Godfather", "Director": "Francis Ford Coppola", "Year": 1972},
    {"Title": "The Dark Knight", "Director": "Christopher Nolan", "Year": 2008},
    {"Title": "Pulp Fiction", "Director": "Quentin Tarantino", "Year": 1994},
    {"Title": "The Lord of the Rings: The Return of the King", "Director": "Peter Jackson", "Year": 2003},
    {"Title": "Forrest Gump", "Director": "Robert Zemeckis", "Year": 1994},
    {"Title": "Inception", "Director": "Christopher Nolan", "Year": 2010},
    {"Title": "Fight Club", "Director": "David Fincher", "Year": 1999},
    {"Title": "The Matrix", "Director": "Lana Wachowski, Lilly Wachowski", "Year": 1999},
    {"Title": "Goodfellas", "Director": "Martin Scorsese", "Year": 1990},
    {"Title": "The Empire Strikes Back", "Director": "Irvin Kershner", "Year": 1980},
    {"Title": "The Lord of the Rings: The Fellowship of the Ring", "Director": "Peter Jackson", "Year": 2001},
    {"Title": "The Lord of the Rings: The Two Towers", "Director": "Peter Jackson", "Year": 2002},
    {"Title": "Interstellar", "Director": "Christopher Nolan", "Year": 2014},
    {"Title": "Se7en", "Director": "David Fincher", "Year": 1995},
    {"Title": "The Silence of the Lambs", "Director": "Jonathan Demme", "Year": 1991},
    {"Title": "Saving Private Ryan", "Director": "Steven Spielberg", "Year": 1998},
    {"Title": "The Green Mile", "Director": "Frank Darabont", "Year": 1999},
    {"Title": "Star Wars: A New Hope", "Director": "George Lucas", "Year": 1977},
    {"Title": "The Prestige", "Director": "Christopher Nolan", "Year": 2006},
    {"Title": "The Departed", "Director": "Martin Scorsese", "Year": 2006},
    {"Title": "Gladiator", "Director": "Ridley Scott", "Year": 2000},
    {"Title": "Whiplash", "Director": "Damien Chazelle", "Year": 2014},
    {"Title": "The Lion King", "Director": "Roger Allers, Rob Minkoff", "Year": 1994},
    {"Title": "The Usual Suspects", "Director": "Bryan Singer", "Year": 1995},
    {"Title": "Schindler's List", "Director": "Steven Spielberg", "Year": 1993},
    {"Title": "Braveheart", "Director": "Mel Gibson", "Year": 1995},
    {"Title": "Memento", "Director": "Christopher Nolan", "Year": 2000},
    {"Title": "Django Unchained", "Director": "Quentin Tarantino", "Year": 2012},
    {"Title": "Coco", "Director": "Lee Unkrich, Adrian Molina", "Year": 2017},
    {"Title": "Avengers: Infinity War", "Director": "Anthony Russo, Joe Russo", "Year": 2018},
    {"Title": "Joker", "Director": "Todd Phillips", "Year": 2019},
    {"Title": "Parasite", "Director": "Bong Joon-ho", "Year": 2019},
    {"Title": "Once Upon a Time in Hollywood", "Director": "Quentin Tarantino", "Year": 2019},
    {"Title": "The Grand Budapest Hotel", "Director": "Wes Anderson", "Year": 2014},
    {"Title": "Logan", "Director": "James Mangold", "Year": 2017},
    {"Title": "The Wolf of Wall Street", "Director": "Martin Scorsese", "Year": 2013},
    {"Title": "Blade Runner 2049", "Director": "Denis Villeneuve", "Year": 2017},
    {"Title": "No Country for Old Men", "Director": "Ethan Coen, Joel Coen", "Year": 2007},
    {"Title": "Mad Max: Fury Road", "Director": "George Miller", "Year": 2015},
    {"Title": "A Beautiful Mind", "Director": "Ron Howard", "Year": 2001},
    {"Title": "12 Years a Slave", "Director": "Steve McQueen", "Year": 2013},
    {"Title": "The Revenant", "Director": "Alejandro González Iñárritu", "Year": 2015},
    {"Title": "Slumdog Millionaire", "Director": "Danny Boyle", "Year": 2008},
    {"Title": "Black Swan", "Director": "Darren Aronofsky", "Year": 2010},
    {"Title": "The Truman Show", "Director": "Peter Weir", "Year": 1998},
    {"Title": "The Social Network", "Director": "David Fincher", "Year": 2010},
    {"Title": "American Beauty", "Director": "Sam Mendes", "Year": 1999},
    {"Title": "Heat", "Director": "Michael Mann", "Year": 1995}
]

def create_movies_list():

    with open("movies.csv", "w", newline="") as file:
        fieldnames = movies_list[0].keys()
        input_list = csv.DictWriter(file, fieldnames = fieldnames)
        input_list.writeheader()
        input_list.writerows(movies_list)

    print("file is created successfully")

def open_movies_list():
    
    with open("movies.csv", "r", newline="") as file:
       
        input_list = csv.DictReader(file)
    
        for r in input_list:
            movies.append(r)
        # print(movies[-1])
        # print(movies)
        return movies
      

def find_movie():
    global movies
    movie_info = input("Which movie are you looking for?")
    found=False
    # print(movies)
    for i in movies:
        
        if movie_info == i["Title"]:
            print("found: {}".format(movie_info))
            found=True
            break
    if not found:
        print("Sorry, we can't find it.") 
        
       
open_movies_list()

find_movie()
# this is for list :
# data = [
#     ["Name", "Age", "City"],
#     ["Alice", 25, "New York"],
#     ["Bob", 30, "Los Angeles"],
#     ["Charlie", 28, "Chicago"]
# ]
# with open ("movies.csv", "w", newline="") as file:
#     list_input = csv.writer(file)
#     list_input.writerows(movies_list)

# print("file is created successfully")