/*
	This is part of pyahocorasick Python module.
	
	Trie declarations

	Author    : Wojciech Mu�a, wojciech_mula@poczta.onet.pl
	WWW       : http://0x80.pl/proj/pyahocorasick/
	License   : 3-clauses BSD (see LICENSE)
	Date      : $Date$

	$Id$
*/

#ifndef ahocorasick_trie_h_included
#define ahocorasick_trie_h_included

#include "common.h"
#include "trienode.h"
#include "Automaton.h"

/* add new word to a trie, returns last node on a path for that word */
static TrieNode*
trie_add_word(Automaton* automaton, const TRIE_LETTER_TYPE* word, const size_t wordlen, bool* new_word);

/* returns last node on a path for given word */
static TrieNode* PURE
trie_find(TrieNode* root, const TRIE_LETTER_TYPE* word, const size_t wordlen);

/* returns node linked by edge labeled with letter including paths going
   through fail links */
static TrieNode* PURE
ahocorasick_next(TrieNode* node, TrieNode* root, const TRIE_LETTER_TYPE letter);

typedef int (*trie_traverse_callback)(TrieNode* node, const int depth, void* extra);

/* traverse trie in DFS order, for each node callback is called
   if callback returns false, then traversing stop */
static void
trie_traverse(
	TrieNode* root,
	trie_traverse_callback callback,
	void *extra
);

/* returns total size of node and it's internal structures */
size_t PURE
trienode_get_size(const TrieNode* node);

#endif
