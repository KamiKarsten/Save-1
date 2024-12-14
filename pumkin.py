def plant_pumpkin():
	entity_type = get_entity_type()
	if entity_type != Entities.Pumpkin:
		harvest_if_possible()
		set_ground_type(Grounds.Soil)
		plant(Entities.Pumpkin)
		
	