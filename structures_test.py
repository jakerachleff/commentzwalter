"""
File: structures-test.py
-------------------
Final Project: Commentz-Walter String Matching Algorithm
Course: CS 166
Authors: Eric Ehizokhale and Jake Rachleff

Tests three data structures: Trie, Aho Corsick, and Commentz-Walter
"""

from structures import Trie, ACAuto, CWAuto


def test_Trie():
	print("TESTING THE TRIE DATA STRUCTURE")
	our_trie = Trie()
	our_trie.add_word("hello")
	our_trie.add_word("help")
	our_trie.add_word("howdy")
	our_trie.add_word("james")
	our_trie.add_word("hello")
	our_trie.lookup("helpo")
	our_trie.lookup("hello")
	our_trie.lookup("help")
	our_trie.lookup("howdy")
	print("DONE TESTING THE TRIE DATA STRUCTURE\n\n\n")

def test_ACAuto():
	print("TESTING THE AHO CORSICK DATA STRUCTURE")
	our_ACAuto = ACAuto()
	print("First testing its trie structure: ")
	our_ACAuto.add_word("hello")
	our_ACAuto.add_word("help")
	our_ACAuto.add_word("howdy")
	our_ACAuto.add_word("james")
	our_ACAuto.add_word("jake")
	our_ACAuto.add_word("ello")
	our_ACAuto.add_word("hello")
	our_ACAuto.add_word("shello")
	our_ACAuto.lookup("helpo")
	our_ACAuto.lookup("hello")
	our_ACAuto.lookup("howdy")

	print("\n\nNow, testing its ACAuto ability:")
	our_ACAuto.create_failure_links()
	our_ACAuto.report_all_matches("jameshelloa;sldkfj;asdljfadello")
	print("DONE TESTING THE AHO CORSICK DATA STRUCTURE\n\n")

def test_CWAuto():
	print("TESTING THE CWAUTO DATA STRUCTURE")
	our_CWAuto = CWAuto()
	our_CWAuto.add_word("cacbaa")
	our_CWAuto.add_word("acb")
	our_CWAuto.add_word("aba")
	our_CWAuto.add_word("acbab")
	our_CWAuto.add_word("ccbab")
	our_CWAuto.lookup("babca")
	our_CWAuto.lookup("acbab")
	our_CWAuto.lookup("aba")
	our_CWAuto.lookup("tom")
	our_CWAuto.lookup("cacbaa")
	our_CWAuto.create_failure_links()
	our_CWAuto.report_all_matches("cacbaababababa")

	print("\n\nNow, testing its CWAUTO ability:")
	our_CWAuto = CWAuto()
	our_CWAuto.add_word("hello")
	our_CWAuto.add_word("help")
	our_CWAuto.add_word("howdy")
	our_CWAuto.add_word("james")
	our_CWAuto.add_word("ame")
	our_CWAuto.add_word("jake")
	our_CWAuto.add_word("ello")
	our_CWAuto.add_word("hello")
	our_CWAuto.add_word("shello")
	our_CWAuto.create_failure_links()
	our_CWAuto.report_all_matches("jameshelloa;sldkfj;asdljfadello")
	print("DONE TESTING THE CWAUTO DATA STRUCTURE\n\n")

def main():
	test_Trie()
	test_ACAuto()
	test_CWAuto()
	

if __name__ == "__main__":
	main()
