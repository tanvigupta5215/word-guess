"""
File: word_guess.py
-------------------
Fill in this comment.
"""

import random

LEXICON_FILE = "Lexicon.txt"  # File to read word list from
INITIAL_GUESSES = 8  # Initial number of guesses player starts with


def play_game(secret_word):
    """
    Add your code (remember to delete the "pass" below)
    """
    # dash_str = '_' * len(secret_word)
    dash_word = ''  # creating empty string here
    user_guess = 8  # initial guesses
    for _ in secret_word:  # iterating over secret word for converting into dashes
        dash_word += '_'  # converting secret word into dashes
    dash_word = list(dash_word)  # storing it in list format
    print(secret_word)
    while user_guess > 0 and dash_word.count(
            '_') > 0:  # checking condition user guess should be greater than 0 and dashes count is also greater than 0
        print("The word now looks like this: " + "".join(
            dash_word))  # showing the word into dashes by calling join function
        print("you have " + str(user_guess) + " guesses left")
        user_input = input("Type a single letter here, then press enter")  # asking user for the input
        while len(user_input) > 1 or user_input == "":  # checking user input should not be double word or blank
            user_input = input('Enter the single character: ')
        match_found = False  # setting a variable for match found
        for i in range(len(secret_word)):
            if user_input.lower() == secret_word[i].lower():  # if user input matches with alphabet in secret word
                dash_word[i] = secret_word[i]  # replacing dash with that correct word
                match_found = True  # the correct alphabet was found
                print("That guess is correct")
        if not match_found:  # if correct alphabet not found
            user_guess -= 1  # number of guesses reduced by 1
            print("There are no " + str(user_input) + "'s in the word")  # printing if the incorrect word entered
    if user_guess == 0:  # if user could not guess the word
        print("Sorry you lost,the secret word was: " + str(
            secret_word))  # printing the user lost and showing user the actual word
    if dash_word.count("_") == 0:
        print("Congratulations, the word is: " + str(secret_word))


def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    """
    index = random.randrange(3)
    if index == 0:
        return 'HAPPY'
    elif index == 1:
        return 'PYTHON'
    else:
        return 'COMPUTER'
    """
    read_lines = open(LEXICON_FILE).readlines()
    random_word = random.choice(read_lines)
    selected_word = random_word.strip()
    return selected_word




def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
