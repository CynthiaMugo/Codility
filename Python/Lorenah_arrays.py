# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

def two_sum(nums, target):
    seen = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        seen[num] = index
print(two_sum([2,7,11,15], 9))

# Write a function hasPair(nums, target) that:
# Takes in a list of integers and a target integer.
# Returns True if there are any two numbers in the list that add up to the target, otherwise False.
def has_pair(nums, target):
    seen = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return True
        seen[num] = index
    return False
print(has_pair([2,7,11,15], 9))
print(has_pair([3,2,4], 6))

# Write a function count_pairs(nums, target) that:
# Returns the number of unique pairs (a, b) in the list such that a + b == target.
# A pair is considered the same regardless of order (so (2,7) is the same as (7,2)).
# Don’t reuse the same element twice.
def count_pairs(nums, target):
    seen = {}
    pairs = set()
    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            pairs.add((min(num, complement), max(num, complement)))
        seen[num] = index
    return len(pairs)
print(count_pairs([2,7,11,15,3,6,4], 9))
print(count_pairs([3,2,4,3,3,2,4], 6))

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
print(max_profit([7,1,5,3,6,4]))


# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation:
# All elements are distinct.
# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:   # duplicate found
            return True
        seen.add(num)     # record we’ve seen this number
    return False

print(contains_duplicate([1,2,3,1]))  # True
print(contains_duplicate([1,2,3,4]))  # False
print(contains_duplicate([1,1,1,3,3,4,3,2,4,2]))  # True

def find_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num   # return the actual duplicate number
        seen.add(num)
    return None   # if no duplicates found
print(find_duplicate([1,2,3,1]))  # 1
print(find_duplicate([1,2,3,4]))  # None



# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
def product_except_self(nums):
    answer = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]
        answer.append(product)
    return answer

# Question 3: Find the Maximum Sum of K Consecutive Elements
# You’re given a list of numbers and a number k.
# Find the maximum sum of any k consecutive elements in the list.

def max_slice_sum(A, k):
    max_sum = 0
    for i in range(len(A) - k + 1):
        current_sum = sum(A[i:i+k])   # sum of subarray of size k
        max_sum = max(max_sum, current_sum)
    return max_sum

print(max_slice_sum([2, 1, 5, 1, 3, 2], 3))  # Output: 9
print(max_slice_sum([1, 9, -1, -2, 7, 3, -1, 2], 4))  # Output: 13


def has_pair_with_sum(nums, target):
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    return False


def find_pair_with_sum(nums, target):
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            return (num, complement)  # return the actual numbers
        seen.add(num)
    return None  # if no pair found
