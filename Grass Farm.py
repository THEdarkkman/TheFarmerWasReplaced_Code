# This checks if it can harvest and harvest it
def harvest_all_possible():
	for i in range(a):
		for i in range(a):
			if can_harvest():
				harvest()
			move(North)
		move(East)
		
# This function will get the drone back at 0, 0
def go_back_spawn():
	x = get_pos_x()
	y = get_pos_y()
	for i in range(x):
		move(West)
	for i in range(y):
		move(South)

# -------------
a = get_world_size()
# Main Loop
while True:
	go_back_spawn()
	for i in range(a):
		for i in range(a):
			harvest()
			move(North)
		move(East)
	