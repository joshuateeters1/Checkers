NUM_ROWS = 8
NUM_COLUMNS = 8
RED = 'r'
BLACK = 'b'
RED_KING = 'R'
BLACK_KING = 'B'
EMPTY = '-'
OOB = '.'
letterToNumber = {'a': 0,'b': 1,'c': 2,'d': 3,'e': 4,'f': 5,'g': 6,'h': 7}

class Board:
    board = []

    def __init__(self):
        self.resetBoard()

    def conv(self, col):
        return letterToNumber[col]

    def set(self, col, row, value):
        self.board[col][row] = value

    def setChessNotation(self, col, row, value):
        col = self.conv(col)
        row -= 1
        self.set(col, row, value)

    def get(self, col, row):
        if self.isInBounds(col, row):
            return self.board[col][row]
        else:
            return OOB

    def getChessNotation(self, col, row):
        col = self.conv(col)
        row -= 1
        return get(col, row)

    def clearBoard(self):
        self.board = []
        for i in range(NUM_COLUMNS):
            col = []
            for j in range(NUM_ROWS):
                col.append(EMPTY)
            self.board.append(col)

    def setStartingPositions(self):
        self.setChessNotation('f', 8, BLACK)
        self.setChessNotation('h', 8, BLACK)
        self.setChessNotation('b', 8, BLACK)
        self.setChessNotation('d', 8, BLACK)
        self.setChessNotation('a', 7, BLACK)
        self.setChessNotation('c', 7, BLACK)
        self.setChessNotation('e', 7, BLACK)
        self.setChessNotation('g', 7, BLACK)
        self.setChessNotation('b', 6, BLACK)
        self.setChessNotation('d', 6, BLACK)
        self.setChessNotation('f', 6, BLACK)
        self.setChessNotation('h', 6, BLACK)
        self.setChessNotation('a', 3, RED)
        self.setChessNotation('c', 3, RED)
        self.setChessNotation('e', 3, RED)
        self.setChessNotation('g', 3, RED)
        self.setChessNotation('b', 2, RED)
        self.setChessNotation('d', 2, RED)
        self.setChessNotation('f', 2, RED)
        self.setChessNotation('h', 2, RED)
        self.setChessNotation('a', 1, RED)
        self.setChessNotation('c', 1, RED)
        self.setChessNotation('e', 1, RED)
        self.setChessNotation('g', 1, RED)

    def resetBoard(self):
        self.clearBoard()
        self.setStartingPositions()

    def printBoard(self):
        for row in range(NUM_ROWS):
            row = NUM_ROWS - row - 1
            for col in range(NUM_COLUMNS):
                print(self.get(col, row), end='')
            print()

    def isInBounds(self, col, row):
        return col < NUM_COLUMNS and col >= 0 and row < NUM_ROWS and row >= 0

    def isInBoundsChessNotation(self, col, row):
        col = self.conv(col)
        row -= 1
        return self.isInBounds(col, row)

    def getAdjacent(self, col, row, direction):
        if direction == 'tl':
            return self.get(col - 1, row + 1)
        elif direction == 'tr':
            return self.get(col + 1, row + 1)
        elif direction == 'bl':
            return self.get(col - 1, row - 1)
        elif direction == 'br':
            return self.get(col + 1, row - 1)
        else:
            raise ValueError("getAdjacent(col, row, direction) only supports " +
            "'tl', 'tr', 'bl', or 'br' as directions")

    def getAdjacentChessNotation(self, col, row, direction):
        col = self.conv(col)
        row -= 1
        return self.getAdjacent(col, row, direction)

    def getOppositeColor(self, colorToSwap):
        if colorToSwap is RED:
            return BLACK
        elif colorToSwap is BLACK:
            return RED
        else:
            raise ValueError("Bad color swap argument")

    def getOppositeColorKing(self, colorToSwap):
        if colorToSwap is RED:
            return BLACK_KING
        elif colorToSwap is BLACK:
            return RED_KING
        else:
            raise ValueError("Bad king color swap argument")

    def getLegalMoves(self, col, row):
        piece = self.get(col, row)
        if piece is EMPTY or piece is OOB:
            return []

        legalMoves = []
        tl = self.getAdjacent(col, row, 'tl')
        tr = self.getAdjacent(col, row, 'tr')
        bl = self.getAdjacent(col, row, 'bl')
        br = self.getAdjacent(col, row, 'br')
        oppositeColor = self.getOppositeColor(piece)
        oppositeColorKing = self.getOppositeColorKing(piece)

        if piece is RED or piece is RED_KING or piece is BLACK_KING:
            if tl is EMPTY:
                legalMoves.append((col -1, row +1))
            elif tl is oppositeColor or tl is oppositeColorKing and \
              self.getAdjacent(col -1, row +1, 'tl') is EMPTY:
                legalMoves.append((col -1 -1, row +1 +1))
            if tr is EMPTY:
                legalMoves.append((col +1, row +1))
            elif tr is oppositeColor or tr is oppositeColorKing and \
               self.getAdjacent(col +1, row +1, 'tr') is EMPTY:
                legalMoves.append((col +1 +1, row +1 +1))

        if piece is BLACK or piece is RED_KING or piece is BLACK_KING:
            if bl is EMPTY:
                legalMoves.append((col -1, row -1))
            elif bl is oppositeColor or bl is oppositeColorKing and \
              self.getAdjacent(col -1, row -1, 'bl') is EMPTY:
                legalMoves.append((col -1 -1, row -1 -1))
            if br is EMPTY:
                legalMoves.append((col +1, row -1))
            elif br is oppositeColor or br is oppositeColorKing and \
               self.getAdjacent(col +1, row -1, 'br') is EMPTY:
                legalMoves.append((col +1 +1, row -1 -1))

        return legalMoves
