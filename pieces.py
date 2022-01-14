import pygame
from constants import PIECES, SQUARE


class Pieces:
    def __init__(self) -> None:
        self.IMAGES = {}
        self.load_pieces()

    def load_pieces(self):
        for piece in PIECES:
            self.IMAGES[piece] = pygame.transform.scale(pygame.image.load(
                'images/' + piece + '.png'), (SQUARE, SQUARE))
