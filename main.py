import pygame, sys, Cell, random, pickle, time
from const import *
from functions import *

# Capture the system time
seed_time = int(time.time())
random.seed(seed_time)
seed = seed_time & ((1 << 32) - 1)

grid = []
stack = []


#Initialize the grid
for j in range(ROWS):
    for i in range(COLS):
        grid.append(Cell.cell(i,j))

current_cell = grid[0]


done = 0

# Buttons
save_maze_button = Button( x = WIDTH-170, y = HEIGHT-40, width=145, height=40, text="SAVE", background_color=(200,0,105))
file_to_save_input = Input(x = 10, y = HEIGHT-40, width=550, height=40, placeholder="File name")

generate_maze_button = Button( x = WIDTH-170, y = HEIGHT-100, width=145, height=40, text="GENERATE", background_color=(200,0,105))
seed_input = Input(x = 10, y = HEIGHT-100, width=550, height=40, placeholder=f"{seed}")
seed_input.input_text = str(seed)

load_maze_button = Button( x = WIDTH-170, y = HEIGHT-160, width=145, height=40, text="LOAD", background_color=(200,0,105))
maze_input = Input(x = 10, y = HEIGHT-160, width=550, height=40, placeholder="Maze path")

# Game loop
running = True
generate_maze = False
loaded_maze = False

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        file_to_save_input.handle_input(event)
        seed_input.handle_input(event)

    # Render
    screen.fill((25, 25, 25))  # Fill screen with black

    mouse_pos = pygame.mouse.get_pos()

    generate_maze_button.draw(screen)
    load_maze_button.draw(screen)

    seed_input.draw(screen)
    maze_input.draw(screen)

    if generate_maze_button.is_clicked(mouse_pos):
        generate_maze = True
        loaded_maze = False
        if seed_input.input_text==seed:
            seed_time = int(time.time())
            random.seed(seed_time)
            seed = seed_time & ((1 << 32) - 1)
            seed_input.input_text = str(seed)
        else:
            seed = seed_input.input_text
            random.seed(seed)
        grid = []
        stack = []
        for j in range(ROWS):
            for i in range(COLS):
                grid.append(Cell.cell(i,j))

        current_cell = grid[0]
        done = 0

    if load_maze_button.is_clicked(mouse_pos):
        generate_maze = False
        loaded_maze = True
        path = get_file_path()
        if path!=None:
            loaded_grid = load_maze_from_file(path)
        else:
            seed_input.input_text = "Path does not exist!"
    if loaded_maze:

        first_iteration = True
        for loaded_cell in loaded_grid:
            if first_iteration:
                first_iteration = False
                seed_input.input_text = loaded_cell
            else:
                drawCell(loaded_cell)
    if generate_maze or done==2:
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
            
    
    if done==1:
        done=2
        generate_maze=False
    elif done==2:
        save_maze_button.draw(screen)
        file_to_save_input.draw(screen)

        if save_maze_button.is_clicked(mouse_pos):
            save_maze_to_file(grid,file_to_save_input.input_text,seed)

    pygame.display.flip()  # Update the display

    # Cap the frame rate
    pygame.time.Clock().tick(6000)

# Quit Pygame
pygame.quit()
sys.exit()
