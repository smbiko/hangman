import string
from random import choice

MAX_INCORRECT_GUESSES = 6

def select_word():
    """
    Get words to use in the wordlist 
    """
    with open("words.txt", mode="r") as words:
        word_list = words.readlines()
    return choice(word_list).strip()


def get_player_input(guessed_letters):
    """
    Select word to Guess
    """
    while True:
        player

