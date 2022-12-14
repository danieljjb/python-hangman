# Hangman Game (Python)

# Goals for this Project

The purpose of this project is to provide a fun interactive game of hangman for users to play. A random word will be selected from a large list of words and the users will have to guess letters in order to win the game. If they guess incorrectly too many times, they will lose.

All of the code for this project will be written in python.

# Live Project
[View the live project here.](https://hangman-python-app.herokuapp.com/)

<img src="/docs/am-i-responsive.png">

# UX

## User Goals
* Easy to understand how play
* Fun to play
* Test their vocabulary

## User Stories
* As a user, I want to easily understand how to play the game
* As a user, I want to be able to test my vocabulary on a wide range of words
* As a user, I want to easily be able to play the game over and over again without much wait time in between games

## Site Owner Goals
* Provide a game that is easy to play
* Have a large number of words that are randomly selected
* Make the game challenging by giving the user a limited number of lives

## Requirements
* Visual image of the hangman changing to represent letters guessed incorrectly
* Option to play again after finishing game

# Design

## Flowchart
The flowchart below shows the logic of how the game will be run from the beginning of the game to the end of the game.

<img src="/docs/flowchart.png">

# Features

## Existing Features

### Start Screen
* The start screen show a simple command for the user to get the game started.

<img src="/docs/start.png">

### The Game Begins
* The game begins and users are shown an image where the man will be hung if they lose lives.
* Beneath this the users are shown several hyphens which represent how many letters are in the word they have to guess.
* Finally, there is a prompt indicating the user to enter a word or letter.

<img src="/docs/user-enter.png">

### User Input Responses
* If the user inputs a letter that is incorrect, there will be a message to tell them and the image of the hangman will be added to.

<img src="/docs/letter-not-in-word.png">

* If the user inputs a letter that is correct, there will be a message to tell them and the image of the hangman will remain the same as before.

<img src="/docs/letter-is-in-word.png">

* * If the user inputs a word that is incorrect, there will be a message to tell them and the image of the hangman will be added to.

<img src="/docs/word-wrong.png">

* If the user inputs an invalid guess such as an invalid character, too many or too little letters in a word or nothing at all, they will be prompted with an invalid message a be told to try again. They will not lose a life for this.

<img src="/docs/input-invalid.png">

* If the user already used a letter or word, they will be prompted with a message telling them to try again. They will not lose a life for this.

<img src="/docs/already-used-letter.png">

### Winning and Losing

* If a user gets the word right, they will be prompted with a message telling them.

<img src="/docs/you-win.png">

* If a user runs out of lives, they will be prompted with a message telling them that they lost and the word they were guessing will be revealed.

<img src="/docs/you-lose.png">

### Play Again?

* If the user wants to play the game again, they must type "YES" and click enter. The game will then be restarted.

<img src="/docs/play-again-yes.png">

* If the user does not want to play the game again, they may enter any key and the game will exit.

<img src="/docs/play-again-exit.png">

## Features to be Added
* Levels of difficulty (More/Less lives)
* Countdown timer option
* Multiplayer mode (Two hangmen take turns guessing letters/words)

# Technologies Used

## Languages
* [HTML](https://en.wikipedia.org/wiki/HTML5 "HTML")
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript "JS")
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Python")

## Tools
* [Gitpod](https://www.gitpod.io/ "Gitpod")
* [Am I Resposive?](https://ui.dev/amiresponsive "Am I Resposive?")
* [Heroku](https://www.heroku.com/ "Heroku")
* [PEP8](http://pep8online.com/ "PEP8")

# Testing

## Code Validation
PEP8 was used to test all of the python code.

The results are given below:

### functions.py
<img src="/docs/function-test.png">

### hangman.py
<img src="/docs/hangman-test.png">

### run.py
<img src="/docs/run-test.png">

### words.py
<img src="/docs/words-test.png">

# Bugs
* I had some issues with the while loop as when I entered characters that weren't letters such as: / ? ! etc. the game would accept them as an entry, even though I only wanted alphabet characters to work. I used w3schools to help me solve this issue.
* When I used "break" and "exit()" on the if/else statement which asked users to play again, I could only enter "YES" and have it work once. The second time the game ended it would automatically exit. To solve this I removed both "break" and "exit()" and it functioned perfectly.

## Unfixed Bugs
There are no unfixed bugs.

# Deployment

The app was deployed using Heroku

* Log in to Heroku (or create an account if necessary).
* Click on New in the Heroku dashboard and select ???Create new app???.
* Give the application an original name, choose your region and click ???Create App???.
* In the settings tab for the new application enter two Config Vars (if necessary):
    * One is CREDS and contains the credentials key for Google Drive API.
    * One is PORT and has the value of 8000.
* Two buildpack scripts are to be added: Python and Nodejs (in that order).
* Go to "Deploy" section, and click the Github icon in 'Deployment Method' and connect github.
* Set the project to 'Automatic Deploys'.
* The app will then be deployed and you will be provided a link to it.

# Credits
* [Code Institute](https://codeinstitute.net/all-access-coding-challenge/?gclsrc=aw.ds&&msclkid=1915e48bf28d11888d1785dfd2b04125&utm_source=bing&utm_medium=cpc&utm_campaign=a%26c_SEA_IRL_BR_Brand_Code_Institute&utm_term=code%20institute&utm_content=exa_Brand) 
* [Simen Daehlin](https://github.com/Eventyret)
* [Kylie Ying](https://www.youtube.com/watch?v=cJJTnI22IF8&t=160s&ab_channel=KylieYing)

# Useful Resources

* [Stack Overflow](https://stackoverflow.com/ "Stack Overflow]")
* [List of words used](https://www.randomlists.com/data/words.json)
* [Hangman Images source](https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c)
* [W3 Schools](https://www.w3schools.com/python/ref_string_isalpha.asp#:~:text=The%20isalpha()%20method%20returns,alphabet%20letters%3A%20(space)!)
* I used w3schools to show me how to use isalpha()
* [isalpha()](https://www.w3schools.com/python/ref_string_isalpha.asp#:~:text=The%20isalpha()%20method%20returns,alphabet%20letters%3A%20(space)!)

