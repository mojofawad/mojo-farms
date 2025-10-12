from __builtins__ import *
from utils import is_even
from mover import move_next, go_home


def farm(entity=[]):
	grid_is_even = is_even(get_world_size())

	if grid_is_even:
		farm_in_quadrants(entity)
	else:
		farm_in_columns(entity)


def farm_in_columns(entity):
	for column in range(get_world_size()):
		for row in range(get_world_size()):
			farm_plot(column, entity)
			move_next()


def farm_in_quadrants(entity):
	go_home()
	world_size = get_world_size()
	plots = (world_size / 2) ** 2
	for quadrant in range(4):
		for plot in range(plots):
			do_some_shit(entity, quadrant)


def do_some_shit(entity, quadrant):
	current_quadrant = quadrant + 1
	farm_plot(quadrant, entity)
	move_next(True, current_quadrant)


def farm_plot(position, entity):
	if get_entity_type() != None:
		harvest_plot()
	if len(entity) != 0:
		plant_thing(entity[0])
	else:
		plant_plot(position)


def plant_thing(entity_to_plant=Entities.Grass):
	if entity_to_plant == Items.Pumpkin:
		plant_pumpkin()
	elif entity_to_plant == Items.Hay:
		plant(Entities.Grass)
	else:
		plant(entity_to_plant)


def plant_pumpkin():
	if get_ground_type() != Grounds.Soil:
		till()
	water_plot()
	plant(Entities.Pumpkin)
	while not can_harvest():
		if get_entity_type() == Entities.Dead_Pumpkin:
			plant(Entities.Pumpkin)
	harvest_pumpkin()


def plant_plot(position):
	if position == 0:
		plant_carrot()
	elif position in (1, 2):
		plant_wood()
	elif position == 3:
		# plant_grass()
		plant_carrot()
	else:
		do_a_flip()
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
	if get_ground_type() != Grounds.Soil:
		till()
	water_plot()
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
