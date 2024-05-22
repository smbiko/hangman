import string
import os
from random import choice
import pyfiglet
from colorama import Fore, init, Style
init(autoreset=True)
width = os.get_terminal_size().columns


MAX_INCORRECT_GUESSES = 7

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
                Fore.LIGHTRED_EX
                + Style.BRIGHT
                + ("Please enter your name:\n".center(width))
        )
            .strip()
            .capitalize()
        )
        print("\n")
        if not name.isalpha():
            print(Fore.MAGENTA + "Name must be alphabets only!!!\n".center(width))
        else:
            clear()
            break
    return name

def clear():
    """
    Function to clear terminal through the game.
    """
    os.system("cls" if os.name == "nt" else "clear")

def rules():
    """
    This function will display rules to the user
    """
    clear()
    welcome_text = pyfiglet.figlet_format("** Skeletan Hangman **")
    print(welcome_text)
    print("\n")
    print(Fore.LIGHTWHITE_EX + "Rules of this game are fairly"
                               " simple!!!\n".center(width))
    print("1.You are guessing letters one by one that makes"
          " hidden word".center(width))
    print("2.Each wrong guess you are losing a"
          "  life and 1 point is deducted from score".center(width))
    print("3.Each right guess you are getting closer"
          " to the win and 1 point is add to the score".center(width))
    print("4. How many TRIES you have ".center(width))
    print("5. You win by guessing all the letters in the"
          " word and getting extra 10 points".center(width))
   
    while True:
        try:
            pas_b = input(
                Fore.LIGHTWHITE_EX + ("Type P to"
                                      " play the game:\n".center(width))
            ).upper()
            if pas_b == "P":
                break
            else:
                clear()
                raise ValueError(Fore.RED + ("Please type letter P!!!"))
        except ValueError as e_rr:
            print(f"Invalid input:{e_rr}")


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
    Get to Validate the players input
    """
    player_input = input("Enter a letter: ").strip().lower() 
    if _validate_input(player_input, guessed_letters):
        return player_input
    else:
        print("Invalid input. Please enter a single letter that hasn't been guessed yet.")
        return get_player_input(guessed_letters)

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
                     __  __
                    | | / /
                    | | /
                    | |/
                    | |
                    | |
                    | |
                    | |
                    | |
                    | |
                    | |
""",
        r"""
                     _________________
                    | ._______________|
                    | | / /
                    | | /
                    | |/
                    | |
                    | |
                    | |
                    | |
                    | |
                    | |
                    | |
""",
        r"""
                    ___________.._______
                    | .__________))_____|
                    | | / /      ||
                    | | /        ||
                    | |/         ||
                    | |          ||
                    | |          ||
                    | |
                    | |
                    | |
                    | |
                    | |
                    | |
""",
        r"""
                    ___________.._______
                    | .__________))_____|
                    | | / /      ||
                    | | /        ||.-''.
                    | |/         |/  _  \\
                    | |          ||  `/,|
                    | |          (\\`_.'
                    | |           -`--'
                    | |
                    | |
                    | |
                    | |
                    | |
""",
        r"""
                     ___________..______
                    | .__________))_____|
                    | | / /      ||
                    | | /        ||.-''.
                    | |/         |/  _  \\
                    | |          ||  `/,|
                    | |          (\\`_.'
                    | |         .-`--'.
                    | |        /Y . . Y
                    | |      //
                    | |     ')
                    | |
                    | |
""",
        r"""
                    ___________.._______
                    | .__________))_____|
                    | | / /      ||
                    | | /        ||.-''.
                    | |/         |/  _  \\
                    | |          ||  `/,|
                    | |          (\\`_.'
                    | |         .-`--'.
                    | |        /Y . . Y\\
                    | |      //         \\
                    | |     ')            (`
                    | |
                    | |
""",
        r"""
                     ___________..______
                    | .__________))_____|
                    | | / /      ||
                    | | /        ||.-''.
                    | |/         |/  _  \\
                    | |          ||  `/,|
                    | |          (\\`_.'
                    | |         .-`--'.
                    | |        /Y . . Y\\
                    | |      //  | . |  \\
                    | |     ')   |   |   (`
                    | |
                    | |
""",
       r"""
                     ___________.._______
                    | .__________))______|
                    | | / /      ||
                    | | /        ||.-''.
                    | |/         |/  _  \\
                    | |          ||  `/,|
                    | |          (\\`_.'
                    | |         .-`--'.
                    | |        /Y . . Y\\
                    | |      //  | . |  \\
                    | |     ')   |   |   (`
                    | |          ||'||
                    | |          || ||
                    | |       __/ | | \\__
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
    welcome_screen()
    rules()
    target_word = select_word()
    guessed_letters = set()
    guessed_word = build_guessed_word(target_word, guessed_letters)
    wrong_guesses = 0
   


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
            print(Fore.GREEN + (f"Great guess!"))
        else:
            print(Fore.RED + (f"Sorry, it's not there."))
            wrong_guesses += 1

        guessed_letters.add(player_guess)
        guessed_word = build_guessed_word(target_word, guessed_letters)

    
    """
    Game Over
    """

    draw_hanged_man(wrong_guesses)
    if wrong_guesses == MAX_INCORRECT_GUESSES:
        print(Fore.RED + (f"Sorry {name} you lost!!!").center(width))
    else:
        print(Fore.GREEN
            + Style.BRIGHT + (f"Congrats {name}! You did it!").center(width))
        print(f"Your word was: {Fore.YELLOW} {target_word}".center)

def end_game():
    """
    Function that will ask user if he wants to play again.
    """
    while True:
        print(f"{Fore.GREEN + Style.BRIGHT}{name} you can play again or exit game.\n".center(width))
        again = input("Press (Y)es, (N)o:\n".center(width))
        try:
            if again == "Y":
                clear()
                break
            elif again == "N":
                clear()
                thank_you()
                break
            else:
                clear()
                raise ValueError("\n You must type Y,N!!!".center(width))
        except ValueError as e_rr:
            print(Fore.RED + (f"Try again:{e_rr}"))

def thank_you():
    """
    This function will just print text for user
    when he decided to stop playing game
    """
    thank_text = pyfiglet.figlet_format(f"Thank you for playing game {name}!")
    print(thank_text)


