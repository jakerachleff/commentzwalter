"""
File: main.py
-------------------
Final Project: Commentz-Walter String Matching Algorithm
Course: CS 166
Author: Christina Gilbert

Main file for testing runtimes of Aho-Corasick vs Rabin Karp vs
Commentz Walter algorithms for plagarism using k-shingles of a test
file against a corpus of other files.
"""

import pathlib
import ahocorasick
import time
from enum import Enum

TEST_FILE = "corpus/text3"
CORPUS = "corpus/"
SHINGLE_LEN = 15

match_count = 0


##### GENERAL UTILITIES #####


class Algorithm(Enum):
	aho_corasick = 0
	rabin_karp = 1
	commentz_walter = 2

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


##### AHO CORASICK #####


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

def ac_match_callback(index, value):
	"""Callback function for ac.find_all

	Prints all matches and increments count.

	@param index: index in string T of match
	@param value: tuple (index, value) number of shingle, text of shingle
	"""
	global match_count
	match_count += 1
	print(index)
	print(value)

def aho_corasick(shingles, file_names):
	"""Uses Aho-Corasick automaton to find all matches

	@param shingles: list of shingles of test document
	@param file_names: list of all file_names to be checked for shingles
	@return: time elapsed to match all shingles to all files
	"""

	#start the timer on aho-corasick
	start_time = time.time()

	ac = build_ahocorasick(shingles)
	for file_name in file_names:
		text = ''.join([line.rstrip('\n') for line in open(file_name)])
		ac.find_all(text, ac_match_callback)

	elapsed_time = time.time() - start_time
	print("TOTAL MATCHES: {matches}".format(matches=match_count))
	return elapsed_time


##### RABIN KARP #####
def rabin_karp(shingles, file_names):
	"""Uses Rabin-Karp algorithm to find all matches

	@param shingles: list of shingles of test document
	@param file_names: list of all file_names to be checked for shingles
	@return: time elapsed to match all shingles to all files
	"""

	#start the timer on rabin-karp
	start_time = time.time()

	###### TODO: IMPLEMENT THIS ######

	elapsed_time = time.time() - start_time
	print("TOTAL MATCHES: {matches}".format(matches=match_count))
	return elapsed_time


##### COMMENTZ WALTER #####


def commentz_walter(shingles, file_names):
	"""Uses Commentz-Walter algorithm to find all matches

	@param shingles: list of shingles of test document
	@param file_names: list of all file_names to be checked for shingles
	@return: time elapsed to match all shingles to all files
	"""

	#start the timer on commentz-walter
	start_time = time.time()

	###### TODO: IMPLEMENT THIS ######

	elapsed_time = time.time() - start_time
	print("TOTAL MATCHES: {matches}".format(matches=match_count))
	return elapsed_time

##### MAIN #####


def run_tests(shingles, file_names, algorithm):
""" Runs all tests on algorithm and prints and returns the runtime

	@param shingles: list of shingles of test document
	@param file_names: list of all file_names to be checked for shingles
	@param algorithm: Algorithm to be tested
	@return: time elapsed to match all shingles to all files
"""

	if(algorithm == Algorithm.aho_corasick):
		runtime = aho_corasick(shingles, file_names)

	if(algorithm == Algorithm.rabin_karp):
		runtime = rabin_karp(shingles, file_names)

	if(algorithm == Algorithm.commentz_walter):
		runtime = commentz_walter(shingles, file_names)
	
	print("ELAPSED TIME: {time}".format(time=runtime))
	return runtime

if __name__ == '__main__':

	#test of document we want to detect plararism in
	test_file_text = ''.join([line.rstrip('\n') for line in open(TEST_FILE)])
	shingles = get_shingles(test_file_text, SHINGLE_LEN)
	
	#filenames of all other files
	file_names = files_in_directory(CORPUS)

	run_tests(shingles, file_names, Algorithm.aho_corasick)
	run_tests(shingles, file_names, Algorithm.rabin_karp)
	run_tests(shingles, file_names, Algorithm.commentz_walter)




