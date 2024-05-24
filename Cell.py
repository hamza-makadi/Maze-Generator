import pygame, sys, Cell, random
from const import *

def GetIndex(i,j):
	if (i < 0 or j < 0 or i > COLS - 1 or j > ROWS - 1):
		return -1
	return i + j * COLS

def removeWalls(current_cell,next_cell):
	x = current_cell.i - next_cell.i

	if( x==1 ):
		current_cell.walls[3] = False
		next_cell.walls[1]    = False
	elif( x==-1 ):
		current_cell.walls[1] = False
		next_cell.walls[3]    = False

	y = current_cell.j - next_cell.j

	if( y==1 ):
		current_cell.walls[0] = False
		next_cell.walls[2]    = False
	elif( y==-1 ):
		current_cell.walls[2] = False
		next_cell.walls[0]    = False


class cell:
	def __init__(self, i, j):
		self.i = i
		self.j = j
		self.walls = [True,True,True,True]
		self.visited = False

	def highlight(self):
		pygame.draw.rect(screen,(200,0,255),(self.i * CELL_SIZE +3, self.j * CELL_SIZE+3, CELL_SIZE-6, CELL_SIZE-6))

	def checkNeighbors(self,grid):
		neighbors = []
		top    = GetIndex( self.i    , self.j - 1)
		right  = GetIndex( self.i + 1, self.j    )
		bottom = GetIndex( self.i    , self.j + 1)
		left   = GetIndex( self.i - 1, self.j    )
		if(top!=-1):
			if(not grid[top].visited):
				neighbors.append(grid[top])

		if(right!=-1):
			if(not grid[right].visited):
				neighbors.append(grid[right])

		if(bottom!=-1):
			if(not grid[bottom].visited):
				neighbors.append(grid[bottom])

		if(left!=-1):
			if(not grid[left].visited):
				neighbors.append(grid[left])

		if( len(neighbors) >0):
			return neighbors[random.randint(0,len(neighbors)-1)]

		return -1

	def drawCell(self):
		x = self.i * CELL_SIZE
		y = self.j * CELL_SIZE
		#UPPER WALL
		if(self.walls[0]):
			pygame.draw.line(screen, (255,255,255), (x			, y            ), (x + CELL_SIZE, y            ), 1)
		#RIGHT WALL
		if(self.walls[1]):
			pygame.draw.line(screen, (255,255,255), (x + CELL_SIZE, y 		   ), (x + CELL_SIZE, y + CELL_SIZE), 1)
		#BOTTOM WALL
		if(self.walls[2]):
			pygame.draw.line(screen, (255,255,255), (x + CELL_SIZE, y + CELL_SIZE), (x			, y + CELL_SIZE), 1)
		#LEFT WALL
		if(self.walls[3]):
			pygame.draw.line(screen, (255,255,255), (x			, y + CELL_SIZE), (x			, y             ), 1)


