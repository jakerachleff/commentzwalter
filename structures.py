from collections import deque


NO_DIFFERENCE_SET = -1

class Node(object):
	def __init__(self, character, depth, parent):
		self.character = character
		self.depth = depth
		self.word = None
		self.parent = parent
		self.ACsuffix_link = None
		self.children = {}

class ACNode(Node):
	def __init__(self, character, depth, parent):
		Node.__init__(self, character, depth, parent)
		self.output_link = None
		self.suffix_link = None


class CWNode(Node):
	def __init__(self, character, depth, parent):
		Node.__init__(self, character, depth, parent)
		self.min_difference = NO_DIFFERENCE_SET
		self.output_link = None
		self.CWsuffix_link = None

class Trie(object):
	def create_node(self, character, depth, parent):
		return Node(character, depth, parent)

	def __init__(self):
		self.size = 0
		self.root = self.create_node(None, 0, None)	#char doesn't exist for root

	def add_word(self, word):
		current_node = self.root
		current_depth = 1
		for character in word:
			next_node = current_node.children.get(character)
			if not next_node:
				next_node = self.create_node(character, current_depth, current_node)
				current_node.children[character] = next_node

			if not next_node.depth == current_depth:
				print ("ERROR: Incorrect depths")

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

	def is_root(self, node):
		return node.character is None

	def node_has_child(self, node, character):
		return node.children.get(character) is not None

	def get_AC_suffix_link(self, node):
		searcher = node.parent.ACsuffix_link
		while (not self.is_root(searcher)) and (not self.node_has_child(searcher, node.character)):
			searcher = searcher.ACsuffix_link
			if not searcher:
				import pdb; pdb.set_trace()

		if (self.node_has_child(searcher, node.character)):
			return searcher.children[node.character]
		else:
			if (not self.is_root(searcher)):
				print ("ERROR: Incorrect looping in suffix links")
			return searcher



class ACAuto(Trie):
	def create_node(self, character, depth, parent):
		return ACNode(character, depth, parent)

	def create_failure_links(self):
		"""
		Creates all failure links for an Aho Corsick Automata, should run in O(n) time
		where n is the length of all strings in the automata put together. ONLY RUN THIS
		ONCE ALL WORDS ARE INCLUDED.
		"""
		bfs_queue = deque()

		# First, set suffix links for first children to root
		for key in self.root.children:
			child = self.root.children[key]
			child.ACsuffix_link = self.root

			for key2 in child.children:
				grandchild = child.children[key2]
				bfs_queue.append(grandchild)

		while (len(bfs_queue) > 0):
			current_node = bfs_queue.popleft();
			for key in current_node.children:
				child = current_node.children[key]
				bfs_queue.append(child)

			current_node.ACsuffix_link = self.get_AC_suffix_link(current_node)
			suffix_is_word = current_node.ACsuffix_link.word is not None
			current_node.output_link = current_node.ACsuffix_link if suffix_is_word else current_node.ACsuffix_link.output_link

	def report_all_matches(self, text):
		matches = deque()
		pos = 0
		current_node = self.root
		for character in text:
			# If our current node has character as a child, go to the next node
			if self.node_has_child(current_node, character):
				current_node = current_node.children[character]
			else:
				while not self.is_root(current_node):
					current_node = current_node.ACsuffix_link
					if self.node_has_child(current_node, character):
						current_node = current_node.children[character]
						break

			if (current_node.word is not None):
				matches.append((current_node.word, pos - len(current_node.word) + 1))

			output_searcher = current_node.output_link
			while (output_searcher is not None):
				matches.append((output_searcher.word, pos - len(output_searcher.word) + 1))
				output_searcher = output_searcher.output_link

			pos += 1

		for match, pos in matches:
			print ("matched with " + match + " at position " + str(pos))

class CWAuto(Trie):
	def create_node(self, character, depth, parent):
		return CWNode(character, depth, parent)

	def __init__(self):
		Trie.__init__(self)
		self.min_depth = None

	def add_word(self, word):
		word = word[::-1]
		super().add_word(word)
		if self.min_depth is None:
			self.min_depth = len(word)
		elif len(word) < self.min_depth:
			self.min_depth = len(word)

	def lookup(self, word):
		word = word[::-1]
		super().lookup(word)

	def create_failure_links(self):
		bfs_queue = deque()

		# First, set suffix links for first children to root
		for key in self.root.children:
			child = self.root.children[key]
			child.ACsuffix_link = self.root

			for key2 in child.children:
				grandchild = child.children[key2]
				bfs_queue.append(grandchild)

		while (len(bfs_queue) > 0):
			current_node = bfs_queue.popleft();
			for key in current_node.children:
				child = current_node.children[key]
				bfs_queue.append(child)

			# Set suffix nodes in reverse
			AC_suffix_node = self.get_AC_suffix_link(current_node)
			current_node.ACsuffix_link = AC_suffix_node
			if AC_suffix_node.min_difference == -1 or AC_suffix_node.min_difference > current_node.depth - AC_suffix_node.depth:
				AC_suffix_node.min_difference = current_node.depth - AC_suffix_node.depth
				AC_suffix_node.CWsuffix_link = current_node
				if AC_suffix_node.word is not None:
					print (AC_suffix_node.word + " now points to character " + current_node.character)


