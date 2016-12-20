import hashlib

input_key = "ngcjuoqr"
cache = {}

def hash(string):
	hasher = hashlib.new("md5")
	hasher.update(string)
	return hasher.hexdigest()

def get_2016_hash(string):
	if cache.has_key(string):
		return cache[string]
	else:
		hash_str = hash(string)
		for _ in range(2016):
			new_hash = hash(hash_str)
			hash_str = new_hash
		cache[string] = hash_str
		return hash_str

def has_triplet(string):
	for i in range(len(string)-2):
		if string[i] == string[i+1] and string[i+1] == string[i+2]:
			return string[i]
	return False

def has_quintet(string, char):
	for i in range(len(string)-4):
		if string[i] == char:
			if string[i+1] == char and string[i+2] == char and string[i+3] == char and string[i+4] == char:
				return True
	return False

def is_key(number):
	new_key = input_key + str(number)
	new_hash = get_2016_hash(new_key)
	i = 1
	result = has_triplet(new_hash)
	if not result:
		return False
	else:
		while i <= 1000:
			new_key = input_key + str(number + i)
			if has_quintet(get_2016_hash(new_key), result):
				return True
			i += 1
		return False

def run():
	index = 0
	salt = 0
	keys = []
	while index < 64:
		if is_key(salt):
			index += 1
			keys.append(salt)
			print salt
		salt += 1
	return keys[-1]

print run()
