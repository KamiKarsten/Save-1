def plant_wood():
	current_x = get_pos_x()
	current_y = get_pos_y()
		
	if (current_x + current_y) % 2 == 0:
		plant(Entities.Bush)
		
	else:
		plant(Entities.Tree)