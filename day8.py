class Screen:
	def __init__(self):
		self.on_count = 0
		self.width = 50
		self.height = 6
		self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]

	def __repr__(self):
		for i in self.board:
			print i
		return ""

	def turn_on(self, col, row):
		to_flip = []
		for i in range(row):
			for j in range(col):
				to_flip.append((i, j))

		for pair in to_flip:
			pixel = self.board[pair[0]][pair[1]]
			if pixel == 0:
				self.board[pair[0]][pair[1]] = 1
				self.on_count += 1

	def shift_down(self, col, count):
		column_contents = []
		for row in self.board:
			column_contents.append(row[col])
		cutoff = self.height - count
		modified_column_contents = column_contents[cutoff:self.height] + column_contents[:cutoff] 
		index = 0
		for row in self.board:
			row[col] = modified_column_contents[index]
			index += 1

	def shift_right(self, row, count):
		current_row = self.board[row]
		cutoff = self.width - count
		new_row = current_row[cutoff:self.width] + current_row[:cutoff]
		self.board[row] = new_row

	def get_x_y(self, string):
		x = ""
		y = ""
		ind = 0
		is_x = True
		while ind < len(string):
			if string[ind] == "x":
				is_x = False
			else:
				if is_x:
					x += string[ind]
				else:
					y += string[ind]
			ind += 1
		return int(x), int(y) 

	def get_loc_count(self, string1, string2):
		return int(string1[2:]), int(string2)

	def parse_line(self, string):
		string_split = string.split(" ")
		if string_split[0] == "rect":
			# next string is a x y
			x, y = self.get_x_y(string_split[1])
			self.turn_on(x, y)
		else:
			if string_split[1] == "row":
				y, count = self.get_loc_count(string_split[2], string_split[4])
				self.shift_right(y, count)
			else:
				x, count = self.get_loc_count(string_split[2], string_split[4])
				self.shift_down(x, count)

	def read_file(self):
		f = open("day8input.txt")
		line = f.readline()
		while line != "":
			line = line.strip()
			self.parse_line(line)
			line = f.readline()

screen = Screen()
screen.read_file()
print screen.on_count
print screen
