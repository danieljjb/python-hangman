# https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c hangman images source

def hangman_images(attempts):
    hangman_parts = [
        '''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        =========
        ''', '''
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
        =========
        ''', '''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        =========
        ''', '''
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========
        ''', '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========
        ''', '''
        +---+
        |   |
        O   |
            |
            |
            |
        =========
        ''', '''
        +---+
        |   |
            |
            |
            |
            |
        =========
        '''
    ]
    return hangman_parts[attempts]
