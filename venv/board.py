import pygame
from constants import GRAY, AQUA, ROWS, WHITE, SQUARE_SIZE, COLS, YELLOW, RED


class Board:
    # sets the array for the board
    def __init__(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]]


    def drawBoard(self, win): # Draws the board with circles corrisponding to if the hole is empty, owned by player 1, or owned by player 2
        win.fill(AQUA)
        for col in range(len(self.board[0])): # goes through each column to assign color chip
            for row in range(len(self.board)): # goes through each row to assign color chip
                if self.board[row][col] == 0: # if the slot is empty
                    pygame.draw.circle(win, WHITE, (col * SQUARE_SIZE - SQUARE_SIZE / 2 + SQUARE_SIZE + 145,
                                                    row * SQUARE_SIZE - SQUARE_SIZE / 2 + SQUARE_SIZE),
                                       SQUARE_SIZE / 2 - 5)
                elif self.board[row][col] == 1: # if the slot has been played in by player 1
                    pygame.draw.circle(win, YELLOW, (col * SQUARE_SIZE - SQUARE_SIZE / 2 + SQUARE_SIZE + 145,
                                                     row * SQUARE_SIZE - SQUARE_SIZE / 2 + SQUARE_SIZE),
                                       SQUARE_SIZE / 2 - 5)
                else: # if the slot has been played in by player 2
                    pygame.draw.circle(win, RED, (col * SQUARE_SIZE - SQUARE_SIZE / 2 + SQUARE_SIZE + 145,
                                                  row * SQUARE_SIZE - SQUARE_SIZE / 2 + SQUARE_SIZE),
                                       SQUARE_SIZE / 2 - 5)

            pygame.draw.rect(win, GRAY, pygame.Rect(col * SQUARE_SIZE + 165, 640, 60, 50)) # drawing the buttons at the bottom of each column

        for i in range(ROWS): # prints out board so we can makes sure it is corrilating with the play window
            print (self.board[i])
        print()

    def IsFull(self, col): # returns true if the column the player has selected is full
        for row in range(len(self.board)): # goes through all the rows in the column in question
            if self.board[row][col] == 0: # if there is an empty slot in the column jn question, returns false
                return False
        return True

    def updateBoard(self, col, PL, win): # changes the board with each click of a bottom button
        pos = 5
        num = 5
        if self.IsFull(col) == False: # if the col they selected is not full
            for row in range(6): # repeats for all rows to find the lowest possible one
                if self.board[num][col] == 0: # if the slot is available (empty)
                    pos = num
                    break
                num = num - 1
            self.board[pos][col] = (PL) # sets the empty slot to the corrisponding number for the player


    def Winner(self):  # checks if there is a winner and returns true if so
        # check horizontal for win
        for c in range(4):
            for r in range(6):
                piece = self.board[r][c]
                if piece !=0 and self.board[r][c + 1] == piece and self.board[r][c + 2] == piece and self.board[r][c + 3] == piece:
                    return True

        # Check vertical locations for win
        for c in range(7):
            for r in range(3):
                piece = self.board[r][c]
                if piece !=0 and self.board[r + 1][c] == piece and self.board[r + 2][c] == piece and self.board[r + 3][c] == piece:
                    return True

        # Check positively sloped diaganols
        for c in range(4):
            for r in range(3):
                piece = self.board[r][c]
                if piece !=0 and self.board[r + 1][c + 1] == piece and self.board[r + 2][c + 2] == piece and self.board[r + 3][c + 3] == piece:
                    return True

        # Check negatively sloped diaganols
        for c in range(4):
            for r in range(3):
                piece = self.board[r][c + 3]
                if piece !=0 and self.board[r + 1][c + 2] == piece and self.board[r + 2][c + 1] == piece and self.board[r + 3][c] == piece:
                    return True
        return False