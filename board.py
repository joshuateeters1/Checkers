class Board:
    NUM_ROWS = 8
    NUM_COLUMNS = 8
    RED = 'r'
    BLACK = 'b'
    RED_KING = 'R'
    BLACK_KING = 'B'
    EMPTY = '-'
    OOB = '.'
    letterToNumber = {'a': 0,'b': 1,'c': 2,'d': 3,'e': 4,'f': 5,'g': 6,'h': 7}

    board = []

    def __init__(self):
        self.resetBoard()

    def conv(self, col):
        return self.letterToNumber[col]

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
        for i in range(self.NUM_COLUMNS):
            col = []
            for j in range(self.NUM_ROWS):
                col.append(self.EMPTY)
            self.board.append(col)

    def setStartingPositions(self):
        self.setChessNotation('f', 8, self.BLACK)
        self.setChessNotation('h', 8, self.BLACK)
        self.setChessNotation('b', 8, self.BLACK)
        self.setChessNotation('d', 8, self.BLACK)
        self.setChessNotation('a', 7, self.BLACK)
        self.setChessNotation('c', 7, self.BLACK)
        self.setChessNotation('e', 7, self.BLACK)
        self.setChessNotation('g', 7, self.BLACK)
        self.setChessNotation('b', 6, self.BLACK)
        self.setChessNotation('d', 6, self.BLACK)
        self.setChessNotation('f', 6, self.BLACK)
        self.setChessNotation('h', 6, self.BLACK)
        self.setChessNotation('a', 3, self.RED)
        self.setChessNotation('c', 3, self.RED)
        self.setChessNotation('e', 3, self.RED)
        self.setChessNotation('g', 3, self.RED)
        self.setChessNotation('b', 2, self.RED)
        self.setChessNotation('d', 2, self.RED)
        self.setChessNotation('f', 2, self.RED)
        self.setChessNotation('h', 2, self.RED)
        self.setChessNotation('a', 1, self.RED)
        self.setChessNotation('c', 1, self.RED)
        self.setChessNotation('e', 1, self.RED)
        self.setChessNotation('g', 1, self.RED)

    def resetBoard(self):
        self.clearBoard()
        self.setStartingPositions()

    def printBoard(self):
        for row in range(self.NUM_ROWS):
            row = self.NUM_ROWS - row - 1
            for col in range(self.NUM_COLUMNS):
                print(self.get(col, row), end='')
            print()

    def isInBounds(self, col, row):
        return col < self.NUM_COLUMNS and col >= 0 \
                and row < self.NUM_ROWS and row >= 0

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
        if colorToSwap is self.RED:
            return self.BLACK
        elif colorToSwap is self.BLACK:
            return self.RED
        else:
            raise ValueError("Bad color swap argument")

    def getOppositeColorKing(self, colorToSwap):
        if colorToSwap is self.RED:
            return self.BLACK_KING
        elif colorToSwap is self.BLACK:
            return self.RED_KING
        else:
            raise ValueError("Bad king color swap argument")

    def getLegalMoves(self, col, row):
        piece = self.get(col, row)
        if piece is self.EMPTY or piece is self.OOB:
            return []

        legalMoves = []
        tl = self.getAdjacent(col, row, 'tl')
        tr = self.getAdjacent(col, row, 'tr')
        bl = self.getAdjacent(col, row, 'bl')
        br = self.getAdjacent(col, row, 'br')
        oppositeColor = self.getOppositeColor(piece)
        oppositeColorKing = self.getOppositeColorKing(piece)

        if piece is self.RED or piece is self.RED_KING or piece is self.BLACK_KING:
            if tl is self.EMPTY:
                legalMoves.append((col -1, row +1))
            elif tl is oppositeColor or tl is oppositeColorKing and \
              self.getAdjacent(col -1, row +1, 'tl') is self.EMPTY:
                legalMoves.append((col -1 -1, row +1 +1))
            if tr is self.EMPTY:
                legalMoves.append((col +1, row +1))
            elif tr is oppositeColor or tr is oppositeColorKing and \
               self.getAdjacent(col +1, row +1, 'tr') is self.EMPTY:
                legalMoves.append((col +1 +1, row +1 +1))

        if piece is self.BLACK or piece is self.RED_KING or piece is self.BLACK_KING:
            if bl is self.EMPTY:
                legalMoves.append((col -1, row -1))
            elif bl is oppositeColor or bl is oppositeColorKing and \
              self.getAdjacent(col -1, row -1, 'bl') is self.EMPTY:
                legalMoves.append((col -1 -1, row -1 -1))
            if br is self.EMPTY:
                legalMoves.append((col +1, row -1))
            elif br is oppositeColor or br is oppositeColorKing and \
               self.getAdjacent(col +1, row -1, 'br') is self.EMPTY:
                legalMoves.append((col +1 +1, row -1 -1))

        return legalMoves
