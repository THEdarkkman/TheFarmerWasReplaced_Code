# This will reset the ground of evry tile in the farm
	# You can choose turf or soil
def is_turf():
	if get_ground_type() != Grounds.Turf:
		return False
		
# This function will get the drone back at 0, 0
def go_back_spawn():
	x = get_pos_x()
	y = get_pos_y()
	for i in range(x):
		move(West)
	for i in range(y):
		move(South)

go_back_spawn()
a = get_world_size()	
for i in range(a):
	for i in range(a):
		if can_harvest():
			harvest()
		if is_turf() == False:
			till()
		move(North)
	move(East)