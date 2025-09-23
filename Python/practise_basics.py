# Reverse a String
# Write a function reverse_string(s) that returns the string s reversed.
def reverse_string(string):
    return string[::-1]
print(reverse_string("hello"))

# Count Vowels
# Write count_vowels(s) to count how many vowels (a, e, i, o, u) are in a string.
def count_vowels(string):
    count = 0
    vowels = "aeiouAEIOU"
    for char in string:
        if char in vowels:
            count += 1
    return count
# print(count_vowels("aeiou"))
# print(count_vowels("Hello World"))
# print(count_vowels("CYNTHIA MUGO"))

# Write a function called count_consonants that takes a string and returns how many consonants (letters that are not vowels) are in the string.
def count_consonants(string):
    count = 0
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    for char in string:
        if char in consonants:
            count += 1
    return count
print(count_consonants("aeiou"))
print(count_consonants("Hello World"))
print(count_consonants("CYNTHIA MUGO"))

def count_vowels(string):
    count = 0
    vowels = "aeiouAEIOU"
    for char in string:
        if char not in vowels and char.isalpha():
            count += 1
    return count
print(count_consonants("aeiou"))
print(count_consonants("Hello World"))
print(count_consonants("CYNTHIA MUGO"))

# Write a function count_vowel_rich_words(sentence) that:
# Takes a string sentence as input.
# Splits it into words.
# Counts how many words have more vowels than consonants.
def count_vowel_rich_words(sentence):
    words = sentence.split(" ")
    vowels = "aeiouAEIOU"
    word_count = 0
    for word in words:
        count_vowels = 0
        count_consonants = 0
        for char in word:
            if char in vowels:
                count_vowels += 1
            elif char.isalpha():
                count_consonants += 1
        if count_vowels > count_consonants:
            word_count += 1
    return word_count
print(count_vowel_rich_words("I still hear your voice when you sit next to me"))
print(count_vowel_rich_words("Education is the passport to the future for tomorrow belongs to those who prepare for it today"))

    
# Write a function longest_vowel_word(sentence) that:
# Takes a sentence (string).
# Finds the word with the highest number of vowels.
# Returns that word.
# If there’s a tie, return the first word with that count.
# Ignore punctuation.
def longest_vowel_word(sentence):
    words = sentence.split()
    vowels = "aeiouAEIOU"
    max_vowels = -1
    longest_word = ""
    for word in words:
        count_vowels = 0
        for char in word:
            if char in vowels:
                count_vowels += 1
    
        if count_vowels > max_vowels:
            max_vowels = count_vowels
            longest_word = word
    return longest_word, max_vowels
print(longest_vowel_word("The queue is unusually quiet today"))
#  "queue"
print(longest_vowel_word("I love programming challenges"))
#  "programming"
print(longest_vowel_word("Crypts rhythm myths"))
#  "Crypts"

# Write a function most_consonant_word(sentence) that:
# Takes in a sentence (string).
# Splits it into words.
# Counts the number of consonants (letters that are not vowels) in each word.
# Returns a tuple (word, consonant_count) for the word that has the most consonants.
# If multiple words tie, return the first one.

def most_consonant_word(sentence):
    words = sentence.split()
    most_consonants = -1
    most_consonant_word = ""
    for word in words:
        vowels = "aeiouAEIOU"
        count_consonants = 0
        for char in word:
            if char.isalpha() and char not in vowels:
                count_consonants += 1
        if count_consonants > most_consonants:
            most_consonants = count_consonants
            most_consonant_word = word
    return most_consonant_word, most_consonants
print(most_consonant_word("I think practice makes perfect"))
print(most_consonant_word("Crypt myths fly"))
print(most_consonant_word("Every coder loves challenges"))

# Palindrome Checker
# Write is_palindrome(s) that returns True if s is the same forward and backward.
def is_palindrome(string):
    return string == string[::-1]
print(is_palindrome("racecar"))
print(is_palindrome("hello"))

# FizzBuzz
# Write a function fizzbuzz(n) that prints numbers from 1 to n.
# Print "Fizz" if divisible by 3
# Print "Buzz" if divisible by 5
# Print "FizzBuzz" if divisible by both
# Otherwise, print the number
def fizzbuzz(num):
    result = []
    for i in range(1, num + 1):
        if i % 5 == 0 and i % 3 == 0:
            result.append("FizzBuzz")
        elif i % 5 == 0:
            result.append("Buzz")
        elif i % 3 == 0:
            result.append("Fizz")
        else:
            result.append(str(i))
    return " ".join(result)
print(fizzbuzz(15))

def fizzbuzz2(num):
    for i in range(1, num + 1):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        else:
            print(i, end=" ")
fizzbuzz2(15)
# Find Max in List
# Write find_max(nums) that returns the largest number in a list.

# Sum of Digits
# Write sum_digits(n) that takes an integer and returns the sum of its digits.
# Example: sum_digits(123) → 6

# Word Frequency Counter
# Write count_words(sentence) that returns a dictionary of word frequencies.

# Factorial (Loop)
# Write factorial_iter(n) using a loop.

# Factorial (Recursion)
# Write factorial_rec(n) using recursion.

# Remove Duplicates from List
# Write remove_duplicates(nums) that takes a list and returns a new list without duplicates.