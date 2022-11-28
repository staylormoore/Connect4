import pygame
from pygame import mouse
from board import Board

from constants import BLACK, WIDTH, HEIGHT, WHITE, YELLOW, RED, AQUA


class Play:
    # def __init__(self, player, ):
       #  self.player = player

    def Winner(self):
        # check horizontal for win
        for c in range(COL):
            for r in range(ROW):
                piece = self.board[r][c]
                if self.board[r][c + 1] == piece and self.board[r][c + 2] == piece and self.board[r][c + 3] == piece:
                    return True

        # Check vertical locations for win
        for c in range(COL):
            for r in range(ROW):
                piece = self.board[r][c]
                if self.board[r + 1][c] == piece and self.board[r + 2][c] == piece and self.board[r + 3][c] == piece:
                    return True

        # Check positively sloped diaganols
        for c in range(COL):
            for r in range(ROW):
                piece = self.board[r][c]
                if board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                    return True

        # Check negatively sloped diaganols
        for c in range(COL):
            for r in range(ROW):
                piece = self.board[r][c]
                if self.board[r - 1][c + 1] == piece and \
                        self.board[r - 2][c + 2] == piece and self.board[r - 3][c + 3] == piece:
                    return True

    def move(self, player, WIN):
        while self.Winner() is False:
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
