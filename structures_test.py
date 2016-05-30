from structures import Trie

def main():
	our_trie = Trie()
	our_trie.add_word("hello")
	our_trie.add_word("help")
	our_trie.add_word("howdy")
	our_trie.add_word("james")
	our_trie.add_word("hello")
	our_trie.lookup("helpo")
	our_trie.lookup("hello")
	our_trie.lookup("howdy")

if __name__ == "__main__":
	main()
