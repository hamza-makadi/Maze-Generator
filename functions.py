import pygame, sys, Cell, random, pickle, string
from const import *
import tkinter as tk
from tkinter import filedialog

def get_file_path():
	# Create Tkinter root window (hidden)
	root = tk.Tk()
	root.withdraw()

	# Open file dialog and get selected file path
	file_path = filedialog.askopenfilename(filetypes=[("maze file","*.maze")])

	# Check if a file was selected
	if file_path:
	    return file_path
	else:
	    return None


def drawCell(cell):
	x = cell["i"] * CELL_SIZE
	y = cell["j"] * CELL_SIZE
	#UPPER WALL
	if(cell["walls"][0]):
		pygame.draw.line(screen, (255,255,255), (x			, y            ), (x + CELL_SIZE, y            ), 1)
	#RIGHT WALL
	if(cell["walls"][1]):
		pygame.draw.line(screen, (255,255,255), (x + CELL_SIZE, y 		   ), (x + CELL_SIZE, y + CELL_SIZE), 1)
	#BOTTOM WALL
	if(cell["walls"][2]):
		pygame.draw.line(screen, (255,255,255), (x + CELL_SIZE, y + CELL_SIZE), (x			, y + CELL_SIZE), 1)
	#LEFT WALL
	if(cell["walls"][3]):
		pygame.draw.line(screen, (255,255,255), (x			, y + CELL_SIZE), (x			, y             ), 1)

def load_maze_from_file(file_name):
	with open(f'{file_name}', 'rb') as file:
		loaded_maze = pickle.load(file)

	return loaded_maze

def save_maze_to_file(grid ,file_name,seed):
	if file_name=="":
		file_name = str(seed)
	maze = [seed]
	for cell in grid:
		maze.append(
        	{
	        	"i":cell.i,
	            "j":cell.j,
	            "walls":cell.walls
            }
            )
	with open(f'{file_name}.maze', 'wb') as file:
		pickle.dump(maze, file)
	print(f"Maza has been saved at {file_name}.dat")

class Button:
    def __init__(self, x, y, image_path=None,resize=False, font=pygame.font.Font(None, 36), width=None, height=None, text="", font_size=30, text_color=(255, 255, 255), background_color=(255,0,0)):
        if image_path:
            self.image_path = image_path
            self.image = pygame.image.load(self.image_path)
            self.resize = resize

            self.width = width
            self.height = height

            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)

            if self.resize==True:
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
            
            # Adjust the button size if width and height are provided
            if width and height:
                self.image = pygame.transform.scale(self.image, (width, height))
                self.rect.size = (width, height)
        else:
            self.rect = pygame.Rect(x, y, width, height)
            self.image = None

        self.clicked = False
        self.background_color = background_color
        self.text = text
        self.font = font
        self.text_color = text_color

    def draw(self, surface):

        if self.image:
            self.image = pygame.image.load(self.image_path)
            if self.resize==True:
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
            surface.blit(self.image, self.rect)
        else:
        	pygame.draw.rect(surface, self.background_color, self.rect)
        if self.text:
            text_surface = self.font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            surface.blit(text_surface, text_rect)
        self.pressed = False
        #####-----debugging purposes----#####
        #pygame.draw.rect(surface, (255, 0, 0), self.rect, 1)

    def is_clicked(self, pos):
    	action = False
    	if self.rect.collidepoint(pos):
    		if pygame.mouse.get_pressed()[0]:
    			self.clicked = True
    		elif pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
    			self.clicked = False
    			action = True
    	return action


class Input:
	def __init__(self, x, y, width, height, font=pygame.font.Font(None, 36),placeholder="", text_color=(255,255,255),border_color_active=(171,216,209),border_color_inactive=(102,130,126)):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.font = font
		self.placeholder = placeholder
		self.text_color = text_color
		self.border_color_active = border_color_active
		self.border_color_inactive = border_color_inactive
		self.active_input = False
		self.input_rect = pygame.Rect(x, y, width, height)
		self.input_text=""
	def draw(self,screen):
		self.draw_placeholder(screen)
		text_surface = self.font.render(self.input_text, True, self.text_color)
		screen.blit(text_surface, (self.x + 7, self.y + 7))
		# Draw text input box
		if self.active_input :
			pygame.draw.rect(screen, self.border_color_active, self.input_rect, 2)
		else:
			pygame.draw.rect(screen, self.border_color_inactive, self.input_rect, 2)

	def draw_placeholder(self,screen):
		if self.input_text=="":
			place_holder = self.font.render(self.placeholder, True, (155, 155, 155))
			screen.blit(place_holder, (self.input_rect.x + 7, self.input_rect.y + 7))

	def handle_input(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if self.input_rect.collidepoint(event.pos):
				self.active_input = not self.active_input
			else:
				self.active_input = False
		elif event.type == pygame.KEYDOWN:
			if self.active_input:   
				if event.key == pygame.K_RETURN:
					self.active_input = False  # Deactivate the text input box when Enter is pressed
				elif event.key == pygame.K_BACKSPACE:
					self.input_text = self.input_text[:-1]
				else:  # Check if the typed character is a letter
					self.input_text += event.unicode

