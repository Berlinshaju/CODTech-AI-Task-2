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

**AI Move Calculation:** After the user's move, the AI player calculates its move using the Minimax algorithm with or without Alpha-Beta Pruning. This involves evaluating possible future game states to determine the best move.
**AI Move Execution:** The AI player places its mark (X or O) on the board based on the calculated move.
**Game Continuation:** The game continues until a player wins, the game ends in a draw, or the user quits. After each move, the program checks for win conditions and updates the game state accordingly.
**Game Over:** When the game concludes, the program displays the final state of the board and announces the winner or declares a draw.
# Conclusion:
The Tic-Tac-Toe AI project provides an opportunity to implement advanced algorithms in a practical context. By creating an unbeatable AI opponent, developers gain insights into game theory and search algorithms. Comprehensive documentation enhances understanding and facilitates future development.

<img width="518" alt="image" src="https://github.com/Berlinshaju/CODTech-AI-Task-2/assets/66897078/7ee99f8d-7f50-4f00-a6f2-481ef439cbd9">
Top-Left (Position 0): Enter 0 0.
Top-Middle (Position 1): Enter 0 1.
Top-Right (Position 2): Enter 0 2.
Middle-Left (Position 3): Enter 1 0.
Center (Position 4): Enter 1 1.
Middle-Right (Position 5): Enter 1 2.
Bottom-Left (Position 6): Enter 2 0.
Bottom-Middle (Position 7): Enter 2 1.
Bottom-Right (Position 8): Enter 2 2.

**User Interaction:**
<img width="518" alt="image" src="https://github.com/Berlinshaju/CODTech-AI-Task-2/assets/66897078/7ee99f8d-7f50-4f00-a6f2-481ef439cbd9">

**Initial State:** The user is presented with an empty game board and prompted to make the first move.

**Image Caption:** The screenshot shows the initial state of the game board with an empty grid and prompts the user to make the first move.

<img width="960" alt="image" src="https://github.com/Berlinshaju/CODTech-AI-Task-2/assets/66897078/63e12e1c-dd2c-4c54-a054-9c6ca577dda4">

**User Move:** The user selects a cell to place their mark (O) on the board.

**Image Caption:** The screenshot shows the user selecting a cell to place their mark (O) on the board.

**AI Move:** The AI player calculates its move and places its mark (X) on the board.
**Image Caption:** The screenshot shows the AI player calculating its move and placing its mark (X) on the board.
**Game Over:** The final state of the board is displayed, announcing the winner or declaring a draw.
**Image Caption:** The screenshot shows the final state of the game board with the AI player winning the game.
