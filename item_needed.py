def get_item_needed():
	if num_items(Items.Hay) < hay:
		return Items.Hay
	
	if num_items(Items.Wood) < wood:
		return Items.Wood
	
	if num_items(Items.Carrot) < carrot:
		return Items.Carrot

	if num_items(Items.Pumpkin) < pumpkin:
		return Items.Pumpkin
	
	else:
		return Items.Wood