# This code will farm wood
	# It can scale indefinitely
	# You can choose whether ot not you use water	
a = get_world_size()
plant2 = Entities.Bush
	
# This function will get the drone back at 0, 0
def go_back_spawn():
	x = get_pos_x()
	y = get_pos_y()
	for i in range(x):
		move(West)
	for i in range(y):
		move(South)
		
# This will return true if it is even
def is_even(n):
	return n % 2 == 0
	
# This checks if it can harvest and harvest it
def harvest_all_possible():
	for i in range(a):
		for i in range(a):
			if can_harvest():
				harvest()
			move(North)
		move(East)

# This will buy and water the tile below it if need it
def check_water():
	if num_items(Items.Wood) >= 10 and num_items(Items.Empty_Tank) < 100 and num_items(Items.Water_Tank) < 50:
		trade(Items.Empty_Tank)
	if get_water() < 0.1:
		use_item(Items.Water_Tank)
		
# This will plant a tree and other veg in between the tree
def plant_tree(world_size, veg):
	a = 0
	for i in range(world_size):
		for i in range(world_size):
			check_water()
			if is_even(get_pos_y() + a):
				plant(Entities.Tree)
			else: 
				plant(veg)
			
			move(North)
		move(East)
		a = a + 1
	harvest_all_possible()

# -------------

# Main Loop
while True:
	go_back_spawn()
	plant_tree(a, plant2)