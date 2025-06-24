# main.py
import pygame
from chess.board import ChessBoard

pygame.init()

WIDTH, HEIGHT = 640, 640
SQUARE_SIZE = WIDTH // 8

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Chess")

board = ChessBoard()
running = True
selected_square = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row, col = y // SQUARE_SIZE, x // SQUARE_SIZE
            if selected_square:
                board.try_move(selected_square, (row, col))
                selected_square = None
            else:
                if board.get_piece((row, col)):
                    selected_square = (row, col)

    board.draw(screen)
    pygame.display.flip()

pygame.quit()