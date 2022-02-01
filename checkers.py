import sys
sys.path.append(".")
from board import Board
from visualization import Visual

board = Board()
visual = Visual()

#print the board
board.printBoard()

visual.updateVisual(board)
