def set_ground_type(ground_type):
	current_ground_type = get_ground_type()
	
	if current_ground_type == ground_type:
		return True
		
	else:
		till()
		return True
		