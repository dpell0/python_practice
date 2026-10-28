"""
Given a list of numbers and a threshold, return the index of the first
number greater than the threshold. Return -1 if no number qualifies.
"""

#solution 1
def first_above_threshold(nums, threshold):
    for i in range (len(nums)):
        if nums[i]>threshold:
            return i
    return -1


#test cases
print("expected: 1 OUTPUT '", first_above_threshold([2, 8, 3, 9, 5], 5), "'")
print("expected: 0 OUTPUT '", first_above_threshold([6, 7, 8], 5), "'")
print("expected: 2 OUTPUT '", first_above_threshold([1, 2, 9], 5), "'")
print("expected: -1 OUTPUT '", first_above_threshold([5, 5, 5], 5), "'")
print("expected: -1 OUTPUT '", first_above_threshold([1, 2, 3], 5), "'")
print("expected: -1 OUTPUT '", first_above_threshold([], 5), "'")
print("expected: 1 OUTPUT '", first_above_threshold([-4, -1, 0, 3], -2), "'")