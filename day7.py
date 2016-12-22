from sets import Set

def has_abba_palindrome(string):
	if len(string) < 4:
		return False
	else:	
		head = 0
		tail = head + 3
		while tail < len(string):
			if string[head] == string[tail]:
				if string[head+1] == string[head+2] and string[head+1] != string[head]:
					return True
			head += 1
			tail += 1
		return False

def break_string_apart(string):
	outside_set = []
	inside_set = []
	current_index = 0
	current_string = []

	while current_index < len(string):
		if string[current_index] == "[":
			outside_set.append(("").join(current_string))
			current_string = []
		elif string[current_index] == "]":
			inside_set.append(("").join(current_string))
			current_string = []
		else:
			current_string.append(string[current_index])
		current_index += 1

	if current_string != []:
		outside_set.append(("").join(current_string))
	return outside_set, inside_set

def supports_tsp(outside, inside):
	for inside_string in inside:
		if has_abba_palindrome(inside_string):
			return False

	for outside_string in outside:
		if has_abba_palindrome(outside_string):
			return True

	return False

def get_aba_set(string):
	result_set = Set()
	if len(string) < 3:
		return result_set
	else:	
		head = 0
		tail = head + 2
		while tail < len(string):
			if string[head] == string[tail]:
				if string[head+1] != string[head]:
					result_set.add(string[head:tail+1])
			head += 1
			tail += 1
		return result_set

def supports_ssl(outside, inside):
	total_outside_aba_set = Set()
	for outside_string in outside:
		temp_set = get_aba_set(outside_string)
		total_outside_aba_set = total_outside_aba_set.union(temp_set)

	combined_inside_set = ("").join(inside)
	for aba in total_outside_aba_set:
		bab = aba[1] + aba[0] + aba[1]
		if combined_inside_set.find(bab) > -1:
			return True
	return False


def parse_input():
	count = 0
	f = open("day7_input.txt")
	line = f.readline()
	while line != "":
		line = line.rstrip()
		o, i = break_string_apart(line)
		if supports_ssl(o, i):
			count += 1
		line = f.readline()
	return count

print parse_input()
#o, i = break_string_apart("zazbz[bzb]cdb")
#print supports_ssl(o, i)