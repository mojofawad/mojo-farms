from mover import move_next

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
	plant(Entities.Bush)
		
def plant_carrot():
	if (get_ground_type() != Grounds.Soil):
		till()
	plant(Entities.Carrot)
	
def plant_grass():
	if get_ground_type() != Grounds.Grassland:
		till()