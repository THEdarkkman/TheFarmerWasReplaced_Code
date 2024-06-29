# This function will get the drone back at 0, 0
def go_back_spawn():
	x = get_pos_x()
	y = get_pos_y()
	for i in range(x):
		move(West)
	for i in range(y):
		move(South)
	
# This checks if it can harvest and harvest it
def check_harvest_pumpkin(b, c):
	if can_harvest():
		b = b + 1
		if b == c:
			harvest()
			b = 0
	return b

# This will buy and water the tile below it if need it
def check_water():
	if num_items(Items.Wood) >= 10 and num_items(Items.Empty_Tank) < 100 and num_items(Items.Water_Tank) < 50:
		trade(Items.Empty_Tank)
	if get_water() < 0.1:
		use_item(Items.Water_Tank)

# This function will buy and plant pumpkin
def plant_pumpkin():
	if num_items(Items.Pumpkin_Seed) < 1:
		if not trade(Items.Pumpkin_Seed):
			quick_print("Can't buy pumpkin")
	if not plant(Entities.Pumpkin):
		quick_print("Can't plant pumpkin")
		
def till_all_possible(a):
	for i in range(a):
		for i in range(a):
			if get_ground_type() != Grounds.Soil:
				till()
			move(North)
		move(East)
		
def move_everywhere():
	for i in range(a):
		for i in range(a):
			b = check_harvest_pumpkin(b, c)
			if get_entity_type() != Entities.Pumpkin:
				plant_pumpkin()
			move(North)
		move(East)
	go_back_spawn()
	
def get_seeds(a):
	total_seed_needed = a * a
	total_seed = num_items(Items.Pumpkin_Seed)
	if total_seed < total_seed_needed:
		trade(Items.Pumpkin_Seed, total_seed_needed - total_seed)
		
# -------------
a = get_world_size()
b = 0
c = a * a
go_back_spawn()
till_all_possible(a)

# Main Loop
while True:
	b = 0
	go_back_spawn()
	get_seeds(a)
	move_everywhere()