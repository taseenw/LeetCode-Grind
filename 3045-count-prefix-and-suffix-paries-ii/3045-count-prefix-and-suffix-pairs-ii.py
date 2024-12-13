# Trie Data Structure for storing words and their corresponding indices
class Trie:
    def __init__(self):
        # Root of the Trie, initially empty
        self.root = {}

    def insert(self, word, reverse=False):
        # `curChars` starts from the root and `indices` keeps track of word endings
        curChars, indices = self.root, set()
        
        # Traverse through each character of the word
        for char in word:
            # If the character already exists in the Trie, move to the next node
            if char in curChars:
                curChars = curChars[char]
            else:
                # Otherwise, add the character as a new node in the Trie
                curChars[char] = {}
                curChars = curChars[char]
            
            # If the 'end' key is found, it means this is the end of a word
            if 'end' in curChars:
                # Add the word's index to the set of indices
                indices.add(curChars['end'])
        
        # Mark the end of the current word, either normally or reversed based on the flag
        curChars['end'] = word if not reverse else word[::-1]
        # Return the set of word indices that end at this node
        return indices

# Main Solution Class
class Solution:
    def countPrefixSuffixPairs(self, words):
        # Create two Tries: one for storing prefixes and one for suffixes
        prefix, suffix = Trie(), Trie()
        
        # `count` will store how many times each word has been encountered
        count, res = defaultdict(int), 0
        
        # Loop through each word in the input list
        for word in words:
            # Insert word into the prefix Trie to track its prefixes
            indicesPrefix = prefix.insert(word)
            # Insert the reversed word into the suffix Trie to track its suffixes
            indicesSuffix = suffix.insert(word[::-1], True)
            
            # For every prefix index found, check if it matches any suffix index
            for chars in indicesPrefix:
                if chars in indicesSuffix:
                    # If there's a match, increment the result by the count of that word's occurrence
                    res += count[chars]
            
            # Increment the occurrence count for the current word
            count[word] += 1
        
        # Return the total number of valid (prefix, suffix) pairs
        return res