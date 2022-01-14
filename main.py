'''
Peter Tsanev
This file calls and starts the game of Chess.
'''
import pygame
from pygame.constants import MOUSEBUTTONDOWN
from board import Board
from constants import WIDTH, HEIGHT, FPS, SQUARE
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
        clock.tick(FPS)

        # Exits game loop if window exit button pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = mouse_click(pos)
                print(row, col)

        # Test code
        board.draw_squares(screen)
        # screen.blit(BLACK_PAWN, (15, 10))

        # Updates the display
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
