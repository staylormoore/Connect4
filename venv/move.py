import pygame
from pygame import mouse

from constants import BLACK, WIDTH, HEIGHT, WHITE, YELLOW, RED, AQUA
class Play:
    # def __init__(self, player, ):
       #  self.player = player

    def Winner(self):
        return False

    def move(self, player, WIN):
        while self.Winner() == False:
            for event in pygame.event.get():
                pygame.init()
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render(('Player ' + str(player)), True, BLACK)
                WIN.blit(text, [10, 110])
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # click sound goes here
                    mx, my = mouse.get_pos()
                    if mx >= 165 and mx <= 225 and my >= 640 and my <= 690:
                        return 0
                    elif mx >= 270 and mx <= 330 and my >= 640 and my <= 690:
                        return 1
                    elif mx >= 375 and mx <= 435 and my >= 640 and my <= 690:
                        return 2
                    elif mx >= 480 and mx <= 540 and my >= 640 and my <= 690:
                        return 3
                    elif mx >= 585 and mx <= 645 and my >= 640 and my <= 690:
                        return 4
                    elif mx >= 690 and mx <= 750 and my >= 640 and my <= 690:
                        return 5
                    elif mx >= 795 and mx <= 855 and my >= 640 and my <= 690:
                        return 6
                    print(player)
                    pygame.display.update()
                pygame.display.update()
            pygame.display.update()
