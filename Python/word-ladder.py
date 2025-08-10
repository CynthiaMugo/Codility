# Given two words, beginWord and endWord, and a dictionary of words wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list.
# Return 0 if no such sequence exists.
# All words have the same length and consist of lowercase letters only.

# beginWord is not considered a transformed word and may not be in wordList.
# Example:
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]

# Output: 5

def word_ladder(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0
    
    queue = [(beginWord, 1)]
    
    while queue:
        word, steps = queue.pop(0)
        
        if word == endWord:
            return steps
        
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]
                if new_word in wordSet:
                    wordSet.remove(new_word)
                    queue.append((new_word, steps + 1))
    
    return 0
print(word_ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"]))