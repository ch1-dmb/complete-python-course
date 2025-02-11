# Incomplete app!
import csv

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []




# movies.append({
#     'title': title,
#     'director': director,
#     'year': year
# })
def add_movie():
    # # You may want to create a function for this code
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    new_movie = [{"Title": title, "Director": director, "Year":year}]
    with open("movies.csv", "a", newline="") as file:
        fieldnames = ["Title" ,"Director", "Year"]
        input_list = csv.DictWriter(file, fieldnames=fieldnames)
        input_list.writerows(new_movie)
       
    # need iterator
    last_movie = None
    with open("movies.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for r in reader:
            last_movie = r
        
    if last_movie:

        print("here is your latest movie input: {}".format(last_movie))
    else: 
        print("please check ur input")
    

# Create other functions for:
#   - listing all movies
#   - finding movies
def load_movies():
    global movies
    movies.clear()
    try:
        with open("movies.csv", "r") as file:
            reader = csv.DictReader(file)
            # movies_list = csv.reader(file)
            for m in reader:
                movies.append({'title': m["Title"], 'director': m["Director"], 'year': m["Year"]})
        # return movies
    except FileNotFoundError:
            print("No movie data found. Please add a movie first.")
def list_movies():
    
    load_movies()
    if movies:
        for movie in movies:
            print(f"{movie['title']} - {movie['director']} ({movie['year']})")
    else:
        print("No movies available.")
        


def find_movie():
    load_movies()
    movie_info = input("Which movie are you looking for?")
    found=False
    for i in movies:
        print(i)
        if movie_info == i["title"]:
            print("found: {}".format(i))
            found=True
            break
    if not found:
        print("Sorry, we can't find it.") 

   
        
       
       


user_options = {
    "a": add_movie,
    "l": list_movies,
    "f": find_movie
}


# And another function here for the user menu
def menu():
    selection = input(MENU_PROMPT)

    while selection != 'q':
        if selection in user_options:
            select_option = user_options[selection]()
        
            
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


# Remember to run the user menu function at the end!
menu()