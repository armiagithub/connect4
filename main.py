import gameboard
import player


def playerAction(Player, Gameboard):
   
   while True:
    try:
        RowInput, ColumnInput = map(int, input(f"{Player.Name} Where do you want to place your checker? (row column): ").split())
        # Add new piece to the board
        if RowInput > 0 and ColumnInput > 0:
            if Gameboard.addNewPiece(Player.CheckerColor, RowInput, ColumnInput) == True:
                break      
            else:
                continue 
        else:
           continue
    except ValueError:
        print("Your input must be a valid value")
        continue



# Game starts here
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
    # Loop and game logic
    while True:

        playerAction(RPLayer, NewGameBoard)
        if NewGameBoard.connectFour(RPLayer.CheckerColor) == True:
           NewGameBoard.printGameboard()
           print(f"{RPLayer.Name} has won the game. Congratulations!")
           break
        NewGameBoard.printGameboard()
        print(" ")
        playerAction(YPLayer, NewGameBoard)
        if NewGameBoard.connectFour(YPLayer.CheckerColor) == True:
           NewGameBoard.printGameboard()
           print(f"{YPLayer.Name} has won the game. Congratulations!")
           break
        NewGameBoard.printGameboard()
        print(" ")
        # Check if neither player has connected
        if NewGameBoard.checkIfGameOver() == True:
           print("Game over.")
           break

def main():
   print("Hello and welcome to the terminal version of Connect four.")
   print("To win the game you must connect four pieces either horizontally, vertically, or diagonally.")
   print("This version is a two player game.\n")

   while True:
    try:
     Choice = int(input("Enter 1 to start a new game or 0 to quit: "))
     if Choice == 1:
        startGame()
        continue
     elif Choice == 0:
        print("\nThank you for playing our game.")
        break
     else:
        print("Invalid input.")
        continue
    except ValueError:
       print("Your input must be an int.")
       continue

main()

