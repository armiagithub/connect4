class Gameboard:
# Here we create the gameboard
# This part of the program will contain most of the game logic:
# 1) Checking available slots
# 2) Checking for possible 4 connections
    def __init__(self):
        self.ROWS = 6
        self.COLUMNS = 7
        self.Gameboard = None

    def createGameboard(self):
        # This will basically be a two-dimensional list.
        self.Gameboard = []
        for i in range(0, self.ROWS):
            self.Gameboard.append(["⚫" for i in range(0, self.COLUMNS)])
        pass
    def printGameboard(self):
        Column = 6
        print("\t      1-7")
        for row in self.Gameboard:
            print(f"{Column} {'  '.join(row)}")
            Column -= 1
        pass
    
    # We will need to know the color, row, and column
    def addNewPiece(self, Color, Row, Column):

        try:
            Placed = False
            Row *= -1
            Column -=1
            # The player will input the rows as 1-6 and columns as 1-7
                # For the rows we just use negative indecies
                # as for the columns we remove one.
            # For the first row, the condition does not matter.
            # For the second row and beyond, the piece cannot be inserted unless the piece below is also occupied.
            if Row == -1:
                # Make sure the slot is not occupied by another piece:
                if self.Gameboard[Row][Column] == "⚫":
                    self.Gameboard[Row][Column] = Color
                    Placed = True
                else:
                    print("This slot is already occupied by another piece.")
            else:
                if self.Gameboard[Row+1][Column] ==  "⚫":
                    print("You must choose another slot.")
                else:
                    self.Gameboard[Row][Column] = Color
                    Placed = True
            return Placed # Boolean value to check if the checker has been placed
        except IndexError:
            print("Your input was out of range.")
        
    # Let's start with the easy ones to check vertical and horizontal connections
    def checkHorizontal(self, Color):
        for c in range(0,self.COLUMNS):
            for r in range(1, self.ROWS-2):
                r *= -1
                if self.Gameboard[r][c] == Color and self.Gameboard[r-1][c] == Color and self.Gameboard[r-2][c] == Color and self.Gameboard[r-3][c] == Color:
                    return True
                
    def checkVertical(self, Color):
        for r in range(1, self.ROWS+1):
            r *= -1
            for c in range(0, self.COLUMNS-3):
                if self.Gameboard[r][c] == Color and self.Gameboard[r][c+1] == Color and self.Gameboard[r][c+2] == Color and self.Gameboard[r][c+3] == Color:
                    return True
    
    def checkDiagonalPositive(self, Color):
        for r in range(1, self.ROWS - 2):
            for c in range(0, self.COLUMNS -3):
                if self.Gameboard[r * -1][c] == Color and  self.Gameboard[(r+1) * -1][c+1] == Color and self.Gameboard[(r+2) * -1][c+2] == Color and self.Gameboard[(r+3) * -1][c+3] == Color:
                    return True
    
    def checkDiagonalNegative(self, Color):
        for r in range(0, self.ROWS - 3):
            for c in range(0, self.COLUMNS - 3):
                if self.Gameboard[r][c] == Color and self.Gameboard[r+1][c+1] == Color and self.Gameboard[r+2][c+2] == Color and self.Gameboard[r+3][c+3] == Color:
                    return True
    

    def connectFour(self, PlayerColor):
        ConnectFour = False

        if self.checkVertical(PlayerColor) == True:
            ConnectFour = True
        elif self.checkHorizontal(PlayerColor) == True:
            ConnectFour = True
        elif self.checkDiagonalPositive(PlayerColor) == True:
            ConnectFour = True
        elif self.checkDiagonalNegative(PlayerColor) == True:
            ConnectFour = True
        
        return ConnectFour
        


    # Game over will occur in the case that there are no more slots left.
    def checkIfGameOver(self):
        GameOver = False
        
        for row in self.Gameboard:
            if row.count('⚫') == 0:
                GameOver = True