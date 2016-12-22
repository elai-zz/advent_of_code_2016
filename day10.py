from sets import Set

class Bots:
	def __init__(self):
		self.deleted = Set()
		self.bot_values = {}
		self.instructions = {}
		self.outputs = {}
		self.comparisons = {}

	def put_value_in_bot(self, bot, value):
		if bot in self.bot_values:
			self.bot_values[bot] += [value]
		else:
			self.bot_values[bot] = [value]

	def parse_instr(self, bot, low, high):
		self.instructions[bot] = (low, high)

	def evaluate_bot(self, bot):
		low_bot = self.instructions[bot][0]
		high_bot = self.instructions[bot][1]
		values = self.bot_values[bot]

		# give them to the different bots, or output
		if type(low_bot) is str:
			self.outputs[int(low_bot[1:])] = min(values)
		else:
			self.put_value_in_bot(low_bot, min(values))

		if type(high_bot) is str :
			self.outputs[int(high_bot[1:])] = max(values)
		else:
			self.put_value_in_bot(high_bot, max(values))

		# take note of the comparison
		if values == [61, 17] or values == [17, 61]:
			print "bot ", bot, "compares ", values
		self.comparisons[bot] = values

	def run_one_round(self):
		for bot in self.bot_values.keys():
			values = self.bot_values[bot]
			if len(values) == 2:
				self.evaluate_bot(bot)
				del self.bot_values[bot]

	def run_instructions(self):
		while len(self.bot_values) > 0:
			self.run_one_round()

	def parse_instruction(self, string):
		str_split = string.split(" ")
		if str_split[0] == "value":
			value = int(str_split[1])
			bot = int(str_split[5])
			self.put_value_in_bot(bot, value)
		else:
			bot = int(str_split[1])
			if str_split[5] == "output":
				low = "O" + str_split[6]
			else:
				low = int(str_split[6])

			if str_split[-2] == "output":
				high = "O" + str_split[-1]
			else:
				high = int(str_split[-1])

			self.instructions[bot] = (low, high)

	def start(self):
		f = open("day10.txt")
		line = f.readline()
		while line != "":
			line = line.strip()
			self.parse_instruction(line)
			line = f.readline()

bots = Bots()
bots.start()
bots.run_instructions()
print bots.outputs

