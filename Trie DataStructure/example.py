from trie import Trie

def main():
    # Create a new Trie
    trie = Trie()

    # Insert words into the Trie
    words = ["apple", "app", "application", "banana", "band", "bandana"]
    for word in words:
        trie.insert(word)
    print("Words inserted into the Trie:", words)

    # Search for words
    search_words = ["apple", "app", "appl", "ban", "bandana", "cat"]
    for word in search_words:
        found = trie.search(word)
        print(f"Searching for '{word}': {'Found' if found else 'Not found'}")

    # Check for prefixes
    prefixes = ["app", "ban", "ca", "z"]
    for prefix in prefixes:
        starts_with = trie.start_with(prefix)
        print(f"Words starting with '{prefix}': {'Yes' if starts_with else 'No'}")

if __name__ == "__main__":
    main()
