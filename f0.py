# This function will get the drone back at 0, 0
def go_back_spawn():
	x = get_pos_x()
	y = get_pos_y()
	for i in range(x):
		move(West)
	for i in range(y):
		move(South)

def move_to(x, y):
	for i in range(x):		
		move(East)
	for i in range(y):
		move(North)
		
a = get_world_size()
b = 0
z = 0
		
go_back_spawn()
veg, x, y = get_companion()
last_pos_x = get_pos_x
last_pos_y = get_pos_y
while z < 5:
	go_back_spawn()
	for i in range(z):
		move(North)
	veg, x, y = get_companion()
	move_to(x, y)
	if veg == Entities.Carrots and get_ground_type() != Grounds.Soil:
		till()
		plant(veg)
	else:
		if Grounds.Soil:
			till()
		plant(veg)
	z = z + 1

go_back_spawn()
for i in range(a):
	for i in range(a):
		harvest()
		move(North)
	move(East)