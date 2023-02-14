"""
This will be responsible for dealing with user input and displaying the updated game.
"""

import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQUARE_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 #For animations later
IMAGES = {}


#Initialize global dictionary of images to be called once in main.
def loadImages():
    pieces = ["wP","wR","wN","wB","wQ","wK","bP","bR","bN","bB","bQ","bK",]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/"+ piece +".png"), (SQUARE_SIZE,SQUARE_SIZE))


#Main driver for the code, handling user input and upating graphics
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gameState = ChessEngine.GameState()
    loadImages()
    running = True
    squareSelected = () #keeps track of last square clicked by user
    playerClicks = [] #keeps track of player clicks, where a piece is moved to from its initial location

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() #this is the x and y coordinates of the mouse
                row = location[1] // SQUARE_SIZE
                column = location[0] // SQUARE_SIZE
                if squareSelected == (row,column): #if user clicked same square twice
                    squareSelected  = ()
                    playerClicks = []
                else:
                    squareSelected = (row,column)
                    playerClicks.append(squareSelected)
                if len(playerClicks) == 2:
                    move = ChessEngine.Move(playerClicks[0],playerClicks[1],gameState.board)
                    print(move.getChessNotation())
                    gameState.makeMove(move)
                    squareSelected = ()
                    playerClicks = [] #resets user clicks

        drawGameState(screen, gameState)
        clock.tick(MAX_FPS)
        p.display.flip()


#Responsible for graphics of current game state
def drawGameState(screen, gameState):
    drawBoard(screen) #draws square  on board
    drawPieces(screen,gameState.board) #draws pieces on top of the squares

#Draws squares on board
def drawBoard(screen):
    colours = [p.Color("white"),p.Color("gray")]
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            colour = colours[(i + j) % 2]
            p.draw.rect(screen,colour,p.Rect(j*SQUARE_SIZE, i*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


#Draws pieces on board
def drawPieces(screen, board):
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            piece = board[i][j]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(j*SQUARE_SIZE, i*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


if __name__ == "__main__":
    main()








