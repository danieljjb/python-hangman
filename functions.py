import random
from words import word_list
from hangman import hangman_images


def select_word():
    word = random.choice(word_list)
    return word.upper()