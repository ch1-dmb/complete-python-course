
class Club:
    def __init__(self, name):
        self.name = name
        self.players = []

    # define a method that allows us to access the i-th player in the club directly via indexing.
    # for example, if some_club is an object of Club class,
    # we can access the i-th player in some_club like this (you may assume i is always valid):
    # some_club[i]
  
    # def __repr__(self):
    #     return "Club {}: {}".format(self.name, self.players)
    
    # str can overide __repr__
    def __str__(self):
        return "Club {} with {} players".format(self.name, len(self.players))
    
    def __repr__(self):
        return f"Club {self.name}: {self.players}"
    def __getitem__(self, i):
        return self.players[i]
    # print(some_club[i]) = some_club.__getitem__(i)
    
    def __len__(self):
            return len(self.players)
    # print(len(some_club))


    
some_club = Club("Real Madrid")
some_club.players = ["Benzema", "Modric", "Vinicius"]
print(repr(some_club))
print(some_club)

    # define a method that returns a string representation of this object,
    # which can be used to recreate this object.
    # The return value should be in such format (beware of the spacing):
    # Club {club_name}: {list_of_players}
    # the club_name and list_of_players should be replaced by the according value of current object


    # define a method that returns a readable string representation of this object for the user.
    # The return value should be in such format (beware of the spacing):
    # Club {club_name} with {count_of_players} players
    # the club_name and count_of_players should be replaced by the according value of current object


# You only need to finish the methods, we will take care of the object creation and call those methods for you!