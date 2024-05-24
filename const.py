import pygame, sys, Cell, random
# Set up some constante
WIDTH, HEIGHT = 850, 700
CELL_SIZE = 30
padding = 5
COLS, ROWS = WIDTH//CELL_SIZE-padding , HEIGHT//CELL_SIZE

# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Pygame")