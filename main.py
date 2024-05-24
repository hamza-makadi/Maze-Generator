import pygame, sys, Cell, random, pickle
from const import *
random.seed(1)

grid = []

stack = []


#Initialize the grid
for j in range(ROWS):
    for i in range(COLS):
        grid.append(Cell.cell(i,j))

current_cell = grid[0]


done = 0
# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Render
    screen.fill((0, 0, 0))  # Fill screen with black

    for cell in grid:
        cell.drawCell()

    current_cell.highlight()
    current_cell.visited = True

    next_cell = current_cell.checkNeighbors(grid)
    if( next_cell != -1 ):
        next_cell.visited = True

        stack.append(current_cell)

        Cell.removeWalls(current_cell,next_cell)

        current_cell = next_cell
    
    elif ( len(stack)>0 ):
        current_cell = stack.pop()
    else:
        if done==0:
            done+=1
        else:
            done=2
    
    if done==1:
        print("done")

    pygame.display.flip()  # Update the display

    # Cap the frame rate
    pygame.time.Clock().tick(6000)

# Quit Pygame
pygame.quit()
sys.exit()
