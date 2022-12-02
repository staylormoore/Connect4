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

    def draw_squares(self, win):
        win.fill(AQUA)
        # pygame.draw.rect(win, GRAY, (855, 0, 350, 1000))
        for col in range(COLS):
            for row in range (ROWS):
                if self.board[col-1][row] == 0:
                    pygame.draw.circle(win, WHITE, (col * SQUARE_SIZE - SQUARE_SIZE/2 + SQUARE_SIZE + 145, row * SQUARE_SIZE - SQUARE_SIZE/2 + SQUARE_SIZE), SQUARE_SIZE/2 - 5)
                elif self.board[col-1][row] == 1:
                    pygame.draw.circle(win, YELLOW, (col * SQUARE_SIZE - SQUARE_SIZE/2 + SQUARE_SIZE + 145, row * SQUARE_SIZE - SQUARE_SIZE/2 + SQUARE_SIZE), SQUARE_SIZE/2 - 5)
                else:
                    pygame.draw.circle(win, RED, (col * SQUARE_SIZE - SQUARE_SIZE/2 + SQUARE_SIZE + 145, row * SQUARE_SIZE - SQUARE_SIZE/2 + SQUARE_SIZE), SQUARE_SIZE/2 - 5)

            pygame.draw.rect(win, GRAY, pygame.Rect(col * SQUARE_SIZE + 165, 640, 60, 50))

        for i in range(ROWS):
            #for j in range(COLS):
            print (self.board[i])
        print()

    def fall(self, col, PL, win):
        pos = 7
        for row in range(6):
            if self.board[abs(6-row)-1][col] == 0:
                pos = row
            if pos == 7:
                print('error')
            else:
                if PL == 1:
                    pygame.draw.circle(win, YELLOW, (col * SQUARE_SIZE - SQUARE_SIZE/2 + SQUARE_SIZE + 145, row * SQUARE_SIZE - SQUARE_SIZE/2 + SQUARE_SIZE), SQUARE_SIZE/2 - 5)
                else:
                    pygame.draw.circle(win, RED, (col * SQUARE_SIZE - SQUARE_SIZE/2 + SQUARE_SIZE + 145, row * SQUARE_SIZE - SQUARE_SIZE/2 + SQUARE_SIZE), SQUARE_SIZE/2 - 5)
        self.board[pos][col] = PL

