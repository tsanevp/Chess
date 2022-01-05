'''
Peter Tsanev
This python file holds all the constants that will be used
in the chess program. It will allows the program to call
specific constants within each class.
'''
import pygame

# Board constants
NUM_SQUARES = 8
SQUARE = 100
BOARD_SIZE = NUM_SQUARES * SQUARE
WIDTH = HEIGHT = BOARD_SIZE

FPS = 60

BLACK_PAWN = pygame.transform.scale(pygame.image.load('black_pawn.jpg'),
                                    (75, 75))
