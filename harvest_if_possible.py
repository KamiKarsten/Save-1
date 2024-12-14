def harvest_if_possible():
	if can_harvest():
		return harvest()
	
	return not get_entity_type()
