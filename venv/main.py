import pygame

from move import Play
from constants import WIDTH, HEIGHT
from board import Board

play = Play()
class Main:

    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Connect 4')

    def main(self): # runs the game aspect of our code
        clock = pygame.time.Clock()
        board = Board()
        play = Play()
        PL = 1
        while board.Winner() == False: # while there is no winner
            clock.tick(60)
            board.drawBoard(self.WIN) # draws the board
            num = play.move(PL, self.WIN) # gets the column that is selected on each turn
            board.updateBoard(num, PL, self.WIN) # updates the board
            if PL == 1: # if player one's turn switch it to player 2
                PL = 2
            else: # if player two's turn switch to player 1
                PL = 1
                pygame.display.update()
        if board.Winner() == True:
            if PL == 1:  # if player one's turn switch it to player 2
                PL = 2
            else:  # if player two's turn switch to player 1
                PL = 1
            return PL
        pygame.display.update()
