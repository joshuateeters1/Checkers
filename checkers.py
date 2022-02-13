import sys
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))
from board import Board
from visualization import Visual

board = Board()
visual = Visual()

print(os.getcwd())
#print the board
board.printBoard()

#visual.updateVisual(board)
