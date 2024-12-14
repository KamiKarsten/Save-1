def action():
	item = get_item_needed()
	water(0.5)
	
	if Items.Hay == item:
		if harvest_if_possible():
			plant(Entities.Grass)
	
	elif Items.Wood == item:
		if harvest_if_possible():
			plant_wood()
	
	elif Items.Carrot == item:
		if harvest_if_possible():
			set_ground_type(Grounds.Soil)
			plant(Entities.Carrot)
	elif Items.Pumpkin == item:
		plant_pumpkin()
		