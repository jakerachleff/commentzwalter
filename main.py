import pathlib
import ahocorasick
from enum import Enum

TEST_FILE = "corpus/text3"
CORPUS = "corpus/"
SHINGLE_LEN = 15

match_count = 0

class Algorithm(Enum):
	aho_corasick = 0
	rabin_karp = 1
	commentz_walter = 2

def build_ahocorasick(shingles):
	"""Return an Aho-Corasick Automaton for a list of shingles

	@param shingles: list of k-shingles
	@return: Aho-Corasick Automaton for shingles
	"""
	a = ahocorasick.Automaton()
	for index, shingle in enumerate(shingles):
		a.add_word(shingle, (index, shingle))
	a.make_automaton()
	return a

def get_shingles(text, k):
	"""Return a list of the k-singles of a text file

	@param text: string to convert to shingles
	@param k: length of each single
	@return: list of shingles
	"""

	length = len(text)
	return [text[i:i+k] for i in range(length) if i + k < length]
	
def files_in_directory(dirname):
	"""CITATION: Taken from the starter code of a CS41 assignment

	Return a list of filenames in the given directory.

	@param dirname: name of directory from which to acquire files.
	@return: list of strings representing names of files in the given directory
	"""
	p = pathlib.Path(dirname)
	if not p.is_dir():
		raise NotADirectoryError("`{d}` is not a directory".format(d=dirname))
	return [str(child) for child in p.iterdir() if child.is_file()]

def ac_match_callback(index, value):
	global match_count
	match_count += 1
	print(index)
	print(value)

def run_tests(shingles, file_names, algorithm):
	if(algorithm == Algorithm.aho_corasick):
		aho_corasick(shingles, file_names)

	if(algorithm == Algorithm.rabin_karp):
		pass

	if(algorithm == Algorithm.commentz_walter):
		pass

def aho_corasick(shingles, file_names):
	ac = build_ahocorasick(shingles)
	for file_name in file_names:
		text = ''.join([line.rstrip('\n') for line in open(file_name)])
		ac.find_all(text, ac_match_callback)
		break

	print("TOTAL MATCHES: {matches}".format(matches=match_count))

if __name__ == '__main__':

	#test of document we want to detect plararism in
	test_file_text = ''.join([line.rstrip('\n') for line in open(TEST_FILE)])
	shingles = get_shingles(test_file_text, SHINGLE_LEN)
	
	#filenames of all other files
	file_names = files_in_directory(CORPUS)

	run_tests(shingles, file_names, Algorithm.aho_corasick)
	run_tests(shingles, file_names, Algorithm.rabin_karp)
	run_tests(shingles, file_names, Algorithm.commentz_walter)




