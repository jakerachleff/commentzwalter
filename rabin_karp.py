"""
File: rabin-karp.py
-------------------
Final Project: Commentz-Walter String Matching Algorithm
Course: CS 166
Authors: Christina Gilbert, Ricardo Castro

RollingHash class from Ricardo Castro's implementation of Rabin-Karp
at https://github.com/mccricardo/Rabin-Karp

Group: Christina Gilbert, Eric Ehizokhale, Jake Rachleff

Main file for testing runtimes of Aho-Corasick vs Rabin Karp vs
Commentz Walter algorithms for plagarism using k-shingles of a test
file against a corpus of other files.
"""

class RollingHash:
	"""
	Class for the "RollingHash" used in Rabin-Karp which allows
	for constant time updates for the hash values of two strings
	that are offset by a single character in a longer string

	This class by Ricardo Castro from 
	https://github.com/mccricardo/Rabin-Karp
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

def rabin_karp_get_matches(text, k, shingles, pattern_set):
	""" Given a document to match against, a set of shingles, and 
	a set of the shingle hashes, returns the total number of matches
	in the document.

	@param text: string of document to match against
	@param k: length of shingles
	@param shingles: set of shingles
	@param pattern_set: set of "rolling" hashcodes of shingles
	@return: total number of matches
	"""
	if k > len(text):
		return 0

	rc_match_count = 0

	hs = RollingHash(text, k)
	for i in range(len(text)- k +1):
		if hs.hash in pattern_set:
			if hs.text() in shingles:
				rc_match_count += 1
		hs.update()

	return rc_match_count



def rabin_karp_pattern_set(test_file_text, k):
	""" Given a document to detect matches for, creates a set of 
	for the "rolling" hashcodes of each shingle.

	Runtime: O(len(test_file_text)) with a very small constant factor

	@param test_file_text: string of file to detect matchse for
	@param k: length of shingles
	@return: set of "rolling" hashes for all shingles
	"""

	#note -- if we want to analyze this we should probably use a
	#bloom filter, because its actually guaranteed constant
	#insertion/lookup
	digest_set = set()

	hs 	 = RollingHash(test_file_text, k)
	for i in range(len(test_file_text) - k + 1):
		digest_set.add(hs.hash)
		hs.update()
	
	return digest_set


