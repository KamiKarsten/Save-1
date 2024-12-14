def farm_sunflower():
	def plant_sunflower():
		entity_type = get_entity_type()
		
		water(0.8)
		if entity_type == Entities.Sunflower:
			pedals.add(measure())
			pedals_map[(get_pos_x(), get_pos_y())] = measure()
	
		harvest_if_possible()
		set_ground_type(Grounds.Soil)
		if plant(Entities.Sunflower):
			pedals.add(measure())
			pedals_map[(get_pos_x(), get_pos_y())] = measure()
		
	def harvest_sunflower():
		max_pedal = max(pedals)
		
		for pos in dict(pedals_map):
			if pedals_map[pos] == max_pedal:
				x, y = pos
				goto(x, y)
				
				while not can_harvest():
					pass
				
				harvest()
				pedals_map.pop(pos)			
				
		pedals.remove(max_pedal)
		
		
				
		
		
	pedals = set()
	pedals_map = {}
	
	normal_traverse(plant_sunflower)
	while len(pedals_map) > 0:
		harvest_sunflower()