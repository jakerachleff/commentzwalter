from structures import Trie, ACAuto

def test_Trie():
	our_trie = Trie()
	our_trie.add_word("hello")
	our_trie.add_word("help")
	our_trie.add_word("howdy")
	our_trie.add_word("james")
	our_trie.add_word("hello")
	our_trie.lookup("helpo")
	our_trie.lookup("hello")
	our_trie.lookup("howdy")

def test_ACAuto():
	our_ACAuto = ACAuto()
	print("First testing its trie structure: ")
	our_ACAuto.add_word("hello")
	our_ACAuto.add_word("help")
	our_ACAuto.add_word("howdy")
	our_ACAuto.add_word("james")
	our_ACAuto.add_word("hello")
	our_ACAuto.lookup("helpo")
	our_ACAuto.lookup("hello")
	our_ACAuto.lookup("howdy")

	print("Now, testing its ACAuto ability")

def main():
	test_Trie()
	test_ACAuto()
	

if __name__ == "__main__":
	main()
