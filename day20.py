
def parse_file():
	pairs = []
	f = open("day20.txt")
	line = f.readline()
	while line != "":
		line = line.strip()
		split = line.split('-')
		pairs.append((int(split[0]), int(split[1])))
		line = f.readline()

	return pairs

def compare(item1, item2):
	return item1[0] - item2[0]

def find_first(pairs):
	window = [pairs[0][0], pairs[0][1]]
	for pair in pairs[1:]:
		if pair[0] > window[1] + 1:
			return window[1] + 1
		if pair[1] > window[1]:
			window[1] = pair[1]
	return 

def count(pairs):
	count = 0
	window = [pairs[0][0], pairs[0][1]]
	for pair in pairs[1:]:
		if pair[0] > window[1] + 1:
			count += (pair[0] - (window[1] + 1))
			window = [pair[0], pair[1]]
		if pair[1] > window[1]:
			window[1] = pair[1]
	return count

def run():
	pairs = parse_file()
	sorted_pairs = sorted(pairs, cmp = compare)
	print count(sorted_pairs)

run()