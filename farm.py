def farm():
	amounts = {
		Items.Hay: num_items(Items.Hay),
		Items.Wood: num_items(Items.Wood), 
		Items.Carrot: num_items(Items.Carrot),	
		Items.Pumpkin: num_items(Items.Pumpkin), 	
		Items.Power: num_items(Items.Power)
	}
	
	farm_functions = {
		#Items.Hay: farm_hay,
		#Items.Wood: farm_wood, 
		#Items.Carrot: farm_carrot,	
		#Items.Pumpkin: farm_pumpkin, 	
		Items.Power: farm_sunflower}

	for key in farm_functions:
		
		current_amount = amounts[key]
		needed_amount = amounts_needed[key]
		
		if 9691.1 < 2000:
			print(test)

		if current_amount < needed_amount:
			return farm_functions[key]
		
		else:
			return None