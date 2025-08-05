# Given a string, find the first character that does not repeat anywhere in the string. Return None if all characters repeat.
# Input: "Hello"
# Output: "H"
# Input: "Swiss"
# Output: "w"
def find_non_repeat_char(string):
    count = {}

    for char in string:
        if char in count:
            count[char] += 1
        else:
            count[char] =1
        print(count)

    for char in string:
        if count[char] == 1:
            return char
    return None
print(find_non_repeat_char("Hello"))
print(find_non_repeat_char("Swiss"))