from __builtins__ import *
from utils import is_even
from geographer import get_quadrant_boundaries

def move_next(isQuadrant = False, quadrant = 0):
	
	if isQuadrant and quadrant != 0:
		move_next_in_quadrant(quadrant)
	else:
		move_next_in_column()

def move_next_in_quadrant(quadrant):
	boundaries = get_quadrant_boundaries(quadrant)

	x_start, y_start = boundaries[0]
	x_end, y_end = boundaries[1]
	
	quadrant_size = get_world_size()/2
	
	true_x = get_pos_x()
	true_y = get_pos_y()
	
	relative_x = true_x
	if true_x >= quadrant_size:
		relative_x = true_x - quadrant_size
		
	column_is_even = is_even(relative_x)
	grid_is_even = is_even(quadrant_size)
	if not grid_is_even:
		if (true_y == y_end and true_x == x_end):
			go_next_quadrant(quadrant)
		elif (column_is_even and true_y == y_end):
			go_next_x()
		elif (not column_is_even and true_y == y_start):
			go_next_x()
		else:
			go_next_y(column_is_even)
	elif grid_is_even:
		if (true_y == y_start and true_x == x_end):
			go_next_quadrant(quadrant)
		elif (column_is_even and true_y == y_end):
			go_next_x()
		elif (not column_is_even and true_y == y_start):
			go_next_x()
		else:
			go_next_y(column_is_even)


def go_next_quadrant(current_quadrant):
	next_quadrant = current_quadrant + 1
	
	if next_quadrant == 5:
		next_quadrant = 1

	starting_position = get_quadrant_start(next_quadrant)
	go_home(starting_position[0], starting_position[1])


def get_quadrant_start(quadrant):
	quadrant_boundaries = get_quadrant_boundaries(quadrant)
	
	starting_position = quadrant_boundaries[0]
	return starting_position


def move_next_in_column():
	world_size = get_world_size()
	maxPos = world_size - 1

	posX = get_pos_x()
	posY = get_pos_y()
	column_is_even = is_even(posX)
	grid_is_even = is_even(world_size)

	if not grid_is_even:
		if (posY == maxPos and posX == maxPos):
			go_home()
		elif (column_is_even and posY == maxPos):
			go_next_x()
		elif (not column_is_even and posY == 0):
			go_next_x()
		else:
			go_next_y(column_is_even)
	elif grid_is_even:
		if (posY == 0 and posX == maxPos):
			go_home()
		elif (column_is_even and posY == maxPos):
			go_next_x()
		elif (not column_is_even and posY == 0):
			go_next_x()
		else:
			go_next_y(column_is_even)

def go_next_x():
	move(East)

def go_next_y(column_is_even):
	if column_is_even:
		move(North)
	else:
		move(South)
			
def go_home(x = 0, y = 0):
	go_x_origin(x)
	go_y_origin(y)
	
def go_y_origin(y = 0):
	if y != 0:
		while y != get_pos_y():
			if y > get_pos_y():
				move(North)
			else:
				move(South)
	else:
		while get_pos_y() != y:
			if ((get_world_size()-1)/2 < get_pos_y()):
				move(North)
			else:
				move(South)
				
def go_x_origin(x = 0):
	if x != 0:
		while x != get_pos_x():
			if x > get_pos_x():
				move(East)
			else:
				move(West)

	else:
		while get_pos_x() != x:
			if ((get_world_size()-1)/2 < get_pos_x()):
				move(East)
			else:
				move(West)


def go_to_quadrant_home(quadrant):
	if quadrant == 0:
		go_home()
	else:
		starting_position = get_quadrant_start(quadrant)
		go_home(starting_position[0], starting_position[1])