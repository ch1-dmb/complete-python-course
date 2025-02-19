from collections import defaultdict, OrderedDict, namedtuple, deque


def task1() -> defaultdict:
    """
    - create a `defaultdict` object, and its default value would be set to the string `Unknown`.
    - Add an entry with key name `Alan` and its value being `Manchester`.
    - Return the `defaultdict` object you created.
    """
    # you code starts here:
    info = defaultdict(lambda: 'Unknown')
    info['Alan'] = 'Manchester'
    return info
    # students_info = [('Alan', 'Manchester')]
    # info_dict = defaultdict(list)
    # for name, school in students_info:
    #     info_dict[name].append(school)
    # print(info_dict['Alan'])
    # print(info_dict)
    


def task2(arg_od: OrderedDict):
    """
    - takes in an OrderedDict `arg_od`
    - Remove the first and last entry in `arg_od`.
    - Move the entry with key name `Bob` to the end of `arg_od`.
    - Move the entry with key name `Dan` to the start of `arg_od`.
    - You may assume that `arg_od` would always contain the keys `Bob` and `Dan`,
        and they won't be the first or last entry initially.
    """
    arg_od.popitem()
    # arg_od.pop('Alan') the same as 
    arg_od.popitem(False)
    arg_od.move_to_end('Bob')
    arg_od.move_to_end('Dan', last=False)
    return arg_od


def task3(name: str, club: str) -> namedtuple:
    """
    - create a `namedtuple` with type `Player`, and it will have two fields, `name` and `club`.
    - create a `Player` `namedtuple` instance that has the `name` and `club` field set by the given arguments.
    - return the `Player` `namedtuple` instance you created.
    """
    # you code starts here:
    Player = namedtuple('Player', ['name', 'club'])
    player = Player(name, club)
    return player



def task4(arg_deque: deque):
    """
    - Manipulate the `arg_deque` in any order you preferred to achieve the following effect:
        -- remove last element in `deque`
        -- move the fist (left most) element to the end (right most)
        -- add an element `Zack`, a string, to the start (left)
    """
    # you code starts here:
    arg_deque.pop()
    arg_deque.append(arg_deque.popleft())
    arg_deque.appendleft('Zack')
    

# print(task1())
# print(task2(OrderedDict([
#     ('Alan', 'Manchester'),
#     ('Bob', 'London'),
#     ('Chris', 'Lisbon'),
#     ('Dan', 'Paris'),
#     ('Eden', 'Liverpool'),
#     ('Frank', 'Newcastle')
# ])))
# info = OrderedDict([
#     ('Alan', 'Manchester'),
#    ('Bob', 'London'),
#     ('Chris', 'Lisbon'),
#    ('Dan', 'Paris'),
#     ('Eden', 'Liverpool'),
#     ('Frank', 'Newcastle')
#  ])
# print(info.popitem())
# print(info.pop('Alan'))
# print(info)