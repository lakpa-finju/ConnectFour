# Implementation of ConnectFour game, with one user player and
# one computer player.
# Original Code by Sara Sprenkle
# Modified By Lakpa Sherpa

import csplot
import random
from time import sleep

def main():
    "Plays Connect Four game."
    game = ConnectFour()
    game.showBoard()
    game.play()


class ConnectFour:
    """ Class representing the game Connect Four. """

    # Represent different values on the board
    FREE = 0
    PLAYER1 = 1
    PLAYER2 = 2
    
    # Represent the dimensions of the board
    ROWS = 6
    COLS = 7

    # dictionary of number-->color mappings
    repToColor = {FREE:'yellow', PLAYER1:'red', PLAYER2:'black'}

    def __init__(self):
        """ Create the board, initially empty"""
        self._board = createBoard(ConnectFour.ROWS, ConnectFour.COLS, ConnectFour.FREE)

    def _isValidMove(self, col):
        """ Return True iff the dropping a checker in this col (an int)
        represents a valid move. """
        return self._board[ConnectFour.ROWS-1][col] == ConnectFour.FREE

    def makeMove(self, whichplayer, col):
       """Change the board so that //whichplayer// occupies
           the next (vertical) spot in the column.
            Procondition: the col is a valid move.
            Returns the index of the row where the checker is placed."""
       for row in range(ConnectFour.ROWS):
            if self._board[row][col] == ConnectFour.FREE:
               self._board[row][col]=whichplayer
               return row
            
        

    def showBoard(self):
        csplot.show(self._board, ConnectFour.repToColor)

    def _isDraw(self):
        """ Return True iff the game is a draw because 
        there are no free/empty spots."""
        Row = ConnectFour.ROWS-1
        freeSpace = 0
        for col in range(ConnectFour.COLS):
            if self._isValidMove(col):
                return False
        return True
    
    def _isWon(self, row, col):
        """ Return True iff the most recent player won."""
        
        # look around position [row][col] on board
        whichplayer = self._board[row][col]
        total =0
        # vertically (down)
        for i in range(row,-1,-1):
            if self._board[i][col]==whichplayer:
                total+=1
                if total ==4:
                    return True
            else:
                total =0
         
            
        # horizontally
        total = 0
        for i in range(ConnectFour.COLS):
            if self._board[row][i]==whichplayer:
                total+=1
                if total ==4:
                    return True
            else:
                total =0
        # diagonally
        total = 0
        tempRow = row 
        tempCol = col 
        for i in range(tempCol,-1,-1):
            if self._board[tempRow][i]==whichplayer:
                total +=1
                
                if total==4:
                    return True
                tempRow-=1
            else:
                total =0
                tempRow=-1
        tempRow = row 
        tempCol = col 
        for col in range(tempCol,6):
            if self._board[tempRow][col]==whichplayer:
                total +=1
                
                if total==4:
                    return True
                tempRow-=1
                if tempRow ==-1:
                    break
            else:
                total =0
                tempRow=-1
                
            
        return False

    def _userMakeMove(self):
        """ Allow the user to pick a column. 
        Returns the column that the user chose to put its checker."""
        col = csplot.sqinput()
        validMove = self._isValidMove(col)
        while not validMove:
            print("NOT A VALID MOVE.")
            print("PLEASE SELECT AGAIN.")
            print()
            col = csplot.sqinput()
            validMove = self._isValidMove(col)
        return col
        
    def _computerMakeMove(self):
        """Make a move on behalf the computer.
        Returns the column that the computer chose
        to put its checker. """
        # Pick a random column
        col = random.randint(0, ConnectFour.COLS-1)
        validMove = self._isValidMove(col)
        while not validMove:
            col = random.randint(0, ConnectFour.COLS-1)
            validMove = self._isValidMove(col)
        return col 
        
    def play(self):
        won = False
        player = ConnectFour.PLAYER1
        
        # also handle draws besides wins...
        while not won:
            print("Player {:d}'s move".format(player))
            if player == ConnectFour.PLAYER1:
                col = self._userMakeMove()
            else: # computer is player 2
                # pause because otherwise move happens to quickly
                # and looks like an error
                sleep(.75)
                col = self._computerMakeMove()
                
            # LAB 11: After implementing the makeMove method above,
            # uncomment the next two lines and test your program
            row = self.makeMove(player, col)
            self.showBoard()

            # EC TODO: 
            won = self._isWon(row, col)
            if won==True:
                whichplayer= self._board[row][col]
                print(whichplayer,"has won the game")
                
            if self._isDraw()==True:
                print("The game is draw!")
                return
            # alternate players
            player = player % 2 + 1


# The following two functions are not part of the ConnectFour class
# because they could be used by other classes/programs/modules.  They
# could go into a separate file/module, but, for simplicity, let's
# keep them here.
        
def createBoard(height, width, value):
    """Returns a board (2D list) with the passed in width and
    height and filled with //value//."""
    board = []
    for x in range(height):
        board.append(createOneRow(width, value))
    return board

            
def createOneRow( n, value ):
    """ returns a list of size n, filled with the //value//...  
    You might use this as the INNER loop in createBoard. """
    row = []
    for col in range(n):
        row.append(value)
    return row


main()
