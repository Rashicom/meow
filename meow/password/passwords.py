import string
import random

def get_random_password(type="alphanumeric", special_char=False, length=8):

    # Define the characters that can be used in the password
    characters = string.ascii_letters + string.digits

    if special_char:
        characters += string.punctuation

    # Generate a random password of length 16
    password = ''.join(random.choice(characters) for _ in range(length))

    return password