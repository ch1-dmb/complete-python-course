from utils import utils
from utils.common.file_operations import save_to_file, read_file
from utils.find import find_in, NotFoundError

save_to_file('Hello, world!', 'test.txt')
print(read_file('test.txt'))

# print(f'app is {__name__}')

