import random
from words import word_list
from hangman import hangman_images


def select_word():
    word = random.choice(word_list)
    return word.upper()

def main():
    word = select_word()
    start(word)
    input('Enter any key to start: ')
    print("temporary")

def start(word):
    words_used = []
    letters_used = []
    full_word = "_" * len(word)
    attempts = 6
    used = False
    print(hangman_images(attempts))
    print(full_word)

    while not used and attempts > 0:
        guess = input("Enter a letter or a word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in letters_used:
                print("You already used ", guess, " try again.")
            elif guess not in word:
                print("The letter ", guess, "is not in the word. :(")
                attempts -= 1
                letters_used.append(guess)
            else:
                print(guess, "is in the word! Keep going! :)")
                letters_used.append(guess)
                listed_words = list(full_word)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    listed_words[index] = guess
                full_word = "".join(listed_words)
                if "_" not in full_word:
                    used = True
