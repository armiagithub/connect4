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

   ## Finished project

### The game board
The program will display a **grid-like board** that shows:
- **Available slots** ⚫ and
- **Slots occupied by pieces** of either the red 🔴 or yellow 🟡 player.
  - I could perhaps allow the user to choose an emoji of their choice which could serve as the game piece

### How Will It Work in the Terminal?
- A basic call to `main.py` will run the game.
- Users need to have Python installed to play.

### Is It One Player or Two Players?
- The game is **two-player** by default.
- A feature allowing players to play against the computer may be added in the future.

---

## Code and How It Works

### Code Structure
The codebase is divided into three key components:
1. **`main.py`**: The entry point for running the game and managing the game loop.
2. **`gameboard.py`**: Contains the game board's structure and logic.
3. **`player.py`**: Defines the `Player` class for handling player information.

---

### 1. **Main Game Loop**
The main game loop is in `main.py`. It initializes the players and the game board, then alternates turns between the two players.

```python
def startGame():
    # Create the players
    RPlayerName = input("Player 1 (red checker): What is your name? ")
    RPLayer = player.Player(RPlayerName, '🔴')

    YPlayerName = input("Player 2 (yellow checker): What is your name? ")
    YPLayer = player.Player(YPlayerName, '🟡')
    
    # Create gameboard
    NewGameBoard = gameboard.Gameboard()
    NewGameBoard.createGameboard()
    NewGameBoard.printGameboard()
    
    # Game logic loop
    while True:
        # Player 1 Turn
        playerAction(RPLayer, NewGameBoard)
        if NewGameBoard.connectFour(RPLayer.CheckerColor):
            print(f"{RPLayer.Name} has won the game. Congratulations!")
            break
        
        # Player 2 Turn
        playerAction(YPLayer, NewGameBoard)
        if NewGameBoard.connectFour(YPLayer.CheckerColor):
            print(f"{YPLayer.Name} has won the game. Congratulations!")
            break

        # Check if the game is a draw
        if NewGameBoard.checkIfGameOver():
            print("Game over. It's a draw!")
            break
```

### 2. **Game Board Logic**
The `Gameboard` class in `gameboard.py` manages the grid and implements the logic for:
- Adding new pieces
- Checking for winning conditions
- Printing the board

```python
class Gameboard:
    def createGameboard(self):
        # Initialize a 6x7 grid with empty slots
        self.Gameboard = [["⚫" for _ in range(self.COLUMNS)] for _ in range(self.ROWS)]

    def printGameboard(self):
        # Display the game board
        print("\t  1  2  3  4  5  6  7")
        for row_index, row in enumerate(reversed(self.Gameboard), start=1):
            print(f"{7 - row_index}\t{'  '.join(row)}")
```

### 3. **Adding a New Piece**
Players can only place pieces in valid slots. The logic enforces:
- Slots must be empty.
- Pieces can only be placed if there is a piece or the bottom of the board below them.

```python
def addNewPiece(self, Color, Row, Column):
    try:
        Row = self.ROWS - Row  # Convert to 0-based index
        Column -= 1  # Convert to 0-based index
        
        if self.Gameboard[Row][Column] == "⚫" and (Row == self.ROWS - 1 or self.Gameboard[Row + 1][Column] != "⚫"):
            self.Gameboard[Row][Column] = Color
            return True
        else:
            print("Invalid move. Try again.")
            return False
    except IndexError:
        print("Invalid input. Make sure your row and column are within range!")
        return False
```

---

### 4. **Checking for Winning Conditions**
The game checks for a "Connect Four" using methods for horizontal, vertical, and diagonal searches.

```python
def checkHorizontal(self, Color):
    for row in self.Gameboard:
        for col in range(self.COLUMNS - 3):
            if row[col:col + 4] == [Color] * 4:
                return True
    return False
```

---

## Future Enhancements
1. **Single Player Mode**: Implement AI for a single-player experience.
2. **Node-Based Search Optimization**: Optimize the "Connect Four" check using a graph-based approach for better performance on larger boards.
3. **Enhanced Graphics**: Use libraries like `curses` or `pygame` for a more polished display.

---

## Running the Game
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/connect4.git
   ```
2. Navigate to the project directory:
   ```bash
   cd connect4
   ```
3. Run the game:
   ```bash
   python main.py
   ```

---

 
