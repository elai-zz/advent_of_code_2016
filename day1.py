from sets import Set

# inputs
input_list = ["R5", "R4", "R2", "L3", "R1", "R1", "L4", "L5", "R3", "L1", "L1", "R4", "L2", "R1", "R4", "R4", "L2", "L2", "R4", "L4", "R1", "R3", "L3", "L1", "L2", "R1", "R5", "L5", "L1", "L1", "R3", "R5", "L1", "R4", "L5", "R5", "R1", "L185", "R4", "L1", "R51", "R3", "L2", "R78", "R1", "L4", "R188", "R1", "L5", "R5", "R2", "R3", "L5", "R3", "R4", "L1", "R2", "R2", "L4", "L4", "L5", "R5", "R4", "L4", "R2", "L5", "R2", "L1", "L4", "R4", "L4", "R2", "L3", "L4", "R2", "L3", "R3", "R2", "L2", "L3", "R4", "R3", "R1", "L4", "L2", "L5", "R4", "R4", "L1", "R1", "L5", "L1", "R3", "R1", "L2", "R1", "R1", "R3", "L4", "L1", "L3", "R2", "R4", "R2", "L2", "R1", "L5", "R3", "L3", "R3", "L1", "R4", "L3", "L3", "R4", "L2", "L1", "L3", "R2", "R3", "L2", "L1", "R4", "L3", "L5", "L2", "L4", "R1", "L4", "L4", "R3", "R5", "L4", "L1", "L1", "R4", "L2", "R5", "R1", "R1", "R2", "R1", "R5", "L1", "L3", "L5", "R2"]

visited = Set()
from sets import Set

# gloabl states
current_direction = "N"
x_loc = 0
y_loc = 0

visited = []

def add_to_visited(steps, sign, pos):
	global visited
	for i in range(1, int(steps) + 1):
		if pos == "x":
			new_position = (x_loc + (sign * i), y_loc)
		else:
			new_position = (x_loc, y_loc + (sign * i))

		visited.append(new_position)

def walk(instruction):
	direction = instruction[0]
	steps = instruction[1:]

	delta_x = 0
	delta_y = 0

	global current_direction
	global x_loc
	global y_loc
	global visited

	if current_direction == "N":
		if direction == "R":
			delta_x += int(steps)
			add_to_visited(steps, 1, "x")
			current_direction = "E"
		else:
			delta_x -= int(steps)
			current_direction = "W"
			add_to_visited(steps, -1, "x")

	elif current_direction == "E":
		if direction == "R":
			delta_y -= int(steps)
			current_direction = "S"
			add_to_visited(steps, -1, "y")
		else: 
			delta_y += int(steps)
			current_direction = "N"
			add_to_visited(steps, 1, "y")

	elif current_direction == "S":
		if direction == "R":
			current_direction = "W"
			delta_x -= int(steps)
			add_to_visited(steps, -1, "x")
		else:
			current_direction = "E"
			delta_x += int(steps)
			add_to_visited(steps, 1, "x")
	else:
		if direction == "R":
			current_direction = "N"
			delta_y += int(steps)
			add_to_visited(steps, 1, "y")

		else:
			current_direction = "S"
			delta_y -= int(steps)
			add_to_visited(steps, -1, "y")

	x_loc += delta_x
	y_loc += delta_y

def find_difference(input_list):
	print "Starting at " + str(x_loc) + ", " + str(y_loc)
	for instruction in input_list:
		if walk(instruction):
			break

	print "Now I am at " + str(x_loc) + ", " + str(y_loc)

	print "Now finding the first intersection..."
	for visited_point in visited:
		if visited.count(visited_point) > 1:
			print "The first point you've visited is: " + str(visited_point)
			break
	print("The first part's answer is: ")
	return abs(x_loc) + abs(y_loc)

print find_difference(input_list)
