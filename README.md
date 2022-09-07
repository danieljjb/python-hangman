# Hangman Game (Python)

# Goals for this Project

The purpose of this project is to provide a fun interactive game of hangman for users to play. A random word will be selected from a large list of words and the users will have to guess letters in order to win the game. If they guess incorrectly too many times, they will lose.

All of the code for this project will be written in python.

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



## Features to be Added