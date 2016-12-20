import hashlib

class PasswordFinder:

	trailingDigit = long(0)
	doorId = ""
	password = ["","","","","","","",""]
	count = 0

	def __init__(self, door):
		self.doorId = door

	def hash(self, string):
		hasher = hashlib.new("md5")
		hasher.update(string)
		return hasher.hexdigest()

	def getDigitIfIsSpecial(self, string):
		hashedString = self.hash(string)
		if hashedString[0:5] == "00000":
			self.password.append(hashedString[5])
			return True
		else:
			return False

	def getDigitAndPositionIfIsSpecial(self, string):
		hashedString = self.hash(string)
		if hashedString[0:5] == "00000":
			position = hashedString[5]
			digit = hashedString[6]
			if position.isdigit() and int(position) < 8 and self.password[int(position)] == "":
				self.password[int(position)] = digit
				self.count += 1
			return True
		else:
			return False

	def findPasswordFromID(self):
		while self.count < 8:
			newString = self.doorId + str(self.trailingDigit)
			self.getDigitAndPositionIfIsSpecial(newString)
			self.trailingDigit += 1
		return self.password

if __name__ == '__main__':
	passwordFinder = PasswordFinder("reyedfim")
	print passwordFinder.findPasswordFromID()