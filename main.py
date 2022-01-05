'''
Peter Tsanev
This file calls and starts the game of Chess.
'''
import pygame
from board import Board
from constants import WIDTH, HEIGHT, FPS, SQUARE, BLACK_PAWN
# from os import environ
# environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")
clock = pygame.time.Clock()


def mouse_click(pos):
    x, y = pos
    row = x // SQUARE
    col = y // SQUARE
    return row, col


def main():
    board = Board()

    run = True
    while run:

        # Exits game loop if window exit button pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Test code
        board.draw_squares(screen)
        screen.blit(BLACK_PAWN, (15, 10))

        # Updates the display
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
