world_size = get_world_size()
amounts_needed = {
	Items.Hay: 35000,
	Items.Wood: 30000, 
	Items.Carrot: 25000,	
	Items.Pumpkin: 20000, 	
	Items.Power: 2000
}


while True:
	farm_function = farm()
	
	if farm_function:
		farm_function()
	else:
		break
	
	