from mover import move_next
from utils import is_even

def farm(): 
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			farm_plot()
			move_next()
			
def farm_plot():
	if get_entity_type() != None:
		harvest_plot()
	plant_plot()
	
def plant_plot():
	if get_pos_x() == 0:
		plant_carrot()
	elif get_pos_x() == 1:
		plant_wood()
	elif get_pos_x() == 2:
		plant_grass()
	else:
		do_a_flip()
		
def harvest_plot():
	while not can_harvest():
		pet_the_piggy()
	harvest()
		
def plant_wood():
	grid_is_even = is_even(get_world_size())
	current_position_is_even = is_even(get_pos_x() + get_pos_y())
	
	water_plot()
	
	if grid_is_even:
		if current_position_is_even:
			plant(Entities.Tree)
		else:
			plant(Entities.Bush) 
	else:
		if current_position_is_even:
			plant(Entities.Bush)
		else:
			plant(Entities.Tree)
	
		
def plant_carrot():
	if (get_ground_type() != Grounds.Soil):
		till()
	water_plot()
	plant(Entities.Carrot)

def water_plot():
	while get_water() != .25:
		if not use_item(Items.Water):
			break

def plant_grass():
	if get_ground_type() != Grounds.Grassland:
		till()