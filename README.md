__Name:__ Berlin Shaju Bellarmin
__ID:__  COD7119
__Domain:__  Artifical Intelligence
__Mentor:__  Sravani Gouni

# AI TASK TWO: TIC-TAC-TOE AI

# Objective:
The objective of this project is to implement an AI agent capable of playing Tic-Tac-Toe against a human player. The AI should utilize algorithms such as Minimax with or without Alpha-Beta Pruning to create an unbeatable opponent. This project provides an opportunity to explore game theory and basic search algorithms.

# Code Explanation:
# Game Representation:
The Tic-Tac-Toe game is represented as a 3x3 grid, where each cell can be empty, contain a player's mark (X or O), or represent an AI move.

# Game Logic:
The game logic handles the rules of Tic-Tac-Toe, including checking for wins, draws, and valid moves. It also provides functions for the AI player to make moves using the Minimax algorithm with or without Alpha-Beta Pruning.

# User Interface:
A graphical user interface (GUI) can be implemented using a library like Tkinter to allow users to interact with the game board.

# Documentation:
Comprehensive documentation includes detailed explanations of the code, algorithms used, and user interactions. Visual aids such as images or screenshots illustrate the program's execution and gameplay to enhance understanding.

# Program Execution:
Initialization: The game initializes with an empty game board and prompts the user to make the first move.
User Move: The user selects a cell to place their mark (X or O) on the board. The program checks for the validity of the move and updates the board accordingly.

# AI Move Calculation: 
After the user's move, the AI player calculates its move using the Minimax algorithm with or without Alpha-Beta Pruning. This involves evaluating possible future game states to determine the best move.

# AI Move Execution: 
The AI player places its mark (X or O) on the board based on the calculated move.

# Game Continuation: 
The game continues until a player wins, the game ends in a draw, or the user quits. After each move, the program checks for win conditions and updates the game state accordingly.

# Game Over: 
When the game concludes, the program displays the final state of the board and announces the winner or declares a draw.

# Conclusion:
The Tic-Tac-Toe AI project provides an opportunity to implement advanced algorithms in a practical context. By creating an unbeatable AI opponent, developers gain insights into game theory and search algorithms. Comprehensive documentation enhances understanding and facilitates future development.

# how to play Tic-Tac-Toe:
<img width="518" alt="image" src="https://github.com/Berlinshaju/CODTech-AI-Task-2/assets/66897078/7ee99f8d-7f50-4f00-a6f2-481ef439cbd9">

# Top-Left (Position 0): Enter 0 0.
# Top-Middle (Position 1): Enter 0 1.
# Top-Right (Position 2): Enter 0 2.
# Middle-Left (Position 3): Enter 1 0.
# Center (Position 4): Enter 1 1.
# Middle-Right (Position 5): Enter 1 2.
# Bottom-Left (Position 6): Enter 2 0.
# Bottom-Middle (Position 7): Enter 2 1.
# Bottom-Right (Position 8): Enter 2 2.

__Welcome Message:__ When you start the game, you'll see a welcome message and an empty 3x3 grid representing the Tic-Tac-Toe board:

<img width="876" alt="image" src="https://github.com/Berlinshaju/CODTech-AI-Task-2/assets/66897078/514405ca-582d-4c39-b5e6-b46416fb6244">

__Enter Move:__ You'll be prompted to enter the row and column numbers where you want to place your mark (X or O). Rows and columns are numbered from 0 to 2, starting from the top-left corner. For example, to place your mark in the top-right corner, you would enter 0 2.

<img width="884" alt="image" src="https://github.com/Berlinshaju/CODTech-AI-Task-2/assets/66897078/d00830e4-032e-4e0e-845e-301fd3427100">

__Game Progression:__ After you enter your move, the game board will be updated to reflect your move. The AI will then make its move, and the board will be updated again.

__Winning or Draw:__ The game continues until one player wins by getting three of their marks in a row, column, or diagonal, or until the board is full (resulting in a draw).

__Game Over:__ When the game ends, the final board state will be displayed along with the outcome (win, lose, or draw).

__Restart:__ You can choose to play again if you'd like.


__User Interaction:__

<img width="518" alt="image" src="https://github.com/Berlinshaju/CODTech-AI-Task-2/assets/66897078/7ee99f8d-7f50-4f00-a6f2-481ef439cbd9">

__Initial State:__ The user is presented with an empty game board and prompted to make the first move.

![image](https://github.com/Berlinshaju/CODTech-AI-Task-2/assets/66897078/549609ed-1216-4268-8f74-685b70a011e4)

__Image Caption:__ The screenshot shows the initial state of the game board with an empty grid and prompts the user to make the first move.

<img width="960" alt="image" src="https://github.com/Berlinshaju/CODTech-AI-Task-2/assets/66897078/63e12e1c-dd2c-4c54-a054-9c6ca577dda4">

__User Move:__ The user selects a cell to place their mark (O) on the board.

<img width="955" alt="image" src="https://github.com/Berlinshaju/CODTech-AI-Task-2/assets/66897078/3761d986-cf98-4e48-a393-27eced3bed76">

__Image Caption:__ The screenshot shows the user selecting a cell to place their mark (O) on the board.

__AI Move:__ The AI player calculates its move and places its mark (X) on the board.

<img width="960" alt="image" src="https://github.com/Berlinshaju/CODTech-AI-Task-2/assets/66897078/fce032a9-7607-414c-82ee-e5f31f493d50">

__Image Caption:__ The screenshot shows the AI player calculating its move and placing its mark (X) on the board.

<img width="960" alt="image" src="https://github.com/Berlinshaju/CODTech-AI-Task-2/assets/66897078/18b4017c-46de-4474-8d53-c815d90d12b2">

__Game Over:__ The final state of the board is displayed, announcing the winner or declaring a draw.

<img width="960" alt="image" src="https://github.com/Berlinshaju/CODTech-AI-Task-2/assets/66897078/68317024-b0c6-4377-901a-bcda75778784">

__Image Caption:__ The screenshot shows the final state of the game board with the AI player winning the game.


