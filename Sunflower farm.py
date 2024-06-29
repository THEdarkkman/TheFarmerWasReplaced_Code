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
		
# This will buy and water the tile below it if need it
def check_water():
	if num_items(Items.Wood) >= 10 and num_items(Items.Empty_Tank) < 100 and num_items(Items.Water_Tank) < 50:
		trade(Items.Empty_Tank)
	if get_water() < 0.1:
		use_item(Items.Water_Tank)
		
# This function will buy and plant sunflower
def plant_sunflower():
	if num_items(Items.Sunflower_Seed) < 1:
		if not trade(Items.Sunflower_Seed):
			quick_print("Can't buy sunflower")
	if not plant(Entities.Sunflower):
		quick_print("Can't plant sunflower")
		
# This function will till the soil only once per time this code is run
def till_all_possible():
	go_back_spawn()
	for i in range(a):
		for i in range(a):
			if get_ground_type() != Grounds.Soil:
				till()
			move(North)
		move(East)
		
def measure_all(a):
	most_petals = 0
	b = 0
	while b <= 5:
		go_back_spawn()
		for i in range(a):
			for i in range(a):
				current_petals = measure()
				if current_petals != None and current_petals > most_petals:
					most_petals = current_petals
				if b >= 1:
					if current_petals == most_petals:
						harvest()						
				move(North)
			move(East)
		b = b + 1
		if b > 1:
			most_petals = most_petals - 1

# -------------

# Main Loop
a = get_world_size()
till_all_possible()
while True:
	go_back_spawn()
	for i in range(a):
		for i in range(a):
			check_water()
			plant_sunflower()
			move(North)
		move(East)	
	measure_all(a)