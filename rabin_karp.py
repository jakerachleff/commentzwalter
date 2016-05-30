class RollingHash:
	"""
	This function from https://github.com/mccricardo/Rabin-Karp
	"""
	def __init__(self, string, size):
		self.str  = string
		self.hash = 0
		
		for i in range(0, size):
			self.hash += ord(self.str[i])
		
		self.init = 0
		self.end  = size
		
	def update(self):
		if self.end <= len(self.str) -1:
			self.hash -= ord(self.str[self.init])
			self.hash += ord(self.str[self.end])
			self.init += 1
			self.end  += 1
			
	def digest(self):
		return self.hash

	def text(self):
		return self.str[self.init:self.end]

# def rabin_karp(substring, string):
# 	"""
# 	This function from https://github.com/mccricardo/Rabin-Karp
# 	"""
# 	if substring == None or string == None:
# 		return -1
# 	if substring == "" or string == "":
# 		return -1

# 	if len(substring) > len(string):
# 		return -1

# 	hs 	 = RollingHash(string, len(substring))
# 	hsub = RollingHash(substring, len(substring))
# 	hsub.update()
		
# 	for i in range(len(string)-len(substring)+1):						
# 		if hs.digest() == hsub.digest():
# 			if hs.text() == substring:
# 				return i
# 		hs.update()

# 	return -1

def rabin_karp_pattern_set(test_file_text, k):
	"""
	"""

	#note -- if we want to analyze this we should probably use a
	#bloom filter, because its actually guaranteed constant
	#insertion/lookup
	digest_set = set()

	hs 	 = RollingHash(test_file_text, k)
	for i in range(len(test_file_text) - k + 1):
		digest_set.add(hs.digest)
		hs.update()
	
	return digest_set


