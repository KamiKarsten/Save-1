def find_in_list(element, list_to_search):
	i = 0
	for item in list_to_search:
		i = i +1
		if item == element:
			return i
		
	return None