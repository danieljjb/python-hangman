import random
from words import word_list
from hangman import hangman_images


def select_word():
    word = random.choice(word_list)
    return word.upper()

def main():
    input('Enter any key to start: ')
    print("temporary")

def start(word):
    words_used = []
    letters_used = []
    full_word = "_" * len(word)
    attempts = 6