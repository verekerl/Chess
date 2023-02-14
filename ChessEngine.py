"""
This class will be where all the information/data is to be stored about the chess game. Responsible for determining
whether a move is legal or illegal depending on the board at the time.
"""

class GameState():
    def __init__(self):
        #8x8 board in 2d array
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.whiteToMove = True
        self.moveLog = []

    def makeMove(self, move):
        self.board[move.startRow][move.startColumn] = "--"
        self.board[move.endRow][move.endColumn] = move.pieceMoved
        self.moveLog.append(move) #logs move so it can be undone later
        self.whiteToMove = not self.whiteToMove #switches turns


class Move():
    #maps keys to values
    #key : value
    ranksToRows = {"1": 7, "2": 6, "3": 5 ,"4": 4, "5": 3, "6": 2, "7": 1,"8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToColumns = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    columnsToFiles = {v: k for k, v in filesToColumns.items()}


    def __init__(self,startSquare,endSquare,board):
        self.startRow = startSquare[0]
        self.startColumn = startSquare[1]
        self.endRow = endSquare[0]
        self.endColumn = endSquare[1]
        self.pieceMoved = board[self.startRow][self.startColumn]
        self.pieceCaptured = board[self.endRow][self.endColumn]


    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startColumn) + self.getRankFile(self.endRow, self.endColumn)

    def getRankFile(self,row,column):
        return self.columnsToFiles[column] + self.rowsToRanks[row]