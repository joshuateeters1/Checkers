EMPTY = 0
NUM_ROWS = 8
NUM_COLUMNS = 8
RED = 'r'
WHITE = 'w'
RED_KING = 'R'
WHITE_KING = 'W'
OOB = '.'
letterToNumber = {'a': 0,'b': 1,'c': 2,'d': 3,'e': 4,'f': 5,'g': 6,'h': 7}

class Board:
    board = []

    def clearBoard(self):
        for i in range(NUM_COLUMNS):
            col = []
            for j in range(NUM_ROWS):
                col.append(EMPTY)
            self.board.append(col)

    def __init__(self):
        self.resetBoard()

    def setStartingPositions(self):
        self.board[self.conv('f')][8 - 1] = WHITE
        self.board[self.conv('h')][8 - 1] = WHITE
        self.board[self.conv('b')][8 - 1] = WHITE
        self.board[self.conv('d')][8 - 1] = WHITE
        self.board[self.conv('a')][7 - 1] = WHITE
        self.board[self.conv('c')][7 - 1] = WHITE
        self.board[self.conv('e')][7 - 1] = WHITE
        self.board[self.conv('g')][7 - 1] = WHITE
        self.board[self.conv('b')][6 - 1] = WHITE
        self.board[self.conv('d')][6 - 1] = WHITE
        self.board[self.conv('f')][6 - 1] = WHITE
        self.board[self.conv('h')][6 - 1] = WHITE
        self.board[self.conv('a')][3 - 1] = RED
        self.board[self.conv('c')][3 - 1] = RED
        self.board[self.conv('e')][3 - 1] = RED
        self.board[self.conv('g')][3 - 1] = RED
        self.board[self.conv('b')][2 - 1] = RED
        self.board[self.conv('d')][2 - 1] = RED
        self.board[self.conv('f')][2 - 1] = RED
        self.board[self.conv('h')][2 - 1] = RED
        self.board[self.conv('a')][1 - 1] = RED
        self.board[self.conv('c')][1 - 1] = RED
        self.board[self.conv('e')][1 - 1] = RED
        self.board[self.conv('g')][1 - 1] = RED

    def resetBoard(self):
        self.board = []
        self.clearBoard()
        self.setStartingPositions()

    def printBoard(self):
        for row in range(NUM_ROWS):
            row = NUM_ROWS - row - 1
            for col in range(NUM_COLUMNS):
                print(self.board[col][row], end='')
            print()

    def conv(self, col):
        return letterToNumber[col]

    def set(self, col, row, value):
        col = self.conv(col)
        row -= 1
        self.board[col][row] = value

    def get(self, col, row):
        if not self.isInBounds(col, row):
            return self.board[conv(col)][row - 1]

    def isInBounds(self, col, row):
        return col < NUM_COLUMNS and col >= 0 and row < NUM_ROWS and row >= 0

    def getLegalMoves(self, col, row):
        col = self.conv(col)
        row -= 1
        #Check if in bounds
        if not self.isInBounds(col, row):
            return []
        piece = self.board[col][row]
        #Check if space is empty
        if piece is EMPTY:
            return []

        legalMoves = []
        tlPiece = None
        trPiece = None
        blPiece = None
        brPiece = None
        if self.isInBounds(col - 1, row + 1):
            tlPiece = self.board[col - 1][row + 1]
        if self.isInBounds(col + 1, row + 1):
            trPiece = self.board[col + 1][row + 1]
        if self.isInBounds(col - 1, row - 1):
            blPiece = self.board[col - 1][row - 1]
        if self.isInBounds(col + 1, row - 1):
            brPiece = self.board[col + 1][row - 1]

        if piece is RED:
            if self.isInBounds(col - 1, row + 1):

                if board[col][row] is EMPTY:
                    legalMoves.append((col, row))
                #else if board[col]
