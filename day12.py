class Assembly:

	def __init__(self):
		self.registers = {"a": 0, "b": 0, "c": 1, "d": 0}
		self.instructions = []
		self.current = 0

	def copy(self, source, register):
		if source.isdigit():
			self.registers[register] = int(source)
		else:
			self.registers[register] = self.registers[source]
		self.current += 1

	def increase(self, register):
		self.registers[register] += 1
		self.current += 1

	def decrease(self, register):
		self.registers[register] -= 1
		self.current += 1

	def jump(self, conditional, steps):
		if conditional.isdigit() and int(conditional) != 0:
			distance = int(steps)
			self.current += distance
		elif self.registers[conditional] != 0:
			distance = int(steps)
			self.current += distance
		else:
			self.current += 1

	def execute_current_line(self):
		instruction = self.instructions[self.current]
		split = instruction.split(" ")
		if split[0] == "inc":
			self.increase(split[1])
		elif split[0] == "dec":
			self.decrease(split[1])
		elif split[0] == "cpy":
			self.copy(split[1], split[2])
		else:
			self.jump(split[1], split[2])

	def parse_file(self):
		f = open("day12.txt")
		line = f.readline()
		while line != "":
			line = line.strip()
			self.instructions.append(line)
			line = f.readline()

	def execute(self):
		self.parse_file()
		while self.current < len(self.instructions):
			self.execute_current_line()
			print self.current
		print self.registers

assembly = Assembly()
assembly.execute()
