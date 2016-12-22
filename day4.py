class FrequencyString():
	def list_sorted_frequency(self):
		return sorted(self.frequencies, cmp = self.compare)

	# custom comparator
	def compare(self, item1, item2):
		if item1[1] > item2[1]:
			return -1
		elif item1[1] < item2[1]:
			return 1
		else:
			if item1[0] < item2[0]:
				return -1
			else:
				return 1

	def __init__(self, string):
		self.frequencies = []
		frequency_map = {}
		for letter in string:
			if letter in frequency_map:
				frequency_map[letter] += 1
			else:
				frequency_map[letter] = 1

		# key is letter, value is number
		for key, value in frequency_map.iteritems():
			self.frequencies.append((key, value))

class Room():
	def __init__(self, string):
		split_input = string.split("[")
		non_hash = split_input[0]
		checksum = split_input[1][:-1]
		split_non_hash = non_hash.split("-")

		self.hash_code = split_input[1][:-1]
		self.room_id = int(split_non_hash[-1])
		self.encrypted_name = (" ").join(split_non_hash[:-1])
		self.frequency_string = FrequencyString(("").join(split_non_hash[:-1]))

	def is_a_room(self):
		frequency = self.frequency_string.list_sorted_frequency()
		for i in range(len(self.hash_code)):
			if self.hash_code[i] != frequency[i][0]:
				return False
		return True

	def decrypt(self):
		for _ in range(self.room_id):
			self.shift()
		print self.encrypted_name, self.room_id

	def shift(self):
		string_as_list = []
		for char in self.encrypted_name:
			if char == "z":
				string_as_list.append("a")
			elif char != " ":
				string_as_list.append(chr(ord(char) + 1))
			else:
				string_as_list.append(" ")
		self.encrypted_name = ("").join(string_as_list)

class RoomDecoder():
	def __init__(self):
		f = open("day4input.txt")
		line = f.readline()
		self.total_sum = 0

		while line != "":
			room = Room(line.strip())
			if room.is_a_room():
				room.decrypt()
			line = f.readline()

rd = RoomDecoder()
# room = Room("totally-real-room-200[decoy]")
# print room.is_a_room()