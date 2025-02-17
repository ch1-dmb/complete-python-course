from utils.common.file_operations import save_to_file, read_file

def find_in(iterable, finder, expected):
    for i in iterable:
        if finder(i) == expected:
   
            return i
    raise NotFoundError(f'cant find{expected}')

class NotFoundError(Exception):
    pass

# print(__name__)
print(find_in(["Rolf", 'Jose', "Jen"], lambda x:x, 'Jose'))