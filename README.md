# AI Task Two: Tic-Tac-Toe AI

# Introduction:
The goal of this project was to implement an AI agent capable of playing Tic-Tac-Toe against a human player. Two algorithms were explored for the AI player: Minimax with and without Alpha-Beta Pruning. The project aimed to provide insights into game theory and basic search algorithms.

# Code Explanation:
# Game Representation:
The Tic-Tac-Toe game is represented as a 3x3 grid using a nested list in Python.
Each cell of the grid can be empty, contain the player's mark (X or O), or represent an AI move.

# Game Logic:
The game logic module contains functions to check for a winner, determine if the board is full, and evaluate the board for the AI player.
The check_winner function checks rows, columns, and diagonals for three consecutive marks of the same player.
The evaluate function assigns scores to different board configurations based on whether the AI player is winning, losing, or the game is a draw.

# Minimax Algorithm:
The minimax function implements the Minimax algorithm, a recursive algorithm used to search through the game tree and determine the best move for the AI player.
The algorithm evaluates possible future game states by recursively exploring all possible moves and their outcomes.
It assigns scores to each game state and selects the move with the highest score for the AI player while assuming the opponent plays optimally.

# Minimax with Alpha-Beta Pruning:
The Minimax algorithm is enhanced with Alpha-Beta Pruning to optimize performance by reducing the number of nodes evaluated.
Alpha-Beta Pruning eliminates branches of the game tree that cannot influence the final decision, thereby speeding up the search process.

# User Interface:
A simple command-line interface allows the human player to interact with the game.
Players input their moves by specifying row and column numbers.
The game board is displayed after each move, and the outcome of the game is determined when a player wins, the game ends in a draw, or the user quits.

# Documentation:
# Detailed Code Explanations:
Comprehensive explanations of the code modules, functions, and algorithms used in the project are provided.
Each code segment is accompanied by comments explaining its purpose and functionality.

# Algorithm Descriptions:
Detailed descriptions of the Minimax algorithm and Alpha-Beta Pruning are included, along with their roles in the Tic-Tac-Toe AI implementation.

# Execution and Interactions:
Screenshots or images illustrating the program's execution and user interactions are included.
Visual aids help users understand how the game progresses and how moves are made by both the human player and the AI.

# Conclusion:
The Tic-Tac-Toe AI project demonstrates the application of game theory and search algorithms in developing an intelligent game-playing agent. By implementing Minimax with and without Alpha-Beta Pruning, developers gain insights into optimizing AI performance and achieving unbeatable gameplay. Comprehensive documentation enhances understanding and serves as a valuable resource for future development and learning.
