# Tic Tac Toe Game

This is a simple Tic Tac Toe game implemented in Python, with a graphical interface created using the turtle library.

## Prerequisites
* Python 3.x installed on your system
* The turtle library installed, which is a part of the standard Python library and does not require any additional installation.

## Setting up the environment

1. Open a terminal or command prompt window.
2. Create a new directory for your project.
3. Change the current working directory to the project directory.
4. Create a new Python file in the project directory, for example tic_tac_toe.py.
5. Open the file using a text editor or an Integrated Development Environment (IDE) of your choice.
6. Write or copy the code for the Tic Tac Toe game into the file.
7. Save the file.

## Running the game

* Open a terminal or command prompt window.
* Change the current working directory to the project directory.
* Run the following command to start the game:

```
python3 tic_tac_toe.py
```

## Features

Two players can take turns marking spaces on the 3x3 grid with either an X or an O.
The game ends when one player has three marks in a row or when all spaces have been filled.

## Implementation Details

The turtle library is used to create the graphical interface for the game.

The Screen class from turtle is used to create the screen and set the title of the game window.
Two turtle objects, one for the X player and one for the O player, are created and configured to draw the marks on the grid.

A grid is drawn on the screen using two for loops and the goto method of the turtle objects.
A function called draw_mark is defined to draw the X or O marks on the grid. It takes as input the turtle object to be used for the current player, and the x and y coordinates of the mark to be drawn.

Another function called game_over is defined to check if the game is over by checking all possible combinations of three marks in a row.
The main game loop uses the onclick method of the screen to listen for clicks from the players, and the draw_mark function is called to draw the marks on the grid. The loop continues until the game is over or all spaces have been filled.
The done method of the turtle library is called at the end of the game to show the winner.

## Conclusion
This simple Tic Tac Toe game provides a basic demonstration of how the turtle library can be used to create a graphical interface in Python. It can be used as a starting point for more complex games or as a fun activity for learning Python.
