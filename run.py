import string
from random import choice
import pyfiglet
from hangman import hangman_as
from words import word_list
from tabulate import tabulate
from colorama import Fore, init, Style

MAX_INCORRECT_GUESSES = 6

def welcome_screen():
    """
    Function to welcome screen will provide users with rules and input for his game.
    """
    welcome_text = pyfiglet.figlet_format("**Skeletan Hangman**")
    print(welcome_text)
    global name
    while True:
        print("\n")
        name = (
            input(
                Fore.LIGHTRED
                + Style.BRIGHT
                + ("Please enter your name:\n".center(width))
        )
            .strip()
            .capitalize()
        )
        print("\n")
        if not name.isalpha():
            print(Fore.RED + "Name must be alphabets only!!!\n".center(width))
        else:
            clear()
            break
    return name


def select_word():
    """
    Get words to use in the wordlist 
    """
    with open("words.txt", mode="r") as words:
        word_list = words.readlines()
    return choice(word_list).strip()

def player_input(prompt):
    """
    Wrapper for the built-in input function to capture user input
    """
    return input(prompt)

def get_player_input(guessed_letters):
    """
    Get the Validate the players input
    """
    while True:
        player_input("Guess a letter").lower()
        if _validate_input(player_input, guessed_letters):
            return player_input
        else:
            print("Invalid input. Please try again.")

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

def build_guessed_word(target_word, guessed_letters):
    """
    Build the word to show player
    """
    current_letters= []
    for letter in target_word:
        if letter in guessed_letters:
            current_letters.append(letter)
        else:
            current_letters.append("_")
    return " ".join(current_letters)

def draw_hanged_man(wrong_guesses):
    """
    Draw the hangman
    """
    hanged_man = [
        r"""
  -----
  |   |
      |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
  |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/     |
|     |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/   \ |
|   | |
      |
-------
""",
    ]

    print(hanged_man[wrong_guesses])

def game_over(wrong_guesses, target_word, guessed_letters):
    """
    Guesses which are incorrect 
    """
    if wrong_guesses == MAX_INCORRECT_GUESSES:
        return True
    if set(target_word) <= guessed_letters:
        return True
    return False

if __name__ == "__main__":
    """
    Initial setup
    """
    target_word = select_word()
    guessed_letters = set()
    guessed_word = build_guessed_word(target_word, guessed_letters)
    wrong_guesses = 0
    print("Welcome to Hangman!")


    """
    Game Loop
    """
    while not game_over(wrong_guesses, target_word, guessed_letters):
        draw_hanged_man(wrong_guesses)
        print(f"Your word is: {guessed_word}")
        print(
            "Current guessed letters: "
            f"{join_guessed_letters(guessed_letters)}\n"
        )
        player_guess = get_player_input(guessed_letters)
        if player_guess in target_word:
            print("Great guess!")
        else:
            print("Sorry, it's not there.")
            wrong_guesses += 1

        guessed_letters.add(player_guess)
        guessed_word = build_guessed_word(target_word, guessed_letters)

    
    """
    Game Over
    """

    draw_hanged_man(wrong_guesses)
    if wrong_guesses == MAX_INCORRECT_GUESSES:
        print("Sorry, you lost!")
    else:
        print("Congrats! You did it!")
    print(f"Your word was: {target_word}")







