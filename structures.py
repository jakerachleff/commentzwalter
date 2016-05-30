NO_DIFFERENCE_SET = -1

class Node(object):
	def __init__(self, character):
		self.character = character
		self.word = None
		self.children = {}
		self.output_link = None
		self.suffix_link = None

class ACNode(Node):
	def __init__(self, character):
		Node.__init__(self, character)


class CWNode(Node):
	def __init__(self, character, depth):
		Node.__init__(self, character)
		self.depth = depth
		self.min_difference = NO_DIFFERENCE_SET

class Trie(object):
	def __init__(self):
		self.size = 0
		self.root = Node(None)	#char doesn't exist for root

	def add_word(self, word):
		current_node = self.root
		for character in word:
			next_node = current_node.children.get(character)
			if not next_node:
				next_node = Node(character)
				current_node.children[character] = next_node

			current_node = next_node

		if current_node.word is not None:
			print ("you have already printed " + word)
			return

		current_node.word = word
		self.size += 1

	def lookup(self,word):
		current_node = self.root
		for character in word:
			next_node = current_node.children.get(character)
			if not next_node:
				print ("The word " + word + " is invalid")
				return False

			current_node = next_node

		if not (current_node.word == word):
			print ("You suck at implementing tries")

		return True

