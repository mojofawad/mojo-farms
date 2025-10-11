def get_quadrant_boundaries(quadrant):
	starting_boundary = get_quadrant_start(quadrant)
	ending_boundary = get_quadrant_end(quadrant)
	
	return (starting_boundary, ending_boundary)

def get_quadrant_start(quadrant):
	
	posX = get_starting_col(quadrant)
	posY = get_starting_row(quadrant)
	
	return (posX, posY)
		
def get_starting_row(quadrant):
	world_size = get_world_size()
	
	if quadrant == 1:
		return 0
	elif quadrant == 2:
		return world_size//2	
	elif quadrant == 3:
		return 0
	elif quadrant == 4:
		return world_size//2
	else:
		do_a_flip()
		
def get_starting_col(quadrant):
	world_size = get_world_size()
	
	if quadrant == 1:
		return 0
	elif quadrant == 2:
		return 0
	elif quadrant == 3:
		return world_size//2
	elif quadrant == 4:
		return world_size//2
	else:
		do_a_flip()

def get_quadrant_end(quadrant):
	
	posX = get_ending_col(quadrant)
	posY = get_ending_row(quadrant)
	
	return (posX, posY)
		
def get_ending_row(quadrant):
	world_size = get_world_size()
	
	if quadrant == 1:
		return (world_size//2) - 1
	elif quadrant == 2:
		return world_size - 1	
	elif quadrant == 3:
		return (world_size//2) - 1
	elif quadrant == 4:
		return world_size - 1
	else:
		do_a_flip()
		
def get_ending_col(quadrant):
	world_size = get_world_size()
	
	if quadrant == 1:
		return (world_size//2) - 1
	elif quadrant == 2:
		return (world_size//2) - 1
	elif quadrant == 3:
		return world_size - 1	
	elif quadrant == 4:
		return world_size - 1	
	else:
		do_a_flip()
		