"""
Given a list of positive numbers and a positive threshold, add numbers
from the beginning of the list until the total is at least the threshold.
Return how many numbers were needed.
Return -1 if the total never reaches the threshold.
"""
def count_until_threshold(nums, threshold):
    total=0
    count=0
    for i in range(len(nums)):
        total+=nums[i]
        count+=1
        if total>=threshold:
            return count
    return -1


#test cases
print("expected: 3 OUTPUT '", count_until_threshold([2, 3, 1, 4, 6], 6), "'")
print("expected: 1 OUTPUT '", count_until_threshold([8, 2, 3], 5), "'")
print("expected: 1 OUTPUT '", count_until_threshold([5, 2, 3], 5), "'")
print("expected: 3 OUTPUT '", count_until_threshold([2, 2, 3], 6), "'")
print("expected: 3 OUTPUT '", count_until_threshold([1, 2, 3], 6), "'")
print("expected: -1 OUTPUT '", count_until_threshold([1, 2, 3], 7), "'")
print("expected: -1 OUTPUT '", count_until_threshold([], 5), "'")