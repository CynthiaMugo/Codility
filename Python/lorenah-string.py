# Given a string s, find the length of the longest substring without duplicate characters.
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

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

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.
# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
def character_replacement(s, k):
    count = {}
    max_count = 0
    left = 0
    result = 0

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        max_count = max(max_count, count[s[right]])

        while (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1

        result = max(result, right - left + 1)

    return result

# calculating gcd with euclidean algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd(48, 18))  # Output: 6

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"

# Output: false
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1
    return True

print(is_anagram("anagram", "nagaram"))  # True
print(is_anagram("rat", "car"))  # False


def is_anagram(s, t):
    if len(s) != len(t):
        return False

    count_s = {}
    count_t = {}

    for char in s:
        count_s[char] = count_s.get(char, 0) + 1

    for char in t:
        count_t[char] = count_t.get(char, 0) + 1

    return count_s == count_t

# missing number in array of n distinct numbers in range [0, n]
def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# calculate time in minutes between two times given in 24 hour format

# Given the head of a singly linked list, reverse the list, and return the reversed list.


# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
def group_anagrams(strs):
    groups = {}  # dictionary to hold grouped anagrams

    for word in strs:
        # Sort the word to get its key
        key = ''.join(sorted(word))

        # Add to the group with this key
        if key not in groups:
            groups[key] = []
        groups[key].append(word)

    # Return just the grouped lists
    return list(groups.values())

# validate password ensuring it has at least one uppercase letter, one lowercase letter, one digit, and one special character. The password should be at least 8 characters long. with if statements
def validate_password(password):
    if len(password) < 8:
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_characters = "!@#$%^&*()-+"
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
    
    return has_upper and has_lower and has_digit and has_special

#  Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
def is_valid_parentheses(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    
    return not stack
print(is_valid_parentheses("()"))  # True

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

def isPalindrome(s):
    cleaned = ""
    for char in s:
        if char.isalnum():  # only letters/numbers
            cleaned += char.lower()

    return cleaned == cleaned[::-1]  # compare to its reverse



