"""
Given a list of integers, return the largest sum of two consecutive
numbers. Assume the list contains at least two numbers.
"""

#solution 1
def largest_consecutive_pair_sum(nums):
    largest= float("-inf")
    for i in range(len(nums)-1):
        if nums[i]+nums[i+1]>largest:
            largest=nums[i]+nums[i+1]
    return largest


# Test cases
print("expected: 11 OUTPUT '", largest_consecutive_pair_sum([2, 5, 1, 8, 3]), "'")
print("expected: 17 OUTPUT '", largest_consecutive_pair_sum([9, 8, 1, 2]), "'")
print("expected: 13 OUTPUT '", largest_consecutive_pair_sum([1, 6, 7, 2]), "'")
print("expected: 9 OUTPUT '", largest_consecutive_pair_sum([4, 5]), "'")
print("expected: 6 OUTPUT '", largest_consecutive_pair_sum([3, 3, 3]), "'")
print("expected: -7 OUTPUT '", largest_consecutive_pair_sum([-5, -2, -8, -1]), "'")
print("expected: 0 OUTPUT '", largest_consecutive_pair_sum([0, 0, 0]), "'")
print("expected: 1 OUTPUT '", largest_consecutive_pair_sum([10, -9, 10]), "'")