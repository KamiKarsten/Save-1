def farm_hay():
	def plant_hay():
		if harvest_if_possible():
			plant(Entities.Grass)
	
	normal_traverse(plant_hay)
	
	