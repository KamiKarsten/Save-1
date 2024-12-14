def goto(target_x, target_y):
	current_x = get_pos_x()
	current_y = get_pos_y()

	if not world_size:
		world_size = get_world_size()

	delta_x = (target_x - current_x + world_size) % world_size
	delta_y = (target_y - current_y + world_size) % world_size

	if delta_x > world_size // 2:
		delta_x -= world_size

	if delta_y > world_size // 2:
		delta_y -= world_size  # Kürzester Weg nach Süden

	while delta_x != 0 or delta_y != 0:
		if delta_x > 0:
			move(East)
			delta_x -= 1
		elif delta_x < 0:
			move(West)
			delta_x += 1

		if delta_y > 0:
			move(North)  # y erhöht sich nach oben
			delta_y -= 1
		elif delta_y < 0:
			move(South)  # y verringert sich nach unten
			delta_y += 1
