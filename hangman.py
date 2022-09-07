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