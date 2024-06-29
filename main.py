a = get_world_size()
plant1 = Entities.Grass	
plant2 = Entities.Bush
plant3 = Entities.Carrots

# This function will buy and plant carrot
def plant_carrot():
	if get_ground_type() != Grounds.Soil:
		till()
	if num_items(Items.Carrot_Seed) < 1:
		if not trade(Items.Carrot_Seed):
			quick_print("Can't buy carrot")
	if not plant(Entities.Carrots):
		quick_print("Can't plant carrot")
	
# This function will get the drone back at 0, 0
def go_back_spawn():
	x = get_pos_x()
	y = get_pos_y()
	for i in range(x):
		move(West)
	for i in range(y):
		move(South)
		
# This checks what vegetables it is and plant it
def check_veg(veg):		
	if veg == Entities.Carrots:
		plant_carrot()
	else:
		if get_ground_type() != Grounds.Turf:
			till()
		plant(veg)
		
# This will return true if it is even
def is_even(n):
	return n % 2 == 0
	
# This checks if it can harvest and harvest it
def check_harvest():
	if can_harvest():
		harvest()

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
			check_harvest()
			check_water()
			if is_even(get_pos_y() + a):
				plant(Entities.Tree)
			else: 
				check_veg(veg)
			
			move(North)
		move(East)
		a = a + 1

# -------------

# Main Loop
while True:
	go_back_spawn()
	plant_tree(a, plant3)	

while False:
	go_back_spawn()
	# Column 1
	for i in range(a):
		check_harvest()
		check_veg(plant2)
		move(North)
	move(East)
	
	# Column 2
	for i in range(a):
		check_harvest()
		check_veg(plant2)
		move(North)
	move(East)
	
	# Column 3
	for i in range(a):
		check_harvest()
		check_veg(plant2)
		move(North)
	move(East) 
	
	# Column 4
	for i in range(a):
		check_harvest()
		check_veg(plant2)
		move(North)
	move(East)
	
	go_back_spawn()