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
    vowels = "aeiouAEIOU"
    for char in string:
        if char in vowels:
            string = string.replace(char, "*")
    return string
print(censor_vowels("Hello World"))  # H*ll* W*rld

# Censor Digits
# Replace all digits in a string with #.
# Input: "My number is 12345"
# Output: "My number is #####"
def censor_digits(string):
    for char in string:
        if char.isdigit():
            string = string.replace(char, "#")
    return string
print(censor_digits("12345"))
print(censor_digits("P1O2N3D4"))

def censor_digits2(string):
    return "".join("#" if char.isdigit() else char for char in string )
print(censor_digits2("12345"))
print(censor_digits2("P1O2N3D4"))

# Censor Consonants
# Replace all consonants with _, keep vowels.
# Input: "CoderByte"
# Output: "o_e__e"
def censor_consonants(string):
    vowels = "aeiouAEIOU"
    return "".join("_" if char.isalpha() and char not in vowels else char for char in string)
print(censor_consonants("Coderbyte"))
print(censor_consonants("Coderbyte 123"))

# Censor Every Nth Character
# Replace every 3rd character in the string with *.
# Input: "abcdefghijk"
# Output: "ab*de*gh*jk"
def replace_third_char(string):
    result = []
    for i, char in enumerate(string, start=1):  # 1-indexed
        if i % 3 == 0:
            result.append("*")
        else:
            result.append(char)
    return "".join(result)
print(replace_third_char("abcdefghijk"))  # ab*de*gh*jk
print(replace_third_char("aaaaaaaaaaaaaa")) 
# Replace every 4th character in the string with *.
def replace_fourth_char(string):
    return "".join("*" if (i+1) % 4 == 0 else c for i, c in enumerate(string))

print(replace_fourth_char("abcdefghijk"))  
# Censor Specific Word
# Replace a banned word in a sentence with [CENSORED].
# Input: "This is bad code" with bad banned.
# Output: "This is [CENSORED] code"
def censor_word(string, banned_word):
    return string.replace(banned_word, "[CENSORED]")
print(censor_word("This is bad code", "bad"))
# Reverse Censor
# Replace all characters except vowels with *.
# Input: "hello"
# Output: "*e**o"
def reverse_censor(string):
    vowels = "aeiouAEIOU"
    return "".join("*" if char.isalpha() and char not in vowels else char for char in string)
print(reverse_censor("Hello"))
def reverse_censor2(string):
    # this one not recommended doesn't check for punc and spaces 
    vowels = "aeiouAEIOU"
    return "".join(char if char in vowels else "*" for char in string)
print(reverse_censor2("Hello"))
# Write a function multiples_of_7(n) that prints all multiples of 7 up to n, separated by spaces.
def multiples_of_7(num):
    for i in range(7, num + 1, 7):
        if i % 7 == 0:
            print(i, end=" ")
multiples_of_7(30) # 7 14 21 28

def multiples2_of_7(num):
    return [i for i in range(7, num + 1, 7)]

print(multiples2_of_7(30))  # [7, 14, 21, 28]


# Write reverse_words(sentence) that reverses each word in a sentence but keeps their order.
def reverse_words(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)
print(reverse_words("Hello World"))  # olleH dlroW

def reverse_words2(sentence):
    return " ".join(word[::-1] for word in sentence.split())

print(reverse_words2("Hello World"))  # olleH dlroW

# Write long_words(sentence, n) that returns words longer than n letters.
def long_words(sentence, n):
    words = sentence.split()
    result = [word for word in words if len(word) > n]
    return result
print(long_words("Python is really fun", 4))  
['Python', 'really']