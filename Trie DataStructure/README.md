# Trie Data Structure

## What is a Trie?

A Trie, also known as a prefix tree, is an efficient tree-like data structure used for storing and retrieving strings. The name "Trie" comes from the word "retrieval," highlighting its primary purpose.

## Why Use a Trie?

Tries are particularly useful for the following reasons:

1. **Fast Prefix Lookups**: Tries excel at prefix-based operations, making them ideal for autocomplete features, IP routing tables, and dictionary implementations.
2. **Space Efficiency**: For strings with common prefixes, Tries can save space compared to storing each string separately.
3. **Quick String Search**: Tries offer O(m) time complexity for searching, where m is the length of the string being searched.
4. **Lexicographic Ordering**: Strings in a Trie are naturally stored in lexicographic order, useful for sorting and range queries.

## Common Use Cases

- Autocomplete and predictive text
- Spell checkers
- IP routing tables
- Dictionary implementations
- Longest prefix matching

## Approach to Implementing a Trie

1. **Define the TrieNode Structure**:

   - Each node contains:
     - A map/dictionary of child nodes
     - A boolean flag indicating if it's the end of a word
2. **Implement the Trie Class**:

   - Initialize with a root TrieNode
3. **Implement Core Operations**:

   - `insert(word)`: Add a word to the Trie
   - `search(word)`: Check if a word exists in the Trie
   - `startsWith(prefix)`: Check if any word in the Trie starts with the given prefix
