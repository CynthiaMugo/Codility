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

# fibonacci sequence 
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
print(fibonacci(10))  # Output: 55