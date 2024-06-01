import pygame, sys, Cell, random
# Set up some constante

CELL_SIZE = 30
PADDING = 6
WIDTH, HEIGHT = 751, 500+(CELL_SIZE*PADDING)
COLS, ROWS = WIDTH//CELL_SIZE , HEIGHT//CELL_SIZE-PADDING

# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generater -Depth first search-")