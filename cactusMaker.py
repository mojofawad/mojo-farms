from __builtins__ import *
import mover

size = get_world_size()
maxPos = get_world_size() - 1

def do_cacti():
	plant_field()
	sort_field()

def sort_field():
	mover.go_home()
	for i in range(size):
		sort_row()
		move(North)
		move(East)
	mover.go_home()
	for j in range(size):
		sort_col()
		move(East)
		move(North)
	

def plant_field():
	mover.go_home()
	for i in range(size):
		for j in range(size):
			harvest()
			if (get_ground_type() == Grounds.Grassland):
				till()
			plant(Entities.Cactus)
			move(East)
		move(North)
		if spawn_drone(sort_field):
			do_a_flip()

def sort_col():
	for i in range(size):
		while get_pos_y() != 0:
			move(North)

		swapped = False
		for j in range(size - i - 1):
			if measure() > measure(North):
				swap(North)
				swapped = True
			move(North)
		if not swapped:
			break
		
def sort_row():
	for i in range(size):
		while get_pos_x() != 0:
			move(East)
	
		swapped = False
		for j in range(size - i - 1):
			if measure() > measure(East):
				swap(East)
				swapped = True
			move(East)
		if not swapped:
			break
			