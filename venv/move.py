import pygame
from pygame import mouse
from constants import BLACK, WIDTH, HEIGHT, WHITE, YELLOW, RED, AQUA
from board import Board

board = Board()
class Play:

    def move(self, player, WIN): # occurs on each players turn
        while board.Winner() == False: # while a winner has not been found yet
            for event in pygame.event.get(): # documents any events so we can see the mouse has been clicked
                pygame.init()
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render(('Player ' + str(player)), True, BLACK)
                WIN.blit(text, [10, 110])
                if event.type == pygame.MOUSEBUTTONDOWN: # if the mouse is pressed
                    # click sound goes here
                    mx, my = mouse.get_pos() # collects the coordinates of the mouse click
                    if mx >= 165 and mx <= 225 and my >= 640 and my <= 690: # if the first column is chosen
                        return 0
                    elif mx >= 270 and mx <= 330 and my >= 640 and my <= 690: # if the second column is chosen
                        return 1
                    elif mx >= 375 and mx <= 435 and my >= 640 and my <= 690: # if the third column is chosen
                        return 2
                    elif mx >= 480 and mx <= 540 and my >= 640 and my <= 690: # if the fourth column is chosen
                        return 3
                    elif mx >= 585 and mx <= 645 and my >= 640 and my <= 690: # if the fifth column is chosen
                        return 4
                    elif mx >= 690 and mx <= 750 and my >= 640 and my <= 690: # if the sixth column is chosen
                        return 5
                    elif mx >= 795 and mx <= 855 and my >= 640 and my <= 690: # if the seventh column is chosen
                        return 6
                    pygame.display.update()
                pygame.display.update()
            pygame.display.update()
