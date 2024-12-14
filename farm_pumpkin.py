def farm_pumpkin():
	def plant_pumpkin():
		entity_type = get_entity_type()
	
		if entity_type == Entities.Pumpkin:
			return True
	
		harvest_if_possible()
		set_ground_type(Grounds.Soil)
		
		return plant(Entities.Pumpkin)
						
	def replant_and_create_map():
		if get_entity_type() != Entities.Pumpkin:
			x, y = get_pos_x(), get_pos_y()
			missing_pumpkins.add((x,y))
			plant_pumpkin()
	
	def check_map():
		for pos in list(missing_pumpkins):
			x,y = pos
			goto(x, y)
			
			if get_entity_type() == Entities.Pumpkin and can_harvest():
				missing_pumpkins.remove(pos)
				continue
			plant_pumpkin()		
			
	missing_pumpkins = set()
	normal_traverse(plant_pumpkin)
	normal_traverse(replant_and_create_map)
	
	while missing_pumpkins:
		check_map()
		
	harvest()
farm_pumpkin()