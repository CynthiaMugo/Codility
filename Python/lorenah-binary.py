# Given two integers a and b, return the sum of the two integers without using the operators + and -.
# Example 1:

# Input: a = 1, b = 2
# Output: 3
# Example 2:

# Input: a = 2, b = 3
# Output: 5
def add(a, b):
    while b != 0:
        carry = (a & b) << 1  # carry
        a = a ^ b             # sum without carry
        b = carry             # set carry as new b
    return a

print(add(5, 3))  # 8


# Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).
# Example 1:
# Input: n = 11
# Output: 3
# Explanation:
# The input binary string 1011 has a total of three set bits.
# Example 2:
# input: n = 128
# Output: 1
# Explanation:
# The input binary string 10000000 has a total of one set bit.
# Example 3:
# Input: n = 2147483645
# Output: 30

# Explanation:
# The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

# Constraints:

# 1 <= n <= 231 - 1
# Follow up: If this function is called many times, how would you optimize it
def hamming_weight(n):
    count = 0
    while n > 0:
        count += n & 1
        n >>= 1
    return count
print(hamming_weight(1))
print(hamming_weight(2147483645))
print(hamming_weight(11))

# here is a faster method 
def hamming_weight2(n):
    return bin(n).count("1")
print(hamming_weight2(1))
print(hamming_weight2(2147483645))
print(hamming_weight2(11))

# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
def count_bits(x):
    ans = []
    for i in range(x + 1):
        ans.append(hamming_weight(i))
    return ans
print(count_bits(2))  # [0,1,1]
print(count_bits(5))

def count_bits2(num):
    ans = []
    for i in range(num + 1):
        ans.append(bin(i).count("1"))
    return ans
print(count_bits2(2))  # [0,1,1]
print(count_bits2(5))  # [0, 1, 1, 2, 1, 2]

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
# Example 1:

# Input: nums = [3,0,1]

# Output: 2
def missing_number(nums):
    n = len(nums)
    num_set = set(nums)
    for i in range(n+1):
        if i not in num_set:
            return i
print(missing_number([3, 0, 1]))

def missingNumber(nums):
    n = len(nums)
    expected = n * (n + 1) // 2
    actual = sum(nums)
    return expected - actual
print(missingNumber([3, 0, 1]))


# Reverse bits of a given 32 bits signed integer.

# Example 1:

# Input: n = 43261596

# Output: 964176192
def reverse_bits(n):
    result = 0
    for i in range(32):
        result <<= 1           # shift result left
        result |= n & 1        # add the last bit of n
        n >>= 1                # shift n right
    return result

print(reverse_bits(43261596))  # 964176192

# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num   # XOR everything together
    return result

print(single_number([2,2,1]))        # 1
print(single_number([4,1,2,1,2]))    # 4


