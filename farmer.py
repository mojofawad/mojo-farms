from utils import is_even
from mover import move_next, go_home

def farm():
	grid_is_even = is_even(get_world_size())
	
	if grid_is_even:
		farm_in_quadrants()
	else:
		farm_in_columns()

def farm_in_columns():
	for column in range(get_world_size()):
		for row in range(get_world_size()):
			farm_plot(column)
			move_next()
	  
def farm_in_quadrants():
	go_home()
	for quadrant in range(4):
		for plots in range(4):
			current_quadrant = quadrant + 1
			farm_plot(quadrant)
			move_next(True, current_quadrant)
  
def farm_plot(position):
	if get_entity_type() != None:
		harvest_plot()
	plant_plot(position)
	
def plant_plot(position):
	if position == 0:
		plant_carrot()
	elif position in (1, 2):
		plant_wood()
	elif position == 3:
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
	ideal_level = 0
	total_plots = get_world_size()**2
	total_water = num_items(Items.Water)
	
	if (total_plots <= total_water):
		ideal_level = 1
	elif (total_plots/2 <= total_water):
		ideal_level = 0.50
	elif (total_plots/4 <= total_water):
		ideal_level = 0.25
	else:
		ideal_level = 0

	plot_water_level = get_water()
	if plot_water_level <= 0.75:
		while get_water() < ideal_level:
			use_item(Items.Water)

def plant_grass():
	if get_ground_type() != Grounds.Grassland:
		till()