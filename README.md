**Introduction**
This project focuses on creating a terminal-based implementation of the classic game Connect 4 using Python. 
The goal is to develop an interactive program where players can input their moves directly in the terminal, enhancing user engagement with real-time feedback. 
Alongside coding the game, the project incorporates the use of Git for version control, command-line tools for file navigation, and culminates in a technical blog post documenting the development process. 
Prerequisites for this project include familiarity with Python, Git/GitHub, and basic command-line operations. This README wills serve as a technical blog post.

**Project Objectives:** 
+ Build a terminal program using Python
+ Add at least one interactive feature using input()
+ Use Git version control
+ Use the command line and file navigation
+ Write a technical blog post on the project

**Prerequisites:**
+ Python
+ Git/GitHub
+ Command Line and File Navigation

**Project Brainstorming**
What does your program do?
  + The program will display grid-like board, that shows available slots and slots already occupied by pieces of their red or yellow player 
How will it work in a terminal?
 + Basic call to the main.py should run the game
 + Users will need download python 
Is it one player or two players?
 + The game is two player.
 + I might add a feature allowing players to play against the computer in the future.

**Checking the game board**
Basically, every time a piece is added to the board, we need to check if a Connect Four has occurred. 
The easiest checks would be for vertical and horizontal connections. 
The more "tricky" ones would involve diagonal connections, for which we will need separate logic for both negative and positive slopes. 
Additionally, we need to account for "dead zones," or areas where it would be impossible to get a Connect Four.
The cases are visualized below:
![blog](https://github.com/user-attachments/assets/661f7ca2-e43b-42d4-b4e2-c7b0ed76590e)

**Adding a new piece.**
The logic needs to take into account the following:
 + The player can insert a new piece only if the slot is not already occupied. 
 + Additionally, except for the first row, the player should only be able to add a piece to slots that have an empty slot below them. 
 + This part will be tedious to program.
 + After every new piece added we should check for connections.
 + We should refresh the screen with every addition as well; otherwise, the terminal would get cluttered.
