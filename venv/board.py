import pygame
from constants import GRAY, AQUA, ROWS, WHITE, SQUARE_SIZE, COLS, YELLOW, RED

class Board:
    def __init__(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]]
        self.selected_piece = None
        self.winner = False

    def drawBoard(self, win):
        win.fill(AQUA)
        for col in range(len(self.board[0])):
            for row in range(len(self.board)):
                if self.board[row][col] == 0:
                    pygame.draw.circle(win, WHITE, (col * SQUARE_SIZE - SQUARE_SIZE / 2 + SQUARE_SIZE + 145,
                                                    row * SQUARE_SIZE - SQUARE_SIZE / 2 + SQUARE_SIZE),
                                       SQUARE_SIZE / 2 - 5)
                elif self.board[row][col] == 1:
                    pygame.draw.circle(win, YELLOW, (col * SQUARE_SIZE - SQUARE_SIZE / 2 + SQUARE_SIZE + 145,
                                                     row * SQUARE_SIZE - SQUARE_SIZE / 2 + SQUARE_SIZE),
                                       SQUARE_SIZE / 2 - 5)
                else:
                    pygame.draw.circle(win, RED, (col * SQUARE_SIZE - SQUARE_SIZE / 2 + SQUARE_SIZE + 145,
                                                  row * SQUARE_SIZE - SQUARE_SIZE / 2 + SQUARE_SIZE),
                                       SQUARE_SIZE / 2 - 5)

            pygame.draw.rect(win, GRAY, pygame.Rect(col * SQUARE_SIZE + 165, 640, 60, 50))

        for i in range(ROWS):
            print (self.board[i])
        print()

    def IsFull(self, col):
        for row in range(len(self.board)):
            if board[row][col] == 0:
                return False
        return True

    def updateBoard(self, col, PL, win):
        pos = 5
        num = 5
        if IsFull(col) == True:
            pass
        for row in range(6):
            if self.board[num][col] == 0:
                pos = num
                break
            num = num - 1
        self.board[pos][col] = (PL)