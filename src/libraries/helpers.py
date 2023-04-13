import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def get_random_letter(except_character):
    letters = string.ascii_lowercase
    character = except_character
    while(character == except_character):
        character = random.choice(letters)
    return character




