def water(water_threshold = 0.3):
	if get_water() < water_threshold:	
		use_item(Items.Water)
	