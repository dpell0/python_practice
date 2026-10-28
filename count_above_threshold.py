"""
Return how many numbers in a list are greater than the threshold.
"""
#solution 1
def count_above_threshold(nums, threshold):
    count=0
    for i in nums:
        if i>threshold:
            count+=1
    return count


#test cases
print("expected: 2 OUTPUT '", count_above_threshold([2, 8, 3, 9, 5], 5), "'")
print("expected: 0 OUTPUT '", count_above_threshold([5, 5, 5], 5), "'")
print("expected: 3 OUTPUT '", count_above_threshold([6, 7, 8], 5), "'")
print("expected: 0 OUTPUT '", count_above_threshold([1, 2, 3], 5), "'")
print("expected: 0 OUTPUT '", count_above_threshold([], 5), "'")
print("expected: 3 OUTPUT '", count_above_threshold([-4, -1, 0, 3], -2), "'")
print("expected: 3 OUTPUT '", count_above_threshold([0, 1, 1, 2], 0), "'")