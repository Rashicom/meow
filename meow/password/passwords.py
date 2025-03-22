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


def generate_memmory_password():
    """
    This method generate memmorizable password using animals words with random numbers
    read animal names from animals.txt, replace space with undersquares
    and then add random numbers to the end.

    """
    with open("meow/data/animals.txt", "r") as file:
        animals = file.read().splitlines()
    with open("meow/data/positiveadjective.txt", "r") as file:
        positive_adjective = file.read().splitlines()

    # Select a random animal name and replace space with underscores
    animal_name = random.choice(animals).replace(" ", "_")

    # Select a random positive adjective
    positive_adjective = random.choice(positive_adjective)

    # Generate a secret
    secret = get_random_password(length=4)

    # Combine the animal name, positive adjective, and secret and return the result
    return f"{positive_adjective}_{animal_name}_{secret}"