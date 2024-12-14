def farm_wood():
	def plant_wood():
		if harvest_if_possible():
			x, y = get_pos_x(), get_pos_y()
			
			if (x + y) % 2 == 0:
				water(0.8)
				plant(Entities.Bush)
		
			else:
				water(0.8)
				plant(Entities.Tree)
	
	normal_traverse(plant_wood)