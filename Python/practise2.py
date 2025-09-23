# Write a function num_to_word(num) that takes a number and:
# Returns "Even" if the number is even.
# Returns "Odd" if the number is odd.
# Returns "Zero" if the number is 0.
def num_to_word(num):
    if num == 0:
        return "Zero"
    elif num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(num_to_word(0))   # Zero
print(num_to_word(7))   # Odd
print(num_to_word(10))  # Even

# Write a function censor_vowels(s) that replaces all vowels in a string with "*".
def censor_vowels(string):
    pass
print(censor_vowels("Hello World"))  # H*ll* W*rld

# Write a function multiples_of_7(n) that prints all multiples of 7 up to n, separated by spaces.
def multiples_of_7(num):
    pass
print(multiples_of_7(30))  # 7 14 21 28

# Write reverse_words(sentence) that reverses each word in a sentence but keeps their order.
def reverse_words(sentence):
    pass
print(reverse_words("Hello World"))  # olleH dlroW

# Write long_words(sentence, n) that returns words longer than n letters.
def long_words(sentence, n)
    pass
print(long_words("Python is really fun", 4))  
# ['Python', 'really']