# part 1
triangles = []

# part 2
col1 = []
col2 = []
col0 = []

def is_triangle(sides):
	s1 = sides[0]
	s2 = sides[1]
	s3 = sides[2] 

	if (s1 + s2 > s3) and (s2 + s3 > s1) and (s1 + s3 > s2):
		return True
	return False

def get_input_from_url():
	global triangles
	file_path = "day3.txt"
	f = open(file_path, 'r')
	line = f.readline()
	while line != "":
		triangle_sides = process_line(line)
		triangles.append(triangle_sides)
		line = f.readline()

def get_input_from_url2():
	global col0
	global col1
	global col2
	
	file_path = "day3.txt"
	f = open(file_path, 'r')
	line = f.readline()
	while line != "":
		triangle_sides = process_line(line)
		col0.append(triangle_sides[0])
		col1.append(triangle_sides[1])
		col2.append(triangle_sides[2])
		line = f.readline()

def find_proper_triangles_p2():
	count = 0
	for i in xrange(0, len(col0), 3):
		s1 = col0[i]
		s2 = col0[i+1]
		s3 = col0[i+2]

		if is_triangle([s1, s2, s3]):
			count += 1
	for i in xrange(0, len(col1), 3):
		s1 = col1[i]
		s2 = col1[i+1]
		s3 = col1[i+2]

		if is_triangle([s1, s2, s3]):
			count += 1

	for i in xrange(0, len(col2), 3):
		s1 = col2[i]
		s2 = col2[i+1]
		s3 = col2[i+2]

		if is_triangle([s1, s2, s3]):
			count += 1
	return count

def process_line(line):
	sides = []
	split_line = line.split(" ")
	for item in split_line:
		if item != "":
			sides.append(int(item))
	return sides

def find_proper_triangles():
	get_input_from_url()
	count = 0
	for triangle in triangles:
		if is_triangle(triangle):
			count += 1
	return count

get_input_from_url2()
print find_proper_triangles_p2()
