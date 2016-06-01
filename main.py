"""
File: main.py
-------------------
Final Project: Commentz-Walter String Matching Algorithm
Course: CS 166
Author: Christina Gilbert
Group: Christina Gilbert, Eric Ehizokhale, Jake Rachleff

Main file for testing runtimes of Aho-Corasick vs Rabin Karp vs
Commentz Walter algorithms for plagarism using k-shingles of a test
file against a corpus of other files.
"""

import pathlib
import rabin_karp
import time
import random
from enum import Enum
from collections import namedtuple
from structures import ACAuto
from structures import CWAuto

TEST_FILE = "corpus/testfile"
CORPUS_PREFIX = "article_scraper/articles/"
SHINGLE_CONSTANT = 50
RANDOM = False
OUTFILE_PATH = "outfile.txt"

ac_match_count = 0


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


def build_automaton(shingles, automaton):
	"""Return an Aho-Corasick Automaton for a list of shingles

	@param shingles: list of k-shingles
	@return: Aho-Corasick Automaton for shingles
	"""
	a = ACAuto() if automaton == Algorithm.aho_corasick else CWAuto()
	for shingle in shingles:
		a.add_word(shingle)
	a.create_failure_links()
	return a

	# a = ahocorasick.Automaton()
	# for index, shingle in enumerate(shingles):
	# 	a.add_word(shingle, (index, shingle))
	# a.make_automaton()
	# return a

def get_random_shingles(text, k):
	"""//TODO DOCUMENT

	@param text: string to convert to shingles
	@param k: length of each single
	@return: list of shingles
	"""

	length = len(text)

	all_shingles = [text[i:i+k] for i in range(length) if i + k < length]
	random_shingles = random.sample(all_shingles, int(len(all_shingles)/SHINGLE_CONSTANT))
	return random_shingles

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
	global ac_match_count
	ac_match_count += 1

def run_aho_corasick(shingles, file_names):
	"""Uses Aho-Corasick automaton to find all matches

	@param shingles: list of shingles of test document
	@param file_names: list of all file_names to be checked for shingles
	@return: (time, matches) time elapsed to match all shingles to all files
	total number of matches found in text
	"""

	#start the timer on aho-corasick
	start_time = time.time()

	ac_total_matches = 0
	ac = build_automaton(shingles, Algorithm.aho_corasick)

	for file_name in file_names:
		#print(file_name)

		text = ''.join([line.rstrip('\n') for line in open(file_name)])
		ac_total_matches += ac.report_all_matches(text)

	elapsed_time = time.time() - start_time
	return Result(elapsed_time, ac_total_matches)


##### RABIN KARP #####
def run_rabin_karp(test_file_text, shingles, shingle_len, file_names):
	"""Uses Rabin-Karp algorithm to find all matches

	@param shingles: list of shingles of test document
	@param file_names: list of all file_names to be checked for shingles
	@param shingle_len: length of shingles
	@return: Result(time, matches) time elapsed to match all shingles to all files
	total number of matches found in text
	"""


	#TODO: Decide if this should come before or after timer
	shingles = set(shingles)

	#start the timer on rabin-karp
	start_time = time.time()

	pattern_set = rabin_karp.rabin_karp_pattern_set(test_file_text, shingle_len)
	rc_matches_count = 0

	for file_name in file_names:
		text = ''.join([line.rstrip('\n') for line in open(file_name)])
		rc_matches_count += rabin_karp.rabin_karp_get_matches(text, shingle_len, shingles, pattern_set)


	elapsed_time = time.time() - start_time
	return Result(elapsed_time, rc_matches_count)


##### COMMENTZ WALTER #####


def run_commentz_walter(shingles, file_names):
	"""Uses Commentz-Walter algorithm to find all matches

	@param shingles: list of shingles of test document
	@param file_names: list of all file_names to be checked for shingles
	@return: Result(time, matches) time elapsed to match all shingles to all files
	total number of matches found in text
	"""

	start_time = time.time()

	cw_total_matches = 0
	cw = build_automaton(shingles, Algorithm.commentz_walter)

	for file_name in file_names:
		text = ''.join([line.rstrip('\n') for line in open(file_name)])
		cw_total_matches += cw.report_all_matches(text)

	elapsed_time = time.time() - start_time
	return Result(elapsed_time, cw_total_matches)


##### MAIN #####


def run_tests(file_names, test_file_text, shingle_len, shingles, algorithm):
	""" Runs all tests on algorithm and prints and returns the runtime

		@param file_names: list of all file_names to be checked for shingles
		@param test_file_text: text of the file we're testing against
		@param shingle_len
		@param algorithm: Algorithm to be tested
		@return: time elapsed to match all shingles to all files
	"""

	if(algorithm == Algorithm.aho_corasick):
		print("####   AHO-CORASICK   ####")
		result = run_aho_corasick(shingles, file_names)

	if(algorithm == Algorithm.rabin_karp):
		print("####    RABIN-KARP    ####")
		result = run_rabin_karp(test_file_text, shingles, shingle_len, file_names)

	if(algorithm == Algorithm.commentz_walter):
		print("#### COMMENTZ-WALTER  ####")
		result = run_commentz_walter(shingles, file_names)
		
	
	print("ELAPSED TIME: {time}".format(time=result.runtime))
	print("TOTAL MATCHES: {matches}".format(matches=result.matches))
	return result.runtime

def write_to_outfile(string_to_write):
	try:
		new_file = open(OUTFILE_PATH, 'a')
		new_file.write(string_to_write)
		new_file.write('\n')
		new_file.close()

	except:
		print('Error creating file {filename}'.format(filename = OUTFILE_PATH))

def run_all_tests(file_names, test_file_text, shingles, shingle_len):
	print("SHINGLE LENGTH: {len}".format(len=shingle_len))

	ac_runtime = run_tests(file_names, test_file_text, shingle_len, shingles, Algorithm.aho_corasick)
	rk_runtime = run_tests(file_names, test_file_text, shingle_len, shingles, Algorithm.rabin_karp)
	cw_runtime = run_tests(file_names, test_file_text, shingle_len, shingles, Algorithm.commentz_walter)

	write_to_outfile("SHINGLE LENGTH: {len}".format(len=shingle_len))
	write_to_outfile(str(ac_runtime))
	write_to_outfile(str(rk_runtime))
	write_to_outfile(str(cw_runtime))

	print("-- -- -- -- -- -- -- -- -- -- -- ")

if __name__ == '__main__':

	Result = namedtuple('Result', ['runtime', 'matches'])
	corpuses = []
	corpuses.append("all_articles2.3MB")

	#test of document we want to detect plagarism in
	test_file_text = ''.join([line.rstrip('\n') for line in open(TEST_FILE)])
	
	for corpus in corpuses:
		write_to_outfile("CORPUS: {corpus}".format(corpus=corpus))

		#filenames of all other files
		file_names = files_in_directory(CORPUS_PREFIX + corpus)
		for i in range(5, 15):
			shingles = get_shingles(test_file_text, i) if not RANDOM else get_random_shingles(test_file_text, i)
			print("RANDOM: {random}".format(random=RANDOM))
			print("CORPUS: {corpus}".format(corpus=corpus))
			run_all_tests(file_names, test_file_text, shingles, i)




