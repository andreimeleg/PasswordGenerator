import random
import string 

# get random string without repeating letters
def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.sample(letters, length))
    print("Random String is:", result_str)

get_random_string(8)
get_random_string(8)