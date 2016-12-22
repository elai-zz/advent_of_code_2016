from sets import Set

class MazeCell:

	def __init__(self, x, y, step):
		self.x = x
		self.y = y
		self.step = step

class Maze:

	def __init__(self, fav, origin, destination):
		self.input = fav 
		self.dest = destination
		self.origin = origin
		self.visited = Set()

	def is_wall(self, x, y):
		num1 = x*x + 3*x + 2*x*y + y*y + y
		bin_string = bin(num1 + self.input)[2:]
		ones = 0
		for char in bin_string:
			if char == '1':
				ones += 1
		return ones % 2 == 1

	def get_all_possibles(self, step, x, y):
		# need to use is_wall
		possibles = []
		if (x > 0) and not self.is_wall(x-1, y) and (x-1, y) not in self.visited:
			possibles.append(MazeCell(x - 1, y, step))
		if (y > 0) and not self.is_wall(x, y-1) and (x, y-1) not in self.visited:
			possibles.append(MazeCell(x, y - 1, step))
		if not self.is_wall(x, y + 1) and (x, y + 1) not in self.visited:
			possibles.append(MazeCell(x, y + 1, step))
		if not self.is_wall(x + 1, y) and (x + 1, y) not in self.visited:
			possibles.append(MazeCell(x + 1, y, step))

		return possibles

	def get_steps(self):
		queue = []
		queue.append(self.origin)
		below_50 = 0

		while queue != []:
			current_cell = queue[0]
			queue = queue[1:]
			all_possible = self.get_all_possibles(current_cell.step + 1, current_cell.x, current_cell.y)

			if current_cell.step + 1 <= 50:
					below_50 += len(all_possible)

			for possible_cell in all_possible:
				if possible_cell.x == self.dest.x and possible_cell.y == self.dest.y:
					# print "found it"
					# print possible_cell.step
					print below_50
					return
				self.visited.add((possible_cell.x, possible_cell.y))
			queue += all_possible

		return

startcell = MazeCell(1, 1, 0)
endcell = MazeCell(31, 39, None)
maze = Maze(1350, startcell, endcell)
maze.get_steps()