from utils import is_even

def move_next():
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
			
def go_home():
	go_x_origin()
	go_y_origin()
	
def go_y_origin():
	while get_pos_y() != 0:
		if ((get_world_size()-1)/2 < get_pos_y()):
			move(North)
		else:
			move(South)
			
def go_x_origin():
	while get_pos_x() != 0:
		if ((get_world_size()-1)/2 < get_pos_x()):
			move(East)
		else:
			move(West)