def traverse_grid():
	for y in range(world_size):
		for x in range(world_size):
			goto(x,y)
			
			action()