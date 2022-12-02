import pygame
from pygame import mouse

from constants import BLACK, WIDTH, HEIGHT, WHITE, YELLOW, RED, AQUA


class Play:
    # def __init__(self, player, ):
    #  self.player = player

    def Winner(self):
        return False

    def button(self, WIN, event):
        color_light = RED  # light shade of the button
        color_dark = (205, 38, 38)  # dark shade of the button
        small_font = pygame.font.SysFont('Roboto', 35)
        text = small_font.render('QUIT', True, WHITE)  # rendering a text written in this font
        mx, my = mouse.get_pos()  # gets the position of the mouse
        if 20 <= mx <= 120 and 600 <= my <= 640:  # if mouse is hovered over the button, it changes to lighter shade
            pygame.draw.rect(WIN, color_light, [20, 600, 120, 40])
        else:
            pygame.draw.rect(WIN, color_dark, [20, 600, 120, 40])
        WIN.blit(text, (48, 610))  # superimposing the text onto the button
        pygame.display.update()  # updates the frames of the game
        if event.type == pygame.MOUSEBUTTONDOWN:  # if the mouse is clicked on the button the game is terminated
            if 20 <= mx <= 120 and 600 <= my <= 640:  # only when the button is
                # clicked
                pygame.quit()

    def move(self, player, WIN):
        while not self.Winner():
            for event in pygame.event.get():
                pygame.init()
                font = pygame.font.SysFont('Roboto', 40)
                text = font.render(('Player ' + str(player)), True, WHITE)
                WIN.blit(text, [10, 110])
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # click sound goes here
                    mx, my = mouse.get_pos()
                    if 165 <= mx <= 225 and 640 <= my <= 690:
                        return 0
                    elif 270 <= mx <= 330 and 640 <= my <= 690:
                        return 1
                    elif 375 <= mx <= 435 and 640 <= my <= 690:
                        return 2
                    elif 480 <= mx <= 540 and 640 <= my <= 690:
                        return 3
                    elif 585 <= mx <= 645 and 640 <= my <= 690:
                        return 4
                    elif 690 <= mx <= 750 and my >= 640 and my <= 690:
                        return 5
                    elif 795 <= mx <= 855 and 640 <= my <= 690:
                        return 6
                    print(player)
                    pygame.display.update()
                pygame.display.update()

                self.button(WIN, event)
            pygame.display.update()
