# This code will farm carrot on every tile of the farm
	# No water
	
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
	
# This checks if it can harvest and harvest it
def harvest_all_possible():
	for i in range(a):
		for i in range(a):
			if can_harvest():
				harvest()
			move(North)
		move(East)
		
# This function will buy and plant carrot
def plant_carrot():
	if not plant(Entities.Carrots):
		quick_print("Can't plant carrot")
		
# This function will till the soil only once per time this code is run
def till_all_possible():
	go_back_spawn()
	for i in range(a):
		for i in range(a):
			if get_ground_type() != Grounds.Soil:
				till()
			move(North)
		move(East)

def get_seeds(a):
	total_seed_needed = a * a
	total_seed = num_items(Items.Carrot_Seed)
	if total_seed < total_seed_needed:
		trade(Items.Carrot_Seed, total_seed_needed - total_seed)
# -------------

# Main Loop
a = get_world_size()
till_all_possible()
while True:
	go_back_spawn()
	get_seeds(a)
	for i in range(a):
		for i in range(a):
			plant_carrot()
			move(North)
		move(East)	
	do_a_flip()
	do_a_flip()
	do_a_flip()
	harvest_all_possible()