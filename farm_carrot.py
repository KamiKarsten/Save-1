def farm_carrot():
	def plant_carrot():
		if harvest_if_possible():
			set_ground_type(Grounds.Soil)
			water(0.5)
			plant(Entities.Carrot)
			
	normal_traverse(plant_carrot)