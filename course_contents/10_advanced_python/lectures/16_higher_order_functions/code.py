def greet():
    print("Hello!")

# `before_and_after` is a higher-order function. That just means it's a function which has another function as a parameter.
def before_and_after(func):  # func is a function passed
    print("Before...")
    func()
    print("After...")


# greet, not greet(). That's because we're passing the function, not the result of calling the function.
before_and_after(greet)


# Another example


movies = [
    {"name": "The Matrix", "director": "Wachowski"},
    {"name": "A Beautiful Day in the Neighborhood", "director": "Heller"},
    {"name": "The Irishman", "director": "Scorsese"},
    {"name": "Klaus", "director": "Pablos"},
    {"name": "1917", "director": "Mendes"},
]

# the finder here is a function
# def find_movie(expected, finder):
#     found = []
#     for i in movies:
#         if finder(i) == expected:
#             found.append(i)
#         return found

# find_by = input("What property are we searching by? ")
# looking_for = input("What are you looking for? ")
# movie_list = find_movie(looking_for, lambda x: x[find_by])
# print(movie_list or "Nothing")

# or

def find_movie(expected, finder):
    found = []
    for i in movies:
        if i[finder] == expected:
            found.append(i)
        return found
find_by = input("What property are we searching by? ")
looking_for = input("What are you looking for? ")
movie_list = find_movie(looking_for, find_by)
print(movie_list or "Nothing")

