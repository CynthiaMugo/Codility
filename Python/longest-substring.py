# Given a string s, find the length of the longest substring without repeating characters.
# Example
# Input: s = "bbbbb"
# Output: 1

# Input: s = "pwwkew"
# Output: 3

def longest_substring(s):
    longest = 0
    current = ""

    for char in s:
        if char in current:
            current = current[current.index(char) + 1:]
        current += char 
        longest = max(longest, len(current))
    
    return longest
print(longest_substring("bbbbb"))
print(longest_substring("pwwkew"))
