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
        # This will basically be two dimensional list
        self.Gameboard = []
        for i in range(0, self.ROWS):
            self.Gameboard.append(["⚫" for i in range(0, self.COLUMNS)])
        pass
    def printGameboard(self):
        
        for row in self.Gameboard:
            print(row)
        pass
    
    # We will need to know the color, row, and column
    def addNewPiece(self, Color, Row, Column):
        Row *= -1
        Column -=1
        # The player will input the rows as 1-6 and columns as 1-7
            # For the rows we just use negative indecies
            # as for the columns we remove one.
        # For the first row it does not matter
        # But second row and beyond we can not insert the piece unless the piece bellow is also occupied
        if Row == -1:
            self.Gameboard[Row][Column] = Color
        else:
            if self.Gameboard[Row-1][Column] ==  "⚫":
                print("You must chose another slot.\n")
            else:
                self.Gameboard[Row][Column] = Color
        pass # Pass for now but I might need to update this part of the code to return a boolean value to check before refreshing the terminal.
        
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
    


ngb = Gameboard()
ngb.createGameboard()
 


