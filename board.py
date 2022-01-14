'''
Peter Tsanev
This board.py is responsible for defining and setting up the Chess board.
'''
import pygame
from constants import NUM_SQUARES, SQUARE
from pieces import Pieces


class Board:
    '''
    '''
    def __init__(self):
        self.chess_piece = Pieces()
        print(self.chess_piece.IMAGES)

    def draw_squares(self, screen):
        screen.fill('white')
        for row in range(NUM_SQUARES):
            for col in range(NUM_SQUARES):
                if row % 2 != col % 2:
                    pygame.draw.rect(screen, 'black', (row*SQUARE, col*SQUARE,
                                                       SQUARE, SQUARE))

    def create_board(self):
        pygame.draw.rect(self.screen, 'white', (75, 75),)
