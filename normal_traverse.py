def normal_traverse(callback):
	for y in range(world_size):
		for x in range(world_size):
			goto(x,y)
			callback()