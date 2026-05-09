def char_frequency(string):
     # to ignore spaces and punctuation
    frequency = {}
    for char in string:
        # char = char.isalpha()
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
print(char_frequency("hello world"))


def find_smallest_missing_positive(nums):
    a=set(nums)
    smallest =1
    for num in nums:
        if smallest  > 0 :
            smallest += 1
            return smallest
        
print(find_smallest_missing_positive([3,4,-1,1]))  #2  


def missing_number(nums):
    n=len(nums)
    expected_sum = n*(n+1)//2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

print(missing_number([3,0,1]))  #2

def reverse_string(s):
    return s[::-1]
print(reverse_string("hello"))  # "olleh"

def char_frequency(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
print(char_frequency("hello world"))               

