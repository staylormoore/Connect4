import pygame

from move import Play
from constants import WIDTH, HEIGHT
from board import Board

play = Play()
class Main:

    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Connect 4')

    def main(self):
        run = True
        clock = pygame.time.Clock()
        board = Board()
        play = Play()
        PL = 1
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                while not play.Winner():
                    board.draw_squares(self.WIN)
                    num = play.move(PL, self.WIN)
                    board.fall(num, PL, self.WIN)
                    if PL == 1:
                        PL = 2
                    else:
                        PL = 1
                    pygame.display.update()
            pygame.display.update()
