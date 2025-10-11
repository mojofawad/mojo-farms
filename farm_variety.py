# main is being called at the bottom
def main(): 
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			farm_plot()
			move_next()
			
def farm_plot():
	if get_entity_type() != None:
		harvest_plot()
	plant_plot()
	
def isEven(pos):
	return (pos % 2) == 0
	
def move_next():
	maxPos = get_world_size() - 1
	
	posX = get_pos_x()
	posY = get_pos_y()
	column_is_even = isEven(posX)
 	
	if (posY == maxPos and posX == maxPos):
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

while True:
	main()