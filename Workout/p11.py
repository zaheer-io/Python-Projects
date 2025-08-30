# Input list of words
words = ["eat", "tea", "ate", "bat", "tab", "arc", "car"]

# Dictionary to store anagram groups
anagram_dict = {}

for word in words:
    # Sort the letters in the word to form the key
    key = "".join(sorted(word))

    # Add the word to the corresponding key in the dictionary
    if key not in anagram_dict:
        anagram_dict[key] = []
    anagram_dict[key].append(word)

# Print the grouped anagrams
for key, group in anagram_dict.items():
    print(f"{key} -> {group}")
