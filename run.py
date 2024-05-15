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
    Get the Validate the players input
    """
    while True:
        player_input("Guess a letter").lower()
        if _validate_input(player_input, guessed_letters):
            return player_input

def _validate_input(player_input, guessed_letters):
    """
    Input validation loop 
    """
    return (
        len(player_input) == 1
        and player_input in string.ascii_lowercase
        and player_input not in guessed_letters
    )

def join_guessed_letters(guessed_letters):
    """
    Displaying the guessed letters and word
    """
    return " ".join(sorted(guessed_letters))

