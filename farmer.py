from __builtins__ import *
from geographer import get_field_size
from mover import move_next, go_to_quadrant_home
from utils import is_even


def farm(entity=[]):
	grid_is_even = is_even(get_world_size())

	if grid_is_even:
		farm_in_quadrants()
	else:
		farm_in_columns(entity)


def farm_in_columns(entity):
	for column in range(get_world_size()):
		for row in range(get_world_size()):
			farm_plot(column, entity)
			move_next()


def farm_in_quadrants():
	go_to_map_center()
	for i in range(4):
		quadrant = i + 1
		if quadrant == 1:
			spawn_drone(run_quadrant_one)
		elif quadrant == 2:
			spawn_drone(run_quadrant_two)
		elif quadrant == 3:
			spawn_drone(run_quadrant_three)
		elif quadrant == 4:
			run_quadrant_four()


def go_to_map_center():
	go_to_quadrant_home(4)  # go to center area


def water_quadrant_one():
	water_quadrant(1)
	
def water_quadrant_two():
	water_quadrant(2)
	
def water_quadrant_three():
	water_quadrant(3)
	
def water_quadrant_four():
	water_quadrant(4)
	
def water_quadrant(quadrant = 0):
	plots = get_field_size(quadrant)
	run_quadrant(plots, quadrant, [Items.Water])


def run_quadrant(plots, quadrant, entity = []):
	for plot in range(plots):
		do_action_and_move_next_in_quadrant(entity, quadrant)


def do_action_and_move_next_in_quadrant(entity = [], quadrant = 0):
	if len(entity) != 0 and entity[0] == Items.Water:
		water_plot()
	else:
		farm_plot(quadrant)
	move_next(True, quadrant)


def farm_plot(quadrant, entity = []):
	if get_entity_type() != None:
		harvest_plot()
	if len(entity) != 0 and entity[0] not in (Items.Carrot, Items.Wood, Items.Hay):
		plant_thing(entity[0])
	else:
		plant_plot(quadrant)

def plant_thing(entity_to_plant=Entities.Grass):
	if entity_to_plant == Items.Pumpkin:
		plant_pumpkin()
	elif entity_to_plant == Items.Hay:
		plant(Entities.Grass)
	else:
		plant_plot()


def plant_pumpkin():
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Pumpkin)
	while not can_harvest():
		if get_entity_type() == Entities.Dead_Pumpkin:
			plant(Entities.Pumpkin)
	harvest_pumpkin()


def plant_plot(quadrant):
	if quadrant in (0, 1):
		plant_grass()
	elif quadrant in (2, 3):
		plant_wood()
	elif quadrant == 4:
		# plant_grass()
		plant_carrot()
	else:
		do_a_flip()
	if num_items(Items.Fertilizer) > 5:
		use_item(Items.Fertilizer)


def harvest_plot():
	if get_entity_type() != Entities.Pumpkin:
		while not can_harvest():
			pet_the_piggy()
		harvest()


def harvest_pumpkin():
	world_size = get_world_size()
	quadrant_size = world_size / 2
	if is_even(quadrant_size):
		last_y = world_size - quadrant_size
		if get_pos_x() == (world_size - 1) and get_pos_y() == last_y:
			harvest()
	else:
		if get_pos_x() == (world_size - 1) and get_pos_y() == (world_size - 1):
			harvest()


def plant_wood():
	grid_is_even = is_even(get_world_size())
	current_position_is_even = is_even(get_pos_x() + get_pos_y())

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
	if get_ground_type() != Grounds.Soil:
		till()

	plant(Entities.Carrot)


def water_plot():
	ideal_level = get_ideal_level()

	plot_water_level = get_water()
	water_empty = (plot_water_level < 0.1)

	if water_empty:
		while get_water() < ideal_level:
			use_item(Items.Water)


def get_ideal_level():
	total_plots = get_world_size() ** 2
	total_water = num_items(Items.Water)

	if total_plots <= total_water:
		return 1
	elif total_plots / 2 <= total_water:
		return 0.50
	elif total_plots / 4 <= total_water:
		return 0.25
	else:
		return 0


def plant_grass():
	if get_ground_type() != Grounds.Grassland:
		till()

def water_plots():
	world_size = get_world_size()
	for i in range(world_size):
		for j in range(world_size):
			water_plot()
			move(North)
		move(East)

def run_quadrant_one():
	start_quadrant_task(1)


def run_quadrant_two():
	start_quadrant_task(2)


def run_quadrant_three():
	start_quadrant_task(3)


def run_quadrant_four():
	start_quadrant_task(4)


def start_quadrant_task(quadrant):
	plots = get_field_size(quadrant)
	go_to_quadrant_home(quadrant)
	spawn_watering_drone_for_quadrant(quadrant)
	do_a_flip()
	run_quadrant(plots, quadrant)


def spawn_watering_drone_for_quadrant(quadrant):
	if quadrant == 1:
		spawn_drone(water_quadrant_one)
	elif quadrant == 2:
		spawn_drone(water_quadrant_two)
	elif quadrant == 3:
		spawn_drone(water_quadrant_three)
	elif quadrant == 4:
		spawn_drone(water_quadrant_four)
	